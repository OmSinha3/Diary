import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton
import mysql.connector

class DiaryWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create GUI
        self.setWindowTitle('Online Diary')
        self.setGeometry(100, 100, 500, 500)

        self.text_area = QTextEdit(self)
        self.text_area.setGeometry(50, 50, 400, 300)

        self.save_button = QPushButton('Save', self)
        self.save_button.setGeometry(50, 370, 100, 50)
        self.save_button.clicked.connect(self.save_entry)

        self.retrieve_button = QPushButton('Retrieve', self)
        self.retrieve_button.setGeometry(350, 370, 100, 50)
        self.retrieve_button.clicked.connect(self.retrieve_entries)

        # Connect to MySQL
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='diary'
        )
        self.cursor = self.db.cursor()

        # Create table
        self.cursor.execute('CREATE TABLE IF NOT EXISTS diary (id INT AUTO_INCREMENT PRIMARY KEY, entry TEXT)')

    def save_entry(self):
        entry = self.text_area.toPlainText()
        self.cursor.execute('INSERT INTO diary (entry) VALUES (%s)', (entry,))
        self.db.commit()

    def retrieve_entries(self):
        self.cursor.execute('SELECT * FROM diary')
        entries = self.cursor.fetchall()
        for entry in entries:
            print(entry)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DiaryWindow()
    window.show()
    sys.exit(app.exec_())
