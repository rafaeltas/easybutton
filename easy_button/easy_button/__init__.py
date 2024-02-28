from krita import DockWidgetFactory, DockWidgetFactoryBase
from .easy_button import EasyButton

DOCKER_ID = 'template_docker'
instance = Krita.instance()
dock_widget_factory = DockWidgetFactory(DOCKER_ID,
                                        DockWidgetFactoryBase.DockRight,
                                        EasyButton)

instance.addDockWidgetFactory(dock_widget_factory)