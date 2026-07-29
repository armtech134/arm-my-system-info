from PySide6.QtWidgets import QVBoxLayout, QWidget

from features.ram_info.info import get_ram_info
from shared.widgets import ListView


class RamInfoList(QWidget):
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout(self)
    layout.addWidget(ListView(label="RAM Info", items=get_ram_info()))
