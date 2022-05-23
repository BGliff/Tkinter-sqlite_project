from tkinter import *


changeInfoWindow = Tk()
changeInfoWindow.withdraw()
changeInfoWindow.resizable(width=False, height=False)
changeInfoWindow.geometry('300x300')
changeInfoWindow.title('Your Info')
changeInfoWindow['bg'] = '#ccc'

changeNameLabel = Label(changeInfoWindow, text=f'Name:', font='Comfortaa 20', fg='#3d3d42', bg='#ccc')
changeSurnameLabel = Label(changeInfoWindow, text=f'Surname:', font='Comfortaa 20', fg='#3d3d42', bg='#ccc')
ageLabel = Label(changeInfoWindow, text=f'Age:', font='Comfortaa 20', fg='#3d3d42', bg='#ccc')

nameEntry = Entry(changeInfoWindow, font='Consolas 15',
                  fg='#eff5c9',
                  bg='#48494f',
                  relief='solid',
                  justify='center')

surnameEntry = Entry(changeInfoWindow, font='Consolas 15',
                     fg='#eff5c9',
                     bg='#48494f',
                     relief='solid',
                     justify='center')

ageEntry = Entry(changeInfoWindow, font='Consolas 15',
                 fg='#eff5c9',
                 bg='#48494f',
                 relief='solid',
                 justify='center')

saveButton = Button(changeInfoWindow, text='Save Changes', font='Consolas 13',
                    fg='#eff5c9',
                    bg='#48494f',
                    relief='solid',
                    activeforeground='#eff5c9',
                    activebackground='#6e6f73')
changeNameLabel.pack()
nameEntry.pack()
changeSurnameLabel.pack()
surnameEntry.pack()
ageLabel.pack()
ageEntry.pack()
saveButton.pack()