import os
from Webscraper import dateiname

def öffnen():
    os.chdir('C:\\Users\\Luca')

    os.system('start excel.exe {}.xlsx'.format(dateiname))