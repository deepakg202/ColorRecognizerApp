from pathlib import Path
import os
import sys

import cv2
from PyQt5 import __file__ as PYQTPATH
from PyQt5.QtGui import QColor, QCursor
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QFrame
from PyQt5.QtCore import Qt
from cvUtils import ColorRecognizer
from gui import UI
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.fspath(
    Path(PYQTPATH).resolve().parent / "Qt5" / "plugins"
)


class ProgramWindow(UI):
    def __init__(self, clipboard):
        super(ProgramWindow, self).__init__()
        self.setWindowTitle('Color Recognizer App')
        self.initializeOutputArea()
        self.colorRecognizer = ColorRecognizer()
        self.clipboard = clipboard
        self.rgbCode = ''

    def onMouseClickOnImageArea(self, event):
        if event.button() == Qt.LeftButton:
            x = event.pos().x()
            y = event.pos().y()
            try:
                qImg = self.imageArea.pixmap().toImage()
                c = qImg.pixel(x, y)
                self.rgbCode = QColor(c).getRgb()
                self.setColorOutput(self.rgbCode)
            except AttributeError:
                print('Wait While the image loads')

    def processImageAfterCapture(self, image):
        return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

    def initializeOutputArea(self):
        self.colorVisual = QFrame()
        self.colorCode = QLabel('Color Code: ')
        self.colorName = QLabel('Color Name: ')
        self.noteLabel = QLabel(
            'Note: The Name representing the color code may not be exact.')

        self.colorVisual.setStyleSheet("background-color:none;")
        self.outputBox.addWidget(self.colorVisual, 0, 0)
        self.outputBox.addWidget(self.colorName, 1, 0)
        self.outputBox.addWidget(self.colorCode, 2, 0)
        self.statusBar.addWidget(self.noteLabel)

        self.imageArea.setCursor(QCursor(Qt.CrossCursor))
        self.colorVisual.setCursor(QCursor(Qt.PointingHandCursor))
        self.colorVisual.setToolTip('Double Click to Copy Rgb Code')

        def copyColorToClipboard(event):
            self.clipboard.setText(f'rgba{self.rgbCode}')
        self.colorVisual.mouseDoubleClickEvent = copyColorToClipboard

    def setColorOutput(self, rgbCode):
        self.colorVisual.setStyleSheet(
            "background-color:rgba{};".format(str(rgbCode)))

        self.colorCode.setText('Color Code:\nrgba{}'.format(str(rgbCode)))
        self.colorName.setText('Color Name:\n{}'.format(
            self.colorRecognizer.getColorName(rgbCode)))


def main(args):
    app = QApplication(args)
    clipboard = app.clipboard()
    root = ProgramWindow(clipboard)
    root.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    sys.exit(main(sys.argv))
