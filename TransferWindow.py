from tkinter import *


transferWindow = Tk()
transferWindow.withdraw()
transferWindow.resizable(width=False, height=False)
transferWindow.geometry('300x300')
transferWindow.title('Transfer')
transferWindow['bg'] = '#ccc'

login2Label = Label(transferWindow, text=f'Name:', font='Comfortaa 20', fg='#3d3d42', bg='#ccc')

login2Entry = Entry(transferWindow, font='Consolas 15',
                  fg='#eff5c9',
                  bg='#48494f',
                  relief='solid',
                  justify='center')

transferWindowButton = Button(transferWindow, text='Transfer', font='Consolas 13',
                    fg='#eff5c9',
                    bg='#48494f',
                    relief='solid',
                    activeforeground='#eff5c9',
                    activebackground='#6e6f73')
login2Label.pack()
login2Entry.pack()
transferWindowButton.pack()