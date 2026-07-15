gender = int(input())
age = int(input())

if gender == 0 :
    # 남자일때
    if age >= 19 :
        # 성인일때
        print("MAN")
    else :
        # 미성년자일때
        print("BOY")
else :
    # 여자일때
    if age >= 19 :
        # 성인일때
        print("WOMAN")
    else :
        # 미성년자일때
        print("GIRL")