from runway import Runway
from airspace import Airspace
from setup_logging import setup_logging
import numpy as np


class Airport:
    logger = setup_logging('dev')

    def __init__(self, coordinate_x=5000, coordinate_y=5000):
        self.localisation = np.array([coordinate_x, coordinate_y, 0])
        self.airspace = Airspace()
        self.runway_alfa = Runway(start_coordinate_x=4000, start_coordinate_y=5000)
        self.runway_beta = Runway(start_coordinate_x=6000, start_coordinate_y=5000)

    def direct_airplane_to_air_corridor(self):
        pass

    def inform_airplane_to_change_direction(self):
        pass

    def inform_about_airplane_collision(self):
        pass

    def change_priority_of_airplane_landing(self):
        pass

    def airplane_out_of_radar(self):
        pass

    def inform_airplane_to_change_airport(self):
        pass

    def count_airplanes(self):
        pass
