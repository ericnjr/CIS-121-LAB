
class Star:
    def __init__(self, _name):
        self.name = _name
    def get_name(self):
        return self.name
    def set_name(self, _new_name):
        self.name = _new_name
    def __str__(self):
        msg = ' '
        msg += f'The name of the star is {self.get_name()}'
        return msg



import math
class Planet:   #creating blueprint for new object and planet is the name of the object 
    def __init__(self, _name, _radius, _mass, _distance):# constructor
        self.name = _name 
        self.radius = _radius
        self.mass = _mass
        self.distance = _distance
    def get_name(self):
        return self.name 
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_distance(self):
        return self.distance
    
    def get_volume(self):
        volume = 4/3 * math.pi * self.radius ** 3
        return volume
    def get_density(self):
        density = self.mass / self.get_volume()
        return density
    def set_name(self, new_name):
        self.name = new_name
    def __str__(self):
        msg = ' '
        msg += f'hello {self.get_name()}. How are you?'
        return msg   


#write a planetary system class that takes a star as an argument, has the ability to add planets to the system, and can print all the planets in the system
class PlanetarySystem:
    def __init__(self, _star):
        self.star = _star
        self.planets = []

    def add_planet(self, _planet):
        self.planets.append(_planet)

    def show_planets(self):
        for planet in self.planets: #iterate through each planet and print the name
            print(planet.get_name())







