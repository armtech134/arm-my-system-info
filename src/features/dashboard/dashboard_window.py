from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from features.basic_info.basic_info_list import BasicInfoList


class DashboardWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My System Info")
    container = QWidget()
    layout = QVBoxLayout(container)
    layout.addWidget(BasicInfoList())
    self.setCentralWidget(container)
