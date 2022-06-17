import os


def datei_öffnen():
    from Webscraper import dateiname
    os.chdir('C:\\Users\\Luca')

    os.system('start excel.exe {}.xlsx'.format(dateiname))