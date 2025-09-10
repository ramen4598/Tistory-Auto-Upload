# PyQt dialogs (skeleton)

from PyQt5.QtWidgets import QDialog

class AuthDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # TODO: 2차 인증 대기 안내 UI
