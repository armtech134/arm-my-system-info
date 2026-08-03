from PySide6.QtWidgets import QVBoxLayout, QWidget

from features.basic_info.info import get_basic_info
from shared.widgets import ListView


class BasicInfoList(QWidget):
  def __init__(self):
    super().__init__()

    layout = QVBoxLayout(self)
    layout.addWidget(ListView(label="Info", items=get_basic_info()))

