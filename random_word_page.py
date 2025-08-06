from PyQt5.QtCore import Qt
from PyQt5. QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from random import choice
from wordlist import my_words


def create_main_layout():
    layout = QVBoxLayout()

    row1 = QHBoxLayout()
    row2 = QHBoxLayout()
    row3 = QHBoxLayout()

    title = QLabel("Random Keywords")
    row1.addWidget(title, alignment=Qt.AlignCenter)

    layout.text1 = QLabel("?")
    layout.text2 = QLabel("??")
    layout.text3 = QLabel("???")

    row2.addWidget(layout.text1, alignment=Qt.AlignCenter)
    row2.addWidget(layout.text2, alignment=Qt.AlignCenter)
    row2.addWidget(layout.text3, alignment=Qt.AlignCenter)

    button1 = QPushButton("Click Me Once")
    button2 = QPushButton("Click Me Twice")
    button3 = QPushButton("Click Me Three")
    switch_button = QPushButton("Switch Layaout")

    row3.addWidget(button1)
    row3.addWidget(button2)
    row3.addWidget(button3)
    row3.addWidget(switch_button)

    def random_Word1():
        word = choice(my_words)
        layout.text1.setText(word)

    def random_Word2():
        word = choice(my_words)
        layout.text2.setText(word)

    def random_Word3():
        word = choice(my_words)
        layout.text3.setText(word)

    layout.addLayout(row1)
    layout.addLayout(row2)
    layout.addLayout(row3)

    button1.clicked.connect(random_Word1)
    button2.clicked.connect(random_Word2)
    button3.clicked.connect(random_Word3)

    layout.switch_button = switch_button

    return layout
