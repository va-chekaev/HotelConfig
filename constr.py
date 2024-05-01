from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy, QWidget)
import assets


class ui_root(object):
    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName(u"root")

        root.resize(360, 490)
        root.setMinimumSize(QSize(360, 490))
        root.setMaximumSize(QSize(690, 490))
        icon = QIcon()
        icon.addFile(u":/res/res/main-icon-ico-01.ico", QSize(), QIcon.Normal, QIcon.Off)
        root.setWindowIcon(icon)

        self.window = QWidget(root)
        self.window.setObjectName(u"window")

        self.inReportCheck = QLineEdit(self.window)
        self.inReportCheck.setObjectName(u"inReportCheck")
        self.inReportCheck.setGeometry(QRect(20, 20, 151, 31))
        self.inReportCheck.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.inFactCheck = QLineEdit(self.window)
        self.inFactCheck.setObjectName(u"inFactCheck")
        self.inFactCheck.setGeometry(QRect(20, 60, 151, 31))
        self.inFactCheck.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.inAmountDay = QLineEdit(self.window)
        self.inAmountDay.setObjectName(u"inAmountDay")
        self.inAmountDay.setGeometry(QRect(190, 20, 151, 31))
        self.inAmountDay.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.inPercent = QLineEdit(self.window)
        self.inPercent.setObjectName(u"inPercent")
        self.inPercent.setGeometry(QRect(190, 60, 151, 31))
        self.inPercent.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.btnCalc = QPushButton(self.window)
        self.btnCalc.setObjectName(u"btnCalc")
        self.btnCalc.setGeometry(QRect(20, 100, 321, 41))
        self.btnCalc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCalc.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.out = QLabel(self.window)
        self.out.setObjectName(u"out")
        self.out.setEnabled(True)
        self.out.setGeometry(QRect(20, 150, 321, 291))
        self.out.setWordWrap = True

        self.out.setStyleSheet(u"background-color: rgb(235, 235, 235); padding: 5px")
        self.out.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.btnAbout = QPushButton(self.window)
        self.btnAbout.setObjectName(u"btnAbout")
        self.btnAbout.setGeometry(QRect(20, 450, 30, 30))
        self.btnAbout.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"res/button/btn_about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAbout.setIcon(icon1)

        self.btnHelp = QPushButton(self.window)
        self.btnHelp.setObjectName(u"btnHelp")
        self.btnHelp.setGeometry(QRect(55, 450, 30, 30))
        self.btnHelp.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"res/button/btn_help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnHelp.setIcon(icon2)

        self.btnCalendar = QPushButton(self.window)
        self.btnCalendar.setObjectName(u"btnCalendar")
        self.btnCalendar.setGeometry(QRect(312, 450, 30, 30))
        self.btnCalendar.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"res/button/btn_config.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCalendar.setIcon(icon3)

        self.calendarWidget = QCalendarWidget(self.window)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(360, 20, 312, 190))
        self.calendarWidget.setStyleSheet('''
            #qt_calendar_navigationbar {
                background-color: rgb(56, 56, 56);
                min-height: 35px; 
            }
            #qt_calendar_prevmonth, #qt_calendar_nextmonth {
                border: none;                  
                margin-top: 0px;
                color: white;
                qproperty-icon: none;    
                background-color: transparent; 
            }
            #qt_calendar_prevmonth {
                qproperty-text: "⯇";
            }
            #qt_calendar_nextmonth {
                qproperty-text: "⯈";
            }
            #qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
                background-color: rgba(225, 225, 225, 100);
            }
            #qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
                background-color: rgba(235, 235, 235, 100);
            }
            #qt_calendar_yearbutton, #qt_calendar_monthbutton {
                color: white;
                margin: 30px;
                min-width: 50px;
                border-radius: 5px;
            }
            #qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
                background-color: rgba(225, 225, 225, 100);
            }
            #qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
                background-color: rgba(235, 235, 235, 100);
            }
            #qt_calendar_yearedit {
                min-width: 50px;
                color: white;
                background: transparent;         
            }
            #qt_calendar_yearedit::up-button {   
                width: 20px;
                subcontrol-position: right;      
            }
            #qt_calendar_yearedit::down-button {
                width: 20px;
                subcontrol-position: left;       
            }
            CalendarWidget QToolButton QMenu {
                background-color: white;
            }
            CalendarWidget QToolButton QMenu::item {
                padding: 10px;
            }
            CalendarWidget QToolButton QMenu::item:selected:enabled {
                background-color: rgb(230, 230, 230);
            }
            CalendarWidget QToolButton::menu-indicator {
                image: none;
                subcontrol-position: right center;
            }
            #qt_calendar_calendarview {
                outline: 0px;
                selection-background-color: rgb(199, 199, 199);
            }
        ''')

        self.inDaily = QLineEdit(self.window)
        self.inDaily.setObjectName(u"inDaily")
        self.inDaily.setGeometry(QRect(360, 400, 311, 31))
        self.inDaily.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.btnSaveDaily = QPushButton(self.window)
        self.btnSaveDaily.setObjectName(u"btnSaveDaily")
        self.btnSaveDaily.setGeometry(QRect(360, 440, 151, 41))
        self.btnSaveDaily.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSaveDaily.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.btnApplyDaily = QPushButton(self.window)
        self.btnApplyDaily.setObjectName(u"btnApplyDaily")
        self.btnApplyDaily.setGeometry(QRect(520, 440, 151, 41))
        self.btnApplyDaily.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnApplyDaily.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        root.setCentralWidget(self.window)
        self.retranslateUi(root)
        QMetaObject.connectSlotsByName(root)

    # setupUi

    def retranslateUi(self, root):
        root.setWindowTitle(QCoreApplication.translate("root", u"HotelConfig", None))
        self.inReportCheck.setPlaceholderText(QCoreApplication.translate("root", u"\u0421\u0442\u043e\u0438\u043c"
                                                                                 u"\u043e\u0441\u0442\u044c "
                                                                                 u"\u043f\u043e "
                                                                                 u"\u0447\u0435\u043a\u0443", None))
        self.inFactCheck.setPlaceholderText(QCoreApplication.translate("root",
                                                                       u"\u0424\u0430\u043a\u0442\u0438\u0447\u0435"
                                                                       u"\u0441\u043a\u0430\u044f "
                                                                       u"\u0441\u0442\u043e\u0438\u043c\u043e\u0441"
                                                                       u"\u0442\u044c",
                                                                       None))
        self.inAmountDay.setPlaceholderText(QCoreApplication.translate("root",
                                                                       u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441"
                                                                       u"\u0442\u0432\u043e \u0434\u043d\u0435\u0439",
                                                                       None))
        self.inPercent.setPlaceholderText(QCoreApplication.translate("root", u"\u041f\u0440\u043e\u0446\u0435\u043d"
                                                                             u"\u0442", None))
        self.btnCalc.setText(QCoreApplication.translate("root", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430"
                                                                u"\u0442\u044c", None))
        self.btnCalc.setShortcut(QCoreApplication.translate("root", u"Return", None))
        self.out.setText("")
        self.btnHelp.setText(QCoreApplication.translate("root", u"", None))
        self.btnAbout.setText(QCoreApplication.translate("root", u"", None))
        self.btnCalendar.setText(QCoreApplication.translate("root", u"", None))
        self.inDaily.setText("")
        self.inDaily.setPlaceholderText(QCoreApplication.translate("root", u"\u0421\u0443\u0442\u043e\u0447\u043d"
                                                                           u"\u044b\u0435", None))
        self.btnSaveDaily.setText(QCoreApplication.translate("root", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438"
                                                                     u"\u0442\u044c", None))
        self.btnApplyDaily.setText(QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438"
                                                                      u"\u0442\u044c", None))
