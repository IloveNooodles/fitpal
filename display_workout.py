import sys
import sqlite3
import webbrowser
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt6.QtGui import QFont, QPixmap, QCursor
from PyQt6.QtCore import Qt, pyqtSignal, QRect

bg_color = '#28293D'
primary_black = '#000000'
primary_white = '#FFFFFF'
primary_button = '#5561FF'
yellow = '#FEC166'
dark_yellow = '#EEA02B'
grape = '#7366FE'
atlantic = 'qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #3eebbe stop:0.0001 #4ec1f3, stop:1 #68fcd6)'
light_yellow = '#FFD9A0'
btn_color = 'qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #5561ff, stop:1 #3643fc);'
btn_color_hover = 'qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #6b75ff, stop:1 #535fff)'

daftar_workout = [
    {
        "id": 1,
        "name": "Push Up",
        "description": "Push-ups are exercises to strengthen your arms and \nchest muscles. They are done by lying with your face \ntowards the floor and pushing with your hands to \nraise your body until your arms are straight.",
        "specification": "10 Repetition",
        "linkTutorial" : "https://www.youtube.com/watch?v=bTJIkQRsmaE",
        "linkIllustration" : "images/push-up.png",
    },
    {
        "id": 2,
        "name": "Sit Up",
        "description": "Sit-ups are exercises that you do to strengthen your \nstomach muscles. They involve sitting up from a lying \nposition while keeping your legs straight on the floor.",
        "specification": "10 Repetition",
        "linkTutorial" : "https://www.youtube.com/watch?v=6eJVLbgxbBE",
        "linkIllustration" : "images/sit-up.png",
    },
    {
        "id": 3,
        "name": "Pull Up",
        "description": "A pull-up is an upper-body strength exercise. The \npull-up is a closed-chain movement where the body \nis suspended by the hands and pulls up.",
        "specification": "10 Repetition",
        "linkTutorial" : "https://www.youtube.com/watch?v=eGo4IYlbE5g",
        "linkIllustration" : "images/pull-up.png",
    },
    {
        "id": 4,
        "name": "Sit Up",
        "description": "Sit-ups are exercises that you do to strengthen your \nstomach muscles. They involve sitting up from a lying \nposition while keeping your legs straight on the floor.",
        "specification": "10 Repetition",
        "linkTutorial" : "https://www.youtube.com/watch?v=6eJVLbgxbBE",
        "linkIllustration" : "images/sit-up.png",
    },
    {
        "id": 5,
        "name": "Pull Up",
        "description": "A pull-up is an upper-body strength exercise. The \npull-up is a closed-chain movement where the body \nis suspended by the hands and pulls up.",
        "specification": "10 Repetition",
        "linkTutorial" : "https://www.youtube.com/watch?v=eGo4IYlbE5g",
        "linkIllustration" : "images/pull-up.png",
    },
    {
        "id": 6,
        "name": "Push Up",
        "description": "Push-ups are exercises to strengthen your arms and \nchest muscles. They are done by lying with your face \ntowards the floor and pushing with your hands to \nraise your body until your arms are straight.",
        "specification": "10 Repetition",
        "linkTutorial" : "https://www.youtube.com/watch?v=bTJIkQRsmaE",
        "linkIllustration" : "images/push-up.png",
    }
]

