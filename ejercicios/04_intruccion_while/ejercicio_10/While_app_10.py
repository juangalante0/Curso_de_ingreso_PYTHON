import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre juan
apellido galante
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        suma_negativos = 0
        suma_positivos = 0
        cantidad_positivos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0

        while True:
            numero = prompt(title="EJ 10", prompt="Ingrese un numero")
            if numero == None:
                break
            numero = int(numero)

            if numero < 0:
                suma_negativos += numero
                cantidad_negativos += 1
            elif numero == 0:
                cantidad_ceros += 1
            else:
                suma_positivos += numero
                cantidad_positivos += 1
        
        diferencia = cantidad_positivos - cantidad_negativos

        mensaje = "La suma acumulada de numeros positivos es {0}.\nLa suma acumulada de numeros negativos es {1}. \nLa cantidad de numeros positivos ingresados es {2}. \nLa cantidad de numeros negativos ingresados es {3}. \nLa cantidad de ceros ingresados es {4}. \nLa diferencia entre numeros positivos y negativos es {5}.".format(suma_positivos, suma_negativos, cantidad_positivos, cantidad_negativos, cantidad_ceros, diferencia)

        alert(title="EJ 10", message=mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
