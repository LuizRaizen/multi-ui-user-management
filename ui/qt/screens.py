# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QCommandLinkButton, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(500, 600))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stk_telas = QStackedWidget(self.centralwidget)
        self.stk_telas.setObjectName(u"stk_telas")
        self.pg_tela_login = QWidget()
        self.pg_tela_login.setObjectName(u"pg_tela_login")
        self.verticalLayout_4 = QVBoxLayout(self.pg_tela_login)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.grid_tela_login = QGridLayout()
        self.grid_tela_login.setObjectName(u"grid_tela_login")
        self.frm_widget_login = QFrame(self.pg_tela_login)
        self.frm_widget_login.setObjectName(u"frm_widget_login")
        self.frm_widget_login.setMaximumSize(QSize(300, 500))
        self.frm_widget_login.setAutoFillBackground(False)
        self.frm_widget_login.setFrameShape(QFrame.NoFrame)
        self.frm_widget_login.setFrameShadow(QFrame.Raised)
        self.frm_widget_login.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frm_widget_login)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_titulo_login = QLabel(self.frm_widget_login)
        self.lbl_titulo_login.setObjectName(u"lbl_titulo_login")
        sizePolicy.setHeightForWidth(self.lbl_titulo_login.sizePolicy().hasHeightForWidth())
        self.lbl_titulo_login.setSizePolicy(sizePolicy)
        self.lbl_titulo_login.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(18)
        self.lbl_titulo_login.setFont(font)
        self.lbl_titulo_login.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_titulo_login)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.lbl_login_nome_usuario_email = QLabel(self.frm_widget_login)
        self.lbl_login_nome_usuario_email.setObjectName(u"lbl_login_nome_usuario_email")
        self.lbl_login_nome_usuario_email.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.lbl_login_nome_usuario_email)

        self.le_login_nome_usuario_email = QLineEdit(self.frm_widget_login)
        self.le_login_nome_usuario_email.setObjectName(u"le_login_nome_usuario_email")
        self.le_login_nome_usuario_email.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.le_login_nome_usuario_email)

        self.lbl_login_senha = QLabel(self.frm_widget_login)
        self.lbl_login_senha.setObjectName(u"lbl_login_senha")
        self.lbl_login_senha.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.lbl_login_senha)

        self.le_login_senha = QLineEdit(self.frm_widget_login)
        self.le_login_senha.setObjectName(u"le_login_senha")
        self.le_login_senha.setMaximumSize(QSize(16777215, 35))
        self.le_login_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.le_login_senha)

        self.chk_lembrar_me = QCheckBox(self.frm_widget_login)
        self.chk_lembrar_me.setObjectName(u"chk_lembrar_me")
        self.chk_lembrar_me.setMaximumSize(QSize(16777215, 50))
        self.chk_lembrar_me.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.chk_lembrar_me)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_entrar = QPushButton(self.frm_widget_login)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(14)
        self.btn_entrar.setFont(font1)
        self.btn_entrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(38, 162, 105);")
        self.btn_entrar.setFlat(False)

        self.verticalLayout_2.addWidget(self.btn_entrar)

        self.verticalSpacer_2 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.cl_criar_conta = QCommandLinkButton(self.frm_widget_login)
        self.cl_criar_conta.setObjectName(u"cl_criar_conta")
        self.cl_criar_conta.setMaximumSize(QSize(16777215, 30))
        self.cl_criar_conta.setCursor(QCursor(Qt.PointingHandCursor))
        self.cl_criar_conta.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.cl_criar_conta)


        self.grid_tela_login.addWidget(self.frm_widget_login, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.grid_tela_login)

        self.stk_telas.addWidget(self.pg_tela_login)
        self.pg_tela_cadastro = QWidget()
        self.pg_tela_cadastro.setObjectName(u"pg_tela_cadastro")
        self.horizontalLayout = QHBoxLayout(self.pg_tela_cadastro)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.grid_tela_cadastro = QGridLayout()
        self.grid_tela_cadastro.setObjectName(u"grid_tela_cadastro")
        self.frm_widget_cadastro = QFrame(self.pg_tela_cadastro)
        self.frm_widget_cadastro.setObjectName(u"frm_widget_cadastro")
        self.frm_widget_cadastro.setMaximumSize(QSize(300, 500))
        self.frm_widget_cadastro.setAutoFillBackground(False)
        self.frm_widget_cadastro.setFrameShape(QFrame.NoFrame)
        self.frm_widget_cadastro.setFrameShadow(QFrame.Raised)
        self.frm_widget_cadastro.setLineWidth(0)
        self.verticalLayout_7 = QVBoxLayout(self.frm_widget_cadastro)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lbl_cadastro_titulo_cadastro = QLabel(self.frm_widget_cadastro)
        self.lbl_cadastro_titulo_cadastro.setObjectName(u"lbl_cadastro_titulo_cadastro")
        sizePolicy.setHeightForWidth(self.lbl_cadastro_titulo_cadastro.sizePolicy().hasHeightForWidth())
        self.lbl_cadastro_titulo_cadastro.setSizePolicy(sizePolicy)
        self.lbl_cadastro_titulo_cadastro.setMaximumSize(QSize(16777215, 30))
        self.lbl_cadastro_titulo_cadastro.setFont(font)
        self.lbl_cadastro_titulo_cadastro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lbl_cadastro_titulo_cadastro)

        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_10)

        self.lbl_cadastro_nome_usuario = QLabel(self.frm_widget_cadastro)
        self.lbl_cadastro_nome_usuario.setObjectName(u"lbl_cadastro_nome_usuario")
        self.lbl_cadastro_nome_usuario.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_7.addWidget(self.lbl_cadastro_nome_usuario)

        self.le_cadastro_nome_usuario = QLineEdit(self.frm_widget_cadastro)
        self.le_cadastro_nome_usuario.setObjectName(u"le_cadastro_nome_usuario")
        self.le_cadastro_nome_usuario.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_7.addWidget(self.le_cadastro_nome_usuario)

        self.lbl_cadastro_email = QLabel(self.frm_widget_cadastro)
        self.lbl_cadastro_email.setObjectName(u"lbl_cadastro_email")
        self.lbl_cadastro_email.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_7.addWidget(self.lbl_cadastro_email)

        self.le_cadastro_email = QLineEdit(self.frm_widget_cadastro)
        self.le_cadastro_email.setObjectName(u"le_cadastro_email")
        self.le_cadastro_email.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_7.addWidget(self.le_cadastro_email)

        self.lbl_cadastro_senha = QLabel(self.frm_widget_cadastro)
        self.lbl_cadastro_senha.setObjectName(u"lbl_cadastro_senha")
        self.lbl_cadastro_senha.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_7.addWidget(self.lbl_cadastro_senha)

        self.le_cadastro_senha = QLineEdit(self.frm_widget_cadastro)
        self.le_cadastro_senha.setObjectName(u"le_cadastro_senha")
        self.le_cadastro_senha.setMaximumSize(QSize(16777215, 35))
        self.le_cadastro_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout_7.addWidget(self.le_cadastro_senha)

        self.lbl_cadastro_confirmar_senha = QLabel(self.frm_widget_cadastro)
        self.lbl_cadastro_confirmar_senha.setObjectName(u"lbl_cadastro_confirmar_senha")
        self.lbl_cadastro_confirmar_senha.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_7.addWidget(self.lbl_cadastro_confirmar_senha)

        self.le_cadastro_confirmar_senha = QLineEdit(self.frm_widget_cadastro)
        self.le_cadastro_confirmar_senha.setObjectName(u"le_cadastro_confirmar_senha")
        self.le_cadastro_confirmar_senha.setMaximumSize(QSize(16777215, 35))
        self.le_cadastro_confirmar_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout_7.addWidget(self.le_cadastro_confirmar_senha)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_11)

        self.btn_cadastrar = QPushButton(self.frm_widget_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMaximumSize(QSize(16777215, 50))
        self.btn_cadastrar.setFont(font1)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(38, 162, 105);")
        self.btn_cadastrar.setFlat(False)

        self.verticalLayout_7.addWidget(self.btn_cadastrar)

        self.verticalSpacer_12 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_12)

        self.cl_fazer_login = QCommandLinkButton(self.frm_widget_cadastro)
        self.cl_fazer_login.setObjectName(u"cl_fazer_login")
        self.cl_fazer_login.setMaximumSize(QSize(16777215, 30))
        self.cl_fazer_login.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.cl_fazer_login)


        self.grid_tela_cadastro.addWidget(self.frm_widget_cadastro, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.grid_tela_cadastro)

        self.stk_telas.addWidget(self.pg_tela_cadastro)

        self.verticalLayout_8.addWidget(self.stk_telas)


        self.verticalLayout.addLayout(self.verticalLayout_8)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stk_telas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tela de Cadastro e Login de Usu\u00e1rios", None))
        self.lbl_titulo_login.setText(QCoreApplication.translate("MainWindow", u"Fazer Login", None))
        self.lbl_login_nome_usuario_email.setText(QCoreApplication.translate("MainWindow", u"Nome de usu\u00e1rio / E-mail:", None))
        self.lbl_login_senha.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.chk_lembrar_me.setText(QCoreApplication.translate("MainWindow", u"Lembrar de mim", None))
        self.btn_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.cl_criar_conta.setText(QCoreApplication.translate("MainWindow", u"Voc\u00ea ainda n\u00e3o tem uma conta?", None))
        self.lbl_cadastro_titulo_cadastro.setText(QCoreApplication.translate("MainWindow", u"Criar Usu\u00e1rio", None))
        self.lbl_cadastro_nome_usuario.setText(QCoreApplication.translate("MainWindow", u"Nome de usu\u00e1rio:", None))
        self.lbl_cadastro_email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.lbl_cadastro_senha.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.lbl_cadastro_confirmar_senha.setText(QCoreApplication.translate("MainWindow", u"Confirmar senha:", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.cl_fazer_login.setText(QCoreApplication.translate("MainWindow", u"Voc\u00ea j\u00e1 tem uma conta?", None))
    # retranslateUi

