class PointsForMeters:
    def __init__(self):
       self.points = 0

    def get_points_for_meters(self, meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            self.points = 0  
        else:
            self.points = meters * 0.5
        return self.points