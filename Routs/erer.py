from pandas import DataFrame



data = {
	"data": [
		{
			"total": 3
		},
		[
			[
				{
					"_id": {
						"$oid": "624fe79e2a05ace65d92bc53"
					},
					"full_name": "یاسر صادقی",
					"phone": 9139727981,
					"req": [
						{
							"date": {
								"$date": {
									"$numberLong": "-89424000000"
								}
							},
							"detail": [
								{
									"code_kala": 3118203,
									"recive_number": 12312311,
									"request_number": 123123
								},
								{
									"code_kala": 3138302,
									"recive_number": 1222222,
									"request_number": 222222
								},
								{
									"code_kala": 3138601,
									"recive_number": 22222,
									"request_number": 22
								}
							],
							"number_issued": 23333
						}
					],
					"state": True,
					"user_id": 1
				},
				{
					"_id": {
						"$oid": "62500cb0f29061b7fd7aff7b"
					},
					"full_name": " صادقی",
					"phone": 91232327981,
					"req": [],
					"state": True,
					"user_id": 2
				},
				{
					"_id": {
						"$oid": "62507d29eba6d8152280fd93"
					},
					"full_name": " صادقی",
					"phone": 5465846546,
					"req": [],
					"state": True,
					"user_id": 3
				}
			]
		]
	],
	"msg": "ثبت با موفقیت انجام شد"
}

kala={
	"data": [
		{
			"code_kala": 4444,
			"name": "dvmsodviknsdv",
			"status": False,
			"volume": "defswdvf"
		},
		{
			"code_kala": 1341535,
			"name": "dvmsodviknsdv",
			"status": False,
			"volume": "defswdvf"
		},
		{
			"code_kala": 424523,
			"name": "یبقایبابفلابفلات",
			"status": False,
			"volume": "defswdvf"
		}
	],
	"msg": "لطفا صبر کنید"
}

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



#####################################براساس شماره صدور
# for item in data['data'][1][0]:
# 	# print(item['req'])
# 	for i in item['req']:
# 		if i['number_issued']==23333:
# 			print(i)



# l1 = [1,2,3,4]
# l2 = [1,2,3,4]
# df = DataFrame({'Stimulus Time': l1, 'Reaction Time': l2})
# print(df)
# df.to_excel('./test.xlsx', sheet_name='sheet1', index=False)

#
# a = [1,2,3]
# print (id(x) for x in a)
# print (a)
#
# for i in range(len(a)):
#     a.append(a[i+1])
#
# print (id(x) for x in a)
# print (a)

# for i in kala['data']:
# 	if i['code_kala']==424523:
# 		print(i)