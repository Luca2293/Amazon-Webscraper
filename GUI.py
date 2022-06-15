from tkinter import *


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

start_button = Button(gui, text="Start")

öffnen_button = Button(gui, text="Öffnen")

beenden_button = Button(gui, text="Beenden")


gui.mainloop()
