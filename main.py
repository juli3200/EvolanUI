import sys
# IMPORT GUI FILE
from src.ui_evolan import *

# IMPORT Custom widgets
from Custom_Widgets import *
# Import QAppSettings
from Custom_Widgets.QAppSettings import QAppSettings

# Import video player
from src.VideoPlayer import VideoPlayer

## MAIN WINDOW CLASS
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # APPLY JSON STYLESHEET
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui, jsonFiles = {
            "json-styles/style.json"
            }
        )

        # Apply theme style, generate icons....
        QAppSettings.updateAppSettings(self)

        self.show()

        self.ui.simulateBtn.setStyleSheet("background-color: #00282a;")

        self.videoPlayer = VideoPlayer(ui=self)


## EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
## END===>
