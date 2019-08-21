import datetime
import json
from tkinter import *

########## CONSTANTS AND GLOBALS
DB_FILE_PATH = 'db.json'
global datenSatz, spielerListe
datenSatz = {}
spielerListe = []

########## Classes
class KaddlAbend:
    def __init__(self, mitspieler1, mitspieler2, mitspieler3, datum, bilanz):
        self.spieler1 = mitspieler1
        self.spieler2 = mitspieler2
        self.spieler3 = mitspieler3
        self.bilanz = bilanz
        self.datum = str(datum)
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

########## FUNCTIONS
def produce_sample_data():
    x = KaddlAbend("Werner", "Schosch", "Jürgen", datetime.date.today(), 3.50)
    y = KaddlAbend("Schosch", "Heinz", "Günther", datetime.date(2019, 5, 20), 2)
    z = KaddlAbend("Bernhard", "Werner", "Hubert", datetime.date(2018, 8, 1), -1.50)
    example_data = [x, y, z]
    alleSpiele = {}
    alleSpiele['Schafkopfabende'] = []

    for bsp in example_data:
        alleSpiele['Schafkopfabende'].append({
            'datum': str(bsp.datum),
            'bilanz': str(bsp.bilanz),
            'mitspieler1': bsp.spieler1,
            'mitspieler2': bsp.spieler2,
            'mitspieler3': bsp.spieler3
        })
    return alleSpiele

def collect_all_Spieler(dataSet):
    global spielerListe
    for abend in dataSet['Schafkopfabende']:
        if abend['mitspieler1'] not in spielerListe:
            spielerListe.append(abend['mitspieler1'])
        if abend['mitspieler2'] not in spielerListe:
            spielerListe.append(abend['mitspieler2'])
        if abend['mitspieler3'] not in spielerListe:
            spielerListe.append(abend['mitspieler3'])


def add_abend(dataSet, bil, dat, spieler):
    newAbend = KaddlAbend(spieler[0], spieler[1], spieler[2], dat, bil)
    dataSet['Schafkopfabende'].append({
        'datum': str(newAbend.datum),
        'bilanz': str(newAbend.bilanz),
        'mitspieler1': newAbend.spieler1,
        'mitspieler2': newAbend.spieler2,
        'mitspieler3': newAbend.spieler3
    })

def save_profile(dataSet, filename):
    with open(filename, 'w') as outfile:
        json.dump(dataSet, outfile)

def load_profile(filename):
    with open(filename, 'r') as infile:
        dataSet = json.load(infile)
    return dataSet

########## MAIN
#demoList = produce_sample_data()
#spielerListe = "Bernd", "Rüdiger", "Jack"
#d = datetime.date(2017, 5, 20)
#add_abend(demoList, -5, d, spielerListe)
#save_profile(demoList, DB_FILE_PATH)
#demoList = load_profile(DB_FILE_PATH)
#for abend in demoList['Schafkopfabende']:
#    print(abend['datum'])



########## Button Handler
def demo_button_pushed():
    global datenSatz
    datenSatz = produce_sample_data()
    lbl.configure(text="Anzahl an Datensätzen: " + str(len(datenSatz['Schafkopfabende'])))

def save_button_pushed():
    global datenSatz
    save_profile(datenSatz, DB_FILE_PATH)

def load_button_pushed():
    global datenSatz
    datenSatz = load_profile( DB_FILE_PATH)
    lbl.configure(text="Anzahl an Datensätzen: " + str(len(datenSatz['Schafkopfabende'])))

def col_spieler_button_pushed():
    global datenSatz, spielerListe
    collect_all_Spieler(datenSatz)
    lbl.configure(text=str(spielerListe))


########## Construct Window
window = Tk()
window.title("Geier Zähler")
window.geometry('700x400')
lbl = Label(window, text="Platzhalter")
lbl.grid(column=0, row=0)
btn_demo = Button(window, text="Erzeuge Beispiel Daten", command=demo_button_pushed)
btn_demo.grid(column=0, row=1)
btn_save = Button(window, text="Speicher Daten", command=save_button_pushed)
btn_save.grid(column=0, row=2)
btn_load = Button(window, text="Lade Daten", command=load_button_pushed)
btn_load.grid(column=0, row=3)
btn_col_spieler = Button(window, text="Lade Spieler", command=col_spieler_button_pushed)
btn_col_spieler.grid(column=0, row=4)
window.mainloop()
