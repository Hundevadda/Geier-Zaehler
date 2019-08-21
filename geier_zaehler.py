import json
import datetime

########## CONSTANTS
DB_FILE_PATH = 'db.json'

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

def save_profile(dataSet, filename):
    with open(filename, 'w') as outfile:
        json.dump(dataSet, outfile)

def load_profile(filename):
    with open(filename, 'r') as infile:
        dataSet = json.load(infile)
    return dataSet

########## MAIN
#demoList = produce_sample_data()
#save_profile(demoList, DB_FILE_PATH)
#demoList = load_profile(DB_FILE_PATH)
#for abend in demoList['Schafkopfabende']:
#    print(abend['datum'])
