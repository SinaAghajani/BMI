
weight = int(input("لطفا وزن خود را وارد کنید : "))
height = int(input("لطفا قد خود را وارد کنید : "))

BMI  = (weight) / (height * height) * 10000 

if BMI>0:
    if BMI<=18.5:
        print(" زیر وزن")
    elif BMI<=24.9:
        print("نرمال")
    elif BMI<=29.9:
        print("اضافه وزن")
    elif BMI<=34.9:
        print("چاقی درجه 1")
    elif BMI<=39.9:
        print("چاقی درجه 2")
    else:
        print("چاقی درجه 3")
        

print("شاخص توده بدنی شما : ", round(BMI))        