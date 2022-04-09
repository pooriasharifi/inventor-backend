import logging
import sys
from mongoengine import errors

from Model.personel import Users
from helper.res_struct import res_str
from flask import request,make_response,Blueprint




sys.path.append('../')

all = Blueprint('all',__name__)


@all.route('/all',methods=['GET'])
def all_req():
    logging.info('___ all IPAddr: '+request.remote_addr+'______')
    try:
        user_obj=Users.objects()
        temp=list()
        temp.append(user_obj)
        total=dict()
        for i in temp:
            total={'total':len(i)}
        return make_response(res_str('registered', [total,temp]), 200)
    except OSError as err:
        make_response(res_str('internal_server_error', err), 500)
