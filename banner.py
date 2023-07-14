import os
from colored import fg, bg, attr

os.system("clear")

red = fg('red')
green = fg('green')
yellow = fg('yellow')
blue = fg('blue')
violet = fg('violet')
white = fg('white')
reset = attr('reset')


def banner():
    print(red + """
   ___ _       _               __ _            _   _     
  / __(_)_ __ | |__   ___ _ __/ _\ | ___ _   _| |_| |__  
 / /  | | '_ \| '_ \ / _ \ '__\ \| |/ _ \ | | | __| '_ \ 
/ /___| | |_) | | | |  __/ |  _\ \ |  __/ |_| | |_| | | |
\____/|_| .__/|_| |_|\___|_|  \__/_|\___|\__,_|\__|_| |_|v1.0
        |_|                                              
    """ + reset 
    + green + """\n[Author: BetterBy0x01]\n[Github: github.com/BetterBy0x01]
    """ + reset
    )