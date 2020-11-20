from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class INBODY(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Button Creation and Placement
        inputLayout = QGridLayout() #위- 입력 받는 부분 
        outputLayout = QGridLayout() #아래- 결과 표시 부분
        
        #최적화 
        #labelgroup = ['학번(number)', '이름(name)', '운동기간(exercise_day)', '키(Height)', '몸무게(Weight)', '희망 몸무게(Wish Weight)']

        #inputLayout
        inputLayout = QGridLayout()
        inputLayout.addWidget(QLabel('학번(number)', self), 0, 0)
        self.display = QLineEdit()
        NumberD = self.display
        inputLayout.addWidget(NumberD, 0, 1)

        inputLayout.addWidget(QLabel('이름(name)', self), 0 , 2)
        self.display = QLineEdit()
        NameD = self.display
        inputLayout.addWidget(NameD, 0, 3)

        inputLayout.addWidget(QLabel('운동기간(exercise_day)', self), 0, 4)
        self.display = QLineEdit()
        exercise_dayD = self.display
        inputLayout.addWidget(exercise_dayD, 0, 5)

        inputLayout.addWidget(QLabel('키(Height)', self), 1, 0)
        self.display = QLineEdit()
        HeightD = self.display
        inputLayout.addWidget(HeightD, 1, 1)

        inputLayout.addWidget(QLabel('몸무게(Weight)', self), 1, 2)
        self.display = QLineEdit()
        WeightD = self.display
        inputLayout.addWidget(WeightD, 1, 3)

        inputLayout.addWidget(QLabel('희망 몸무게(Wish Weight)', self), 1, 4)
        self.display = QLineEdit()
        Wish_WeightD = self.display
        inputLayout.addWidget(Wish_WeightD, 1, 5)

        showB = QPushButton("show", self)
        showB.setMaximumHeight(100)
        inputLayout.addWidget(showB, 0, 6, 2, 2)

        #outputLayout
        outputLayout.addWidget(QLabel('결과(result)', self), 0, 0)
        resultD = QTextEdit()
        resultD.setMaximumHeight(50000) #버튼 크기 조절 
        #resultD.setGeometry(300, 300, 50, 50)
        outputLayout.addWidget(resultD, 1, 0)

        # MainLayout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addLayout(inputLayout, 0, 0)
        mainLayout.addLayout(outputLayout, 1, 0)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Inbody")


    def buttonClicked(self):

        if self.display.text() == 'Error!':
            self.display.setText('')

        button = self.sender()
        key = button.text()

        if key == 'show':
            try:
                #main()
                result = 'success'
            except:
                result = 'Error!'
            self.display.setText(result)
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    inbody = INBODY()
    inbody.show()
    sys.exit(app.exec_())


