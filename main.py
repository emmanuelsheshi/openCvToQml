# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from ImageProvider import MyImageProvider
from VideoStreamer import VideoStreamer, AppClass


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).resolve().parent / "main.qml"


    videoStreamer = VideoStreamer()
    videoConverter = AppClass()
    imageProvider = MyImageProvider()


    engine.rootContext().setContextProperty("videoStreamer", videoStreamer)
    engine.rootContext().setContextProperty("imageProvider", imageProvider)

    videoStreamer.newImage.connect(videoConverter.update_image)
    videoConverter.globalImage.connect(imageProvider.updateImage)
    engine.addImageProvider("live", imageProvider)








    engine.load(qml_file)









    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
