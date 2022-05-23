class User:
    def __init__(self, login, password, name, surname, age, cash):
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.age = age
        self.cash = cash


    def printInfo(self):
        print(self.login, self.password, self.name, self.surname, self.age, self.cash)

