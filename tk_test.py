import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Datalogger")
        self.geometry("400x100")

        self.Display = tk.Frame(self)
        self.Display.pack(expand=0, pady=10)

        self.Control = tk.Frame(self)
        self.Control.pack(expand=0)

        self.label = tk.Label(self.Display, text='', width=20, background="#333333", fg="#00FF00")
        self.label.grid(column=0, row=0)

        self.label_time = tk.Label(self.Display, text='', width=20, background="#333333", fg="#00FF00")
        self.label_time.grid(column=1, row=0)

        self.con_btn = tk.Button(self.Control, text="Connect")
        self.con_btn.grid(column=0, row=0)

        self.dis_btn = tk.Button(self.Control, text="Disconnect")
        self.dis_btn.grid(column=1, row=0)

        self.save = tk.Button(self.Control, text="Save")
        self.save.grid(column=2, row=0)

        self.plot = tk.Button(self.Control, text="Plot")
        self.plot.grid(column=3, row=0)

        self.check = tk.Label(self.Control, text="Disconnected..", width=20)
        self.check.grid(column=0, row=1, columnspan=2)


if __name__ == "__main__":
    app = App()
    app.mainloop()