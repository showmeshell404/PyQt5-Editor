from PyQt5.QtWidgets import QMainWindow, QAction, QTextEdit, QApplication, QMessageBox, QFontDialog, QColorDialog, \
    QFileDialog
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QFileInfo
import frozen_dir

SETUP_DIR = frozen_dir.app_path()
sys.path.append(SETUP_DIR)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Editor By ShowMeShell"
        self.top = 200
        self.left = 500
        self.width = 500
        self.height = 400
        self.iconName = SETUP_DIR + r"/ico/title.png"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createEditor()
        self.CreateMenu()
        self.show()

    def CreateMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("view")
        helpMenu = mainMenu.addMenu("help")

        choiceAction = QAction(QIcon(SETUP_DIR + r"/ico/new.png"), "Choice Message", self)
        choiceAction.triggered.connect(self.chocieMessageBox)
        helpMenu.addAction(choiceAction)

        helpAction = QAction(QIcon(SETUP_DIR + r"/ico/about.png"), "About Application", self)
        helpAction.triggered.connect(self.AboutMessageBox)
        helpMenu.addAction(helpAction)

        pdfAction = QAction(QIcon(SETUP_DIR + r"/ico/pdf.png"), "Export PDF", self)
        pdfAction.triggered.connect(self.pdfExport)
        fileMenu.addAction(pdfAction)

        printpreviewAction = QAction(QIcon(SETUP_DIR + r"/ico/preview.png"), "Print Preview", self)
        printpreviewAction.triggered.connect(self.printPreviewDialog)
        fileMenu.addAction(printpreviewAction)

        printAction = QAction(QIcon(SETUP_DIR + r"/ico/print.png"), "Print", self)
        printAction.triggered.connect(self.printDialog)
        fileMenu.addAction(printAction)

        copyAction = QAction(QIcon(SETUP_DIR + r"/ico/copy.png"), 'Copy', self)
        copyAction.setShortcut("Ctrl+C")
        # copyAction.triggered.connect(self.copy)
        editMenu.addAction(copyAction)

        cutAction = QAction(QIcon(SETUP_DIR + r"/ico/cut.png"), 'Cut', self)
        cutAction.setShortcut("Ctrl+X")
        # cutAction.triggered.connect(self.cut)
        editMenu.addAction(cutAction)

        clearAction = QAction(QIcon(SETUP_DIR + r"/ico/clear.png"), 'clear', self)
        clearAction.triggered.connect(self.clear)
        editMenu.addAction(clearAction)

        saveAction = QAction(QIcon(SETUP_DIR + r"/ico/save.png"), 'Save', self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.triggered.connect(self.save)
        editMenu.addAction(saveAction)

        openAction = QAction(QIcon(SETUP_DIR + r"/ico/open.png"), 'Open', self)
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.open)
        fileMenu.addAction(openAction)

        exitAction = QAction(QIcon(SETUP_DIR + r"/ico/exit.png"), 'Exit', self)
        exitAction.setShortcut("Ctrl+E")
        exitAction.triggered.connect(self.exitWindow)
        fileMenu.addAction(exitAction)

        fontAction = QAction(QIcon(SETUP_DIR + r"/ico/font.png"), 'Font', self)
        fontAction.setShortcut("Ctrl+F")
        fontAction.triggered.connect(self.fontDialog)
        viewMenu.addAction(fontAction)

        colorAction = QAction(QIcon(SETUP_DIR + r"/ico/color.png"), 'Color', self)
        colorAction.triggered.connect(self.colorDialog)
        viewMenu.addAction(colorAction)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(openAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(exitAction)
        toolbar.addAction(clearAction)
        toolbar.addAction(fontAction)
        toolbar.addAction(colorAction)
        toolbar.addAction(printAction)
        toolbar.addAction(printpreviewAction)
        toolbar.addAction(pdfAction)
        toolbar.addAction(helpAction)

    def save(self):
        filename = QFileDialog.getSaveFileName(self, 'save file', None, "Text files (*.txt);;HTML files (*.html)")
        with open(filename[0], 'w') as f:
            my_text = self.textEdit.toPlainText()
            f.write(my_text)

    def open(self):
        filename = QFileDialog.getOpenFileName(self, 'open file', None)
        with open(filename[0], 'r') as f:
            my_txt = f.read()
            self.textEdit.setPlainText(my_txt)

    def clear(self):
        self.textEdit.clear()

    def exitWindow(self):
        self.close()

    def createEditor(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def colorDialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

    def printPreviewDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec_()

    def printPreview(self, printer):
        self.textEdit.print_(printer)

    def pdfExport(self):
        fn, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf);;All Files")
        if fn != '':
            if QFileInfo(fn).suffix() == "": fn += '.pdf'
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print_(printer)

    def AboutMessageBox(self):
        message = QMessageBox.about(self, "Choice Message", "This is simple texteditor Application")

    def chocieMessageBox(self):
        message = QMessageBox.question(self, "Choice Message", "Do you like Pyqt5 ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if message == QMessageBox.Yes:
            self.textEdit.setText("Yes I like Pyqt5")
        else:
            self.textEdit.setText("No I don't like Pyqt5")


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
