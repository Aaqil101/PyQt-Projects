# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QFont, QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# Main App Objects and Settings
# Initialize the main application object
# Set application settings such as window title, size, and icon
app = QApplication([])
window = QWidget()
window.setWindowTitle("Calculator")
window.setWindowIcon(QIcon("icon.png"))
# window.resize(250, 300)
window.setFixedSize(250, 300)
window.setWindowFlags(window.windowFlags() | Qt.WindowStaysOnTopHint)
window.setStyleSheet(
    """
    QWidget {
        background-color: #404040;
    }
    """
)

# Create all App Objects
# Create the main window object
# Create buttons, display, and other widgets
text_box = QLineEdit()
text_box.setFixedHeight(35)
text_box.setFont(QFont("Arial", 15, QFont.Bold))
text_box.setAlignment(Qt.AlignmentFlag.AlignRight)
text_box.setValidator(QDoubleValidator())
text_box.setStyleSheet(
    """
    QLineEdit {
        background-color: #ffffff;
        padding: 3px 6px;
        border-radius: 8px;
    }
    """
)

grid = QGridLayout()

buttons = [
    "7",
    "8",
    "9",
    "/",
    "4",
    "5",
    "6",
    "*",
    "1",
    "2",
    "3",
    "-",
    "0",
    ".",
    "=",
    "+",
]

clear = QPushButton("C")
clear.setStyleSheet(
    """
    QPushButton {
        background-color: #ff3b3b;
        color: black;
        font-size: 16px;
        font-weight: bold;
        padding: 3px 6px;
        border-radius: 8px;
        border: 2px solid #d32f2f;
    }

    QPushButton:hover {
        background-color: #d32f2f;
        border: 2px solid #b71c1c;
    }

    QPushButton:pressed {
        background-color: #b71c1c;
        border: 2px solid #9a0007;
    }
    """
)

delete = QPushButton(">")
delete.setStyleSheet(
    """
    QPushButton {
        background-color: #4a90e2; /* Blue */
        color: white;
        font-size: 16px;
        font-weight: bold;
        padding: 3px 6px;
        border-radius: 8px;
        border: 2px solid #357ABD;
    }

    QPushButton:hover {
        background-color: #357ABD;
        border: 2px solid #2a5d9e;
    }

    QPushButton:pressed {
        background-color: #2a5d9e;
        border: 2px solid #1f447d;
    }
    """
)

row = 0
col = 0

for button in buttons:
    button = QPushButton(button)
    # button.clicked.connect(None)
    button.setStyleSheet(
        """
        QPushButton {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            font-weight: bold;
            padding: 3px 6px;
            border-radius: 8px;
            border: 2px solid #388E3C;
        }

        QPushButton:hover {
            background-color: #388E3C;
            border: 2px solid #2E7D32;
        }

        QPushButton:pressed {
            background-color: #2E7D32;
            border: 2px solid #1B5E20;
        }
        """
    )
    grid.addWidget(button, row, col)
    col += 1

    if col > 3:
        col = 0
        row += 1

# All Design Elements
# Set layout for the main window
# Add widgets to the layout
# Apply styles to the widgets
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)

button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)

master_layout.addLayout(button_row)

window.setLayout(master_layout)

# Create Functions
# Define functions for calculator operations (addition, subtraction, etc.)
# Define helper functions for updating the display, clearing the display, etc.

# Events
# Connect buttons to their respective functions
# Handle user input and button clicks

# Show/Run our App
# Show the main window
# Execute the application's main loop
window.show()
app.exec_()
