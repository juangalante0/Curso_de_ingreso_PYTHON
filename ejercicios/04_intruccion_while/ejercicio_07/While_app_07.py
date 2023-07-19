import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt). 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        acumulador = 0
        cantidad = 0

        while True:
            numero = prompt(title="EJ 07", prompt="Ingrese un numero")
            if numero == None:
                break
            numero = int(numero)
            cantidad += 1
            acumulador += numero

        
        promedio = acumulador / cantidad
        
        self.txt_promedio.delete(0, 100)
        self.txt_promedio.insert(0, promedio)
        self.txt_suma_acumulada.delete(0, 100)
        self.txt_suma_acumulada.insert(0, acumulador)

            

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
