def res_str(msg, data):
    switcher = {
        'wait': 'لطفا صبر کنید',
        'internal_server_error': 'خطای داخلی سرور',
        'incorrect_username_or_password': 'نام کاربری یا رمز عبور نامعتبر',
        'invalid_email_address': 'آدرس ایمیل نامعتبر',
        'duplicate_username': 'شماره تلفن تکراری',
        'duplicate_email': 'id تکراری',
        'username_required': 'عدم شناسایی نام کاربری',
        'password_required': 'عدم شناسایی id کاربر',
        'email_required': 'عدم شناسایی آدرس ایمیل',
        'registered': 'ثبت با موفقیت انجام شد',
        'logged': 'ورورد موفقیت آمیز',
        'symbol_sign_required': 'عدم شناسایی کد نماد',
        'favorite_duplicate': 'نماد در لیست موجود است',
        'favorite_added': 'به علاقه مندی ها اضافه شد',
        'favorite_not_found': 'علاقه مندی موجود نیست',
        'duplicate_kala': 'کد کالا موجود است',
        'explorer_not_found': 'نماد مورد تائیدی یافت نشد'
    }
    msg = switcher.get(msg, 'خطای سرور')
    return dict(
        msg=msg,
        data=data
    )
