import sys
import sqlite3
import webbrowser
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt6.QtGui import QFont, QPixmap, QCursor, QIcon
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWebEngineWidgets import QWebEngineView
# defined style
bg_color = '#28293D'
atlantic = 'qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #3eebbe stop:0.0001 #4ec1f3, stop:1 #68fcd6)'
light_yellow = '#FFD9A0'
light_purple = '#A19AFE'
primary_red = '#F10628'
primary_red_hover = "#f43853"
btn_color = 'qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #5561ff, stop:1 #3643fc);'
btn_color_hover = 'qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #6b75ff, stop:1 #535fff)'
hello_label_style = f'color: rgba(255, 255, 255, 0.8); background-color: {bg_color}'
logout_btn_style = '''
      QPushButton {
        color: #ffffff;
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #5561ff, stop:1 #3643fc);
        border: none;
        border-radius: 12px;
      }
      QPushButton:hover {
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #6b75ff, stop:1 #535fff);
      }
    '''
back_btn_style = f'''
      QPushButton {{
        color: #ffffff;
        background-color: {primary_red};
        border: none;
        border-radius: 12px;
      }}
      QPushButton:hover {{
        background-color: {primary_red_hover};
      }}
    '''
card_content_style = "color: #FFF; background-color: #3E405B"

history_list = [
    {
        "id": 1,
        "name": "Push Up",
        "specification": "10 Repetition",
        "date": "06-March-2022",
        "linkTutorial": "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley",
        "linkIllustration": "images/push_up.png",
    },
    {
        "id": 2,
        "name": "Sit Up",
        "specification": "20 Repetition",
        "date": "07-March-2022",
        "linkTutorial": "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley",
        "linkIllustration": "images/sit_up.png",
    },
    {
        "id": 3,
        "name": "Pull Up",
        "specification": "30 Repetition",
        "date": "08-March-2022",
        "linkTutorial": "https://www.youtube.com/watch?v=bTJIkQRsmaE",
        "linkIllustration": "images/pull_up.png",
    },
    {
        "id": 4,
        "name": "Push Up",
        "specification": "100 Repetition",
        "date": "09-March-2022",
        "linkTutorial": "https://www.youtube.com/watch?v=bTJIkQRsmaE",
        "linkIllustration": "images/push_up.png",
    },
    {
        "id": 5,
        "name": "TEMPIKKK",
        "specification": "30 Repetition",
        "date": "10-March-2022",
        "linkTutorial": "https://www.youtube.com/watch?v=bTJIkQRsmaE",
        "linkIllustration": "images/sit_up.png",
    }
]


