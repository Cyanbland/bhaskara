import tkinter as tk
from tkinter import ttk, END
import math
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
matplotlib.use("TkAgg")
import numpy as np

LARGE_FONT =("Verdana", 12)
DEFAULT_FONT =("Verdana", 10)
voltou = False


def calculate():
    global valor_1
    global valor_2
    global valor_3
    value_list = [valor_1, valor_2, valor_3]
    if "" in value_list:
        return False
    else:
        delta = (int(valor_2)**2) - 4*int(valor_1)*int(valor_3)
        if delta >= 0:
            global delta_root
            delta_root = math.sqrt(delta)
            global bhask_pos
            global bhask_neg
            bhask_pos = (int(-valor_2) + (delta_root))/2*int(valor_1)
            bhask_neg = (int(-valor_2) - (delta_root))/2*int(valor_1)

        else:
            pass

        return True

def render_graph():
        eixo_x = []
        eixo_y = []
        zero = []
        print(voltou)
        global bhask_pos
        global bhask_neg

        bhask_neg = ""
        bhask_pos = ""
        if voltou is True:
            variacao = abs(bhask_pos - bhask_neg)
            if variacao < 3:
                variacao = 3
            print(variacao)

            for x in np.arange(bhask_pos - variacao, bhask_neg + variacao, variacao / 100):
                y = valor_1 * (x ** 2 ) + valor_2 * (x) + valor_3
                eixo_x.append(x)
                eixo_y.append(y)
                zero.append(0.0)
            plt.plot(eixo_x,eixo_y,color="blue")
            plt.plot(eixo_x,zero,color="black")
            plt.draw()
            print("foi")

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args, **kwargs)
        #self.geometry("720x360")
        self.title("Bhaskara Solver")

        self.valor_1 = ""
        self.valor_2 = ""
        self.valor_3 = ""
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global result
        button = ttk.Button(self, text="Inserir valores", command=lambda: controller.show_frame(PageOne))
        button.pack(side="top", padx=10, pady=20, expand=False)
        # canvas = tk.Canvas(self, width=400, height=200, bg="#C0C0C0", bd="10")
        # canvas.pack(side="bottom", padx=10, pady=20, expand=False)
        global label
        label = tk.Label(self, text="Valores ainda não definidos", bg="#D3D3D3", bd=10, width=80)
        label.pack(side="bottom")
        calculation_button = ttk.Button(self, text="Calcular raízes", command=calculate)
        calculation_button.pack()
        creditos = tk.Label(self, text="Bhaskara Solver by Paulo Jr  09/02/2019")
        creditos.pack(padx=10, pady=20, side="right")
        graph_button = ttk.Button(self, text="Ver gráfico", command=lambda: controller.show_frame(Graph))
        graph_button.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def get_entry_data_a():
            global valor_1
            valor_1 = int(controller.valor_a.get())
            entry_a.delete(0, END)
            print(valor_1)

        def get_entry_data_b():
            global valor_2
            valor_2 = int(controller.valor_b.get())
            entry_b.delete(0, END)
            print(valor_2)

        def get_entry_data_c():
            global valor_3
            valor_3 = int(controller.valor_c.get())
            entry_c.delete(0, END)
            print(valor_3)

        def event_data_a(event):
            global valor_1
            valor_1 = int(controller.valor_a.get())
            entry_a.delete(0, END)
            print(valor_1)

        def event_data_b(event):
            global valor_2
            valor_2 = int(controller.valor_b.get())
            entry_b.delete(0, END)
            print(valor_2)

        def event_data_c(event):
            global valor_3
            valor_3 = int(controller.valor_c.get())
            entry_c.delete(0, END)
            print(valor_3)

        text_a = tk.Label(self, text="Valor de a:", padx=10, pady=10)
        text_a.grid(row=1, column=1)
        text_b = tk.Label(self, text="Valor de b:", padx=10, pady=10)
        text_b.grid(row=2, column=1)
        text_c = tk.Label(self, text="Valor de c", padx=10, pady=10)
        text_c.grid(row=3, column=1)

        controller.valor_a = tk.IntVar()
        entry_a = tk.Entry(self, textvariable=controller.valor_a)
        entry_a.grid(row=1, column=2)
        entry_a.delete(0, END)
        button_a = ttk.Button(self, text="Salvar valor", command=get_entry_data_a)
        button_a.grid(row=1, column=3, padx=10, pady=10)

        controller.valor_b = tk.IntVar()
        entry_b = tk.Entry(self, textvariable=controller.valor_b)
        entry_b.grid(row=2, column=2)
        entry_b.delete(0, END)
        button_b = ttk.Button(self, text="Salvar valor", command=get_entry_data_b)
        button_b.grid(row=2, column=3, padx=10, pady=10)

        controller.valor_c = tk.IntVar()
        entry_c = tk.Entry(self, textvariable=controller.valor_c)
        entry_c.grid(row=3, column=2)
        entry_c.delete(0, END)
        button_c = ttk.Button(self, text="Salvar valor", command=get_entry_data_c)
        button_c.grid(row=3, column=3,padx=10, pady=10)

        def backbutton_callback():
            global voltou
            voltou = True
            controller.show_frame(StartPage)
            print(voltou)
            if voltou is True:
                if calculate() is False:
                    result = tk.StringVar()
                    sentence = "Não foi possível calcular as raízes pois o delta é negativo."
                    result.set(str(sentence))
                    print(result.get())
                    print("erro")
                elif calculate() is True:
                    global bhask_neg
                    global bhask_pos

                    result = tk.StringVar()
                    sentence = "A equação {0}x² + {1}x + {2} tem como resultado as raízes {3} e {4}.".format(valor_1, valor_2, valor_3, bhask_neg, bhask_pos)
                    result.set(str(sentence))
                    label.config(text=result.get())
                    print(result.get())

                    print("certo")
                else:
                    pass
            return True
        entry_a.bind("<Return>", event_data_a)
        entry_b.bind("<Return>", event_data_b)
        entry_c.bind("<Return>", event_data_c)
        back_button = ttk.Button(self, text="Retornar à página principal", command=backbutton_callback)
        back_button.grid(row=5, column=2, padx=20, pady=20)


class Graph(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Teste")
        if voltou is True:
            render_graph()



print(voltou)

app = App()
app.mainloop()

