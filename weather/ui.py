"""
UI Class
"""


from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from custom_widget import CustomHeader, CustomLabel


class MainUI:
    """ UI Components """

    def __init__(self):
        self.main_layout = qtw.QVBoxLayout()
        search_layout = qtw.QHBoxLayout()
        grid_layout = qtw.QGridLayout()

        spacer_1 = qtw.QSpacerItem(24, 24)
        spacer_2 = qtw.QSpacerItem(24, 24)
        spacer_3 = qtw.QSpacerItem(24, 24)

        self.input_city = qtw.QLineEdit()
        self.input_city.setPlaceholderText("Enter City Name")
        self.search_btn = qtw.QPushButton("Search")

        self.weather_icon = qtw.QLabel()
        self.weather_icon.setAlignment(qtc.Qt.AlignCenter)

        self.place_name  = CustomHeader("City:")
        self.temp        = CustomHeader("Temprature:")
        self.desc        = CustomHeader("Description:")
        self.timezone    = CustomHeader("Timezone:")
        self.coordinates = CustomHeader("Coordinates:")
        self.pressure    = CustomHeader("Pressure:")
        self.humidity    = CustomHeader("Humidity:")
        self.sunrise     = CustomHeader("Sunrise:")
        self.sunset      = CustomHeader("Sunset:")

        # Placeholder for fethced values
        self.place_name_val  = CustomLabel()
        self.temp_val        = CustomLabel()
        self.desc_val        = CustomLabel()
        self.timezone_val    = CustomLabel()
        self.coordinates_val = CustomLabel()
        self.pressure_val    = CustomLabel()
        self.humidity_val    = CustomLabel()
        self.sunrise_val     = CustomLabel()
        self.sunset_val      = CustomLabel()

        search_layout.addWidget(self.input_city)
        search_layout.addWidget(self.search_btn)

        # ROW 1
        grid_layout.addWidget(self.place_name, 0, 0)
        grid_layout.addWidget(self.temp, 0, 1)
        grid_layout.addWidget(self.desc, 0, 2)

        # ROW 2
        grid_layout.addWidget(self.place_name_val, 1, 0)
        grid_layout.addWidget(self.temp_val, 1, 1)
        grid_layout.addWidget(self.desc_val, 1, 2)

        # ROW 3
        grid_layout.addItem(spacer_1, 2, 0)

        # ROW 4
        grid_layout.addWidget(self.timezone, 3, 0)
        grid_layout.addWidget(self.coordinates, 3, 1)
        grid_layout.addWidget(self.pressure, 3, 2)

        # ROW 5
        grid_layout.addWidget(self.timezone_val, 4, 0)
        grid_layout.addWidget(self.coordinates_val, 4, 1)
        grid_layout.addWidget(self.pressure_val, 4, 2)

        # ROW 6
        grid_layout.addItem(spacer_2, 5, 0)

        # ROW 7
        grid_layout.addWidget(self.humidity, 6, 0)
        grid_layout.addWidget(self.sunrise, 6, 1)
        grid_layout.addWidget(self.sunset, 6, 2)

        # ROW 8
        grid_layout.addWidget(self.humidity_val, 7, 0)
        grid_layout.addWidget(self.sunrise_val, 7, 1)
        grid_layout.addWidget(self.sunset_val, 7, 2)

        # ROW 9
        grid_layout.addItem(spacer_3, 8, 0)

        self.main_layout.addLayout(search_layout)
        self.main_layout.addWidget(self.weather_icon)
        self.main_layout.addLayout(grid_layout)
