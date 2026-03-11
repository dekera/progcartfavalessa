from datetime import date

class person():
    def __init__(self, name: str, country:str, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def age(self):
        hoje = date.today()
        return hoje.year - self.dob[0] - ((hoje.month,hoje.day)<(self.dob[1],self.dob[2]))

if __name__ == "__main__":
    pessoa = person("André","Brasil",[2001, 8, 6])
    print(pessoa.age())