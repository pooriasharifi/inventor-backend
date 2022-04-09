import logging
import sys
from mongoengine import errors

from helper.res_struct import res_str

sys.path.append('../')
from flask import request, make_response, Blueprint
from Model.kala import Kala
from Model.personel import Users,Request_main,Request_details
requ = Blueprint('requ', __name__)


@requ.route('/req/<user_id>', methods=['POST','GET'])
def add_req(user_id):
    logging.info('--- kala IPAddr: ' + request.remote_addr + ' ---')
    if request.method=='POST':
        try:
            content = request.json
            user=Users.objects(user_id=user_id).first()
            print(user.req)
            if not user:
                return make_response('user not found',400)
            else:
                temp=list()

                for item in content['detail']:
                    user_obj=Request_details(
                    code_kala=item['code_kala'],
                    request_number =item['request_number'],
                    recive_number =item['recive_number'],
                    )
                    temp.append(user_obj)
                req_obj = Request_main(
                    number_issued=content['number_issued'],
                    date=content['date'],
                    detail=temp
                )
                user.req.append(req_obj)

                # temp.append(user_obj)
                # req_obj.detail.append(temp)
                user.save()
                return make_response(res_str('registered',None),200)
        except OSError as err:
            return make_response(res_str('internal_server_error',err),500)
    elif request.method=='GET':
        try:
            user=Users.objects(user_id=user_id).first()
            temp=list()

            temp.append(user['req'])
            # print(len(temp))
            # print(len(temp[0][0]))

            total_request=dict

            for i in temp:
                total_request={
                    'total_request':len(i)
                }
                for item in i:
                    pass

            # print(temp[0])
            return make_response(res_str('registered', [temp,total_request]),200)
        except OSError as err:
            return make_response(res_str('internal_server_error',err),500)

