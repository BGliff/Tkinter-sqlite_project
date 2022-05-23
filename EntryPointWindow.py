from tkinter import *


entryPointWindow = Tk()
entryPointWindow.withdraw()

entryPointWindow.resizable(width=False, height=False)
entryPointWindow.geometry('300x200')
entryPointWindow.title('Test Window')
entryPointWindow['bg'] = '#ccc'


loginLabel = Label(entryPointWindow, text='Login:', font='Comfortaa 20', fg='#3d3d42', bg='#ccc')
loginEntry = Entry(entryPointWindow, font='Consolas 15',
              fg='#eff5c9',
              bg='#48494f',
              relief='solid',
              justify='center')

passwordLabel = Label(entryPointWindow, text='Password:', font='Comfortaa 20', fg='#3d3d42', bg='#ccc')
passwordEntry = Entry(entryPointWindow, font='Consolas 15',
                 fg='#eff5c9',
                 bg='#48494f',
                 relief='solid',
                 justify='center',
                 show='*')

regButton = Button(entryPointWindow, text='Зарегистрироваться', font='Consolas 13',
               fg='#eff5c9',
               bg='#48494f',
               relief='solid',
               activeforeground='#eff5c9',
               activebackground='#6e6f73')

logButton = Button(entryPointWindow, text='Войти', font='Consolas 13',
               fg='#eff5c9',
               bg='#48494f',
               relief='solid',
               activeforeground='#eff5c9',
               activebackground='#6e6f73')


loginLabel.pack()
loginEntry.pack()

passwordLabel.pack()
passwordEntry.pack()

regButton.pack()
logButton.pack()


