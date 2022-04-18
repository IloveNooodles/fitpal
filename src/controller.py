import sys
import sqlite3
from PyQt6.QtWidgets import QApplication
from login_window import LoginWindow
from register_window import RegisterWindow
from dashboard_user import UserDashboard
from dashboard_trainer import TrainerDashboard
from add_workout import trainer_AddWorkout
from display_workout import DisplayWorkout
from display_workout_trainer import DisplayWorkoutTrainer

class Controller:
    def __init__(self):
        self.initializeDatabase()
        self.loginWindow = LoginWindow()
        self.loginWindow.switch.connect(self.fromLogin)
        self.registerWindow = RegisterWindow()
        self.registerWindow.switch.connect(self.fromRegister)
        self.userDashboard = UserDashboard()
        self.userDashboard.switch.connect(self.fromUserDashboard)
        self.addWorkout = trainer_AddWorkout()
        self.addWorkout.switch.connect(self.fromAddWorkout)
        self.displayWorkout = DisplayWorkout()
        self.displayWorkout.switch.connect(self.fromDisplayWorkout)
        self.displayWorkoutTrainer = DisplayWorkoutTrainer()
        self.displayWorkoutTrainer.switch.connect(
            self.fromDisplayWorkoutTrainer)
        self.finishWorkout = finish_workout()
        self.finishWorkout.switch.connect(self.fromFinishWorkout)
        self.trainerDashboard = TrainerDashboard()
        self.trainerDashboard.switch.connect(self.fromTrainerDashboard)
        self.loginWindow.show()
        pass

    def fromRegister(self):
        self.registerWindow.close()
        self.loginWindow.clearForm()
        self.loginWindow.show()

    def fromLogin(self, page, user):
        self.loginWindow.close()
        if page == "register":
            self.registerWindow.show()
        elif page == "user_dashboard":
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

    def fromTrainerDashboard(self, page, user):
        self.trainerDashboard.close()
        if page == "login":
            self.loginWindow.clearForm()
            self.loginWindow.show()
        elif page == "display_workout":
            self.displayWorkoutTrainer.updateUser(user)
            self.displayWorkoutTrainer.show()

    def fromAddWorkout(self, page, user):
        self.addWorkout.close()
        if page == "login":
            self.loginWindow.clearForm()
            self.loginWindow.show()
        elif page == "trainer_dashboard":
            self.trainerDashboard.updateUser(user)
            self.trainerDashboard.show()

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
        """)

    def fromUserDashboard(self, page, user):
        self.userDashboard.close()
        if page == "login":
            self.loginWindow.clearForm()
            self.loginWindow.show()
        elif page == "finish_workout":
            self.finishWorkout.updateUser(user)
            self.finishWorkout.show()

    def fromTrainerDashboard(self, page, user):
        self.trainerDashboard.close()
        if page == "login":
            self.loginWindow.clearForm()
            self.loginWindow.show()

    def fromFinishWorkout(self, page, user):
        self.finishWorkout.close()
        if page == "login":
            self.loginWindow.clearForm()
            self.loginWindow.show()
        elif page == "user_dashboard":
            self.userDashboard.updateUser(user)
            self.userDashboard.show()

    def initializeDatabase(self):
        self.conn = sqlite3.connect("fitpal.db")
        c = self.conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS user (
          fullname text,
          username text,
          email text,
          password text,
          type text
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
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.start()
    sys.exit(app.exec())
