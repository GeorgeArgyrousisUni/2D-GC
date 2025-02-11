from PyQt5.QtWidgets import QAction

from gc2d.controller.integration.selector import Selector


class DrawAction(QAction):

    def __init__(self, parent, model_wrapper, shortcut=None):
        """
        A DrawAction is a QAction that when triggered, makes a Selector object
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Draw Selection', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        if shortcut is not None:
            self.setShortcut(shortcut)
        self.setStatusTip('Select integration area')

        self.setEnabled(self.model_wrapper.model is not None)
        self.model_wrapper.add_observer(self, self.notify)

        self.triggered.connect(self.draw)

    def draw(self):
        """
        Makes a new Selector object, which initializes itself in the model wrapper
        :return: None
        """
        if self.model_wrapper.model is not None:
            Selector(self.model_wrapper)

    def notify(self, name, value):
        if name == 'model':
            self.setEnabled(value is not None)
