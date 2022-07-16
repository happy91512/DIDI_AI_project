from UI import Ui_MainWindow
from PyQt5 import QtGui, QtWidgets, QtCore
from signal import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import sys
import cv2
import time
from detect import object_set_arg, object_main


class VideoThread(QThread):
    global ring_hour, ring_minute, ring_time
    ring_hour, ring_minute, ring_time, = 23, 15, 10
    change_pixmap_signal = pyqtSignal(np.ndarray)
    set_time = pyqtSignal(str)
    camera_flag = pyqtSignal(bool)
    check_person_up = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam or video
        # img_flag = "video.avi"
        img_flag = 0
        cap = cv2.VideoCapture(img_flag)
        ret, frame = cap.read()
        PRE_TIME = time.time()
        if ret:
            self.camera_flag.emit(True)
            arg_list = list(object_set_arg(cap))
            # print(len(self.arg_list)) labels,input_height,input_width,times,check_wakeup,alarm_clock
        # sleep_time = cap.get(cv2.CAP_PROP_FPS)
        frame_counter = 0   
        check_person_up = False                                                                                                                 
        while self._run_flag:
            ret, frame = cap.read()
            old_arg_list = arg_list.copy()
            arg_list.append(cap)
            ala_list = [ring_hour, ring_minute, ring_time]
            arg_list.extend(ala_list)
            if ret:
                frame_counter += 1
                frame, get_up = object_main(
                    arg_list[0],
                    arg_list[1],
                    arg_list[2],
                    arg_list[3],
                    arg_list[4],
                    arg_list[5],
                    arg_list[6],
                    arg_list[7],
                    arg_list[8],
                    arg_list[9],
                    arg_list[10],
                    frame_counter,
                )
            
                self.change_pixmap_signal.emit(frame)
            self.set_time.emit(time.strftime("%H:%M", time.localtime()))
            if frame_counter == 7:
                frame_counter = 0
            if get_up:
                check_person_up = True
                print(check_person_up)
                self.check_person_up.emit(True)
                # 此處可加入語音辨識

            arg_list = old_arg_list.copy()
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        self.setWindowTitle("Alarm")
        self.disply_width = 640
        self.display_height = 480
        self.set_time_flag = False

        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.set_time.connect(self.update_time)
        self.thread.camera_flag.connect(self.update_mes)
        self.thread.check_person_up.connect(self.update_getup_mes)
        # start the thread
        self.thread.start()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    def setup_control(self):
        self.ui.set_time_Button.clicked.connect(self.time_buttomClicked)
        self.ui.now_time_text.setText(time.strftime("%H:%M", time.localtime()))

    def time_buttomClicked(self):
        self.set_time_flag = True
        self.set_time = str(self.ui.timeEdit.dateTime())
        self.set_time = self.set_time.split(",")
        global ring_time, ring_hour, ring_minute, check_person_up
        ring_time = self.ui.spinBox.value()
        ring_hour = int(self.set_time[3])
        ring_minute = int(self.set_time[4][1:-1])
        self.ui.history.setText(f"成功設定{ring_hour}點{ring_minute}分的鬧鐘，響鈴{ring_time}分鐘")

    @pyqtSlot(str)
    def update_time(self, time_text):
        self.ui.now_time_text.setText(time_text)

    @pyqtSlot(bool)
    def update_getup_mes(self):
        self.ui.history.setText("成功辨識起身，等待語音偵測中...")

    @pyqtSlot(bool)
    def update_mes(self, camera_flag):
        if camera_flag == True:
            self.ui.history.setText("成功開啟鏡頭，等待動作中...")
            camera_flag = False

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.ui.view.setPixmap(qt_img)
    #convert the image to QT-standard format 
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(
            rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888
        )
        p = convert_to_Qt_format.scaled(
            self.disply_width, self.display_height, Qt.KeepAspectRatio
        )
        return QPixmap.fromImage(p)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())
