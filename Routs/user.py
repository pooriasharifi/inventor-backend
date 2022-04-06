import logging
import sys
from mongoengine import errors

from helper.res_struct import res_str

sys.path.append('../')
from flask import request, make_response, Blueprint
from Model.personel import Users

user = Blueprint('user', __name__)


@user.route('/user', methods=['POST','GET'])
def add_user():
    logging.info('--- user IPAddr: ' + request.remote_addr + ' ---')
    if request.method=='POST':
        try:
            content = request.json
            user = Users(
                user_id=content['id'],
                full_name=content['full_name'],
                phone=content['phone'],
                state=content['state'],
                req=[]
            ).save()
            return make_response(res_str('registered', None), 201)
        except errors.ValidationError as err:
            return make_response('internal_sever_error', None, 500)
        except errors.NotUniqueError as err:
            if "phone" in str(err):
                return make_response(res_str('duplicate_username', None), 500)
            elif "id" in str(err):
                return make_response(res_str('duplicate_email',None),500)
            else:
                return make_response(res_str('internal_server_error', None), 500)
        except KeyError as err:
            if "phone" in str(err):
                return make_response(res_str('username_required', None), 504)
            elif "id" in str(err):
                return make_response(res_str('password_required', None), 500)

            else:
                return make_response(res_str('internal_server_error', None), 500)
        except OSError as err:
            return make_response(res_str('internal_server_error', err), 500)
    elif request.method=='GET':
        try:
            user_obj=Users.objects()
            res_data=list()
            for item in user_obj:
                user_temp=dict(
                    name=item.full_name,
                    id=item.user_id
                )
                res_data.append(user_temp)
            print(res_data)
            return make_response(res_str('wait',res_data),200)
        except OSError as err:
            return make_response(res_str('internal_server_error',err),500)

