from tkinter import *



personalPageWindow = Tk()
personalPageWindow.withdraw()
personalPageWindow.resizable(width = False, height = False)
personalPageWindow.geometry('500x500')
personalPageWindow.title('Your Page')
personalPageWindow['bg'] = '#ccc'
nameLabel = Label(personalPageWindow, font='Comfortaa 20', fg='#3d3d42', bg='#ccc')
surnameLabel = Label(personalPageWindow, font='Comfortaa 20', fg='#3d3d42', bg='#ccc')
cashLabel = Label(personalPageWindow, font='Comfortaa 20', fg='#3d3d42', bg='#ccc')
setInfoButton = Button(personalPageWindow, text = 'Изменить личные данные', font = 'Consolas 13',
           fg='#eff5c9',
           bg='#48494f',
           relief='solid',
           activeforeground = '#eff5c9',
           activebackground = '#6e6f73')
transferButton = Button(personalPageWindow, text = 'Отправить деньги', font = 'Consolas 13',
           fg='#eff5c9',
           bg='#48494f',
           relief='solid',
           activeforeground = '#eff5c9',
           activebackground = '#6e6f73')

nameLabel.pack()
surnameLabel.pack()
cashLabel.pack()
setInfoButton.pack()
transferButton.pack()
