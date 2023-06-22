from datetime import date
import csv
import os

CURRENCIES = ("EUR", "USD")

class Movement:
    def __init__(self, input_date, abstract, amount, currency):
        self.date = input_date

        self.abstract = abstract
        self.amount = amount
        self.currency = currency

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        self._date = date.fromisoformat(value)
        if self._date > date.today():
            raise ValueError("date must be today or lower")

class MovementDAO:
    def __init__(self, file_path):
        self.path = file_path
        if not os.path.exists(self.path):
            f = open(file_path, "w")
            f.write("date,abstract,amount,currency\n")

    def insert(self, movement):
        f = open(self.path, "a", newline="")
        writer = csv.writer(f, delimiter=",", quotechar='"')
        writer.writerow([movement.date, movement.abstract, 
                         movement.amount, movement.currency])
        f.close()
        
    def all(self):
        # devolver una lista de Movements con todos los registros del fichero
        pass
