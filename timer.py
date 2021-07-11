import time
name = input('hi , whats your name ?')
# pip3 install time
secound = int(input('{} A few seconds? \n'.format(name)))
run = input('{} start ?> enter yes or no \n'.format(name))
secound +=1
secounds = 0
if run == 'no' :
    print('see you later')

elif run == 'yes':
 while secounds != secound:
    print('>', secounds)
    time.sleep(1)
    secounds +=1

 print('{} the end secounds , good bye'.format(name))