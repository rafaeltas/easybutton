from krita import DockWidget
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
from .buttons_list import blending_modes

DOCKER_TITLE = 'Easy Button'

class EasyButton(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(DOCKER_TITLE)
        self.button_mapping = {}

        mainWidget = QWidget(self)
        self.setWidget(mainWidget)
        # Read all option of blending modes in "button_lis.py" files.
        for key, value in blending_modes.items():
            
            button = QPushButton(key)
            # Stryle of BM Buttons.
            button.setStyleSheet("background-color: #7f00ff; color: #ffffff")
            self.button_mapping.update({button: value})
            button.clicked.connect(lambda _, button=button: self._on_button_click(button))

            mainWidget.setLayout(QVBoxLayout())
            mainWidget.layout().addWidget(button)

    def _on_button_click(self, source):

        blending_mode = self.button_mapping.get(source)
        if blending_mode:
            self._apply_blending_mode(blending_mode)
        #Debugging

        # app = Krita.instance()
        # activeDocument = app.activeDocument()
        # activeNode = activeDocument.activeNode()
        # layoutForButtons = QHBoxLayout()
        # newButton = QPushButton(blending_mode)
        # layoutForButtons.addWidget(newButton)
        # newDialog = QDialog()
        # newDialog.setLayout(layoutForButtons)
        # newDialog.setWindowTitle(blending_mode)
        # newDialog.exec_()

    # Normal Layer
    def _apply_blending_mode(self, blending_mode):
        mode = blending_mode
        modifiers = QApplication.keyboardModifiers()
        def changeBlendingModeLayer(i):
            app = Krita.instance()
            activeDocument = app.activeDocument()
            activeNode = activeDocument.activeNode()            
            #create new paint layer
            if  i == 0 and modifiers == Qt.ShiftModifier:
                i = i + 3

            if i == 1:
                app.action('add_new_paint_layer').trigger()

            if  i == 2 and modifiers == Qt.ControlModifier:
                app.action('move_layer_down').trigger()

            #change the new layer to blending mode
            if i == 3:
                activeNode.setBlendingMode(mode)
                            
            if i < 4: QTimer.singleShot(4, lambda: changeBlendingModeLayer(i+1) )
        changeBlendingModeLayer(0)


    # notifies when views are added or removed
    #pass means do not do anything
    def canvasChanged(self, canvas):
        pass