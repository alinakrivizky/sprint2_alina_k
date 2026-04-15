class PointsForPlace:
    def __init__(self):
        self.points = 0
    def get_points_for_place(self,place):
        if place >100:
            print ('Баллы начисляются только первым 100 участникам')
            self.points = 0      
        elif place <1:
            print ('Спортсмен не может занять нулевое или отрицательное место')
            self.points = 0
        else:
            self.points = 101 - place
        return self.points
        