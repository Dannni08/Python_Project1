from PyQt5.QtCore import Qt
from PyQt5. QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout


def create_second_layout():
    layout = QVBoxLayout()

    row1 = QHBoxLayout()
    last_row = QHBoxLayout()

    title = QLabel("Page 2")
    row1.addWidget(title, alignment=Qt.AlignCenter)

    back_button = QPushButton("Back to Main")
    last_row.addWidget(back_button)

    layout.back_button = back_button

    layout.addLayout(row1)
    layout.addLayout(last_row)

    return layout
