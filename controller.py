import sys
import sqlite3
from PyQt6.QtWidgets import QApplication
from login_window import LoginWindow
from register_window import RegisterWindow
from dashboard_user import UserDashboard
from dashboard_trainer import TrainerDashboard
from add_workout import trainer_AddWorkout

class Controller:
  def __init__(self):
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
    self.initializeDatabase()
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
    elif page == "add_workout":
      self.addWorkout.updateUser(user)
      self.addWorkout.show()
  
  def fromAddWorkout(self, page, user):
    self.addWorkout.close()
    if page == "login":
      self.loginWindow.clearForm()
      self.loginWindow.show()
    elif page == "trainer_dashboard":
      self.trainerDashboard.updateUser(user)
      self.trainerDashboard.show()

  
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
      CREATE TABLE IF NOT EXISTS workout (
        title text,
        specification text,
        description text,
        illustration text,
        tutorial text
      )
    """)
    self.conn.commit()
    self.conn.close()

if __name__ == "__main__":
  app = QApplication(sys.argv)
  controller = Controller()
  controller.start()
  sys.exit(app.exec())