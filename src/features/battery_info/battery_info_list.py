from PySide6.QtWidgets import QVBoxLayout, QWidget

from features.battery_info.info import get_battery_info
from shared.widgets import ListView


class BatteryInfoList(QWidget):
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout(self)
    layout.addWidget(ListView(label="Battery Info", items=get_battery_info()))
