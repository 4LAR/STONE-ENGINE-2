from tkinter import *
from tkinter import scrolledtext



class console_window():
    def __init__(self):
        self.window = Tk()
        self.window.title("Terminal")
        self.window.geometry('640x380')
        self.window.resizable(False, False)

        # список
        self.terminal_text = scrolledtext.ScrolledText(self.window, width=75, height=20, state='disabled')
        self.terminal_text.grid(column=0, row=0, padx=10, pady=10, columnspan=4)

        # поле для ввода команды
        self.terminal_input = Entry(self.window, width=80)
        self.terminal_input.grid(column=0, row=1, padx=10, pady=0, columnspan=3, sticky="SW")
        self.terminal_input.focus()

        # кнопка отправки комманды
        self.send_button = Button(self.window, text="send", width=15, pady=-1, command=self.send)
        self.send_button.grid(column=3, row=1, padx=10)

    def send(self):
        pass

    # Функция для открытия терминала
    def show(self):
        self.window.mainloop()

    # функция для какрытия терминала
    def destroy(self):
        self.window.quit()

console_window = console_window()
console_window.show()
