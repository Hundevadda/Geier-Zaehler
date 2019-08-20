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
print(x.toJSON())
print(x.datum)