daftar_workout_plan = [
    {
        "id": 1,
        "name": "Leg Day",
        "description": "This workout plan is made to strengthen your \nleg muscles.",
        "seeMore" : "inilinkseemore1"
    },
    {
        "id": 2,
        "name": "Chest Day",
        "description": "This workout plan is made to strengthen your \nabdominal muscles.",
        "seeMore" : "inilinkseemore1"
    }
]

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
        self.pageWorkout = 0
        self.pageWorkoutPlan = 0
        self.workoutPlan = []
        self.listWorkoutPlan = None
        self.fetchWorkout()
        self.setUpDisplayWorkoutWindow()
    
    def setUpDisplayWorkoutWindow(self):
        self.setFixedSize(1280, 720)
        self.setWindowTitle("FitPal - Display Workout")
        self.setUpWidgets()
    
    def setUpWidgets(self):
        # Fonts
        inter24 = QFont()
        inter24.setFamily("Inter")
        inter24.setPixelSize(24)
        
        inter16 = QFont()
        inter16.setFamily("Inter")
        inter16.setPixelSize(16)

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

        # Set up log out button
        logOutBtn = QPushButton(self)
        logOutBtn.setText("Log Out")
        logOutBtn.setStyleSheet(f'''
        QPushButton {{
            color: #ffffff;
            background-color: {btn_color};
            border: none;
            border-radius: 12px;
        }}
        QPushButton:hover {{
            background-color: {btn_color_hover};
        }}
        ''')
        logOutBtn.setFixedSize(121, 48)
        logOutBtn.setFont(inter16)
        logOutBtn.move(1099, 88)
        logOutBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        logOutBtn.clicked.connect(self.logOut)

        # Set up workout cards from workout
        self.initializeWorkoutCards()
        self.setUpDisplayWorkout()
        # self.setUpDisplayWorkoutPlan()

        self.rightWorkoutButton = QPushButton(self)
        self.rightWorkoutButton.setGeometry(QRect(1130, 308, 48, 48))
        self.rightWorkoutButton.setStyleSheet(f"background-image: url(images/right-btn.png);")
        self.rightWorkoutButton.clicked.connect(self.rightWorkoutButtonClicked)

        self.leftWorkoutButton = QPushButton(self)
        self.leftWorkoutButton.setGeometry(QRect(102, 308, 48, 48))
        self.leftWorkoutButton.setStyleSheet(f"background-image: url(images/left-btn.png);")
        self.leftWorkoutButton.clicked.connect(self.leftWorkoutButtonClicked)

        self.rightWorkoutPlanButton = QPushButton(self)
        self.rightWorkoutPlanButton.setGeometry(QRect(1130, 590, 48, 48))
        self.rightWorkoutPlanButton.setStyleSheet(f"background-image: url(images/right-btn.png);")
        self.rightWorkoutPlanButton.clicked.connect(self.rightWorkoutPlanButtonClicked)

        self.leftWorkoutPlanButton = QPushButton(self)
        self.leftWorkoutPlanButton.setGeometry(QRect(102, 590, 48, 48))
        self.leftWorkoutPlanButton.setStyleSheet(f"background-image: url(images/left-btn.png);")
        self.leftWorkoutPlanButton.clicked.connect(self.leftWorkoutPlanButtonClicked)

        # Set up back button from page workout plan
        self.backWPButton = QPushButton(self)
        self.backWPButton.setText("Back")
        self.backWPButton.setStyleSheet(f'''
        QPushButton {{
            color: #ffffff;
            background-color: {btn_color};
            border: none;
            border-radius: 12px;
        }}
        QPushButton:hover {{
            background-color: {btn_color_hover};
        }}
        ''')
        self.backWPButton.setGeometry(QRect(60, 620, 120, 48))
        self.backWPButton.setFont(inter16)
        self.backWPButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.backWPButton.clicked.connect(self.backWP)
        self.backWPButton.hide()

    def initializeWorkoutCards(self):
        # Set up font
        inter10 = QFont()
        inter10.setFamily("Inter")
        inter10.setPixelSize(10)

        inter12 = QFont()
        inter12.setFamily("Inter")
        inter12.setPixelSize(12)

        inter16bold = QFont()
        inter16bold.setFamily("Inter")
        inter16bold.setPixelSize(16)
        inter16bold.setBold(True)

        inter24bold = QFont()
        inter24bold.setFamily("Inter")
        inter24bold.setPixelSize(24)
        inter24bold.setBold(True)

        inter48 = QFont()
        inter48.setFamily("Inter")
        inter48.setPixelSize(48)
        inter48.setBold(True)

        # Set up heading Workout label
        self.headingTop = QLabel(self)
        self.headingTop.setText("Workout Activity")
        self.headingTop.move(60, 120)
        self.headingTop.setStyleSheet(f"color: {atlantic}; background-color: {bg_color}")
        self.headingTop.setFont(inter48)
        
        # Set up heading Workout Plan label
        self.headingBottom = QLabel(self)
        self.headingBottom.setText("Workout Plan")
        self.headingBottom.move(60, 500)
        self.headingBottom.setStyleSheet(f"color: {atlantic}; background-color: {bg_color}")
        self.headingBottom.setFont(inter48)

        # Set up workout cards with empty set
        self.workoutCards = []
        for i in range(3):
            self.workoutCards.append({})
            self.workoutCards[i]["card"] = QLabel(self)
            self.workoutCards[i]["card"].setGeometry(QRect(150 + (i * 340), 188, 300, 300))
            self.workoutCards[i]["card"].setStyleSheet(f"background-color: {bg_color}")
            self.workoutCards[i]["card"].setPixmap(QPixmap("images/template-yellow-card.png"))
            self.workoutCards[i]["cardIllustration"] = QLabel(self)
            self.workoutCards[i]["cardIllustration"].setGeometry(QRect(240 + (i%3*340), 200, 120, 120))
            self.workoutCards[i]["cardIllustration"].setStyleSheet(f"background-color: {yellow}")
            self.workoutCards[i]["cardIllustration"].setPixmap(QPixmap("images/push-up.png"))
            self.workoutCards[i]["cardTitle"] = QLabel(self)
            self.workoutCards[i]["cardTitle"].setGeometry(QRect(172 + (i%3*340), 339, 90, 20))
            self.workoutCards[i]["cardTitle"].setStyleSheet(f"color: {primary_black}; background-color: {light_yellow}")
            self.workoutCards[i]["cardTitle"].setText("Title")
            self.workoutCards[i]["cardTitle"].setFont(inter16bold)
            self.workoutCards[i]["cardDescription"] = QLabel(self)
            self.workoutCards[i]["cardDescription"].setText("Description")
            self.workoutCards[i]["cardDescription"].setGeometry(QRect(172 + (i%3*340), 366, 256, 64))
            self.workoutCards[i]["cardDescription"].setStyleSheet(f"color: {primary_black}; background-color: {light_yellow}")
            self.workoutCards[i]["cardDescription"].setFont(inter10)
            self.workoutCards[i]["cardSpecification"] = QLabel(self)
            self.workoutCards[i]["cardSpecification"].setText("Specification")
            self.workoutCards[i]["cardSpecification"].setGeometry(QRect(350 + (i*340), 344, 80, 14))
            self.workoutCards[i]["cardSpecification"].setStyleSheet(f"color: {primary_black}; background-color: {light_yellow}")
            self.workoutCards[i]["cardSpecification"].setFont(inter12)

            self.workoutCards[i]["cardAddButton"] = QPushButton(self)
            self.workoutCards[i]["cardAddButton"].setGeometry(QRect(308 + (i*340), 441, 120, 30))
            self.workoutCards[i]["cardAddButton"].setText("Add To Activity")
            self.workoutCards[i]["cardAddButton"].setStyleSheet(f"color: #ffffff; background-color: {dark_yellow}; border: none; border-radius: 12px; font-weight: bold;")
            self.workoutCards[i]["cardAddButton"].clicked.connect(lambda x, i=i: self.addWorkoutCardToActivity(i))

            self.workoutCards[i]["cardTutorialButton"] = QPushButton(self)
            self.workoutCards[i]["cardTutorialButton"].setGeometry(QRect((172) + (i*340), 441, 90, 30))
            self.workoutCards[i]["cardTutorialButton"].setText("Tutorial")
            self.workoutCards[i]["cardTutorialButton"].setStyleSheet(f"color: #6E7198; background: transparent; border: 2px solid; border-color: #6E7198; border-radius: 12px;")
            self.workoutCards[i]["cardTutorialButton"].clicked.connect(lambda x, i=i: self.openTutorial(i))
        
        self.workoutPlanCards = []
        for i in range(3):
            self.workoutPlanCards.append({})
            self.workoutPlanCards[i]["card"] = QLabel(self)
            self.workoutPlanCards[i]["card"].setPixmap(QPixmap("images/template-blue-card.png"))
            self.workoutPlanCards[i]["card"].setStyleSheet(f"background-color: {bg_color}")
            self.workoutPlanCards[i]["card"].move(150 + (i%3*340), 568)
            self.workoutPlanCards[i]["cardTitle"] = QLabel(self)
            self.workoutPlanCards[i]["cardTitle"].setText("Title")
            self.workoutPlanCards[i]["cardTitle"].move(172 + (i%3*340), 586)
            self.workoutPlanCards[i]["cardTitle"].setStyleSheet(f"color: {primary_white}; background-color: {grape}")
            self.workoutPlanCards[i]["cardTitle"].setFont(inter24bold)
            self.workoutPlanCards[i]["cardDescription"] = QLabel(self)
            self.workoutPlanCards[i]["cardDescription"].setText("Desciption")
            self.workoutPlanCards[i]["cardDescription"].move(172 + (i%3*340), 620)
            self.workoutPlanCards[i]["cardDescription"].setStyleSheet(f"color: {primary_white}; background-color: {grape}")
            self.workoutPlanCards[i]["cardDescription"].setFont(inter12)
            self.workoutPlanCards[i]["cardSeeMoreButton"] = QPushButton(self)
            self.workoutPlanCards[i]["cardSeeMoreButton"].setGeometry(QRect(337 + (i*340), 586, 90, 30))
            self.workoutPlanCards[i]["cardSeeMoreButton"].setText("See More")
            self.workoutPlanCards[i]["cardSeeMoreButton"].setStyleSheet(f"color: {primary_white}; background-color: {primary_button}; border: none; border-radius: 12px; font-weight: bold;")
            self.workoutPlanCards[i]["cardSeeMoreButton"].clicked.connect(lambda x, i=i: self.openWorkoutPlan(i))

    def setUpDisplayWorkout(self):
        if self.listWorkoutPlan == None:
            listWorkout = self.workout
        else:
            # Untuk kasus display workout dalam sebuah workout plan
            listWorkout = self.listWorkoutPlan

        start = self.pageWorkout*3
        for i in range(3):
            if start+i < len(listWorkout):
                self.workoutCards[i]["cardTitle"].setText(listWorkout[start+i]["name"])
                self.workoutCards[i]["cardIllustration"].setPixmap(QPixmap(listWorkout[start+i]["linkIllustration"]))
                self.workoutCards[i]["cardDescription"].setText(listWorkout[start+i]["description"])
                self.workoutCards[i]["cardSpecification"].setText(listWorkout[start+i]["specification"])
                self.workoutCards[i]["card"].show()
                self.workoutCards[i]["cardIllustration"].show()
                self.workoutCards[i]["cardTitle"].show()
                self.workoutCards[i]["cardDescription"].show()
                self.workoutCards[i]["cardSpecification"].show()
                self.workoutCards[i]["cardAddButton"].show()
                self.workoutCards[i]["cardTutorialButton"].show()
            else:
                self.workoutCards[i]["card"].hide()
                self.workoutCards[i]["cardIllustration"].hide()
                self.workoutCards[i]["cardTitle"].hide()
                self.workoutCards[i]["cardDescription"].hide()
                self.workoutCards[i]["cardSpecification"].hide()
                self.workoutCards[i]["cardAddButton"].hide()
                self.workoutCards[i]["cardTutorialButton"].hide()

    def setUpDisplayWorkoutPlan(self):
        startWorkoutPlan = self.pageWorkoutPlan*3
        for i in range(3):
            if startWorkoutPlan+i < len(self.workoutPlan):
                self.workoutPlanCards[i]["cardTitle"].setText(self.workoutPlan[startWorkoutPlan+i]["name"])
                self.workoutPlanCards[i]["cardDescription"].setText(self.workoutPlan[startWorkoutPlan+i]["description"])
                self.workoutPlanCards[i]["card"].show()
                self.workoutPlanCards[i]["cardTitle"].show()
                self.workoutPlanCards[i]["cardDescription"].show()
                self.workoutPlanCards[i]["cardSeeMoreButton"].show()
            else:
                self.workoutPlanCards[i]["card"].hide()
                self.workoutPlanCards[i]["cardTitle"].hide()
                self.workoutPlanCards[i]["cardDescription"].hide()
                self.workoutPlanCards[i]["cardSeeMoreButton"].hide()

    def addWorkoutCardToActivity(self, idx):
        idx += self.pageWorkout*3
        print("add", self.workout[idx]["name"], "to activity")
        # add workout to history

    def openTutorial(self, idx):
        idx += self.pageWorkout*3
        webbrowser.open(self.workout[idx]["linkTutorial"])
    
    def openWorkoutPlan(self, idx):
        idx += self.pageWorkoutPlan*3
        # change view to page workout plan
        print("Open workout plan", self.workoutPlan[idx]["name"])
        self.headingTop.setText(self.workoutPlan[idx]["name"])
        self.pageWorkout = 0
        
        # masih data dummy
        listWorkoutPlan = []
        c = self.conn.cursor()
        c.execute("""
            SELECT olahraga_id, name, description, specification, linkIllustration, linkTutorial
            FROM workout NATURAL JOIN list_olahraga
            WHERE request_id = ?
        """, [self.workoutPlan[idx]["id"]])
        temp = c.fetchall()
        c.close()
        print("panjang temp", len(temp))
        for t in temp:
            listWorkoutPlan.append({
                "olahraga_id": t[0],
                "name": t[1],
                "description": t[2],
                "specification": t[3],
                "linkIllustration": t[4],
                "linkTutorial": t[5]
            })
        self.listWorkoutPlan = listWorkoutPlan

        self.headingBottom.hide()
        self.rightWorkoutPlanButton.hide()
        self.leftWorkoutPlanButton.hide()
        for i in range(3):
            self.workoutPlanCards[i]["card"].hide()
            self.workoutPlanCards[i]["cardTitle"].hide()
            self.workoutPlanCards[i]["cardDescription"].hide()
            self.workoutPlanCards[i]["cardSeeMoreButton"].hide()

        self.setUpDisplayWorkout()
        self.backWPButton.show()

    def rightWorkoutButtonClicked(self):
        print("Right workout button clicked")
        if (self.pageWorkout + 1 < (len(self.workout)//3)):
            self.pageWorkout += 1
            print("page: ", self.pageWorkout)
            self.setUpDisplayWorkout()
        else:
            print("No more workout")

    def leftWorkoutButtonClicked(self):
        print("Left workout button clicked")
        if (self.pageWorkout > 0):
            self.pageWorkout -= 1
            print("page: ", self.pageWorkout)
            self.setUpDisplayWorkout()
        else:
            print("No more workout")

    def rightWorkoutPlanButtonClicked(self):
        print("Right workout plan button clicked")
        if (self.pageWorkoutPlan + 1 < (len(self.workoutPlan)//3)):
            self.pageWorkoutPlan += 1
            print("page: ", self.pageWorkoutPlan)
            self.setUpDisplayWorkoutPlan()
        else:
            print("No more workout plan")

    def leftWorkoutPlanButtonClicked(self):
        print("Left workout plan button clicked")
        if (self.pageWorkoutPlan > 0):
            self.pageWorkoutPlan -= 1
            print("page: ", self.pageWorkoutPlan)
            self.setUpDisplayWorkoutPlan()
        else:
            print("No more workout plan")
    
    def backWP(self):
        print("Back Button pressed")
        self.listWorkoutPlan = None
        self.pageWorkout = 0
        self.headingTop.setText("Workout Activity")
        self.headingBottom.show()
        self.rightWorkoutPlanButton.show()
        self.leftWorkoutPlanButton.show()
        self.backWPButton.hide()
        self.setUpDisplayWorkout()
        self.setUpDisplayWorkoutPlan()
    
    def fetchWorkout(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM list_olahraga")
        workouts = c.fetchall()
        c.close()

        dataWorkout = []
        for workout in workouts:
            dataWorkout.append({
                "olahraga_id": workout[0],
                "name": workout[1],
                "description": workout[2],
                "specification": workout[3],
                "linkIllustration": workout[4],
                "linkTutorial": workout[5]
            })
        self.workout = dataWorkout
    
    def fetchWorkoutPlan(self, user):
        c = self.conn.cursor()
        c.execute("""
            SELECT request_id, title, description
            FROM daftar_request
            WHERE user_id = ?
        """, [user["id"]])
        workoutPlans = c.fetchall()
        c.close()

        dataWorkoutPlan = []
        for workoutPlan in workoutPlans:
            dataWorkoutPlan.append({
                "id": workoutPlan[0],
                "name": workoutPlan[1],
                "description": workoutPlan[2]
            })
        self.workoutPlan = dataWorkoutPlan
        self.setUpDisplayWorkoutPlan()

    def updateUser(self, user):
        self.user = user
        self.helloLabel.setText(f"Hello, {self.user['fullname']}!")
    
    def logOut(self):
        self.switch.emit("login", {})

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DisplayWorkout()
    window.show()
    sys.exit(app.exec())
