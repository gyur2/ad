import pickle
import random

filename_personal = "personal.dat"
filename_wish = "personal_wish.dat"  # information about name,studentnumber, lose weight, exercise minutes
filename = "met.dat"
fh = open(filename, "rb")
met = pickle.load(fh)
fh.close()
numitems = len(met.values())  # met개수입니다

def search(name, number, resdefault):  # 동일인물일 경우 이전에 측정해둔 몸무게값과 랜덤으로 받았던 운동종목 반환
    for i in resdefault:
        if name in i.values() and number in i.values():
            return [i["weight"], i["exercise"]]


def read():
    info_peronal = []
    info_wish = []
    fh = open(filename_personal, "rb")
    info_personal = pickle.load(fh)
    fh.close()
    fo = open(filename_wish, "rb")
    info_wish = pickle.load(fo)
    fo.close()
    return [info_personal, info_wish]


def write(resdefault, reswish):
    fh = open(filename_personal, "wb")
    pickle.dump(resdefault, fh)
    fh.close()
    fo = open(filename_wish, "wb")
    pickle.dump(reswish, fo)
    fo.close()


def main(resdefault, reswish):
    while (True):
        person = input("input your information > ").split()  # input your name,studentnumber,weight,height and your wish weight
        order = input("input show result or quit > ")  # input order show result or quit동
        try:
            global wish_weight
            name = person[0]
            number = person[1]
            weight = person[2]  # unit:kg
            height = person[3]  # unit:cm
            wish_weight = person[4]  # unit:kg
            exercise_day = person[5]  # unit:day
        except IndexError:
            print("You miss about your informaiton")
            print("Retry to input your informaiton")
            continue
        if not weight.isdigit() or not wish_weight.isdigit() or not exercise_day.isdigit():
            print("weight, wish_weight and exercise_day are only number")
            continue

        lose_weight = int(weight) - int(wish_weight)
        if lose_weight < 0:
            print("Your wish weight was bigger than your real weight")
            print("you don't need exercise")
            continue
        elif lose_weight == 0:
            print("Your weight was already you wish wight")
            continue
        else:
            # 동일인물인지 아닌지 판단
            next = False
            for i in reswish:
                if name in i.values() and number in i.values():
                    orgdata = search(name, number, resdefault)
                    orgweight = orgdata[0]  # 이전에 측정해둔 몸무게
                    orgexercise = orgdata[1]  # 이전에 랜덤으로 뽑았던 운동종목정
                    print("이전에 측정하셨 데이터가 존재합니다")
                    print("현재 몸무게: {}".format(orgweight))
                    print("운동 종목: {}".format(orgexercise))
                    print("하루에 해야하는 운동시간: %.4f분" %i["exercise_minutes"]) #소수점 4자리까지
                    next = True
                    break
            else:  # 동일인물이 아닌 경우 inbody 측정
                # 지방 1kg당 약 7000kcal
                # lose_calorie변수 : 빼야할 체중을 칼로리로 환산한 값
                lose_calorie = 7000 * lose_weight
                randnum = random.randint(0, numitems - 1)  # 랜덤으로 met의 인덱스 뽑기
                # 랜덤으로 특정met에서 운동종목 뽑기
                numexer = len(met[list(met.keys())[randnum]])
                randexer = (met[list(met.keys())[randnum]])[random.randint(0, numexer - 1)]  # 랜덤으로 뽑힌 운동종목
                exermet = float(list(met.keys())[randnum])
                whole_exercise_minutes = (int(lose_calorie) * 1000) / (exermet * 5 * 3.5 * float(weight)) # 운동해야 할 총 시간
                exercise_minutes = whole_exercise_minutes / int(exercise_day)  # 하루에 운동해야 하는 시간
                resdefault += [{"name": name, "number": number, "weight": weight, "height": height, "exercise": randexer}]
                reswish += [{"name": name, "number": number, "lose_weight": lose_weight, "exercise_minutes": exercise_minutes}]

                if order == 'show':
                    BMI = int(weight) / (int(height)/100)** 2
                    if BMI < 20:
                        condition = '저체중'
                    elif 20 < BMI < 24:
                        condition = '정상'
                    elif 25 < BMI < 29:
                        condition = '과체중'
                    else:
                        condition = '비만'
                    print("BMI: ", int(BMI))
                    print("상태 : ", condition)
                    print("운동종목:", randexer)
                    print("감량할 체중:", lose_weight, "kg")
                    print("하루에 해야하는 운동시간: %.4f분" %exercise_minutes)
                elif order == 'quit':
                    break
                else:
                    print("Invalid command: " + order)

        if next:
            continue  # 다시 입력받는 곳으로 이동


# excute inbody.py

resdefault = read()[0]
reswish = read()[1]
main(resdefault,reswish)
write(resdefault,reswish)
