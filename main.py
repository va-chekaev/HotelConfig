import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSettings
from constr import ui_root


class root(QMainWindow, ui_root):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnCalc.clicked.connect(self.funcCalc)
        self.btnAbout.clicked.connect(self.funcAbout)
        self.btnHelp.clicked.connect(self.funcHelp)

    def funcCalc(self):
        try:
            AmountDay = float(self.inAmountDay.text())
            ReportCheck = float(self.inReportCheck.text())
            resultReport = ReportCheck * AmountDay
            FactCheck = float(self.inFactCheck.text())
            resultFact = FactCheck * AmountDay
            proc = float(self.inProc.text())
            difference = (ReportCheck * AmountDay) - (FactCheck * AmountDay)
            diffProc = difference * proc
            benefit = difference - diffProc

            self.out.setText(
                f' Ваша выгода состаила {benefit} руб.\n\n'
                f' По отченым докуменам заплачено\n'
                f' За {AmountDay} дней проживания {resultReport} руб.\n'
                f' Фактически заплачено\n'
                f' За {AmountDay} дней проживания {resultFact} руб.\n\n'
                f' Разница составила {difference} руб.\n'
                f' Вы должны заплатить {difference * proc} руб. процентов\n'
                f' Процент {proc}'
            )

        except Exception as e:
            None

    def funcAbout(self):
        strAbout = """
        HotelConfig ver. 0.1\n
        Copyright © Чекаев В.А.
        Ресурсы www.flaticon.com\n
        Лицензия
        GNU General Public License v3.0
        """

        msgAbout = QMessageBox()
        msgAbout.setWindowTitle("About")
        msgAbout.setWindowIcon(QIcon('res/about-context.png'))
        msgAbout.setText(strAbout)
        msgAbout.setIconPixmap(QPixmap("res/about-context.png"))
        msgAbout.setStandardButtons(QMessageBox.Ok)
        msgAbout.exec()

    def funcHelp(self):
        strAbout = """
        HotelConfig ver. 0.1\n
        """

        msgAbout = QMessageBox()
        msgAbout.setWindowTitle("About")
        msgAbout.setWindowIcon(QIcon('res/about-context.png'))
        msgAbout.setText(strAbout)
        msgAbout.setIconPixmap(QPixmap("res/about-context.png"))
        msgAbout.setStandardButtons(QMessageBox.Ok)
        msgAbout.exec()


if __name__ == "__main__":
    sys.argv += ['-platform', 'windows:darkmode=1']
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    w = root()
    w.show()
    sys.exit(app.exec())
