from tkinter import *
import random as rm


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        btn = Button(
            root, text='Камень', font=('Arial', 24),
            command=lambda x=1: self.btn_click(x)
        )
        btn2 = Button(
            root, text='Ножницы', font=('Arial', 24),
            command=lambda x=2: self.btn_click(x)
        )
        btn3 = Button(
            root, text='Бумага', font=('Arial', 24),
            command=lambda x=3: self.btn_click(x)
        )

        btn.place(x=250, y=300, width=200, height=80)
        btn2.place(x=500, y=300, width=200, height=80)
        btn3.place(x=750, y=300, width=200, height=80)

        self.lbl = Label(root, text='Начало игры!', bg="#FFF", font=('Arial', 36, 'bold'))
        self.lbl.place(x=440, y=25)

        self.win = self.drow = self.lose = 0

        self.lbl2 = Label(
            root, justify='left', font=('Arial', 16),
            text=f'Побед: {self.win}\nПроигрышей:'
                 f' {self.lose}\nНичей: {self.drow}',
            bg="#FFF"
        )
        self.lbl2.place(x=15, y=15)

    def btn_click(self, choise):
        comp_choise = rm.randint(1, 3)

        if choise == comp_choise:
            self.drow += 1
            self.lbl.configure(text="Ничья")
        elif choise == 1 and comp_choise == 2 \
                or choise == 2 and comp_choise == 3 \
                or choise == 3 and comp_choise == 1:
            self.win += 1
            self.lbl.configure(text="Победа")
        else:
            self.lose += 1
            self.lbl.configure(text="Проигрыш")

        self.lbl2.configure(
            text=f"Побед: {self.win}\nПроигрышей:"
                 f" {self.lose}\nНичей: {self.drow}"
        )

        del comp_choise


if __name__ == '__main__':
    root = Tk()
    root.geometry('1200x800+200+200')
    root.title('Камень, ножницы, бумага')
    root.resizable(False, False)
    root['bg'] = '#90EE90'
    app = Main(root)
    app.pack()
    root.mainloop()
