#!usr/bin/env Python3

"""
Weather App

Author: Deepak Talan
Github: @d02d33pak
"""

import datetime
import os
import sys
import urllib.request

import requests

from dotenv import load_dotenv
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from ui import MainUI


class WorkerSignal(qtc.QObject):
    """ Signal for the Worker class """

    error = qtc.pyqtSignal(str)
    success = qtc.pyqtSignal(dict)
    finished = qtc.pyqtSignal()


class WeatherWorker(qtc.QRunnable):
    """ Worker Thread """

    signals = WorkerSignal()

    def __init__(self, location):
        super(WeatherWorker, self).__init__()
        self.location = location

    @qtc.pyqtSlot()
    def run(self):
        """ Fetch Weather Data """
        try:
            load_dotenv()
            url = "http://api.openweathermap.org/data/2.5/weather"
            params = dict(units="metric", q=self.location, appid=os.getenv("API_KEY"))
            response = requests.get(url, params).json()
            if response["cod"] != 200:
                raise Exception(response["message"])
            self.signals.success.emit(response)
        except Exception as error:
            self.signals.error.emit(str(error))
        self.signals.finished.emit()


class MainWindow(qtw.QWidget, MainUI):
    """ Main Window """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.widht  = 600
        self.height = 200
        self.pos_x  = 400
        self.pos_y  = 200
        self.setGeometry(self.pos_x, self.pos_y, self.widht, self.height)
        self.setWindowTitle("Weather App")

        self.threadpool = qtc.QThreadPool()

        self.input_city.returnPressed.connect(self.update_weather)
        self.search_btn.pressed.connect(self.update_weather)

        self.setLayout(self.main_layout)
        self.show()

    def show_error(self, message):
        """ Show Alert Dialog on error """
        alert = qtw.QMessageBox.warning(None, "Warning", message.title())

    def update_weather(self):
        """ Fetch Weather Data """
        worker = WeatherWorker(self.input_city.text())
        worker.signals.success.connect(self.set_weather)
        worker.signals.error.connect(self.show_error)
        self.threadpool.start(worker)

    def set_weather(self, weather):
        """ Set Weather Info in UI """
        self.input_city.setText("")

        image_url = "https://openweathermap.org/img/w/"
        img = urllib.request.urlopen(
            image_url + weather["weather"][0]["icon"] + ".png"
        ).read()
        pixmap = qtg.QPixmap()
        pixmap.loadFromData(img)
        self.weather_icon.setPixmap(pixmap)

        self.place_name_val.setText(
            str(weather["name"]) + ", " + weather["sys"]["country"]
        )
        self.temp_val.setText(
            str(weather["main"]["temp"])
            + "°C, feels like "
            + str(weather["main"]["feels_like"])
            + "°C"
        )
        self.desc_val.setText(weather["weather"][0]["description"].title())
        self.timezone_val.setText(self.from_sec_to_hours(weather["timezone"]))
        self.coordinates_val.setText(
            str(weather["coord"]["lon"]) + "°, " + str(weather["coord"]["lat"]) + "°"
        )
        self.pressure_val.setText(str(weather["main"]["pressure"]))
        self.humidity_val.setText(str(weather["main"]["humidity"]))
        self.sunrise_val.setText(
            str(self.from_ts_to_time_of_the_day(weather["sys"]["sunrise"]))
        )
        self.sunset_val.setText(
            str(self.from_ts_to_time_of_the_day(weather["sys"]["sunset"]))
        )

    def from_ts_to_time_of_the_day(self, timestamp):
        """ Convert Timestamp to Time in AM/PM """
        dt_time = datetime.datetime.fromtimestamp(timestamp)
        return dt_time.strftime("%I %p").upper()

    def from_sec_to_hours(self, seconds):
        """ Convert Seconds to TimeZone hours """
        hours = seconds // 3600
        seconds = seconds % 3600
        minutes = seconds // 60
        return f"GMT {hours:+03}:{minutes:02}"


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
