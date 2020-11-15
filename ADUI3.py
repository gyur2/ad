
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import pickle,random,sys
#메인함수 기능에 필요한 변수 생성
filename_personal = "personal.dat"
filename_wish = "personal_wish.dat"  # information about name,studentnumber, lose weight, exercise minutes
filename = "MET.dat"
fh = open(filename, "rb")
met = pickle.load(fh)
fh.close()
numitems = len(met.values())  # met개수입니다


class Ui_Form(object):
    def __init__(self):
        super().__init__()
        #GUI호출
        widget = QtWidgets.QWidget()
        self.setupUi(widget)
        res = self.read()
        self.resdefault = res[0]
        self.reswish = res[1]
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(845, 447)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(480, 20, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 70, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 0, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(230, 40, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 110, 831, 61))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 280, 821, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(610, 30, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 160, 141, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 200, 141, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        # 결과를 보여주게되는 버튼 추가
        self.showBttn = QtWidgets.QPushButton(Form)
        self.showBttn.setGeometry(QtCore.QRect(600,200,50,50))
        self.showBttn.move(600,200)
        self.showBttn.clicked.connect(self.bttn_clicked)




        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(370, 240, 141, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 91, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(10, 90, 101, 41))
        self.label_8.setObjectName("label_8")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(650, 30, 161, 71))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(80, 100, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "\n"
"Please enter your height:"))
        self.label_2.setText(_translate("Form", "\n"
"Please enter your weight:"))
        self.label_3.setText(_translate("Form", "BMI:"))
        self.label_4.setText(_translate("Form", "\n"
"Please chose your sports"))
        self.label_5.setText(_translate("Form", "\n"
"Please set your time/mins"))
        self.label_6.setText(_translate("Form", "Wish_weight(KG)\n"
""))
        self.label_7.setText(_translate("Form", "학번(number)"))
        self.label_8.setText(_translate("Form", "이름(name)"))

        #버튼 이름 설
        self.showBttn.setText(_translate("Form","show"))

    def search(self, name, number, resdefault):  # 동일인물일 경우 이전에 측정해둔 몸무게값과 랜덤으로 받았던 운동종목 반환
        for i in resdefault:
            if name in i.values() and number in i.values():
                return [i["weight"], i["exercise"]]

    def read(self):
        info_peronal = []
        info_wish = []
        fh = open(filename_personal, "rb")
        try:
            info_personal = pickle.load(fh)
        except EOFError:  # 프로그램을 처음 시작할때 빈 파일을 읽게 되어 에러 발생-> 빈 리스트를 반환해주어 해결
            info_personal = []
            pass
        fh.close()
        fo = open(filename_wish, "rb")
        try:
            info_wish = pickle.load(fo)
        except EOFError:  # 프로그램을 처음 시작할때 빈 파일을 읽게 되어 에러 발생-> 빈 리스트를 반환해주어 해결
            info_wish = []
            pass
        fo.close()
        return [info_personal, info_wish]

    def write(resdefault, reswish):
        fh = open(filename_personal, "wb")
        pickle.dump(resdefault, fh)
        fh.close()
        fo = open(filename_wish, "wb")
        pickle.dump(reswish, fo)
        fo.close()

    def bttn_clicked(self):
        order = self.showBttn.text()

        global wish_weight
        name = self.lineEdit_7.text()
        number = self.lineEdit_6.text()
        weight = self.lineEdit_2.text()  # unit:kg
        height = self.lineEdit.text()  # unit:cm
        wish_weight = self.lineEdit_3.text()  # unit:kg
        exercise_day = self.lineEdit_5.text()  # unit:day
        if "" in [name, number, weight, height, wish_weight, exercise_day]:
            self.textBrowser.append("You miss about your informaiton")
            self.textBrowser.append("Retry to input your informaiton")

        if not weight.isdigit() or not wish_weight.isdigit() or not exercise_day.isdigit():
            self.textBrowser.setText("weight, wish_weight and exercise_day are only number")

        lose_weight = int(weight) - int(wish_weight)
        if lose_weight < 0:
            self.textBrowser.append("Your wish weight was bigger than your real weight")
            self.textBrowser.append("you don't need exercise")

        elif lose_weight == 0:
            self.textBrowser.setText("Your weight was already you wish wight")

        else:
            if lose_weight < 0:
                self.textBrowser.append("Your wish weight was bigger than your real weight")
                self.textBrowser.append("you don't need exercise")

            elif lose_weight == 0:
                self.textBrowser.setText("Your weight was already you wish wight")

            else:
                # 동일인물인지 아닌지 판단
                for i in self.reswish:
                    if name in i.values() and number in i.values():
                        orgdata = self.search(name, number, self.resdefault)
                        orgweight = orgdata[0]  # 이전에 측정해둔 몸무게
                        orgexercise = orgdata[1]  # 이전에 랜덤으로 뽑았던 운동종목정
                        self.textBrowser.append("이전에 측정하셨 데이터가 존재합니다")
                        self.textBrowser.append("현재 몸무게: {}".format(orgweight))
                        self.textBrowser.append("운동 종목: {}".format(orgexercise))
                        self.textBrowser.append("하루에 해야하는 운동시간: %.4f분" % i["exercise_minutes"])  # 소수점 4자리까지
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
                    whole_exercise_minutes = (int(lose_calorie) * 1000) / (
                            exermet * 5 * 3.5 * float(weight))  # 운동해야 할 총 시간
                    exercise_minutes = whole_exercise_minutes / int(exercise_day)  # 하루에 운동해야 하는 시간
                    self.resdefault += [
                        {"name": name, "number": number, "weight": weight, "height": height, "exercise": randexer}]
                    self.reswish += [{"name": name, "number": number, "lose_weight": lose_weight,
                                        "exercise_minutes": exercise_minutes}]

                    if order == 'show':
                        BMI = int(weight) / (int(height) / 100) ** 2
                        if BMI < 20:
                            condition = '저체중'
                        elif 20 < BMI < 24:
                            condition = '정상'
                        elif 25 < BMI < 29:
                            condition = '과체중'
                        else:
                            condition = '비만'
                        BMI=int(BMI)
                        self.textBrowser_2.append("BMI: {}".format(str(BMI)))
                        self.textBrowser_2.append("상태 : {}".format(condition))
                        self.textBrowser.append("운동종목: {}".format(randexer))
                        self.textBrowser.append("감량할 체중: {}kg".format(lose_weight))
                        self.textBrowser.append("하루에 해야하는 운동시간: %.4f분" % exercise_minutes)
                    else:
                        self.textBrowser.setText("Invalid commend")

    def closeEvent(self, event):
        self.write(self.resdefault, self.reswish)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())