import os,time,platform
os.system('clear')
#print('[>] Checking Updates')
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    import SHARE
elif bit=='32bit':
    import SH32
else:
    print('\033[1;31m[×] unknown Device 32')
 
