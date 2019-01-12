print('saifullah, 18B-092-CS, A')
print('LAB-05, Exercise 1')
import math
def area():
    radius = eval(input('Enter value of radius in metres(m)= ' ))
    height = eval(input('Enter value for height in metres(m)= '))
    area = (2*math.pi*radius*height) + (2*math.pi*radius**2)
    print('The area of the cylinder is {0:{1}f}cm\u00b2'.format(area,height))
def volume():
    radius = eval(input('Enter value of radius in metres(m)= ' ))
    height = eval(input('Enter value for height in metres(m)= '))
    volume = (math.pi*radius**2*height)
    print("The volume of the cylinder is {0:{1}f}cm\u00b3".format(volume,height))
