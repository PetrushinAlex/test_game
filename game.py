from tkinter import *
import random as rm


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        btn = Button(root, text="Камень", font=("Times New Roman", 15))
        btn = Button(root, text="Ножницы", font=("Times New Roman", 15))
        btn3 = Button(root, text="Бумага", font=("Times New Roman", 15))
        
        btn.place(x=10, y=100, width=120, height=50)
        btn2.place(x=155, y=100, width=120, height=50)
        btn3.place(x=300, y=100, width=120, height=50)


if __name__ == '__main__':
    root = Tk()
    root.geometry('1000x1200+200+200')
    root.title('Камень, ножницы, бумага')
    root.resizable(False, False)
    root['bg'] = '#90EE90'
    app = Main(root)
    app.pack()
    root.mainloop()
