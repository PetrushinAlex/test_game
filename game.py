from tkinter import *
import random as rm


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        pass


if __name__ == '__main__':
    root = Tk()
    root.geometry('1000x1200+200+200')
    root.title('Камень, ножницы, бумага')
    root.resizable(False, False)
    root['bg'] = '#90EE90'
    app = Main(root)
    app.pack()
    root.mainloop()
