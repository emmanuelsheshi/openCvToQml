from PySide6.QtQuick import QQuickImageProvider
from PySide6.QtCore import Slot, Signal
from PySide6.QtGui import QImage, QColor


class MyImageProvider(QQuickImageProvider):
    IMAGE_TYPE = QQuickImageProvider.ImageType.Image
    imageChanged = Signal(bool)


    def __init__(self):
        QQuickImageProvider.__init__(self, MyImageProvider.IMAGE_TYPE)
        self.image = QImage(3, 3, QImage.Format_RGB32)
        self.image.fill(QColor("black"))
        self.image = QImage("loading.png")




    def requestImage(self, id, size, requestedSize):
        return self.image


    @Slot(QImage)
    def updateImage(self, image: QImage):
        if not(self.image.isNull()) and self.image != image:
            self.image = image
            self.imageChanged.emit(True)

