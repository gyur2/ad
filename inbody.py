import pickle
import random
filename_personal = "personal.dat"
filename_wish = "personal_wish.dat" #information about name,studentnumber, lose weight, exercise minutes
filename = "MET.dat"
fh = open(filename,"rb")
met = pickle.load(fh)
fh.close()
numitems = len(met.values()) #met개수입니다
def search(name,number,resdefault): #동일인물일 경우 이전에 측정해둔 몸무게값과 랜덤으로 받았던 운동종목 반환
    for i in resdefault:
        if name in i.values() and number in i.values():
            return [i["weight"],i["exercise"]]

def read():
    info_peronal = []
    info_wish = []
    fh = open(filename_personal,"rb")
    info_personal = pickle.load(fh)
    fh.close()
    fo = open(filename_wish,"rb")
    info_wish = pickle.load(fo)
    fo.close()
    return [info_personal,info_wish]

def write(resdefault, reswish):
    fh = open(filename_personal,"wb")
    pickle.dump(resdefault,fh)
    fh.close()
    fo = open(filename_wish,"wb")
    pickle.dump(reswish,fo)
    fo.close()

def main(resdefault,reswish):
    while(True):
        person = input("input your information > ").split()#input your name,studentnumber,weight,height and your wish weight
        order = input("input show result or quit")#input order show result or quit동
        try:
            name = person[0]
            number = person[1]
            weight = person[2]#unit:kg
            height = person[3]#unit:cm
            wish_weight = person[4]#unit:kg
            exercise_day = person[5]#unit:day
        except IndexError:
            print("You miss about your informaiton")
            print("Retry to input your informaiton")
            continue
        lose_weight = weight - wish_weight
        if lose_weight < 0:
            print("Your wish weight was bigger than your real weight")
            print("you don't need exercise")
            continue
        elif lose_weight == 0:
            print("Your weight was already you wish wight")
            continue
        else:
            #동일인물인지 아닌지 판단
            next = False
            for i in reswish:
                if name in i.values() and number in i.values():
                    orgdata = search(name,number,resdefault)
                    orgweight = orgdata[0]#이전에 측정해둔 몸무게
                    orgexercise = orgdata[1]#이전에 랜덤으로 뽑았던 운동종목정
                    print("이전에 측정하셨 데이터가 존재합니")
                    print("현재 몸무게: {}".format(orgweight))
                    print("희망 몸무게: {}".format(i[wish_weight]))#희망 몸무게
                    print("운동 종목: {}".format(orgexercise))
                    print("운동 시간: {}".format(i["exercise_minutes"]))
                    next = True
                    break
            else:#동일인물이 아닌 경우 inbody 측정
                # 지방 1kg당 약 7000kcal
                # lose_calorie변수 : 빼야할 체중을 칼로리로 환산한 값
                lose_calorie = 7000 * lose_weight
                randnum = random.randint(0, numitems - 1)  # 랜덤으로 met의 인덱스 뽑기
                # 랜덤으로 특정met에서 운동종목 뽑기
                numexer = len(met[randnum])
                randexer = met.keys()[randnum][random.randint(0, numexer - 1)]  # 랜덤으로 뽑힌 운동종목
                exermet = met.valules()[randnum]  # 랜덤으로 뽑힌 met
                whole_exercise_minutes = (lose_calorie * 1000) / exermet * 5 * 3.5 * weight  # 운동해야 할 총 시간
                exercise_minutes = whole_exercise_minutes / exercise_day  # 하루에 운동해야 하는 시간
                resdefault += [
                    {"name": name, "number": number, "weight": weight, "height": height, "exercise": randexer}]
                reswish += [
                    {"name": name, "number": number, "lose_weight": lose_weight, "exercise_minutes": exercise_minutes}]
                """
                여기에 main()남은 부분 써주시면 될 것 같습니다(입력받은 명령어가 show인지 quit인지에 따라 다른 기능 구현)
                """

           if next:
                continue #다시 입력받는 곳으로 이동















# excute inbody.py
"""   
resdefault = read()[0]
reswish = read()[1]
main(resdefault,reswish)
write(resdefault,reswish)
"""


