import sys
import sqlite3
from PyQt6.QtWidgets import QApplication
from login_window import LoginWindow
from register_window import RegisterWindow

class Controller:
  def __init__(self):
    self.loginWindow = LoginWindow()
    self.loginWindow.switch.connect(self.showRegister)
    self.registerWindow = RegisterWindow()
    self.registerWindow.switch.connect(self.showLogin)
    self.initializeDatabase()
    pass

  def showLogin(self):
    self.registerWindow.close()
    self.loginWindow.show()

  def showRegister(self):
    self.loginWindow.close()
    self.registerWindow.show()
  
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
    self.conn.commit()
    self.conn.close()

if __name__ == "__main__":
  app = QApplication(sys.argv)
  controller = Controller()
  controller.showLogin()
  sys.exit(app.exec())