# ini cuma shortcut buat bantu para nub
# wk belajar makanya jangan cuma recode KONTOL
# GW juga belajar dari karjok 
import os
from time import sleep
import socket,struct,time,os,sys

def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ', '[\033[1;32m\xe2\x9c\x93\033[1;37m]']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;95m\xe2\x80\xa2\x1b[1;97m] \x1b[1;96minstallation \x1b[1;97m'+o,
        sys.stdout.flush()
        time.sleep(0.7)
def looding2():
    looding2 = [
     '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[\033[1;32m\xe2\x9c\x93\033[0m]\n']
    for o in looding2:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mPelease wait \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.1)

def setup():
       try:
           os.mkdir('/data/data/com.termux/files/home/.termux')
       except:
           pass
       key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
       open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(key)
       os.system('termux-reload-settings')

os.system('clear')
ana = raw_input('\033[37;1mDo you want to \033[34;1mcontinue\033[31;1m? \n\033[31;1mENTER \033[37;1mto Continue : ')
os.system('clear')
looding2()
print('')
tik()
setup()
os.system('clear')
wk = raw_input('\033[37;1mCLOSE your app [\033[32;1mCTRL \033[33;1m+ \033[32;1mD\033[37;1m]')
os.system('exit')
# ini cuma shortcut buat bantu para nub
# wk belajar makanya jangan cuma recode KONTOL
# GW juga belajar dari karjok 
