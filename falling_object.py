# This is my falling object calculator, It will output where an object will be and its velocity
# at a given time. Give it different gravity values to simulate dropping something on another planet's
# gravity. It was made by me, Enzo Carter.
# Note: 9.81 m/s is Earth's gravity, the moon's gravity is 1.62 m/s

print('''
This is my falling object calculator, It will output where an object will be and its velocity
at a given time. Give it different gravity values to simulate dropping something on another planet's
gravity. It was made by me, Enzo Carter.
Note: 9.81 m/s is Earth's gravity, the moon's gravity is 1.62 m/s
''')


# These are the questions that will determine what the output consists of
object = float(input("Mass of object one (kgs): "))

gravity = float(input("\nEffect of gravity (m/s): "))

position = float(input("\nVertical position of object one (m): "))

time_input = input("\nHow long will the object be recorded (s): ")
temporal = float(time_input)


# This class makes the object that will have its velocity measured
class Object:
    def __init__(self, mass, current_position):
        self.mass = mass
        self.current_position = current_position


# This makes the specific gravity we are applying to the object
class Gravity:
    def __init__(self, gravity_value):
        self.gravity_value = gravity_value


# This function shows where the object is and how much velocity it has
def falling(position1, velocity1, force_added):
    force_added = force_added * temporal
    position2 = position1 - force_added
    velocity2 = velocity1 + (gravity * temporal)
    if position2 <= 0:
        position2 = 0
        impact_str = " on impact with the ground"
    else:
        impact_str = ""
    position3 = round(position2, 1)
    velocity3 = round(velocity2, 2)
    if temporal == 1:
        plural = ""
    else:
        plural = "s"
    print("\nTime Span: " + time_input + " second" + plural + " of falling")
    print("Position:", position3, "meters above ground")
    print("Velocity:", velocity3, "meters per second" + impact_str)


# This makes an instance of object and prints it
object1 = Object(object, position)
gravity1 = Gravity(gravity)


# This does the calculation of gravities effect
force = object1.mass * gravity1.gravity_value

print("\nCalculating...")

falling(position, 0, force)
