from tkinter import *
from öffnen import datei_öffnen
from Webscraper import webscraper

   
gui = Tk()
gui.resizable(width=False, height=False)
gui.title("Amazon Webscraper")


info_label = Label(gui, text="""\
    ************* Amazon Webscraper *************
    1) Gewünschtes Produkt eintragen.
    2) Anzahl der zu suchenden Seiten auswählen.
    3) Name der Excel Datei eintragen.
    4) "Start" Button drücken
    5) Warten bis das Programm beendet ist
    6) Button "Öffnen" drücken
    7) Beenden Button drücken""")


product_label = Label(gui, text="Zu suchendes Produkt eintragen:")
product_entry = Entry(gui, bd=5, width=20)

seiten_label = Label(gui, text="Anzahl der Seiten eintragen:")
options = [1,2,3,4,5,6,7,8,9,10]
seiten_dropdown = IntVar()
seiten_dropdown.set(1)
drop = OptionMenu(gui, seiten_dropdown, *options)

dateiname_label = Label(gui, text="Namen der Datei eintragen:")
dateiname_entry = Entry(gui, bd=5, width=20)


start_button = Button(gui, text="Webscraper: Start", command=lambda : webscraper())

öffnen_button = Button(gui, text="Öffnen", command=lambda : datei_öffnen())

beenden_button = Button(gui, text="Beenden", command=gui.destroy)


info_label.grid(row=0, column=0, columnspan=2)

product_label.grid(row=1, column=0)
product_entry.grid(row=1, column=1)

seiten_label.grid(row=2, column=0)
drop.grid(row=2, column=1)

dateiname_label.grid(row=3, column=0)
dateiname_entry.grid(row=3, column=1)

start_button.grid(row=4, column=0)

öffnen_button.grid(row=4, column=1)

beenden_button.grid(row=4, column=2)


gui.mainloop()