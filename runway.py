class Runway:

    def __init__(self, start_coordinate_x, start_coordinate_y, length=2000):
        self.length = length
        self.start_point_localisation = {
            "x": start_coordinate_x,
            "y": start_coordinate_y,
            "z": 0
        }
        self.end_point_localisation = {
            "x": start_coordinate_x,
            "y": start_coordinate_y + length,
            "z": 0
        }
        self.is_free = True

    def block_the_runway(self):
        self.is_free = False

    def open_the_runway(self):
        self.is_free = True

