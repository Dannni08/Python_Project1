# Import Modules
from calculator import create_second_layout
from random_word_page import create_main_layout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStackedLayout

from random_word_page import create_main_layout
from calculator import create_second_layout


# Main App Objects and Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Inventory")
main_window.resize(300, 200)

stacked_layout = QStackedLayout()


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


main_window.setLayout(stacked_layout)
main_window.show()
app.exec()