class finish_workout(QWidget):
    switch = pyqtSignal(str, dict)

    def __init__(self, user=None):
        super().__init__()
        if (user != None):
            self.user = user
        else:
            self.user = {
                "fullname": "John Doe",
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "johndoe",
                "type": "user"
            }
        self.pageHistory = 0
        self.history = None
        self.fetchHistory()
        self.setUpDashboardWindow()

    def setUpDashboardWindow(self):
        self.setFixedSize(1280, 720)
        self.setWindowTitle("FitPal - Finish Workout")
        self.setUpWidgets()

    def setUpWidgets(self):

        # background
        self.setStyleSheet(f'background-color: {bg_color}')

        # font
        inter13 = QFont()
        inter13.setFamily("Inter")
        inter13.setPixelSize(13)

        inter16 = QFont()
        inter16.setFamily("Inter")
        inter16.setPixelSize(16)

        inter24 = QFont()
        inter24.setFamily("Inter")
        inter24.setPixelSize(24)

        inter24bold = QFont()
        inter24bold.setFamily("Inter")
        inter24bold.setPixelSize(24)
        inter24bold.setBold(True)

        inter48 = QFont()
        inter48.setFamily("Inter")
        inter48.setPixelSize(48)
        inter48.setBold(True)
        # end of font

        # logo
        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap("images/dashboard-fitpal-logo.png"))
        self.logo.move(60, 30)
        self.logo.setStyleSheet(f"background-color: {bg_color}")
        # end of logo

        # title
        self.title = QLabel(self)
        self.title.setText("Workout History")
        self.title.setFont(inter48)
        self.title.setStyleSheet(
            f"color: {atlantic}; background-color: {bg_color}")
        self.title.move(60, 120)
        # end of title
        self.initializeHistoryPage()
        self.setUpHistoryPage()

        # arrow left and right gatau cara buatnya
        self.arrowleft = QPushButton(self)
        self.arrowleft.setStyleSheet(
            "background: url(images/chevron-compact-left.png);")
        self.arrowleft.setGeometry(200, 370, 48, 48)
        self.arrowleft.clicked.connect(self.leftButtonClicked)
        self.arrowright = QPushButton(self)
        self.arrowright.setStyleSheet(
            "background: url(images/chevron-compact-right.png);")
        self.arrowright.move(1130, 370)
        self.arrowright.clicked.connect(self.rightButtonClicked)
        self.arrowright.setGeometry(1130, 370, 48, 48)
        # end of arrow

        # hello label user
        self.helloLabel = QLabel(self)
        self.helloLabel.setText(f"Hello, {self.user['fullname']}")
        self.helloLabel.move(635, 44)
        self.helloLabel.setStyleSheet(hello_label_style)
        self.helloLabel.setFixedSize(585, 29)
        self.helloLabel.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.helloLabel.setFont(inter24)
        # end of hello label

        # logout button
        self.logOutBtn = QPushButton(self)
        self.logOutBtn.setText("Log Out")
        self.logOutBtn.setStyleSheet(logout_btn_style)
        self.logOutBtn.setFont(inter16)
        self.logOutBtn.setFixedSize(121, 48)
        self.logOutBtn.move(1099, 88)
        self.logOutBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logOutBtn.clicked.connect(self.logOut)
        # end of logout button

        # back button
        self.backBtn = QPushButton(self)
        self.backBtn.setText("Back")
        self.backBtn.setStyleSheet(back_btn_style)
        self.backBtn.setFont(inter16)
        self.backBtn.setFixedSize(121, 48)
        self.backBtn.move(60, 627)
        self.backBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.backBtn.clicked.connect(self.userDashboard)
        # end of button

        # add new workout btn
        self.addBtn = QPushButton(self)
        self.addBtn.setText("Add Workout")
        self.addBtn.setStyleSheet(logout_btn_style)
        self.addBtn.setFont(inter16)
        self.addBtn.setFixedSize(121, 48)
        self.addBtn.move(190, 627)
        self.addBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # self.addBtn.clicked.connect(self.addWorkout)
        # end of add new workout

    def initializeHistoryPage(self):

        inter16 = QFont()
        inter16.setFamily("Inter")
        inter16.setPixelSize(16)

        inter24 = QFont()
        inter24.setFamily("Inter")
        inter24.setPixelSize(24)

        inter24bold = QFont()
        inter24bold.setFamily("Inter")
        inter24bold.setPixelSize(24)
        inter24bold.setBold(True)

        self.cards = []
        for i in range(3):
            self.cards.append({})
            self.cards[i]["card"] = QLabel(self)
            self.cards[i]["card"].setPixmap(QPixmap("images/Card.png"))
            self.cards[i]["card"].move(250 + 300 * i, 209)
            self.cards[i]["image"] = QLabel(self)
            self.cards[i]["image"].move(300 + 300 * i, 250)
            self.cards[i]["image"].setStyleSheet(f"background-color: #373951")
            self.cards[i]["heading"] = QLabel(self)
            self.cards[i]["heading"].move(270 + 300 * i, 450)
            self.cards[i]["heading"].setFont(inter24bold)
            self.cards[i]["heading"].setStyleSheet(card_content_style)
            self.cards[i]["text"] = QLabel(self)
            self.cards[i]["text"].move(270 + 300 * i, 490)
            self.cards[i]["text"].setFont(inter16)
            self.cards[i]["text"].setStyleSheet(card_content_style)
            self.cards[i]["date"] = QLabel(self)
            self.cards[i]["date"].setFont(inter16)
            self.cards[i]["date"].move(400 + 300*i, 490)
            self.cards[i]["date"].setStyleSheet(card_content_style)
            self.cards[i]["tutorial"] = QPushButton(self)
            self.cards[i]["tutorial"].setStyleSheet(logout_btn_style)
            self.cards[i]["tutorial"].setText("Tutorial Video")
            self.cards[i]["tutorial"].setFont(inter16)
            self.cards[i]["tutorial"].setFixedSize(121, 48)
            self.cards[i]["tutorial"].move(270 + 300 * i, 540)
            self.cards[i]["tutorial"].setCursor(
                QCursor(Qt.CursorShape.PointingHandCursor))
            self.cards[i]["tutorial"].clicked.connect(
                lambda x, i=i: self.openTutorial(i))

    def setUpHistoryPage(self):
        start = self.pageHistory * 3
        print(start)
        for i in range(3):
            if start + i < len(self.history):
                self.cards[i]["date"].setText(
                    self.history[i + start]["date"])
                self.cards[i]["heading"].setText(
                    self.history[i + start]["name"])
                self.cards[i]["text"].setText(
                    self.history[i + start]["specification"])
                self.cards[i]["image"].setPixmap(
                    QPixmap(self.history[i + start]["linkIllustration"]))
                self.cards[i]["date"].show()
                self.cards[i]["text"].show()
                self.cards[i]["heading"].show()
                self.cards[i]["image"].show()
                self.cards[i]["card"].show()
                self.cards[i]["tutorial"].show()
            else:
                self.cards[i]["date"].hide()
                self.cards[i]["text"].hide()
                self.cards[i]["heading"].hide()
                self.cards[i]["image"].hide()
                self.cards[i]["card"].hide()
                self.cards[i]["tutorial"].hide()

    def openTutorial(self, idx):
        idx += self.pageHistory*3
        webbrowser.open(self.history[idx]["linkTutorial"])

    def rightButtonClicked(self):
        print(len(history_list), len(self.history))
        print(len(self.history) // 3)
        print("Right workout button clicked")
        if(self.pageHistory + 1 <= (len(self.history) // 3)):
            self.pageHistory += 1
            print("page: ", self.pageHistory)
            self.setUpHistoryPage()

    def leftButtonClicked(self):
        print("Left workout button clicked")
        if self.pageHistory > 0:
            self.pageHistory -= 1
            print("page: ", self.pageHistory)
            self.setUpHistoryPage()

    def updateUser(self, user):
        self.user = user
        self.helloLabel.setText(f"Hello, {self.user['fullname']}")

    def userDashboard(self):
        self.switch.emit("user_dashboard", self.user)

    def fetchHistory(self):
        self.history = history_list

    def logOut(self):
        self.switch.emit("login", self.user)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = finish_workout()
    window.show()
    sys.exit(app.exec())
