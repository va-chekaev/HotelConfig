import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap, QIcon
from constr import ui_root


class root(QMainWindow, ui_root):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnCalc.clicked.connect(self.funcCalc)
        self.btnAbout.clicked.connect(self.funcAbout)
        self.btnHelp.clicked.connect(self.funcHelp)

        self.btnCalendar.setCheckable(True)
        self.btnCalendar.clicked.connect(self.funcGear)

    def funcCalc(self):
        try:
            inDay = float((self.inAmountDay.text()))
            ReportCheck = float(self.inReportCheck.text())
            FactCheck = float(self.inFactCheck.text())
            procent = float(self.inPercent.text())

            AmountDay = round(inDay)
            resultReport = round(ReportCheck * AmountDay)
            resultFact = round(FactCheck * AmountDay)
            difference = round((ReportCheck * AmountDay) - (FactCheck * AmountDay))
            dif_procent = round(difference * procent)
            benefit = round(difference - dif_procent)
            daily = round(inDay * 700)
            gen = round(daily+resultReport)

            self.out.setText(
                f'Ваша выгода составила {benefit} руб.\n\n'
                f'Детальная информация\n'
                f'По отченым документам {resultReport} руб.\n'
                f'Фактически заплачено {resultFact} руб.\n\n'
                f'Проценты\n'
                f'Заплатить процентов {dif_procent} руб. \n'
                f'Процент {procent:.0%}\n\n'
                f'Подробности\n'
                f'Проживание {AmountDay} дней\n'
                f'Суточные {daily} руб.\n'
                f'Общие расходы {gen} руб.'
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
        msgAbout.setWindowIcon(QIcon('res/context/about/icon_about_wi.svg'))
        msgAbout.setText(strAbout)
        msgAbout.setIconPixmap(QPixmap("res/context/about/about-context.png"))
        msgAbout.setStandardButtons(QMessageBox.Ok)
        msgAbout.exec()

    def funcHelp(self):
        strAbout = """
        Процент вносить в формате 0.1 до 1.0    \n
        0.1 = 10%
        1.0 = 100%\n
        HOTKEY
        Расчет клавиша "Enter"
        """

        msgAbout = QMessageBox()
        msgAbout.setWindowTitle("About")
        msgAbout.setWindowIcon(QIcon('res/context/help/icon_help_wi.svg'))
        msgAbout.setText(strAbout)
        msgAbout.setIconPixmap(QPixmap("res/context/help/icon_help.png"))
        msgAbout.setStandardButtons(QMessageBox.Ok)
        msgAbout.exec()

    def funcGear(self):

        if self.btnCalendar.isChecked():
            self.resize(690, 490)
        else:
            self.resize(360, 490)


if __name__ == "__main__":
    sys.argv += ['-platform', 'windows:darkmode=1']
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    w = root()
    w.show()
    sys.exit(app.exec())
