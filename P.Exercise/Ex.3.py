print('saifullah, 18B-092-CS, A')
print('LAB-05, Exercise 3')
def airthmetic_seq():
    nth_term = n = eval(input('Enter the number of your desired term in digit: '))
    f_term = a = eval(input('Enter the first term in digit: '))
    common_difference = d = eval(input('Enter the value of common difference: '))
    res = a+((n-1)*d)
    print('The',str(n),'th term in the given sequence is: ', res)
    user = input('Do you want another term ? ( enter yes/ no): ')
    while user == 'yes':
        n = eval(input('Enter the number of another term: '))
        res = a+((n-1)*d)
        print('The',str(n),'th term in the given sequence is: ', res)
        user = input('Do you want another term ? ( enter yes/ no): ')
    if user == 'no':
        print('Thank you')
    
                
