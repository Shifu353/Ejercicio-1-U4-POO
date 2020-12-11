import sys

PYTHON_VERSION = sys.version_info.major

if (PYTHON_VERSION < 3):
    try:
        import Tkinter as tk
    except ImportError:
        raise ImportError ("Se requiere el modulo Tkinter version 3.X")
else:
    try:
        import tkinter as tk
        import getpass
        #from tkinter import *
        from tkinter import ttk,font

        class IMC (tk.Tk):
            __ventana = None
            __mensaje = None
            __estado = None
            __peso = None
            __altura = None

            def __init__ (self):
                self.__ventana = tk.Tk()
                texto = "Bienvenido/a %s a mi ejercicio 1\t" %getpass.getuser()
                #tk.Label(self.__ventana,text=texto,anchor="center").pack()
                self.__ventana.geometry("576x353")
                self.__ventana.title(texto)
                self.__ventana.resizable(False,False)

                self.__peso = tk.IntVar()
                self.__altura = tk.IntVar()
                self.__mensaje = tk.StringVar()
                self.__estado = tk.StringVar()
                
                self.cabecera = ttk.Frame(self.__ventana,relief="raised",padding=(20,10))
                self.labelcabecera = ttk.Label(self.cabecera,text="Calculadora de IMC",font="Arial 18",padding=(20,5))
                self.cuerpo = ttk.Frame(self.__ventana,padding=(10,5))
                self.separador = ttk.Separator(self.cuerpo,orient=tk.HORIZONTAL)
                
                self.Altura = ttk.Label(self.cuerpo,text="Altura: ",font="Arial 15",padding=(0,15))
                self.entryAltura = ttk.Entry(self.cuerpo,textvariable=self.__altura,font="Arial 12",width=30)
                self.cm= ttk.Label(self.cuerpo,text="cm",font="Arial 12",background="#AFB0AF",anchor=tk.CENTER,padding=5)

                self.Peso = ttk.Label(self.cuerpo,text="Peso: ",font="Arial 15")
                self.entrypeso = ttk.Entry(self.cuerpo,textvariable=self.__peso,font="Arial 12",width=30)
                self.km = ttk.Label(self.cuerpo,text="KG",font="Arial 12",background="#AFB0AF",anchor=tk.CENTER)

                self.cabecera.pack()
                self.labelcabecera.grid(row=0,column=0,columnspan=3,sticky="we")
                self.separador.grid(row=1,column=0,columnspan=4,sticky="we")
                self.cuerpo.pack()
                self.Altura.grid(row=3,column=1,sticky="nw")
                self.entryAltura.grid(row=3,column=2)
                self.cm.grid(row=3,column=3)

                self.Peso.grid(row=6,column=1,sticky="nw")
                self.entrypeso.grid(row=6,column=2)
                self.km.grid(row=6,column=3)
                self.separador2 = ttk.Separator(self.cuerpo,orient=tk.HORIZONTAL)
                self.separador2.grid(row=7,column=0)

                self.Boton = tk.Button(self.cuerpo,text="Calcular",activebackground="green",command=self.Calcular)
                self.Boton.grid(row=9,column=2,sticky="w")
                self.Boton2 = tk.Button(self.cuerpo,text="Limpiar",activebackground="green",command=self.Limpiar)
                self.Boton2.grid(row=9,column=2,sticky="e")

                self.resultado = ttk.Frame(self.__ventana)
                self.resultado.pack(padx=30,pady=20)
                self.res = ttk.Label(self.resultado,text="Tu indice de masa corporal es: ",font="Arial 15",background="#9CE59C",foreground="#027602")
                self.res.grid(row=0,column=0,sticky="nw")
                self.res2 = ttk.Label(self.resultado,textvariable=self.__mensaje,font="Helvetica 16 bold",background="#9CE59C",foreground="#027602")
                self.res2.grid(row=0,column=1,sticky="nw")
                self.estado = ttk.Label(self.resultado,textvariable=self.__estado,font="Arial 14",foreground="#027602",background="#9CE59C",anchor=tk.CENTER)
                self.estado.grid(row=1,column=0,sticky="nswe")
                self.__ventana.mainloop()

            def Calcular(self):
                self.alturaM = float(self.__altura.get())/100
                self.alturaM =  self.alturaM**2
                if(self.alturaM==0):
                    self.alturaM = 1
                self.__total=float(self.__peso.get())/self.alturaM
                self.__mensaje.set("{:.2f}".format(self.__total))

                if(self.__total<18.5):
                    self.res2.configure(foreground='black', background='blue')
                    self.__estado.set("Peso inferior al normal")

                if(self.__total>=18.5 and self.__total<=24.9):
                    self.res2.configure(foreground='black', background='green')
                    self.__estado.set("Peso normal")

                if(self.__total>=25 and self.__total<=29.9):
                    self.res2.configure(foreground='black', background='orange')
                    self.__estado.set("Peso superior al normal")

                if(self.__total>30):
                    self.res2.configure(foreground='black', background='red')
                    self.__estado.set("Obesidad")
                
            def Limpiar (self):
                self.__estado.set("")
                self.__mensaje.set("")
                self.__altura.set("")
                self.__peso.set("")
                self.res2.configure(foreground='#9CE59C', background='#9CE59C')

        if __name__ == "__main__":
            app = IMC()
    except ImportError:
        raise ImportError ("Se requiere el modulo tkinter")
