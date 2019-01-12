print('saifullah, 18B-092-CS, A')
print('LAB-05, Exercise 2')
user = (input('What do you want to calculate area/volume of the rectangle: '))
if user == 'area':
        def area():
            length = eval(input('Enter the length of rectangle: '))
            width = eval(input('Enter the width of rectangle: '))
            res = length*width
            print('The area of the rectangle is {0:{1}f}cm\u00b2'.format(res,width))
elif user == 'volume':
        def volume():
            length = eval(input('Enter the length of rectangle: '))
            width = eval(input('Enter the width of rectangle: '))
            height = eval(input('Enter the height of rectangle: '))
            res = length*width*height
            print('The volume of the rectangle is{0:{1}f}cm\u00b3'.format(res,length))
