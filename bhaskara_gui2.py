import tkinter as tk
from tkinter import ttk, END


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #return_button = tk.Button(self, text="Salvar valores", command = )
        # label = tk.Label(self, text="Após inserir os valores, aperte Enter ou clique no botão abaixo.", font="LARGE_FONT", padx=10, pady=10)
        # label.grid(row=4, column=1)

        # root = Tk()
        # frame.bind("<Escape>", lambda: controller.show_frame(StartPage))
        def get_entry_data_a():
            global valor_1
            valor_1 = int(valor_a.get())
            entry_a.delete(0, END)
            print(valor_1)

        def get_entry_data_b():
            global valor_2
            valor_2 = int(valor_b.get())
            entry_b.delete(0, END)
            print(valor_2)

        def get_entry_data_c():
            global valor_3
            valor_3 = int(valor_c.get())
            entry_c.delete(0, END)
            print(valor_3)

        def event_data_a(event):
            valor_1 = int(valor_a.get())
            entry_a.delete(0, END)
            print(valor_1)

        def event_data_b(event):
            valor_2 = int(valor_b.get())
            entry_b.delete(0, END)
            print(valor_2)

        def event_data_c(event):
            valor_3 = int(valor_c.get())
            entry_c.delete(0, END)
            print(valor_3)

        text_a = tk.Label(self, text="Valor de a:", padx=10, pady=10)
        text_a.grid(row=1, column=1)
        text_b = tk.Label(self, text="Valor de b:", padx=10, pady=10)
        text_b.grid(row=2, column=1)
        text_c = tk.Label(self, text="Valor de c", padx=10, pady=10)
        text_c.grid(row=3, column=1)

        valor_a = tk.IntVar()
        entry_a = tk.Entry(self, textvariable=valor_a)
        entry_a.grid(row=1, column=2)
        entry_a.delete(0, END)
        button_a = ttk.Button(self, text="Salvar valor", command=get_entry_data_a)
        button_a.grid(row=1, column=3, padx=10, pady=10)

        valor_b = tk.IntVar()
        entry_b = tk.Entry(self, textvariable=valor_b)
        entry_b.grid(row=2, column=2)
        entry_b.delete(0, END)
        button_b = ttk.Button(self, text="Salvar valor", command=get_entry_data_b)
        button_b.grid(row=2, column=3, padx=10, pady=10)

        valor_c = tk.IntVar()
        entry_c = tk.Entry(self, textvariable=valor_c)
        entry_c.grid(row=3, column=2)
        entry_c.delete(0, END)
        button_c = ttk.Button(self, text="Salvar valor", command=get_entry_data_c)
        button_c.grid(row=3, column=3,padx=10, pady=10)

        entry_a.bind("<Return>", event_data_a)
        entry_b.bind("<Return>", event_data_b)
        entry_c.bind("<Return>", event_data_c)

        # back_button = ttk.Button(self, text="Retornar à página principal", command=lambda:controller.show_frame(StartPage))
        # back_button.grid(row=5, column=2, padx=20, pady=20)
