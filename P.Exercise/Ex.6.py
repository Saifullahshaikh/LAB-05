print('saifullah, 18B-092-CS, A')
print('LAB-05, Exercise 6')
user = input('Enter which law of motion you want to calculate? (first/second/third): ')
if user == 'first':
    def first_law_of_motion():
        Vi= int(input('Enter the initial velocity of the body in m/s: '))
        a= int(input('Enter the accelaration of the body m/s²: '))
        t= int (input('Time taken by the body in seconds:' ))
        Vf= Vi + (a*t)
        print('The Final Velocity of the body is:',Vf, ' m/s')
        first_law_of_motion()
if user == 'second' or '2':
    def second_law_of_motion():
        Vi= eval(input('Enter the initial velocity of the body in m/s: '))
        a= eval(input('Enter the accelaration of the body i m/s²: '))
        t= eval(input('Time taken by the body in seconds:' ))
        S =  Vi*t+ 1/2*(a*(t**2))
        print('The distance taken by the body is: ',str(S),'m')
        second_law_of_motion()
if user == 'third' or '3':
    def third_law_of_motion():
        vf = int(input('Enter the final velocity of the body in m/s: '))
        vi = int(input('Enter the initial velocity of the bodyin m/s: '))
        a2= (input("What does you want to find, acceleration or distamce..?"))
        if a2== 'acceleration':
            s= int(input("Enter the distance cover by body in metres(m):"))
            a= (vf**2-vi**2)/2*s
            print("The acceleration of the body at that time will be: ",a,' m/s²')
        else:
            a= int(input("Enter the accelaration of the body in m/s²:"))
            s= abs((vf**2-vi**2)/2*a)
            print('The distance covered by the body is:' , s, 'm')
        third_law_of_motion()
user = input('Do you want to execute the programe again: ')
while user == 'yes':
    user = input('Do you want to execute the programe again: ')
    user2 = input('Enter which law of motion you want to calculate? (first/second/third): ')
    if user2 == 'first':
        first_law_of_motion()
    if user2 == 'second' or '2':
        second_law_of_motion()
    if user2 == 'third' or '3':
        third_law_of_motion()
    else:
        print('Thank you!')

    
