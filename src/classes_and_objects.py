# Classes are templates to define objects. It can contain whatever we want, namely variables, functions, lists, etc.

class my_class:
    variable_1 = "This is the first class I define"
    variable_2 = 2

    def my_function(self):
        print("What do u think about this class?")

    def my_second_function(self):
        print("In the following exercises we will explain why the argument self is mandatory")


# Thanks to the classes we can define objects according to the template we have created:

my_object = my_class()

# Moreover we can access to the different items of the class using the dot, for instance:

first_variable_of_my_object = my_object.variable_1
print(first_variable_of_my_object)

# We can also define the variables inside the class according the object we are dealing with, no matter if the type is
# different. Check the example below:

my_second_object = my_class()
my_second_object.variable_1 = 4
print(my_second_object.variable_1)

# In the very same way we can access to the functions defined in the classes:

my_second_object.my_function()


# EXERCISE 1: We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red
# convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00

print(car1.description())
print(car2.description())


# EXERCISE 2: Define a class called 'Circle' which includes the center and the radius of it, and a function that returns
# the diameter and circle area, keeping into account that the radius cannot be a non positive number:

class circle:
    radius = 'nan'
    center = [0, 0]

    def get_center_and_radius(self):
        if self.radius == 'nan':
            output_message = "Please, introduce a value for the radius of the circle"
        elif self.radius == 0:
            output_message = "The circle is degenerated"
        else:
            output_message = "The center of the circle is (%.2f, %.2f) and the radius is %.2f" % (self.center[0],
                                                                                                  self.center[1], self.radius)

        return output_message

    def get_area(self):
        if self.radius == 'nan':
            output_message = "Please, introduce a value for the radius of the circle"
        else:
            area = 3.14*self.radius**2
            output_message = "The area of the circle of radius %.2f is %.2f" % (self.radius, area)

        return output_message


my_circle = circle()
my_circle.radius = 2
print(my_circle.get_center_and_radius())
print(my_circle.get_area())


my_second_circle = circle()
my_second_circle.radius = 'nan'
print(my_second_circle.get_center_and_radius())
print(my_second_circle.get_area())

my_third_circle = circle()
my_third_circle.radius = 0
print(my_third_circle.get_center_and_radius())
print(my_third_circle.get_area())