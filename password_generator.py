##the main idea of this project is to generate random password of given characters,symbols, numerical values
import random
pas=[]
while True:
    char=input("do you wanna include charcters in the password?")
    if char=='yes':
        char_pass=str(input("enter the characters you want to include in the password: "))
        c=random.choices(char_pass,k=3)
        print(c)
        for chars in c:
            pas.append(chars)
        # result=''.join(map(str,pas))
        result=''.join(pas)
        print(result)

    inte=input("do you want to include any integers in the password?: ")
    if inte == 'yes':
        num=int(input("how many integers do you wanna include here? "))
        for i in range(0,num):
            r=random.randint(0,9)
            print(r)
            pas.append(r)
        print(pas)
    print("Your Required Password Is: ")
    pass_list=pas
    pass_string=''.join(map(str,pass_list))
    print(pass_string)
    break

####   map(str, my_list): This converts each item in the list my_list into a string.
# ###  ''.join(): Joins all the string elements into a single string.