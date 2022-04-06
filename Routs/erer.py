a = {
	"data": [
		[
			{
				"date": {
					"$date": "2022-04-03T00:00:00Z"
				},
				"detail": [
					{
						"code_kala": 3666,
						"recive_number": 546584635,
						"request_number": 165165
					},
					{
						"code_kala": 3666,
						"recive_number": 546584635,
						"request_number": 165165
					},
					{
						"code_kala": 3666,
						"recive_number": 546584635,
						"request_number": 165165
					}
				],
				"number_issued": 1212
			},
			{
				"date": {
					"$date": "2022-04-03T00:00:00Z"
				},
				"detail": [
					{
						"code_kala": 345,
						"recive_number": 546584635,
						"request_number": 165165
					},
					{
						"code_kala": 545,
						"recive_number": 546584635,
						"request_number": 165165
					},
					{
						"code_kala": 34554,
						"recive_number": 546584635,
						"request_number": 165165
					}
				],
				"number_issued": 1212
			}
		]
	],
	"msg": "ثبت با موفقیت انجام شد"
}
print(len(a['data'][0]))
print(len(a['data'][0][0]))
for i in a['data']:
    print(len(i))
    for item in i:
        pass
    print(len(item))
        # print(len(i))