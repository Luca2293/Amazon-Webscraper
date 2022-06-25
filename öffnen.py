import os

def datei_öffnen():
    from Webscraper import dateiname
    os.system('start excel.exe {}.xlsx'.format(dateiname))