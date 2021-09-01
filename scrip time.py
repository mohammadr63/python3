import time
import sys
from tqdm import trange


def do_something():
    time.sleep(1)

def do_another_something():
    time.sleep(1)

def scrip ():
    for i in trange(10, file=sys.stdout, desc='outer loop'):
        do_something()

        for j in trange(100,file=sys.stdout, leave=False, unit_scale=True, desc='inner loop'):
            do_another_something()
    again()
def again():

    timer_again = input('''
    Do you want to scrip time again?
    Please type Y for YES or N for NO.
    ''')
    if timer_again.upper() == 'Y':
      scrip ()
    elif timer_again.upper() == 'N':
        print('See you later.')
    else:
        again()