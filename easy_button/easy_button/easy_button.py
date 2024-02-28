from krita import DockWidget
from PyQt5.QtWidgets import *

DOCKER_TITLE = '❤️ Easy Buttons'

class EasyButton(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(DOCKER_TITLE)
        self.constructor()

    # constructor of Buttons
    def constructor(self): 
        mainWidget = QWidget(self)
        self.setWidget(mainWidget)

        blendingModeNormal = QPushButton() 
        blendingModeNormal.setText("Normal")# 
        blendingModeNormal.clicked.connect(self.createLayerInNormalMode) # How send parameter her????
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(blendingModeNormal)

        blendingModeDarken = QPushButton() 
        blendingModeDarken.setText("Darken")# 
        blendingModeDarken.clicked.connect(self.createLayerInDarkenMode) # How send parameter her????
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(blendingModeDarken)

        blendingModeMultiply = QPushButton() 
        blendingModeMultiply.setText("Multiply")# 
        blendingModeMultiply.clicked.connect(self.createLayerInMultiplyMode) # How send parameter her????
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(blendingModeMultiply)

        blendingModeBurn = QPushButton() 
        blendingModeBurn.setText("Burn")# 
        blendingModeBurn.clicked.connect(self.createLayerInBurnMode) # How send parameter her????
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(blendingModeBurn)

        blendingModeLighten = QPushButton() 
        blendingModeLighten.setText("Lighten")# 
        blendingModeLighten.clicked.connect(self.createLayerInlightenMode) # How send parameter her????
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(blendingModeLighten)

        blendingModeScreen = QPushButton() 
        blendingModeScreen.setText("Screen")# 
        blendingModeScreen.clicked.connect(self.createLayerInScreenMode) # How send parameter her????
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(blendingModeScreen)

        blendingModeColorDodge = QPushButton() 
        blendingModeColorDodge.setText("Color Dodge")# 
        blendingModeColorDodge.clicked.connect(self.createLayerInColorDodgeMode) # How send parameter her????
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(blendingModeColorDodge)

        blendingModeOverlay = QPushButton() 
        blendingModeOverlay.setText("Overlay")# 
        blendingModeOverlay.clicked.connect(self.createLayerInOverlayMode) # How send parameter her????
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(blendingModeOverlay)

        blendingModeSoftLight = QPushButton() 
        blendingModeSoftLight.setText("Soft Light")# 
        blendingModeSoftLight.clicked.connect(self.createLayerInSoftLightMode) # How send parameter her????
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(blendingModeSoftLight)

        blendingModeDivide = QPushButton() 
        blendingModeDivide.setText("Divide")# 
        blendingModeDivide.clicked.connect(self.createLayerInDivideMode) # How send parameter her????
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(blendingModeDivide)

        blendingModeSaturation = QPushButton() 
        blendingModeSaturation.setText("Saturation")# 
        blendingModeSaturation.clicked.connect(self.createLayerInSaturationMode) # How send parameter her????
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(blendingModeSaturation)

        blendingModeColor = QPushButton() 
        blendingModeColor.setText("Color")# 
        blendingModeColor.clicked.connect(self.createLayerInColorMode) # How send parameter her????
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(blendingModeColor)

        blendingModeLuminosity = QPushButton() 
        blendingModeLuminosity.setText("Luminosity")# 
        blendingModeLuminosity.clicked.connect(self.createLayerInLuminosityMode) # How send parameter her????
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(blendingModeLuminosity)
    # Normal Layer
    def createLayerInNormalMode(self):
        app = Krita.instance()
        activeDocument = app.activeDocument()
        activeNode = activeDocument.activeNode()
        def changeBlendingModeLayer(i):
            app = Krita.instance()
            activeDocument = app.activeDocument()
            activeNode = activeDocument.activeNode()
            
            #create new paint layer
            if i == 0:
                app.action('add_new_paint_layer').trigger()

            #change the new layer to blending mode
            if i == 1:
                activeDocument.refreshProjection()
                activeNode.setBlendingMode("normal") #has a list of Bledinding Modes?
                            
            if i < 1: QtCore.QTimer.singleShot(1, lambda: changeBlendingModeLayer(i+1) )
        changeBlendingModeLayer(0)

    def createLayerInDarkenMode(self):
        app = Krita.instance()
        activeDocument = app.activeDocument()
        activeNode = activeDocument.activeNode()
        def changeBlendingModeLayer(i):
            app = Krita.instance()
            activeDocument = app.activeDocument()
            activeNode = activeDocument.activeNode()
            
            #create new paint layer
            if i == 0:
                app.action('add_new_paint_layer').trigger()

            #change the new layer to blending mode
            if i == 1:
                activeDocument.refreshProjection()
                activeNode.setBlendingMode("darken") #has a list of Bledinding Modes?
                            
            if i < 1: QtCore.QTimer.singleShot(1, lambda: changeBlendingModeLayer(i+1) )
        changeBlendingModeLayer(0)

    def createLayerInMultiplyMode(self):
        app = Krita.instance()
        activeDocument = app.activeDocument()
        activeNode = activeDocument.activeNode()
        def changeBlendingModeLayer(i):
            app = Krita.instance()
            activeDocument = app.activeDocument()
            activeNode = activeDocument.activeNode()
            
            #create new paint layer
            if i == 0:
                app.action('add_new_paint_layer').trigger()

            #change the new layer to blending mode
            if i == 1:
                activeDocument.refreshProjection()
                activeNode.setBlendingMode("multiply") #has a list of Bledinding Modes?
                            
            if i < 1: QtCore.QTimer.singleShot(1, lambda: changeBlendingModeLayer(i+1) )
        changeBlendingModeLayer(0)

    def createLayerInBurnMode(self):
        app = Krita.instance()
        activeDocument = app.activeDocument()
        activeNode = activeDocument.activeNode()
        def changeBlendingModeLayer(i):
            app = Krita.instance()
            activeDocument = app.activeDocument()
            activeNode = activeDocument.activeNode()
            
            #create new paint layer
            if i == 0:
                app.action('add_new_paint_layer').trigger()

            #change the new layer to blending mode
            if i == 1:
                activeDocument.refreshProjection()
                activeNode.setBlendingMode("burn") #has a list of Bledinding Modes?
                            
            if i < 1: QtCore.QTimer.singleShot(1, lambda: changeBlendingModeLayer(i+1) )
        changeBlendingModeLayer(0)

    def createLayerInlightenMode(self):
        app = Krita.instance()
        activeDocument = app.activeDocument()
        activeNode = activeDocument.activeNode()
        def changeBlendingModeLayer(i):
            app = Krita.instance()
            activeDocument = app.activeDocument()
            activeNode = activeDocument.activeNode()
            
            #create new paint layer
            if i == 0:
                app.action('add_new_paint_layer').trigger()

            #change the new layer to blending mode
            if i == 1:
                activeDocument.refreshProjection()
                activeNode.setBlendingMode("lighten") #has a list of Bledinding Modes?
                            
            if i < 1: QtCore.QTimer.singleShot(1, lambda: changeBlendingModeLayer(i+1) )
        changeBlendingModeLayer(0)

    def createLayerInScreenMode(self):
        app = Krita.instance()
        activeDocument = app.activeDocument()
        activeNode = activeDocument.activeNode()
        def changeBlendingModeLayer(i):
            app = Krita.instance()
            activeDocument = app.activeDocument()
            activeNode = activeDocument.activeNode()
            
            #create new paint layer
            if i == 0:
                app.action('add_new_paint_layer').trigger()

            #change the new layer to blending mode
            if i == 1:
                activeDocument.refreshProjection()
                activeNode.setBlendingMode("screen") #has a list of Bledinding Modes?
                            
            if i < 1: QtCore.QTimer.singleShot(1, lambda: changeBlendingModeLayer(i+1) )
        changeBlendingModeLayer(0)

    def createLayerInColorDodgeMode(self):
        app = Krita.instance()
        activeDocument = app.activeDocument()
        activeNode = activeDocument.activeNode()
        def changeBlendingModeLayer(i):
            app = Krita.instance()
            activeDocument = app.activeDocument()
            activeNode = activeDocument.activeNode()
            
            #create new paint layer
            if i == 0:
                app.action('add_new_paint_layer').trigger()

            #change the new layer to blending mode
            if i == 1:
                activeDocument.refreshProjection()
                activeNode.setBlendingMode("dodge") #has a list of Bledinding Modes?
                            
            if i < 1: QtCore.QTimer.singleShot(1, lambda: changeBlendingModeLayer(i+1) )
        changeBlendingModeLayer(0)

    def createLayerInOverlayMode(self):
        app = Krita.instance()
        activeDocument = app.activeDocument()
        activeNode = activeDocument.activeNode()
        def changeBlendingModeLayer(i):
            app = Krita.instance()
            activeDocument = app.activeDocument()
            activeNode = activeDocument.activeNode()
            
            #create new paint layer
            if i == 0:
                app.action('add_new_paint_layer').trigger()

            #change the new layer to blending mode
            if i == 1:
                activeDocument.refreshProjection()
                activeNode.setBlendingMode("overlay") #has a list of Bledinding Modes?
                            
            if i < 1: QtCore.QTimer.singleShot(1, lambda: changeBlendingModeLayer(i+1) )
        changeBlendingModeLayer(0)

    def createLayerInSoftLightMode(self):
        app = Krita.instance()
        activeDocument = app.activeDocument()
        activeNode = activeDocument.activeNode()
        def changeBlendingModeLayer(i):
            app = Krita.instance()
            activeDocument = app.activeDocument()
            activeNode = activeDocument.activeNode()
            
            #create new paint layer
            if i == 0:
                app.action('add_new_paint_layer').trigger()

            #change the new layer to blending mode
            if i == 1:
                activeDocument.refreshProjection()
                activeNode.setBlendingMode("soft_light") #has a list of Bledinding Modes?
                            
            if i < 1: QtCore.QTimer.singleShot(1, lambda: changeBlendingModeLayer(i+1) )
        changeBlendingModeLayer(0)

    def createLayerInDivideMode(self):
        app = Krita.instance()
        activeDocument = app.activeDocument()
        activeNode = activeDocument.activeNode()
        def changeBlendingModeLayer(i):
            app = Krita.instance()
            activeDocument = app.activeDocument()
            activeNode = activeDocument.activeNode()
            
            #create new paint layer
            if i == 0:
                app.action('add_new_paint_layer').trigger()

            #change the new layer to blending mode
            if i == 1:
                activeDocument.refreshProjection()
                activeNode.setBlendingMode("divide") #has a list of Bledinding Modes?
                            
            if i < 1: QtCore.QTimer.singleShot(1, lambda: changeBlendingModeLayer(i+1) )
        changeBlendingModeLayer(0)

    def createLayerInSaturationMode(self):
        app = Krita.instance()
        activeDocument = app.activeDocument()
        activeNode = activeDocument.activeNode()
        def changeBlendingModeLayer(i):
            app = Krita.instance()
            activeDocument = app.activeDocument()
            activeNode = activeDocument.activeNode()
            
            #create new paint layer
            if i == 0:
                app.action('add_new_paint_layer').trigger()

            #change the new layer to blending mode
            if i == 1:
                activeDocument.refreshProjection()
                activeNode.setBlendingMode("saturation") #has a list of Bledinding Modes?
                            
            if i < 1: QtCore.QTimer.singleShot(1, lambda: changeBlendingModeLayer(i+1) )
        changeBlendingModeLayer(0)

    def createLayerInColorMode(self):
        app = Krita.instance()
        activeDocument = app.activeDocument()
        activeNode = activeDocument.activeNode()
        def changeBlendingModeLayer(i):
            app = Krita.instance()
            activeDocument = app.activeDocument()
            activeNode = activeDocument.activeNode()
            
            #create new paint layer
            if i == 0:
                app.action('add_new_paint_layer').trigger()

            #change the new layer to blending mode
            if i == 1:
                activeDocument.refreshProjection()
                activeNode.setBlendingMode("color") #has a list of Bledinding Modes?
                            
            if i < 1: QtCore.QTimer.singleShot(1, lambda: changeBlendingModeLayer(i+1) )
        changeBlendingModeLayer(0)

    def createLayerInLuminosityMode(self):
        app = Krita.instance()
        activeDocument = app.activeDocument()
        activeNode = activeDocument.activeNode()
        def changeBlendingModeLayer(i):
            app = Krita.instance()
            activeDocument = app.activeDocument()
            activeNode = activeDocument.activeNode()
            
            #create new paint layer
            if i == 0:
                app.action('add_new_paint_layer').trigger()

            #change the new layer to blending mode
            if i == 1:
                activeDocument.refreshProjection()
                activeNode.setBlendingMode("luminize") #has a list of Bledinding Modes?
                            
            if i < 1: QtCore.QTimer.singleShot(1, lambda: changeBlendingModeLayer(i+1) )
        changeBlendingModeLayer(0)

    # notifies when views are added or removed
    #pass means do not do anything
    def canvasChanged(self, canvas):
        pass