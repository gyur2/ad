from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout,QTreeView,QTreeWidgetItem
import json, random


class INBODY(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # 메인함수 기능에 필요한 변수 생성
        self.filename_personal = "personal.json"
        self.filename_wish = "personal_wish.json"  # information about name,studentnumber, lose weight, exercise minutes
        self.filename = "MET.json"
        fh = open(self.filename, "r")
        self.met = json.load(fh)
        fh.close()
        self.numitems = len(self.met.values())  # met개수입니다

        # 측정기록들 읽어오기
        res = self.read()
        self.resdefault = res[0]#기본 인적 사항들 : 이름,학번,몸무게,키
        self.reswish = res[1]#기본 인적사항 + 원하는 설정값: 이름,학번 + 감량 몸무게, 운동 시간

        # Button Creation and Placement
        inputLayout = QGridLayout()  # 위- 입력 받는 부분
        outputLayout = QGridLayout()  # 아래- 결과 표시 부분
        treeviewLayout = QGridLayout()  #트리뷰 표시부분(데이터 구조화)

        # 최적화
        # labelgroup = ['학번(number)', '이름(name)', '운동기간(exercise_day)', '키(Height)', '몸무게(Weight)', '희망 몸무게(Wish Weight)']

        # inputLayout
        inputLayout = QGridLayout()
        inputLayout.addWidget(QLabel('학번(number)', self), 0, 0)

        self.NumberD = QLineEdit()
        inputLayout.addWidget(self.NumberD, 0, 1)

        inputLayout.addWidget(QLabel('이름(name)', self), 0, 2)
        self.NameD = QLineEdit()
        inputLayout.addWidget(self.NameD, 0, 3)

        inputLayout.addWidget(QLabel('운동기간(exercise_day)', self), 0, 4)
        self.exercise_dayD = QLineEdit()
        inputLayout.addWidget(self.exercise_dayD, 0, 5)

        inputLayout.addWidget(QLabel('키(Height)', self), 1, 0)
        self.HeightD = QLineEdit()
        inputLayout.addWidget(self.HeightD, 1, 1)

        inputLayout.addWidget(QLabel('몸무게(Weight)', self), 1, 2)
        self.WeightD = QLineEdit()
        inputLayout.addWidget(self.WeightD, 1, 3)

        inputLayout.addWidget(QLabel('희망 몸무게(Wish Weight)', self), 1, 4)
        self.Wish_WeightD = QLineEdit()
        inputLayout.addWidget(self.Wish_WeightD, 1, 5)

        self.showB = QPushButton("show", self)
        self.showB.setMaximumHeight(100)
        inputLayout.addWidget(self.showB, 0, 6, 2, 2)
        self.showB.clicked.connect(self.buttonClicked)

        # outputLayout
        outputLayout.addWidget(QLabel('결과(result)', self), 0, 0)
        self.resultD = QTextEdit()
        self.resultD.setMaximumHeight(50000)  # 버튼 크기 조절
        # resultD.setGeometry(300, 300, 50, 50)
        outputLayout.addWidget(self.resultD, 1, 0)

        # MainLayout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)


        ####
        # treeviewLayout
        treeviewLayout.addWidget(QLabel("측정 기록",self),0,0)
        self.textTreeview = QTreeView(self)
        self.textTreeview.setRootIsDecorated(True)
        self.textTreeview.setAlternatingRowColors(True)
        infoHeader = ["번호","이름","학번","체중","키","운동종목","감량할 체중","운동시간"]
        infoData = ["name","number","weight","height","exercise","lose_weight","exercise_minutes"]

        #헤더(목록)설정
        self.resultTreeview = QStandardItemModel(0,len(infoHeader),self)
        for i in range(len(infoHeader)):
            self.resultTreeview.setHeaderData(i,Qt.Horizontal,infoHeader[i])
        #내용 표시
        for i in range(len(self.resdefault)):
            self.resultTreeview.insertRows(self.resultTreeview.rowCount(),1)
            for k in range(0,len(infoData)):#처음 5개 항목은 resdefault데이터, 남은 2개 항목은 reswish데이터
                self.resultTreeview.setData(self.resultTreeview.index(i,0),self.resultTreeview.rowCount())
                if k<=4: #resdefault 데이터
                    self.resultTreeview.setData(self.resultTreeview.index(i,k+1),self.resdefault[i][infoData[k]])
                else:
                    self.resultTreeview.setData(self.resultTreeview.index(i,k+1),self.reswish[i][infoData[k]])


        self.textTreeview.setModel(self.resultTreeview)# 트리뷰위젯에 resultTreeview에서 설정한 내용들을 세팅
        treeviewLayout.addWidget(self.textTreeview,1,0)
        #####




        mainLayout.addLayout(inputLayout, 0, 0)
        mainLayout.addLayout(treeviewLayout,1,0)
        mainLayout.addLayout(outputLayout, 2, 0)


        self.setLayout(mainLayout)

        self.setWindowTitle("My Inbody")

    def search(self, name, number):  # 동일인물일 경우 이전에 측정해둔 몸무게값과 랜덤으로 받았던 운동종목 반환
        for i in self.resdefault:
            if name in i.values() and number in i.values():
                return [i["weight"], i["exercise"]]

    def read(self):
        info_peronal = []
        info_wish = []
        fh = open(self.filename_personal, "r")
        try:
            info_personal = json.load(fh)
        except json.JSONDecodeError:  # 프로그램을 처음 시작할때 빈 파일을 읽게 되어 에러 발생-> 빈 리스트를 반환해주어 해결
            info_personal = []
            pass
        fh.close()
        fo = open(self.filename_wish, "r")
        try:
            info_wish = json.load(fo)
        except json.JSONDecodeError:  # 프로그램을 처음 시작할때 빈 파일을 읽게 되어 에러 발생-> 빈 리스트를 반환해주어 해결
            info_wish = []
            pass
        fo.close()
        return [info_personal, info_wish]

    def write(self):
        fh = open(self.filename_personal, "w")
        json.dump(self.resdefault, fh, indent="\t")
        fh.close()
        fo = open(self.filename_wish, "w")
        json.dump(self.reswish, fo, indent="\t")
        fo.close()

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        self.resultD.clear() #버튼 클릭시 빈 결과창으로 시작
        name = self.NameD.text()
        number = self.NumberD.text()
        weight = self.WeightD.text()  # unit:kg
        height = self.HeightD.text()  # unit:cm
        wish_weight = self.Wish_WeightD.text() # unit:kg
        exercise_day = self.exercise_dayD.text()  # unit:day

        if "" in [name, number, weight, height, wish_weight, exercise_day]:
            self.resultD.append("You miss about your informaiton")
            self.resultD.append("Retry to input your informaiton")

        elif not weight.isdigit() or not wish_weight.isdigit() or not exercise_day.isdigit():
            self.resultD.setText("weight, wish_weight and exercise_day are only number")
        else:
            lose_weight = int(weight) - int(wish_weight)
            if lose_weight < 0:
                self.resultD.append("Your wish weight was bigger than your real weight")
                self.resultD.append("you don't need exercise")
            elif lose_weight == 0:
                self.resultD.setText("Your weight was already you wish wight")

            else:
                # 동일인물인지 아닌지 판단
                for i in self.reswish:
                    if name in i.values() and number in i.values() and "" != name and "" != number:
                        orgdata = self.search(name, number)
                        orgweight = orgdata[0]  # 이전에 측정해둔 몸무게
                        orgexercise = orgdata[1]  # 이전에 랜덤으로 뽑았던 운동종목정
                        self.resultD.append("이전에 측정하셨 데이터가 존재합니다")
                        self.resultD.append("현재 몸무게: {}".format(orgweight))
                        self.resultD.append("운동 종목: {}".format(orgexercise))
                        self.resultD.append("하루에 해야하는 운동시간: %.4f분" % i["exercise_minutes"])  # 소수점 4자리까지
                        break
                else:  # 동일인물이 아닌 경우 inbody 측정
                    # 지방 1kg당 약 7000kcal
                    # lose_calorie변수 : 빼야할 체중을 칼로리로 환산한 값
                    lose_calorie = 7000 * lose_weight
                    randnum = random.randint(0, self.numitems - 1)  # 랜덤으로 met의 인덱스 뽑기
                    # 랜덤으로 특정met에서 운동종목 뽑기
                    numexer = len(self.met[list(self.met.keys())[randnum]]) #랜덤으로 뽑힌 met수치에 해당하는 운동종목의 개수
                    randexer = (self.met[list(self.met.keys())[randnum]])[random.randint(0, numexer - 1)]  # 랜덤으로 뽑힌 운동종목
                    metValue = float(list(self.met.keys())[randnum])
                    whole_exercise_minutes = (int(lose_calorie) * 1000) / (
                            metValue * 5 * 3.5 * float(weight))  # 운동해야 할 총 시간
                    exercise_minutes = whole_exercise_minutes / int(exercise_day)  # 하루에 운동해야 하는 시간
                    self.resdefault += [
                        {"name": name, "number": number, "weight": weight, "height": height, "exercise": randexer}]
                    self.reswish += [{"name": name, "number": number, "lose_weight": lose_weight,
                                      "exercise_minutes": exercise_minutes}]
                    if key == 'show':
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
                        self.resultD.append("BMI: {}".format(BMI))
                        self.resultD.append("상태 : {}".format(condition))
                        self.resultD.append("운동종목: {}".format(randexer))
                        self.resultD.append("감량할 체중: {}kg".format(lose_weight))
                        self.resultD.append("하루에 해야하는 운동시간: %.4f분" % exercise_minutes)
                    else:
                        self.resultD.setText("Invalid commend")

    def closeEvent(self, event):
        self.write()

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    inbody = INBODY()
    inbody.show()
    sys.exit(app.exec_())
