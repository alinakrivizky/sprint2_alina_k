class PointsForPlace:
    @staticmethod
    def get_points_for_place(place : int):
        points = 0
        if place >100:
            print ('Баллы начисляются только первым 100 участникам')    
        elif place <1:
            print ('Спортсмен не может занять нулевое или отрицательное место')
        else:
            points = 101 - place
        return points

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters: int):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = meters * 0.5
        return points


class TotalPoints(PointsForPlace, PointsForMeters):
    @staticmethod
    def get_total_points(meters : int, place : int):
        points_from_place = PointsForPlace.get_points_for_place(place)
        points_from_meters = PointsForMeters.get_points_for_meters(meters)
        total = points_from_meters + points_from_place
        return total
    
print(PointsForPlace.get_points_for_place(10))

print(PointsForMeters.get_points_for_meters(10))

print(TotalPoints.get_points_for_place(10))
print(TotalPoints.get_points_for_meters(10))
print(TotalPoints.get_total_points(100, 10))