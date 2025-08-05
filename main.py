# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStackedLayout

from random import choice

my_words = ['apple', 'mirror', 'cloud', 'galaxy', 'blanket', 'tunnel', 'whisper', 'quartz', 'fire', 'moss', 'feather', 'canyon', 'pencil', 'orbit', 'shadow', 'thunder', 'lantern', 'gravel', 'ripple', 'shimmer', 'voyage', 'prism', 'velvet', 'blaze', 'cobweb', 'glacier', 'comet', 'branch', 'maple', 'bronze', 'spark', 'horizon', 'fossil', 'silence', 'willow', 'anchor', 'ladder', 'jungle', 'copper', 'storm', 'echo', 'turbine', 'crystal', 'raindrop', 'velvet', 'lantern', 'pine', 'summit', 'meadow', 'blaze', 'pebble', 'twilight', 'rocket', 'falcon', 'dune', 'clover', 'brook', 'drift', 'shield', 'geyser', 'magnet', 'riddle', 'blossom', 'bamboo', 'compass', 'nectar', 'marble', 'echo', 'timber', 'breeze', 'canyon', 'blaze', 'orbit', 'frost', 'silence', 'lante'
            ]

# Main App Objects and Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Inventory")
main_window.resize(300, 200)

stacked_layout = QStackedLayout()


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


def create_second_layout():
    layout = QVBoxLayout()

    row1 = QHBoxLayout()
    row2 = QHBoxLayout()

    title = QLabel("Page 2")
    row1.addWidget(title, alignment=Qt.AlignCenter)

    button1 = QPushButton("Click Me Once")
    back_button = QPushButton("Back to Main")
    row2.addWidget(back_button)

    layout.text1 = QLabel("?")
    layout.text2 = QLabel("??")
    layout.text3 = QLabel("???")

    layout.back_button = back_button

    layout.addLayout(row1)
    layout.addLayout(row2)

    return layout


main_layout = create_main_layout()
second_layout = create_second_layout()

main_widget = QWidget()
main_widget.setLayout(main_layout)

second_widget = QWidget()
second_widget.setLayout(second_layout)

stacked_layout.addWidget(main_widget)
stacked_layout.addWidget(second_widget)

main_layout.switch_button.clicked.connect(
    lambda: stacked_layout.setCurrentWidget(second_widget))
second_layout.back_button.clicked.connect(
    lambda: stacked_layout.setCurrentWidget(main_widget))

# # Create all App Objects


# text1 = QLabel("?")
# text2 = QLabel("??")
# text3 = QLabel("???")

# button1 = QPushButton("Click Me Once")
# button2 = QPushButton("Click Me Twice")
# button3 = QPushButton("Click Me Three")
# switch_button = QPushButton("Switch Layaout")


# # All Design Here
# main_layout = create_main_layout()
# second_layout = create_secondary_layout()

# master_layout = QVBoxLayout()

# row1 = QHBoxLayout()
# row2 = QHBoxLayout()
# row3 = QHBoxLayout()
# #
# row1.addWidget(title, alignment=Qt.AlignCenter)

# row2.addWidget(text1, alignment=Qt.AlignCenter)
# row2.addWidget(text2, alignment=Qt.AlignCenter)
# row2.addWidget(text3, alignment=Qt.AlignCenter)

# row3.addWidget(button1)
# row3.addWidget(button2)
# row3.addWidget(button3)

# master_layout.addLayout(row1)
# master_layout.addLayout(row2)
# master_layout.addLayout(row3)
# row3.addWidget(switch_button)

# main_window.setLayout(master_layout)

# #  Create Functions


# def random_Word1():
#     word = choice(my_words)
#     text1.setText(word)


# def random_Word2():
#     word = choice(my_words)
#     text2.setText(word)


# def random_Word3():
#     word = choice(my_words)
#     text3.setText(word)


# # Events
# button1.clicked.connect(random_Word1)
# button2.clicked.connect(random_Word2)
# button3.clicked.connect(random_Word3)

# layout.switch_button = switch_button

# Show/Run our App
main_window.setLayout(stacked_layout)
main_window.show()
app.exec()
