country = input('請問你是哪國人?')
age = input('請問你幾歲?')
age = int(age)
if country == '台灣': 
    if age >= 18:
        print('你可以考駕照')   
    else:
        print('你不可以考')
elif country == '美國':
    if age >= 16:
        print('你可以考駕照')
    else:
        print('你不可以考駕照')
else:
    print('你只可以輸入美國或台灣')
