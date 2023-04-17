import sys
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow,
                               QHBoxLayout, QVBoxLayout,
                               QCheckBox, QLineEdit, QPushButton)

from downloader import Downloader

class MainWindow(QMainWindow):
    """
    finestra principale (e unica) dell'applicazione
    """
    def __init__(self):
        super().__init__()

        self.make_ui()
        self.make_internals()
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

    def make_internals(self):
        self.downloader = Downloader()

    def connect_ui(self):
        self.download_button.clicked.connect(self.download_command)

    def download_command(self):
        self.downloader.download(link=self.link_widget.text(),
                                 down_playlist=self.playlist_checkbox.isChecked(),
                                 just_audio=self.just_audio_checkbox.isChecked())
        print("Hello from the other side")
        if self.playlist_checkbox.isChecked():
            print("playlist")
        if self.just_audio_checkbox.isChecked():
            print("just the audio")

if __name__ == "__main__":
    app = QApplication()
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
