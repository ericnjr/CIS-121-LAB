from my_classes import Planet
from my_classes import Star
from my_classes import PlanetarySystem

sun = Star("Sun")
ss = PlanetarySystem(sun)


p = Planet('mercury', 1, 2, 3)
ss.add_planet(p)

p = Planet('earth', 3, 4, 5)
ss.add_planet(p)

p = Planet('venus', 5, 6,7)
ss.add_planet(p)

ss.show_planets()
