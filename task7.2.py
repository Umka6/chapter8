class Plane:
    make = str()
    model = str()
    year = int()
    max_speed = int()
    odometer = int()
    is_flying = bool()

    def take_off(self):
        Plane.is_flying = True

    def land(self):
        Plane.odometer = 0
        Plane.is_flying = False

    def fly(self, dist):
        Plane.odometer = dist

    def stats(self):
        Plane.make = 'Boeing'
        Plane.model = '747 MAX'
        Plane.year = 2015
        Plane.max_speed = 967
        return 'Company: ' + Plane.make + '\nModel: ' + Plane.model + '\nYear: ' + str(
            Plane.year) + '\nMax speed: ' + str(Plane.max_speed) + 'km/h\nDistance: ' + str(
            Plane.odometer) + 'km\nIs flying: ' + str(Plane.is_flying)


plane1 = Plane()
print(plane1.stats())
plane1.fly(9490)
print(plane1.stats())
plane1.take_off()
print(plane1.stats())
plane1.land()
print(plane1.stats())