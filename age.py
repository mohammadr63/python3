import time
from typing import Sequence



name = input('please enter your name ? \n ')
time.sleep(1)
def ages() :
    welcome = print('welcome the  Ages\n ')
    time.sleep(1)
    sen = int(input(" Hi , {} please enter your age \n".format(name)))
    time.sleep(1.4) 
    if sen>0 and sen < 6 :
        print("({}, you are a children)".format(name))
        time.sleep(1.2)
    elif sen >=6 and sen <10 :
        time.sleep(1.2)
        print("({}, you are a baby )".format(name))
        time.sleep(1.2)
    elif sen >=10 and sen <14 :
        print("({}, you are a teenager)".format(name))
        time.sleep(1.2)
    elif sen >=14 and sen <24 :
        print("({}, you are a  young )".format(name))
        time.sleep(1.2)
    elif  sen >=24 and sen <40 :
        print("({}, you are a adult)".format(name))
        time.sleep(1.2)
    elif sen >=40:
        print("({}, you are a middle-aged)".format(name ))
        time.sleep(1.2)
    again()
def again():

    age_again = input('''
    {} Do you want to Ages again?
    Please type Y for YES or N for NO.
    '''.format(name))
    time.sleep(1)

   
    if age_again.upper() == 'Y':
        ages()
        time.sleep(1)
    elif age_again.upper() == 'N':
        print('See you later.')
        time.sleep(1)
    else:
        again()

ages()