import datetime
import logging
import sys
from mongoengine import errors

from helper.res_struct import res_str

sys.path.append('../')
from flask import request, make_response, Blueprint
from Model.kala import Kala

kala = Blueprint('kala', __name__)


@kala.route('/kala', methods=['POST','GET'])
def add_kala():
    logging.info('--- kala IPAddr: ' + request.remote_addr + ' ---')
    if request.method=='POST':
        try:
            content = request.json
            kala = Kala(
                code_kala=content['code_kala'],
                name=content['name'],
                volume=content['volume']
            ).save()
            return make_response(res_str('registered', None), 201)
        except errors.ValidationError as err:
            return make_response('internal_sever_error', None, 500)
        except errors.NotUniqueError as err:
            if "kalaname" in str(err):
                return make_response(res_str('internal_sever_error', None), 500)
            elif "email" in str(err):
                return make_response(res_str('duplicate_email', None), 500)
            else:
                return make_response(res_str('duplicate_kala', None), 500)
        except KeyError as err:
            if "kalaname" in str(err):
                return make_response(res_str('kalaname_required', None), 500)
            elif "password" in str(err):
                return make_response(res_str('password_required', None), 500)
            elif "email" in str(err):
                return make_response(res_str('email_required', None), 500)
            else:
                return make_response(res_str('internal_server_error', None), 500)
        except OSError as err:
            return make_response(res_str('internal_server_error', err), 500)
    elif request.method=='GET':
        try:
            user_obj=Kala.objects()
            res_data=list()
            for item in user_obj:
                user_temp=dict(
                    name=item.name,
                    code_kala=item.code_kala,
                    volume=item.volume,
                    status=False
                )
                res_data.append(user_temp)
            return make_response(res_str('wait',res_data),200)
        except OSError as err:
            return make_response(res_str('internal_server_error',err),500)

