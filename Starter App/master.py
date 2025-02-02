# Import Modules
from random import choice

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# Main App Objects and Settings
app = QApplication([])
window = QWidget()
window.setWindowTitle("Starter App")
window.resize(300, 200)

# Create all App Objects
title = QLabel("Ready to Start?")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click Me")
button2 = QPushButton("Click Me")
button3 = QPushButton("Click Me")

texts = [text1, text2, text3]
buttons = [button1, button2, button3]
words = ["Blender", "3D", "Python", "Code", "Game", "Design", "Art", "Model", "Render"]

# All Design Elements
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()
#
rows = [row1, row2, row3]

row1.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)

for text in texts:
    row2.addWidget(text, alignment=Qt.AlignmentFlag.AlignCenter)

for button in buttons:
    row3.addWidget(button)

for row in rows:
    master_layout.addLayout(row)

window.setLayout(master_layout)


# Create Functions
def random_word1():
    word = choice(words)
    text1.setText(word)


def random_word2():
    word = choice(words)
    text2.setText(word)


def random_word3():
    word = choice(words)
    text3.setText(word)


# Events
button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)

# Show/Run our App
window.show()
app.exec_()
