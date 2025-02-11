from tkinter import *
import random as rm


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        btn = Button(
            root, text="Камень", font=("Times New Roman", 20),
            command=lambda x=1: self.btn_click(x)
        )
        btn2 = Button(
            root, text="Ножницы", font=("Times New Roman", 20),
            command=lambda x=2: self.btn_click(x)
        )
        btn3 = Button(
            root, text="Бумага", font=("Times New Roman", 20),
            command=lambda x=3: self.btn_click(x)
        )

        btn.place(x=40, y=100, width=120, height=50)
        btn2.place(x=240, y=100, width=120, height=50)
        btn3.place(x=480, y=100, width=120, height=50)

        self.lbl = Label(root, text="Начало игры!", bg="#FFF", font=("Times New Roman", 21, "bold"))
        self.lbl.place(x=150, y=25)

        self.win = self.drow = self.lose = 0

        self.lbl2 = Label(
            root, justify="left", font=("Times New Roman", 13),
            text=f"Побед: {self.win}\nПроигрышей:"
                 f" {self.lose}\nНичей: {self.drow}",
            bg="#FFF"
        )
        self.lbl2.place(x=5, y=5)

    def btn_click(self, choise):
        pass


if __name__ == '__main__':
    root = Tk()
    root.geometry('1200x1400+200+200')
    root.title('Камень, ножницы, бумага')
    root.resizable(False, False)
    root['bg'] = '#90EE90'
    app = Main(root)
    app.pack()
    root.mainloop()
