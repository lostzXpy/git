import os 

os.system('apt install mpg123')
file = 'assets/main.mp3'
os.system('mpg123 ' + file)
