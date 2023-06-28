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
        
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        self._amount = float(value)
        if self._amount == 0:
            raise ValueError("amount must be positive or negative")
        
    @property
    def currency(self):
        return self._currency
    
    @currency.setter
    def currency(self, value):
        self._currency = value
        if self._currency not in CURRENCIES:
            raise ValueError(f"currency must be in {CURRENCIES}")

    def __eq__(self, other):
        return self.date == other.date and self.abstract == other.abstract and self.amount == other.amount and self.currency == other.currency

    def __repr__(self):
        return f"Movimiento: {self.date} - {self.abstract} - {self.amount} {self.currency}"

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
        f = open(self.path, "r")
        reader = csv.DictReader(f, delimiter=",", quotechar='"')
        movements = []
        for register in reader:
            m = Movement(register["date"], register["abstract"], register["amount"], register["currency"])
            movements.append(m)
        return movements
    
    def get(self, pos):
        f = open(self.path, "r")
        reader = csv.DictReader(f, delimiter=",", quotechar='"')
        ix = float("-inf")
        for ix, register in enumerate(reader):
            if ix == pos:
                break

        if pos > ix:
            raise IndexError("movement don't exist")
        
        m = Movement(register["date"], register["abstract"], register["amount"], register["currency"])
        return m

    def update(self, pos, movement):
        rows = []
        with open(self.path, "r") as f:
            reader = csv.DictReader(f, delimiter=",", quotechar='"')
            for i, row in enumerate(reader):
                if i == pos:
                    row["date"] = movement.date
                    row["abstract"] = movement.abstract
                    row["amount"] = str(movement.amount)
                    row["currency"] = movement.currency
                rows.append(row)

        with open(self.path, "w", newline="") as f:
            writer = csv.writer(f, delimiter=",", quotechar='"')
            writer.writerow(["date", "abstract", "amount", "currency"])
            for row in rows:
                writer.writerow([row["date"], row["abstract"], row["amount"], row["currency"]])
        
        f.close()
        
        """
        1. Alternativa
            - abrir el fichero original en lectura
            - abrir otro fichero con nombre el que querais en escritura
            - ir leyendo el fichero original y copiando cada registro en el nuevo
            - hasta llegar a la posición pos, en que se escriben los datos de movement
            - seguir copiando el resto de registros hasta el final
            - borrar el fichero original 
            - renombrar el fichero copia con el nombre de self.path

        2. alternativa
            - abrir el fichero en modo de escritura lectura
            - leer hasta encontrar el registro
            - sustituirlo (para eso tendrás que llevar el puntero de lectura a la posición inicila del
            ultimo registro leido)
            - cerrar y salir
        """
        



