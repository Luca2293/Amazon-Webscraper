from tkinter import *
from Webscraper import starten
from öffnen import öffnen

gui = Tk()
gui.resizable(width=False, height=False)
gui.title("Amazon Webscraper")


info_label = Label(gui, text="""\
    ************* Amazon Webscraper *************
       1) Gewünschtes Produkt eintragen.
       2) Anzahl der zu suchenden Seiten eintragen.
       3) Name der Excel Datei eintragen.
       4) "Start" Button drücken
       5) Warten bis das Programm beendet ist
       6) Button "Öffnen" drücken
       7) Beenden Button drücken""")

product_label = Label(gui, text="Zu suchendes Produkt eintragen:")
product_entry = Entry(gui, bd=5, width=20)

seiten_label = Label(gui, text="Anzahl der Seiten eintragen:")
seiten_entry = Entry(gui, bd=5, width=20)

dateiname_label = Label(gui, text="Namen der Datei eintragen:")
dateiname_entry = Entry(gui, bd=5, width=20)

start_button = Button(gui, text="Start", command=starten())

öffnen_button = Button(gui, text="Öffnen", command=öffnen())

beenden_button = Button(gui, text="Beenden", command=gui.destroy)


info_label.grid(row=0, column=0)

product_label.grid(row=1, column=0)
product_entry.grid(row=1, column=1)

seiten_label.grid(row=2, column=0)
seiten_entry.grid(row=2, column=1)

dateiname_label.grid(row=3, column=0)
dateiname_entry.grid(row=3, column=1)

start_button.grid(row=4, column=0)

öffnen_button.grid(row=4, column=1)

beenden_button.grid(row=4, column=2)


gui.mainloop()
