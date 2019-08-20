import json
import datetime

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

x = KaddlAbend("Nusse", "Reissy", "Flo", datetime.date.today(), 3.50)
y = KaddlAbend("Maxi", "Reissy", "Nusse", datetime.date(2019, 5, 20), 2)
z = KaddlAbend("Flo", "Werner", "Maxi", datetime.date(2018, 8, 1), -1.50)
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

with open('db.json', 'w') as outfile:
    json.dump(alleSpiele, outfile)
