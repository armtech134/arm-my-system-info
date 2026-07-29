from PySide6.QtWidgets import QApplication

from features.dashboard.dashboard_window import DashboardWindow

app = QApplication()
window = DashboardWindow()
window.show()
app.exec()
