from PySide6.QtWidgets import QLabel, QListWidget, QVBoxLayout, QWidget


class ListView(QWidget):
  def __init__(self, parent=None, items=None, label=""):
    if items is None:
      items = []
    super().__init__(parent)
    self.label = QLabel(f"&{label}")
    self.my_list = QListWidget()
    self.my_list.addItems(items)
    self.label.setBuddy(self.my_list)
    self.my_list.setAccessibleName(f"{label}({len(items)}):")
    layout = QVBoxLayout(self)
    layout.addWidget(self.label)
    layout.addWidget(self.my_list)
