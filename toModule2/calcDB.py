
import json,random
class CalcDB:
    def __init__(self):
        # 메인함수 기능에 필요한 변수 생성
        self.filename_personal = "personal.json"
        self.filename_wish = "personal_wish.json"  # information about name,studentnumber, lose weight, exercise minutes
        self.filename = "MET.json"
        fh = open(self.filename, "r")
        self.met = json.load(fh)
        fh.close()
        self.numitems = len(self.met.values())  # met개수입니다
    def calcCalorie(self,lose_weight,weight,exercise_day):
        lose_calorie = 7000 * lose_weight
        randnum = random.randint(0, self.numitems - 1)  # 랜덤으로 met의 인덱스 뽑기
        # 랜덤으로 특정met에서 운동종목 뽑기
        numexer = len(self.met[list(self.met.keys())[randnum]])  # 랜덤으로 뽑힌 met수치에 해당하는 운동종목의 개수
        randexer = (self.met[list(self.met.keys())[randnum]])[random.randint(0, numexer - 1)]  # 랜덤으로 뽑힌 운동종목
        metValue = float(list(self.met.keys())[randnum])
        whole_exercise_minutes = (int(lose_calorie) * 1000) / (
                metValue * 5 * 3.5 * float(weight))  # 운동해야 할 총 시간
        exercise_minutes = whole_exercise_minutes / int(exercise_day)  # 하루에 운동해야 하는 시간
        return [randexer,exercise_minutes]
    def calcBMI(self,weight,height):
        BMI = int(weight) / (int(height) / 100) ** 2
        if BMI < 20:
            condition = '저체중'
        elif 20 < BMI < 24:
            condition = '정상'
        elif 25 < BMI < 29:
            condition = '과체중'
        else:
            condition = '비만'
        BMI = int(BMI)
        return [BMI,condition]