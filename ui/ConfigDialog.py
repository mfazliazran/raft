# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfigDialog.ui'
#
# Created: Tue Aug  2 19:35:33 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_configDialog(object):
    def setupUi(self, configDialog):
        configDialog.setObjectName(_fromUtf8("configDialog"))
        configDialog.resize(693, 593)
        self.verticalLayout = QtGui.QVBoxLayout(configDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.configTab = QtGui.QTabWidget(configDialog)
        self.configTab.setObjectName(_fromUtf8("configTab"))
        self.configGeneralTab = QtGui.QWidget()
        self.configGeneralTab.setObjectName(_fromUtf8("configGeneralTab"))
        self.groupBox = QtGui.QGroupBox(self.configGeneralTab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 328, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.bhNetworkBox = QtGui.QCheckBox(self.groupBox)
        self.bhNetworkBox.setChecked(True)
        self.bhNetworkBox.setObjectName(_fromUtf8("bhNetworkBox"))
        self.gridLayout.addWidget(self.bhNetworkBox, 0, 0, 1, 1)
        self.checkBoxUseProxy = QtGui.QCheckBox(self.groupBox)
        self.checkBoxUseProxy.setObjectName(_fromUtf8("checkBoxUseProxy"))
        self.gridLayout.addWidget(self.checkBoxUseProxy, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.confProxyEdit = QtGui.QLineEdit(self.groupBox)
        self.confProxyEdit.setEnabled(False)
        self.confProxyEdit.setObjectName(_fromUtf8("confProxyEdit"))
        self.gridLayout.addWidget(self.confProxyEdit, 3, 0, 1, 1)
        self.confProxyPort = QtGui.QLineEdit(self.groupBox)
        self.confProxyPort.setEnabled(False)
        self.confProxyPort.setObjectName(_fromUtf8("confProxyPort"))
        self.gridLayout.addWidget(self.confProxyPort, 3, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.configGeneralTab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 331, 161))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.browserAutoLoadImagesCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.browserAutoLoadImagesCheckBox.setGeometry(QtCore.QRect(10, 120, 181, 20))
        self.browserAutoLoadImagesCheckBox.setObjectName(_fromUtf8("browserAutoLoadImagesCheckBox"))
        self.browserEnablePluginsCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.browserEnablePluginsCheckBox.setGeometry(QtCore.QRect(10, 60, 191, 20))
        self.browserEnablePluginsCheckBox.setObjectName(_fromUtf8("browserEnablePluginsCheckBox"))
        self.browserEnableJavaCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.browserEnableJavaCheckBox.setGeometry(QtCore.QRect(10, 90, 151, 20))
        self.browserEnableJavaCheckBox.setObjectName(_fromUtf8("browserEnableJavaCheckBox"))
        self.browserEnableWebStorageCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.browserEnableWebStorageCheckBox.setGeometry(QtCore.QRect(10, 30, 181, 20))
        self.browserEnableWebStorageCheckBox.setObjectName(_fromUtf8("browserEnableWebStorageCheckBox"))
        self.configTab.addTab(self.configGeneralTab, _fromUtf8(""))
        self.configCrawlerTab = QtGui.QWidget()
        self.configCrawlerTab.setObjectName(_fromUtf8("configCrawlerTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.configCrawlerTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.spiderConfigGroupBox = QtGui.QGroupBox(self.configCrawlerTab)
        self.spiderConfigGroupBox.setObjectName(_fromUtf8("spiderConfigGroupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.spiderConfigGroupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.spiderSubmitFormsCheckBox = QtGui.QCheckBox(self.spiderConfigGroupBox)
        self.spiderSubmitFormsCheckBox.setChecked(False)
        self.spiderSubmitFormsCheckBox.setObjectName(_fromUtf8("spiderSubmitFormsCheckBox"))
        self.verticalLayout_3.addWidget(self.spiderSubmitFormsCheckBox)
        self.spiderUseDataBankCheckBox = QtGui.QCheckBox(self.spiderConfigGroupBox)
        self.spiderUseDataBankCheckBox.setChecked(False)
        self.spiderUseDataBankCheckBox.setObjectName(_fromUtf8("spiderUseDataBankCheckBox"))
        self.verticalLayout_3.addWidget(self.spiderUseDataBankCheckBox)
        self.spiderSubmitUsernamePasswordCheckBox = QtGui.QCheckBox(self.spiderConfigGroupBox)
        self.spiderSubmitUsernamePasswordCheckBox.setChecked(False)
        self.spiderSubmitUsernamePasswordCheckBox.setObjectName(_fromUtf8("spiderSubmitUsernamePasswordCheckBox"))
        self.verticalLayout_3.addWidget(self.spiderSubmitUsernamePasswordCheckBox)
        self.spiderEvaluateJavascriptCheckBox = QtGui.QCheckBox(self.spiderConfigGroupBox)
        self.spiderEvaluateJavascriptCheckBox.setChecked(False)
        self.spiderEvaluateJavascriptCheckBox.setObjectName(_fromUtf8("spiderEvaluateJavascriptCheckBox"))
        self.verticalLayout_3.addWidget(self.spiderEvaluateJavascriptCheckBox)
        self.spiderRetrieveMediaFilesCheckBox = QtGui.QCheckBox(self.spiderConfigGroupBox)
        self.spiderRetrieveMediaFilesCheckBox.setObjectName(_fromUtf8("spiderRetrieveMediaFilesCheckBox"))
        self.verticalLayout_3.addWidget(self.spiderRetrieveMediaFilesCheckBox)
        self.spiderExcludeDangerouPathCheckBox = QtGui.QCheckBox(self.spiderConfigGroupBox)
        self.spiderExcludeDangerouPathCheckBox.setObjectName(_fromUtf8("spiderExcludeDangerouPathCheckBox"))
        self.verticalLayout_3.addWidget(self.spiderExcludeDangerouPathCheckBox)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.spiderConfigGroupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.spiderMaxChildrenEdit = QtGui.QLineEdit(self.spiderConfigGroupBox)
        self.spiderMaxChildrenEdit.setText(_fromUtf8(""))
        self.spiderMaxChildrenEdit.setCursorPosition(0)
        self.spiderMaxChildrenEdit.setObjectName(_fromUtf8("spiderMaxChildrenEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.spiderMaxChildrenEdit)
        self.label_4 = QtGui.QLabel(self.spiderConfigGroupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.spiderConfigGroupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.spiderConfigGroupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_6)
        self.spiderMaxUniqueParametersEdit = QtGui.QLineEdit(self.spiderConfigGroupBox)
        self.spiderMaxUniqueParametersEdit.setText(_fromUtf8(""))
        self.spiderMaxUniqueParametersEdit.setObjectName(_fromUtf8("spiderMaxUniqueParametersEdit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.spiderMaxUniqueParametersEdit)
        self.spiderRedundantContentLimit = QtGui.QLineEdit(self.spiderConfigGroupBox)
        self.spiderRedundantContentLimit.setText(_fromUtf8(""))
        self.spiderRedundantContentLimit.setObjectName(_fromUtf8("spiderRedundantContentLimit"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.spiderRedundantContentLimit)
        self.spiderRedundantStructureLimit = QtGui.QLineEdit(self.spiderConfigGroupBox)
        self.spiderRedundantStructureLimit.setText(_fromUtf8(""))
        self.spiderRedundantStructureLimit.setObjectName(_fromUtf8("spiderRedundantStructureLimit"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.spiderRedundantStructureLimit)
        self.label_7 = QtGui.QLabel(self.spiderConfigGroupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.spiderDangerousPathEdit = QtGui.QLineEdit(self.spiderConfigGroupBox)
        self.spiderDangerousPathEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spiderDangerousPathEdit.sizePolicy().hasHeightForWidth())
        self.spiderDangerousPathEdit.setSizePolicy(sizePolicy)
        self.spiderDangerousPathEdit.setMinimumSize(QtCore.QSize(360, 0))
        self.spiderDangerousPathEdit.setText(_fromUtf8(""))
        self.spiderDangerousPathEdit.setCursorPosition(0)
        self.spiderDangerousPathEdit.setObjectName(_fromUtf8("spiderDangerousPathEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spiderDangerousPathEdit)
        self.spiderMediaExtensionsEdit = QtGui.QLineEdit(self.spiderConfigGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spiderMediaExtensionsEdit.sizePolicy().hasHeightForWidth())
        self.spiderMediaExtensionsEdit.setSizePolicy(sizePolicy)
        self.spiderMediaExtensionsEdit.setMinimumSize(QtCore.QSize(360, 0))
        self.spiderMediaExtensionsEdit.setText(_fromUtf8(""))
        self.spiderMediaExtensionsEdit.setObjectName(_fromUtf8("spiderMediaExtensionsEdit"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.spiderMediaExtensionsEdit)
        self.label_8 = QtGui.QLabel(self.spiderConfigGroupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtGui.QLabel(self.spiderConfigGroupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtGui.QLabel(self.spiderConfigGroupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_10)
        self.spiderMaxLinksEdit = QtGui.QLineEdit(self.spiderConfigGroupBox)
        self.spiderMaxLinksEdit.setText(_fromUtf8(""))
        self.spiderMaxLinksEdit.setObjectName(_fromUtf8("spiderMaxLinksEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.spiderMaxLinksEdit)
        self.spiderMaxLinkDepthEdit = QtGui.QLineEdit(self.spiderConfigGroupBox)
        self.spiderMaxLinkDepthEdit.setText(_fromUtf8(""))
        self.spiderMaxLinkDepthEdit.setObjectName(_fromUtf8("spiderMaxLinkDepthEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.spiderMaxLinkDepthEdit)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.verticalLayout_2.addWidget(self.spiderConfigGroupBox)
        self.contentDiscoveryGroupBox = QtGui.QGroupBox(self.configCrawlerTab)
        self.contentDiscoveryGroupBox.setObjectName(_fromUtf8("contentDiscoveryGroupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.contentDiscoveryGroupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.spiderIterateUserAgentsCheckBox = QtGui.QCheckBox(self.contentDiscoveryGroupBox)
        self.spiderIterateUserAgentsCheckBox.setChecked(False)
        self.spiderIterateUserAgentsCheckBox.setObjectName(_fromUtf8("spiderIterateUserAgentsCheckBox"))
        self.verticalLayout_4.addWidget(self.spiderIterateUserAgentsCheckBox)
        self.verticalLayout_2.addWidget(self.contentDiscoveryGroupBox)
        self.configTab.addTab(self.configCrawlerTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.configTab)
        self.buttonBox = QtGui.QDialogButtonBox(configDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(configDialog)
        self.configTab.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), configDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), configDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(configDialog)

    def retranslateUi(self, configDialog):
        configDialog.setWindowTitle(QtGui.QApplication.translate("configDialog", "RAFT - Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("configDialog", "Network Communication", None, QtGui.QApplication.UnicodeUTF8))
        self.bhNetworkBox.setToolTip(QtGui.QApplication.translate("configDialog", "Do not make requests to site while rendering captured content", None, QtGui.QApplication.UnicodeUTF8))
        self.bhNetworkBox.setText(QtGui.QApplication.translate("configDialog", "Black Hole Network", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxUseProxy.setText(QtGui.QApplication.translate("configDialog", "Use Proxy", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("configDialog", "HTTP/HTTPS Proxy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("configDialog", "Proxy Port", None, QtGui.QApplication.UnicodeUTF8))
        self.confProxyEdit.setToolTip(QtGui.QApplication.translate("configDialog", "Specifying a proxy is not available in this release", None, QtGui.QApplication.UnicodeUTF8))
        self.confProxyEdit.setText(QtGui.QApplication.translate("configDialog", "localhost", None, QtGui.QApplication.UnicodeUTF8))
        self.confProxyPort.setText(QtGui.QApplication.translate("configDialog", "8080", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("configDialog", "Browser Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.browserAutoLoadImagesCheckBox.setText(QtGui.QApplication.translate("configDialog", "Auto Load Images?", None, QtGui.QApplication.UnicodeUTF8))
        self.browserEnablePluginsCheckBox.setText(QtGui.QApplication.translate("configDialog", "Enable Plugins?", None, QtGui.QApplication.UnicodeUTF8))
        self.browserEnableJavaCheckBox.setText(QtGui.QApplication.translate("configDialog", "Enable Java?", None, QtGui.QApplication.UnicodeUTF8))
        self.browserEnableWebStorageCheckBox.setText(QtGui.QApplication.translate("configDialog", "Enable Web Storage?", None, QtGui.QApplication.UnicodeUTF8))
        self.configTab.setTabText(self.configTab.indexOf(self.configGeneralTab), QtGui.QApplication.translate("configDialog", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.spiderConfigGroupBox.setTitle(QtGui.QApplication.translate("configDialog", "Spider", None, QtGui.QApplication.UnicodeUTF8))
        self.spiderSubmitFormsCheckBox.setText(QtGui.QApplication.translate("configDialog", "Submit Forms", None, QtGui.QApplication.UnicodeUTF8))
        self.spiderUseDataBankCheckBox.setText(QtGui.QApplication.translate("configDialog", "Use Data Bank Fill Values", None, QtGui.QApplication.UnicodeUTF8))
        self.spiderSubmitUsernamePasswordCheckBox.setText(QtGui.QApplication.translate("configDialog", "Submit Username and Password", None, QtGui.QApplication.UnicodeUTF8))
        self.spiderEvaluateJavascriptCheckBox.setText(QtGui.QApplication.translate("configDialog", "Evaluate JavaScript", None, QtGui.QApplication.UnicodeUTF8))
        self.spiderRetrieveMediaFilesCheckBox.setText(QtGui.QApplication.translate("configDialog", "Retrieve Media Files", None, QtGui.QApplication.UnicodeUTF8))
        self.spiderExcludeDangerouPathCheckBox.setText(QtGui.QApplication.translate("configDialog", "Exclude Dangerous Paths", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("configDialog", "Max Children:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("configDialog", "Redundant Content Limit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("configDialog", "Max Unique Parameters:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("configDialog", "Redundant Structure Limit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("configDialog", "Dangerous Path (Regex):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("configDialog", "Media Extensions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("configDialog", "Max Links:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("configDialog", "Max Link Depth:", None, QtGui.QApplication.UnicodeUTF8))
        self.contentDiscoveryGroupBox.setTitle(QtGui.QApplication.translate("configDialog", "Content Discovery", None, QtGui.QApplication.UnicodeUTF8))
        self.spiderIterateUserAgentsCheckBox.setText(QtGui.QApplication.translate("configDialog", "Iterate User-Agents", None, QtGui.QApplication.UnicodeUTF8))
        self.configTab.setTabText(self.configTab.indexOf(self.configCrawlerTab), QtGui.QApplication.translate("configDialog", "Crawler", None, QtGui.QApplication.UnicodeUTF8))

