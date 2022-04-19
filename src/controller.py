import sys
import sqlite3
from tkinter import E
from PyQt6.QtWidgets import QApplication
from login_window import LoginWindow
from register_window import RegisterWindow
from dashboard_user import UserDashboard
from dashboard_trainer import TrainerDashboard
from add_workout import trainer_AddWorkout
from display_workout import DisplayWorkout
from display_workout_trainer import DisplayWorkoutTrainer
from workout_history import WorkoutHistory
from add_history import addHistory

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
        self.displayWorkoutTrainer.switch.connect(self.fromDisplayWorkoutTrainer)
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
    
    def fromAddHistory(self, page, user):
        self.addHistory.close()
        if page == "workout_history":
            self.workoutHistory.updateUser(user)
            self.workoutHistory.updateWorkoutHistory()
            self.workoutHistory.show()
            
    def initializeDatabase(self):
        self.conn = sqlite3.connect("fitpal.db")
        c = self.conn.cursor()
        c.execute("""
          CREATE TABLE IF NOT EXISTS user (
            user_id integer PRIMARY KEY AUTOINCREMENT,
            fullname text,
            username text,
            email text,
            password text,
            type text
          )
        """)
        c.execute("""
          CREATE TABLE IF NOT EXISTS list_olahraga (
            olahraga_id integer PRIMARY KEY AUTOINCREMENT,
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
            request_id integer PRIMARY KEY AUTOINCREMENT,
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
            olahraga_id integer,
            specification text,
            date text,
            FOREIGN KEY(olahraga_id) REFERENCES list_olahraga(olahraga_id)
          )
        """)
        self.conn.commit()
        self.conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.start()
    sys.exit(app.exec())
