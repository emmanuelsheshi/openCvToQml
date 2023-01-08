import cv2
from PySide6.QtCore import QObject, Signal, Slot, QThread, Qt
from PySide6.QtGui import QImage
import numpy as np



class VideoStreamer(QThread):
    newImage = Signal(np.ndarray)
    def __init__(self):
        super().__init__()
        self._run_flag = True


    def run(self):
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            cv2.waitKey(1)
            if ret:
                self.newImage.emit(cv_img)


            # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()


class AppClass(QObject):
    globalImage = Signal(QImage)


    def __init__(self):
        QObject.__init__(self)
        self.thread = VideoStreamer()
        self.thread.newImage.connect(self.update_image)
        self.thread.start()
        self.img = QImage(3, 3, QImage.Format_Indexed8)


    def closeEvent(self, event):
        self.thread.stop()
        event.accept()


    @Slot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.img = qt_img
        self.globalImage.emit(self.img)


    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(640, 480, Qt.KeepAspectRatio)
        return p





