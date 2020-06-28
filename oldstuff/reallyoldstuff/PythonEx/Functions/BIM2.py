name1 = "Yolo"
height_m1 = 1.75
weight_kg1 = 80

name2 = "Yolo's sister"
height_m2 = 2
weight_kg2 = 75

name3 = "Yolo's Brother"
height_m3 = 1.58
weight_kg3 = 95

def bmi_calc(name,height_m,weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print ("bmi: ")
    print (bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"

res1 = bmi_calc(name1, height_m1, weight_kg1)

res2 = bmi_calc(name2, height_m2, weight_kg2)

res3 = bmi_calc(name3, height_m3, weight_kg3)

print(res1)
print(res2)
print(res3)
