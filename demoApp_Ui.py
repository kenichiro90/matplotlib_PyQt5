# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoApp.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

# -----------------------------------------------------------------------------
# PyQt5で、matplotlibを使うために必要なモジュール類
#   [参考にしたサイト]
#      https://matplotlib.org/2.1.0/gallery/user_interfaces/embedding_in_qt5_sgskip.html?highlight=qt5
#      https://matplotlib.org/gallery/user_interfaces/embedding_in_qt_sgskip.html
# -----------------------------------------------------------------------------
import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
# -----------------------------------------------------------------------------

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 630)
        self.axisGroupBox = QtWidgets.QGroupBox(Form)
        self.axisGroupBox.setGeometry(QtCore.QRect(565, 100, 221, 171))
        self.axisGroupBox.setObjectName("axisGroupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.axisGroupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(15, 30, 191, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.xAxisMinLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.xAxisMinLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.xAxisMinLineEdit.setObjectName("xAxisMinLineEdit")
        self.gridLayout.addWidget(self.xAxisMinLineEdit, 0, 1, 1, 1)
        self.xAxisMaxLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.xAxisMaxLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.xAxisMaxLineEdit.setObjectName("xAxisMaxLineEdit")
        self.gridLayout.addWidget(self.xAxisMaxLineEdit, 1, 1, 1, 1)
        self.xAxisMaxLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.xAxisMaxLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.xAxisMaxLabel.setObjectName("xAxisMaxLabel")
        self.gridLayout.addWidget(self.xAxisMaxLabel, 1, 0, 1, 1)
        self.xAxisMinLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.xAxisMinLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.xAxisMinLabel.setObjectName("xAxisMinLabel")
        self.gridLayout.addWidget(self.xAxisMinLabel, 0, 0, 1, 1)
        self.yAxisMinLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.yAxisMinLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.yAxisMinLabel.setObjectName("yAxisMinLabel")
        self.gridLayout.addWidget(self.yAxisMinLabel, 2, 0, 1, 1)
        self.yAxisMinLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.yAxisMinLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.yAxisMinLineEdit.setObjectName("yAxisMinLineEdit")
        self.gridLayout.addWidget(self.yAxisMinLineEdit, 2, 1, 1, 1)
        self.yAxisMaxLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.yAxisMaxLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.yAxisMaxLabel.setObjectName("yAxisMaxLabel")
        self.gridLayout.addWidget(self.yAxisMaxLabel, 3, 0, 1, 1)
        self.yAxisMaxLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.yAxisMaxLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.yAxisMaxLineEdit.setObjectName("yAxisMaxLineEdit")
        self.gridLayout.addWidget(self.yAxisMaxLineEdit, 3, 1, 1, 1)
        self.graphGroupBox = QtWidgets.QGroupBox(Form)
        self.graphGroupBox.setGeometry(QtCore.QRect(15, 100, 531, 521))
        self.graphGroupBox.setObjectName("graphGroupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.graphGroupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 511, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        # self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        # self.graphicsView.setObjectName("graphicsView")
        # self.verticalLayout.addWidget(self.graphicsView)
        # ---------------------------------------------------------------------
        # Canvasウィジェットの生成
        # ---------------------------------------------------------------------
        self.canvas = MyMplCanvas(self.verticalLayoutWidget, 
                                                    width=5, height=4, dpi=100)
        self.verticalLayout.addWidget(self.canvas)
        # ---------------------------------------------------------------------
        # ToolBarの追加
        # ---------------------------------------------------------------------
        self.toolBar = NavigationToolbar(self.canvas, MyMplCanvas())
        self.verticalLayout.addWidget(self.toolBar)
        # ---------------------------------------------------------------------
        self.fileGroupBox = QtWidgets.QGroupBox(Form)
        self.fileGroupBox.setGeometry(QtCore.QRect(15, 10, 771, 80))
        self.fileGroupBox.setObjectName("fileGroupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.fileGroupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(15, 30, 741, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.fileLineEdit.setObjectName("fileLineEdit")
        self.horizontalLayout.addWidget(self.fileLineEdit)
        self.openFilePushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.openFilePushButton.setObjectName("openFilePushButton")
        self.horizontalLayout.addWidget(self.openFilePushButton)
        self.refreshCanvasPushButton = QtWidgets.QPushButton(Form)
        self.refreshCanvasPushButton.setGeometry(QtCore.QRect(620, 570, 113, 32))
        self.refreshCanvasPushButton.setObjectName("refreshCanvasPushButton")

        self.retranslateUi(Form)
        self.openFilePushButton.clicked.connect(Form.openFileDialog)
        self.refreshCanvasPushButton.clicked.connect(Form.refreshCanvas)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.axisGroupBox.setTitle(_translate("Form", "軸の設定"))
        self.xAxisMinLineEdit.setText(_translate("Form", "0"))
        self.xAxisMaxLineEdit.setText(_translate("Form", "0"))
        self.xAxisMaxLabel.setText(_translate("Form", "X(max)"))
        self.xAxisMinLabel.setText(_translate("Form", "X(min)"))
        self.yAxisMinLabel.setText(_translate("Form", "Y(min)"))
        self.yAxisMinLineEdit.setText(_translate("Form", "0"))
        self.yAxisMaxLabel.setText(_translate("Form", "Y(max)"))
        self.yAxisMaxLineEdit.setText(_translate("Form", "0"))
        self.graphGroupBox.setTitle(_translate("Form", "グラフウィンドウ"))
        self.fileGroupBox.setTitle(_translate("Form", "ファイル関係"))
        self.openFilePushButton.setText(_translate("Form", "Open"))
        self.refreshCanvasPushButton.setText(_translate("Form", "Refresh"))

# -----------------------------------------------------------------------------
# Canvas領域の定義
# -----------------------------------------------------------------------------
class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        # Figure, subplotの初期化
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.plt = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
