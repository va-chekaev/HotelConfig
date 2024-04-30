from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QSizePolicy, QWidget)
import assets


class ui_root(object):
    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName(u"root")
        root.resize(400, 550)
        root.setMinimumSize(QSize(400, 550))
        root.setMaximumSize(QSize(400, 550))
        icon = QIcon()
        icon.addFile(u":/res/res/main-icon-ico-01.ico", QSize(), QIcon.Normal, QIcon.Off)
        root.setWindowIcon(icon)

        self.window = QWidget(root)
        self.window.setObjectName(u"window")
        self.lbReportCheck = QLabel(self.window)
        self.lbReportCheck.setObjectName(u"lbReportCheck")
        self.lbReportCheck.setGeometry(QRect(40, 0, 151, 16))

        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)

        self.inReportCheck = QLineEdit(self.window)
        self.inReportCheck.setObjectName(u"inReportCheck")
        self.inReportCheck.setGeometry(QRect(40, 20, 151, 41))

        self.inFactCheck = QLineEdit(self.window)
        self.inFactCheck.setObjectName(u"inFactCheck")
        self.inFactCheck.setGeometry(QRect(40, 70, 151, 41))

        self.inAmountDay = QLineEdit(self.window)
        self.inAmountDay.setObjectName(u"inDay")
        self.inAmountDay.setGeometry(QRect(210, 20, 151, 41))

        self.inProc = QLineEdit(self.window)
        self.inProc.setObjectName(u"inProc")
        self.inProc.setGeometry(QRect(210, 70, 151, 41))

        self.btnCalc = QPushButton(self.window)
        self.btnCalc.setObjectName(u"btnCalc")
        self.btnCalc.setGeometry(QRect(40, 120, 321, 41))
        self.btnCalc.setCursor(QCursor(Qt.PointingHandCursor))

        self.out = QLabel(self.window)
        self.out.setObjectName(u"label_5")
        self.out.setGeometry(QRect(40, 175, 321, 291))
        self.out.setStyleSheet(u"background-color: rgb(226, 226, 226);")

        """self.lbResult = QLabel(self.window)
        self.lbResult.setObjectName(u"lbResult")
        self.lbResult.setGeometry(QRect(40, 180, 321, 16))"""

        self.btnHelp = QPushButton(self.window)
        self.btnHelp.setObjectName(u"btnHelp")
        self.btnHelp.setGeometry(QRect(220, 510, 141, 31))
        self.btnHelp.setCursor(QCursor(Qt.PointingHandCursor))

        self.btnAbout = QPushButton(self.window)
        self.btnAbout.setObjectName(u"btnAbout")
        self.btnAbout.setGeometry(QRect(40, 510, 161, 31))
        self.btnAbout.setCursor(QCursor(Qt.PointingHandCursor))

        root.setCentralWidget(self.window)
        self.retranslateUi(root)

        QMetaObject.connectSlotsByName(root)

    # setupUi

    def retranslateUi(self, root):
        root.setWindowTitle(QCoreApplication.translate("root", u"HotelConfig ver 0.1 (beta)", None))
        self.btnCalc.setText(QCoreApplication.translate("root", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430"
                                                                u"\u0442\u044c", None))
        self.btnCalc.setShortcut(QCoreApplication.translate("root", u"Return", None))
        self.lbReportCheck.setText(QCoreApplication.translate("root",
                                                              u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442"
                                                              u"\u044c \u043f\u043e \u0447\u0435\u043a\u0443",
                                                              None))
        self.inReportCheck.setPlaceholderText(QCoreApplication.translate("root",
                                                                         u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441"
                                                                         u"\u0442\u044c \u043f\u043e "
                                                                         u"\u0447\u0435\u043a\u0443",
                                                                         None))
        self.inFactCheck.setPlaceholderText(QCoreApplication.translate("root",
                                                                       u"\u0424\u0430\u043a\u0442\u0438\u0447\u0435"
                                                                       u"\u0441\u043a\u0430\u044f "
                                                                       u"\u0441\u0442\u043e\u0438\u043c\u043e\u0441"
                                                                       u"\u0442\u044c",
                                                                       None))
        self.inAmountDay.setPlaceholderText(QCoreApplication.translate("root",
                                                                       u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441"
                                                                       u"\u0442"
                                                                       u"\u0432\u043e \u0434\u043d\u0435\u0439",
                                                                       None))
        self.inProc.setPlaceholderText(
            QCoreApplication.translate("root", u"\u041f\u0440\u043e\u0446\u0435\u043d\u0442", None))
        self.btnCalc.setText(
            QCoreApplication.translate("root", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.out.setText("")
        self.btnHelp.setText(QCoreApplication.translate("root", u"Help", None))
        self.btnAbout.setText(QCoreApplication.translate("root", u"About", None))
    # retranslateUi
