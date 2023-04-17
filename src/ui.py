import sys
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow,
                               QHBoxLayout, QVBoxLayout,
                               QCheckBox, QLineEdit, QPushButton)

class MainWindow(QMainWindow):
    """
    finestra principale (e unica) dell'applicazione
    """
    def __init__(self):
        super().__init__()

        self.make_ui()
        self.connect_ui()

    def make_ui(self):
        """
        layout desiderato
        |----------------------------------|
        |  INCOLLA LINK QUI                |
        |  BOTTONE    checkbox opzione     |
        |             checkbox opzione     |
        |             ...                  |
        |                                  |
        |----------------------------------|
        """
        self.link_widget = QLineEdit()
        self.download_button = QPushButton("Download")

        self.playlist_checkbox = QCheckBox("playlist")
        self.just_audio_checkbox = QCheckBox("just the audio")

        self.main_column = QVBoxLayout()
        self.main_column.addWidget(self.link_widget)
        self.main_column.addWidget(self.download_button)

        self.checkbox_column = QVBoxLayout()
        self.checkbox_column.addWidget(self.playlist_checkbox)
        self.checkbox_column.addWidget(self.just_audio_checkbox)

        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(self.main_column)
        self.main_layout.addLayout(self.checkbox_column)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

    def connect_ui(self):
        self.download_button.clicked.connect(self.download_command)

    def download_command(self):
        print("Hello from the other side")

if __name__ == "__main__":
    app = QApplication()
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
