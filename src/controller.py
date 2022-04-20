import os.path
import sqlite3
import sys
from tkinter import E

from PyQt6.QtWidgets import QApplication

from add_history import addHistory
from add_workout import trainer_AddWorkout
from dashboard_trainer import TrainerDashboard
from dashboard_user import UserDashboard
from display_workout import DisplayWorkout
from display_workout_trainer import DisplayWorkoutTrainer
from login_window import LoginWindow
from register_window import RegisterWindow
from workout_history import WorkoutHistory


class Controller:
    def __init__(self):
        self.initializeDatabase()
        self.loginWindow = LoginWindow()
        self.loginWindow.switch.connect(self.fromLogin)
        self.registerWindow = RegisterWindow()
        self.registerWindow.switch.connect(self.fromRegister)
        self.userDashboard = UserDashboard()
        self.userDashboard.switch.connect(self.fromUserDashboard)
        self.trainerDashboard = TrainerDashboard()
        self.trainerDashboard.switch.connect(self.fromTrainerDashboard)
        self.addWorkout = trainer_AddWorkout()
        self.addWorkout.switch.connect(self.fromAddWorkout)
        self.displayWorkout = DisplayWorkout()
        self.displayWorkout.switch.connect(self.fromDisplayWorkout)
        self.displayWorkoutTrainer = DisplayWorkoutTrainer()
        self.displayWorkoutTrainer.switch.connect(
            self.fromDisplayWorkoutTrainer)
        self.workoutHistory = WorkoutHistory()
        self.workoutHistory.switch.connect(self.fromWorkoutHistory)
        self.addHistory = addHistory()
        self.addHistory.switch.connect(self.fromAddHistory)
        pass

    def start(self):
        self.loginWindow.show()

    def fromRegister(self):
        self.registerWindow.close()
        self.loginWindow.clearForm()
        self.loginWindow.show()

    def fromLogin(self, page, user):
        self.loginWindow.close()
        if page == "register":
            self.registerWindow.show()
        elif page == "user_dashboard":
            self.displayWorkout.fetchWorkoutPlan(user)
            self.userDashboard.updateUser(user)
            self.userDashboard.show()
        elif page == "trainer_dashboard":
            self.trainerDashboard.updateUser(user)
            self.trainerDashboard.show()

    def fromUserDashboard(self, page, user):
        self.userDashboard.close()
        if page == "login":
            self.loginWindow.clearForm()
            self.loginWindow.show()
        elif page == "display_workout":
            self.displayWorkout.updateUser(user)
            self.displayWorkout.updateDisplayWorkout()
            self.displayWorkout.show()
        elif page == "finish_workout":
            self.workoutHistory.updateUser(user)
            self.workoutHistory.updateWorkoutHistory()
            self.workoutHistory.show()

    def fromTrainerDashboard(self, page, user):
        self.trainerDashboard.close()
        if page == "login":
            self.loginWindow.clearForm()
            self.loginWindow.show()
        elif page == "display_workout":
            self.displayWorkoutTrainer.updateUser(user)
            self.displayWorkoutTrainer.updateDisplayWorkout()
            self.displayWorkoutTrainer.show()
        elif page == "add_workout":
            self.addWorkout.updateUser(user)
            self.addWorkout.show()

    def fromAddWorkout(self, page, user):
        self.addWorkout.close()
        if page == "login":
            self.loginWindow.clearForm()
            self.loginWindow.show()
        elif page == "display_workout":
            self.displayWorkoutTrainer.updateUser(user)
            self.displayWorkoutTrainer.updateDisplayWorkout()
            self.displayWorkoutTrainer.show()

    def fromDisplayWorkout(self, page, user):
        self.displayWorkout.close()
        if page == "login":
            self.loginWindow.clearForm()
            self.loginWindow.show()
        elif page == "user_dashboard":
            self.userDashboard.updateUser(user)
            self.userDashboard.show()

    def fromDisplayWorkoutTrainer(self, page, user):
        self.displayWorkoutTrainer.close()
        if page == "login":
            self.loginWindow.clearForm()
            self.loginWindow.show()
        elif page == "trainer_dashboard":
            self.trainerDashboard.updateUser(user)
            self.trainerDashboard.show()
        elif page == "add_workout":
            self.addWorkout.updateUser(user)
            self.addWorkout.show()

    def fromWorkoutHistory(self, page, user):
        self.workoutHistory.close()
        if page == "user_dashboard":
            self.userDashboard.updateUser(user)
            self.userDashboard.show()
        elif page == "add_history":
            self.addHistory.updateUser(user)
            self.addHistory.show()
        elif page == "login":
            self.loginWindow.clearForm()
            self.loginWindow.show()

    def fromAddHistory(self, page, user):
        self.addHistory.close()
        if page == "workout_history":
            self.workoutHistory.updateUser(user)
            self.workoutHistory.updateWorkoutHistory()
            self.workoutHistory.show()

    def initializeDatabase(self):
        if not os.path.exists("fitpal.db"):
            self.conn = sqlite3.connect("fitpal.db")
            c = self.conn.cursor()
            c.execute("""
            CREATE TABLE IF NOT EXISTS user (
            id integer PRIMARY KEY,
            fullname text,
            username text,
            email text,
            password text,
            type text
            )
            """)
            c.execute("""
            CREATE TABLE IF NOT EXISTS list_olahraga (
            olahraga_id integer PRIMARY KEY,
            name text,
            description text,
            specification text,
            linkIllustration text,
            linkTutorial text,
            forUser integer
            )
            """)
            c.execute("""
            CREATE TABLE IF NOT EXISTS daftar_request (
            request_id integer PRIMARY KEY,
            user_id integer,
            trainer_id integer,
            umur integer,
            jenis_kelamin text,
            berat_badan integer,
            tinggi_badan integer,
            tujuan text,
            status boolean,
            title text,
            description text
            )
            """)
            c.execute("""
            CREATE TABLE IF NOT EXISTS workout (
            request_id integer,
            olahraga_id integer,
            status boolean
            )
            """)
            c.execute("""
            CREATE TABLE IF NOT EXISTS workout_history (
            history_id integer PRIMARY KEY AUTOINCREMENT,
            user_id integer,
            olahraga_id integer,
            name text,
            specification text,
            date text
            )
            """)
            c.execute("""
            INSERT INTO list_olahraga 
                (name, description, specification, linkIllustration, linkTutorial, forUser)
            VALUES 
                ('Push Up', 'Push-ups are exercises to strengthen your arms and \nchest muscles. They are done by lying with your face \ntowards the floor and pushing with your hands to \nraise your body until your arms are straight.', '10 Repetition', '../img/push-up.png', 'https://www.youtube.com/watch?v=bTJIkQRsmaE', NULL),
                ("Sit Up", "Sit-ups are exercises that you do to strengthen your \nstomach muscles. They involve sitting up from a lying \nposition while keeping your legs straight on the floor.", "10 Repetition", "../img/sit-up.png", "https://www.youtube.com/watch?v=6eJVLbgxbBE", NULL),
                ("Pull Up", "A pull-up is an upper-body strength exercise. The \npull-up is a closed-chain movement where the body \nis suspended by the hands and pulls up.", "10 Repetition", "../img/pull-up.png", "https://www.youtube.com/watch?v=eGo4IYlbE5g", NULL),
                ("Jumping Rope", "Jumping rope is jumping over a rope held with \none end in each hand as the rope is repeatedly \nspun over the head and under the feet.", "20 Repetition", "../img/jumping-rope.png", "https://www.youtube.com/watch?v=FJmRQ5iTXKE", NULL),
                ("Weightlifting", "Weight training is a common type of strength training \nfor developing the strength and size of skeletal \nmuscles.", "70Kg", "../img/weightlifting.png", "https://www.youtube.com/watch?v=RP85w6g7jPU", NULL),
                ("Swimming", "The propulsion of the body through water by \ncombined arm and leg motions and the natural \nflotation of the body.", "300 meters", "../img/swimming.png", "https://www.youtube.com/watch?v=gh5mAtmeR3Y", NULL),
                ("Running", "Running is a form of exercise that is usually \ndone to develop the speed and endurance of the body.", "5Km", "../img/running.png", "https://www.youtube.com/watch?v=ZQQ6_XQQxQ4", NULL)
            """)
            c.execute("""
            INSERT INTO daftar_request
                (user_id, trainer_id, umur, jenis_kelamin, berat_badan, tinggi_badan, tujuan, status, title, description)
            VALUES
                (1, 2, 20, 'Laki-laki', 65, 170, 'I want to have a sixpack stomach', True, 'Chest Day', 'This workout plan is made to strengthen your \nabdominal muscles.'),
                (1,2,20, 'Laki-laki', 65, 170, 'I want to have a strong leg muscles', True, 'Leg Day', 'This workout plan is made to strengthen your \nleg muscles.')
            """)
            c.execute("""
            INSERT INTO workout
                (request_id, olahraga_id, status)
            VALUES
                (1, 2, False),
                (1, 3, False),
                (1, 6, False),
                (2, 4, False),
                (2, 7, False)
            """)

            self.conn.commit()
            self.conn.commit()
            self.conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.start()
    sys.exit(app.exec())
