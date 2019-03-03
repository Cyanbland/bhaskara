import math
import tkinter as tk
# class App():
#     #Janela Principal
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Bhaskara Solver")
#         self.root.geometry("600x300")
#         self.root.resizable(0, 0)
#         self.root.configure(background="#DCDCDC")
#         self.root.bind('Escape', self.esc_pressed)
#         #Cria sequência de columns e rows
#         rows = 0
#         while rows < 10:
#             self.root.rowconfigure(rows, weight=1)
#             self.root.columnconfigure(rows, weight=1)
#             rows += 1
#
#         #Botão(função = abrir nova janela)
#         value_insertion = tk.Button(self.root, text="Insira os valores", command=TopLevelWindow)
#         value_insertion.grid(row=0, column=1)
#         value_insertion.config(height=3, width=15, font=15)
#         value_insertion.grid(row=1, column=1)
#
#         #Canvas da tela principal
#         text_output = tk.Canvas(self.root, width=200, height=175)
#         text_output.configure(bg="#C0C0C0")
#         text_output.grid(row=1, column=3)
#         #Mainloop
#         self.root.mainloop()
#
#     #Shortcuts
#     def esc_pressed(self, event):
#         print("esc_pressed")
#         self.root.destroy()
#
#     def appexit(self):
#         print("appexit")
#         self.root.destroy()
#
#
# class TopLevelWindow():
#     def __init__(self,master):
#         self.master = master
#         self.master.geometry("400x400")
#         self.master.title("Valores")
#


def main():
    a = int(input("Valor de a:"))
    b = int(input("Valor de b:"))
    c = int(input("Valor de c:"))
    yes_list = ["sim", "s", "yes", "y"]

    delta = (b**2) - 4*a*c

    if delta >= 0:
        delta_root = math.sqrt(delta)
        bhask_pos = ((-b + delta_root)/2*a)
        bhask_neg = ((-b - delta_root)/2*a)

        print("A equação",a,"x² +",b,"x +",c,"tem como raiz positiva: ", bhask_pos," e como raiz negativa:", bhask_neg)

    else:
        escolha = str(input("não foi possível realizar o cálculo pois o delta não é positivo. Deseja recomeçar?:")).lower()
        if escolha in yes_list:
            main()
        else:
            exit()

main()

# App()
