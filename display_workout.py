import sys
import sqlite3
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt6.QtGui import QFont, QPixmap, QCursor
from PyQt6.QtCore import Qt, pyqtSignal, QRect

bg_color = '#28293D'
primary_black = '#000000'
yellow = '#FEC166'
dark_yellow = '#EEA02B'
atlantic = 'qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #3eebbe stop:0.0001 #4ec1f3, stop:1 #68fcd6)'
light_yellow = '#FFD9A0'

daftar_workout = [
    {
        "id": 1,
        "name": "Push Up",
        "description": "Push-ups are exercises to strengthen your arms and \nchest muscles. They are done by lying with your face \ntowards the floor and pushing with your hands to \nraise your body until your arms are straight.",
        "specification": "10 Repetition",
        "linkTutorial" : "iniLinkTutorial1",
        "linkIllustration" : "images/push-up.png",
    },
    {
        "id": 2,
        "name": "Sit Up",
        "description": "Sit-ups are exercises that you do to strengthen your \nstomach muscles. They involve sitting up from a lying \nposition while keeping your legs straight on the floor.",
        "specification": "10 Repetition",
        "linkTutorial" : "iniLinkTutorial2",
        "linkIllustration" : "images/sit-up.png",
    },
    {
        "id": 3,
        "name": "Pull Up",
        "description": "A pull-up is an upper-body strength exercise. The \npull-up is a closed-chain movement where the body \nis suspended by the hands and pulls up.",
        "specification": "10 Repetition",
        "linkTutorial" : "iniLinkTutorial3",
        "linkIllustration" : "images/pull-up.png",
    }
]

# class WorkoutCard(QWidget):
#     # make a card based on daftar_workout
#     def __init__(self, workout):
#         super().__init__()
#         self.workout = workout
#         self.setUpWorkoutCard()
    
#     def setUpWorkoutCard(self):
#         # Set up background image
#         self.setStyleSheet(f"background-color: {bg_color}")
#         # Set up logo
#         self.logo = QLabel(self)
#         self.logo.setGeometry(QRect(20, 20, 100, 100))
#         self.logo.setPixmap(QPixmap("assets/images/logo.png"))
#         self.logo.setScaledContents(True)
#         # Set up title
#         self.title = QLabel(self)
#         self.title.setGeometry(QRect(140, 20, 600, 100))
#         self.title.setFont(QFont("Inter", 24, QFont.Bold))
#         self.title.setText(self.workout["name"])
#         self.title.setStyleSheet(f"color: {light_yellow}")
#         # Set up description
#         self.description = QLabel(self)
#         self.description.setGeometry(QRect(140, 60, 600, 100))
#         self.description.setFont(QFont("Inter", 16, QFont.Normal))
#         self.description.setText(self.workout["description"])
#         self.description.setStyleSheet(f"color: {light_yellow}")
#         # Set up specification
#         self.specification = QLabel(self)
#         self.specification.setGeometry(QRect(140, 100, 600, 100))
#         self.specification.setFont(QFont("Inter", 16, QFont.Normal))
#         self.specification.setText(self.workout["specification"])
#         self.specification.setStyleSheet(f"color: {light_yellow}")
#         # Set up button
#         self.btn = QPushButton(self)
#         self.btn.setGeometry(QRect(140, 140, 600, 100))
#         self.btn.setFont(QFont("Inter", 16, QFont.Normal))
#         self.btn.setText("Start Workout")
#         self.btn.setStyleSheet(f"background-color: {btn_color}")

#         # self.btn.clicked.connect(self.onClick)

class DisplayWorkout(QWidget):
    switch = pyqtSignal(str, dict)

    def __init__(self, user = None):
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
        self.conn = sqlite3.connect('fitpal.db')
        self.fetchWorkout()
        self.setUpDisplayWorkoutWindow()
    
    def setUpDisplayWorkoutWindow(self):
        self.setFixedSize(1280, 720)
        self.setWindowTitle("FitPal - Display Workout")
        self.setUpWidgets()
    
    def setUpWidgets(self):
        # Fonts
        inter10 = QFont()
        inter10.setFamily("Inter")
        inter10.setPixelSize(10)

        inter16 = QFont()
        inter16.setFamily("Inter"); 
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

        # Set up background image
        self.setStyleSheet(f"background-color: {bg_color}")

        # Set up logo
        logoPixmap = QPixmap("images/dashboard-fitpal-logo.png")
        logo = QLabel(self)
        logo.setPixmap(logoPixmap)
        logo.move(60, 30)
        logo.setStyleSheet(f"background-color: {bg_color}")

        # Set up hello label
        self.helloLabel = QLabel(self)
        self.helloLabel.setText(f"Hello, {self.user['fullname']}!")
        self.helloLabel.move(635, 44)
        self.helloLabel.setStyleSheet(f'color: rgba(255, 255, 255, 0.8); background-color: {bg_color}')
        self.helloLabel.setFixedSize(585, 29)
        self.helloLabel.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.helloLabel.setFont(inter24)

        # Set up heading label
        heading = QLabel(self)
        heading.setText("Workout Activity")
        heading.move(60, 120)
        heading.setStyleSheet(f"color: {atlantic}; background-color: {bg_color}")
        heading.setFont(inter48)

        # Set up workout cards from workout
        self.workoutCards = []
        for i in range(len(self.workout)):
            card = QLabel(self)
            cardPixmap = QPixmap("images/template-yellow-card.png")
            card.setPixmap(cardPixmap)
            card.setStyleSheet(f"background-color: {bg_color}")
            card.move(60 + (i*360), 200)
            card.setFixedSize(300, 360)
            card.setStyleSheet(f"background-color: {bg_color}")
            picture = QLabel(self)
            picture.setGeometry(QRect(130 + (i*360), 220, 160, 160))
            picture.setStyleSheet(f"background-color: {yellow}")
            picture.setPixmap(QPixmap(self.workout[i]["linkIllustration"]))
            cardHeading = QLabel(self)
            cardHeading.setText(self.workout[i]['name'])
            cardHeading.move(80 + (i*360), 400)
            cardHeading.setStyleSheet(f"color: {primary_black}; background-color: {light_yellow}")
            cardHeading.setFont(inter24bold)
            cardDescription = QLabel(self)
            cardDescription.setText(self.workout[i]['description'])
            cardDescription.move(80 + (i*360), 440)
            cardDescription.setStyleSheet(f"color: {primary_black}; background-color: {light_yellow}")
            cardDescription.setFont(inter10)
            cardSpecification = QLabel(self)
            cardSpecification.setText(self.workout[i]['specification'])
            cardSpecification.move(240 + (i*360), 405)
            cardSpecification.setStyleSheet(f"color: {primary_black}; background-color: {light_yellow}")
            cardSpecification.setFont(inter16)
            cardAddButton = QPushButton(self)
            cardAddButton.setGeometry(QRect(220 + (i*360), 500, 120, 30))
            cardAddButton.setText("Add To Activity")
            cardAddButton.setStyleSheet(f"color: #ffffff; background-color: {dark_yellow}; border: none; border-radius: 12px; font-weight: bold;")

            cardTutorialButton = QPushButton(self)
            cardTutorialButton.setGeometry(QRect(80 + (i*360), 500, 90, 30))
            cardTutorialButton.setText("Tutorial")
            cardTutorialButton.setStyleSheet(f"color: #6E7198; background: transparent; border: 2px solid; border-color: #6E7198; border-radius: 12px;")
            
            self.workoutCards.append(card)
    
    def fetchWorkout(self):
        self.workout = daftar_workout

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DisplayWorkout()
    window.show()
    sys.exit(app.exec())