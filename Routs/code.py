import datetime
import logging
import sys
from mongoengine import errors

from helper.res_struct import res_str

sys.path.append('../')
from flask import request, make_response, Blueprint
from Model.kala import Kala


code=Blueprint('/code',__name__)

@code.route('/code/<code_kala>', methods=['GET'])
def search_code(code_kala):
    logging.info('--- kala IPAddr: ' + request.remote_addr + ' ---')
    try:
        kala_obj = Kala.objects(code_kala==code_kala).first()
        res_data=list()
        res_data.append(kala_obj)
        # for i in kala_obj:
        #     # print(i)
        #     if i['code_kala']==code_kala:
        #         print('aaaaaa')
            # temp=dict(
            #     name=i.name,
            #     code_kala=i.code_kala,
            #     volume=i.volume,
            # )
            # res_data.append(temp)
            # if i['code_kala']==code_kala:
            #     res_data.append(i)
            # else:
            #     pass
        return make_response(res_str('wait',res_data),200)
    except OSError as err:
        return make_response(res_str('internal_server_error', err), 500)

    # try:
    #    kala_obj=Kala.objects()
    #    res_data=list()
    #     for i in kala_obj['data']:
    #         if i['code_kala']==code_kala:
    #             res_data.append({i})
    #         else:
    #             pass
    #     return make_response(res_str('wait',res_data),200)
    #
    # except OSError as err:
    #         return make_response(res_str('internal_server_error', err), 500)







#####################################براساس کد کالا
# code=list()
# recive=list()
# radif=list()
# for item in data['data'][1][0]:
# 	# print(item['req'])
# 	for i in item['req']:
# 		# print(i['detail'])
# 		for count in i['detail']:
# 			if count['code_kala']==3138601:
# 				print(count)
# 				print(i['number_issued'])
# 				print(i['date'])
# 				code.append(count['code_kala'])
# 				recive.append(count['recive_number'])
# 				radif.count(c)
# df = DataFrame({'swdvsdv':radif,'کد کالا': code, 'شرح کالا': 'l2','vahed':'5645','تعداد':recive})
# df.to_excel('./test.xlsx', sheet_name='sheet1', index=False,index_label='ردیف',startrow=0)

