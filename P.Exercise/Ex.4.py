print('saifullah, 18B-092-CS, A')
print('LAB-05, Exercise 4')
def palindrome():
    s = input('Enter a word to check it is palindrome or not: ')
    word = s.casefold()
    Rword = reversed(s)
    if list(s) == list (Rword):
        print('Yes your word is palindrome', s)
    else:
        print('Sorry, your word is not palindrome.')
palindrome()
user = input('Want to check another word? (enter: yes / no): ')
while user == 'yes':
    palindrome()
    user = input('Want to check another word? (enter: yes/no): ')
else:
    print('Thank you')
