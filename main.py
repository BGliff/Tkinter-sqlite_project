from DataBase import *
from User import *
from EntryPointWindow import *
from PersonalPageWindow import *
from ChangeInfoWindow import *
from TransferWindow import *
from tkinter import messagebox


def checkFields(login, password):
    if login and password:
        return True
    else:
        return False


def registration(login, password):
    if checkFields(login, password):
        if dataBase.searchUser(login):
            messagebox.showwarning('Внимание!', 'Этот логин уже занят')
        else:
            user = User(login, password, 'default', 'default', '0', 0)
            dataBase.setInfo(user)
            messagebox.showinfo('Success', 'Вы успешно зарегистрировались')
            showPersonalPageWindow(dataBase.getInfo(login))
    else:
        messagebox.showwarning('Внимание!', 'Заполните все поля')


def logIn(login, password):
    dataBase.show()
    if checkFields(login, password):
        if dataBase.searchUser(login):
            user = dataBase.getInfo(login)
            if user.password == password:
                messagebox.showinfo('Success', 'Вы успешно вошли в систему')
                showPersonalPageWindow(user)
            else:
                messagebox.showwarning('Внимание!', 'Неверный пароль')
        else:
            messagebox.showwarning('Внимание!', 'Пользователь не зарегистрирован')
    else:
        messagebox.showwarning('Внимание!', 'Заполните все поля')


def showPersonalPageWindow(user):
    entryPointWindow.destroy()
    nameLabel.configure(text=user.name)
    surnameLabel.configure(text=user.surname)
    cashLabel.configure(text=str(user.cash))
    setInfoButton.configure(command=lambda: showChangeInfoWindow(user))
    transferButton.configure(command=lambda: showTransferWindow(user))
    personalPageWindow.deiconify()


def showTransferWindow(user):
    transferWindow.deiconify()
    transferWindowButton.configure(command=lambda: transferCash(user, 50))


def transferCash(user, summ):
    user2 = dataBase.getInfo(login2Entry.get())
    user.cash -= summ
    user2.cash += summ
    dataBase.setInfo(user)
    dataBase.setInfo(user2)
    cashLabel.configure(text=str(user.cash))


def showChangeInfoWindow(user):
    saveButton.configure(command=lambda: changePersonalInfo(user))
    changeInfoWindow.deiconify()


def changePersonalInfo(user):
    user.name = nameEntry.get()
    user.surname = surnameEntry.get()
    user.age = ageEntry.get()
    dataBase.setInfo(user)
    



dataBase = DataBase()
regButton.configure(command=lambda: registration(loginEntry.get(), passwordEntry.get()))
logButton.configure(command=lambda: logIn(loginEntry.get(), passwordEntry.get()))
entryPointWindow.deiconify()
entryPointWindow.mainloop()
