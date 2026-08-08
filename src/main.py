from PySide6.QtWidgets import QApplication

from features.dashboard.dashboard_window import DashboardWindow
from shared.elevate_privileges import elevate_privileges

elevate_privileges()

app = QApplication()
app.setStyle("Windows")
window = DashboardWindow()
window.show()
app.exec()
