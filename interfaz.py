from tkinter import *
from  tkinter import ttk
from lexico import *


class Interfaz:
    
    def __init__(self):
        self.ventana = Tk()
        self.ventana.attributes('-fullscreen', True)
        self.ventana.config(bg="#E2B6F0")
        self.createWidgets()
        self.ventana.mainloop()
        self.lexico = None

    def createWidgets(self):
        self.text1 = Text(self.ventana)
        self.tabla = ttk.Treeview(self.ventana)
        self.boton1 = Button(self.ventana, text='Run', command = self.compilar)
        self.boton2 = Button(self.ventana, text='Limpiar', command = self.limpiar)
        self.text1.place(x=10, y=50,height=750,width=500)
        self.tabla.place(x=520, y=50,height=750,width=835)
        self.tabla['columns']= ('token','reservada','identificador','operador','numero','simbolo')
        self.boton1.place(x=10, y=10, width = 80, height= 30)
        self.boton2.place(x=920, y=10, width = 80, height= 30)
        #forta de las columnas
        self.tabla.column("#0", width=0,  stretch=NO)
        self.tabla.column("token",anchor=CENTER, width=50)
        self.tabla.column("reservada",anchor=CENTER, width=80)     
        self.tabla.column("identificador",anchor=CENTER, width=80)    
        self.tabla.column("operador",anchor=CENTER, width=80)       
        self.tabla.column("numero",anchor=CENTER, width=80)
        self.tabla.column("simbolo",anchor=CENTER, width=80)
        #cabeceras de las columnas
        self.tabla.heading("#0",text="",anchor=CENTER)
        self.tabla.heading("token",text="Token",anchor=CENTER)
        self.tabla.heading("reservada",text="Reservada",anchor=CENTER)
        self.tabla.heading("identificador",text="Identificador",anchor=CENTER)
        self.tabla.heading("operador",text="Operador",anchor=CENTER)
        self.tabla.heading("numero",text="Numero",anchor=CENTER)
        self.tabla.heading("simbolo",text="Simbolo",anchor=CENTER)
        
    def compilar(self):
        index = 0
        datosIngresados = self.text1.get(1.0, "end-1c")
        self.lexico = Lexico()
        resultados = self.lexico.test(datosIngresados)
        for valor in resultados:
            if str(valor.get('token')) == "IDENTIFICADOR":
                self.tabla.insert(parent='',index='end',iid=index,text='',
                values=(valor.get('lexema'),"","X","","",""))    
            elif valor.get('token') == "RESERVADA":
                self.tabla.insert(parent='',index='end',iid=index,text='',
                values=(valor.get('lexema'),"X","","","",""))
            elif valor.get('token') == "OPERADOR":
                self.tabla.insert(parent='',index='end',iid=index,text='',
                values=(valor.get('lexema'),"","","X","",""))
            elif valor.get('token') == "NUMERO":
                self.tabla.insert(parent='',index='end',iid=index,text='',
                values=(valor.get('lexema'),"","","","X",""))
            elif valor.get('token') == "SIMBOLO":
                self.tabla.insert(parent='',index='end',iid=index,text='',
                values=(valor.get('lexema'),"","","","","X"))
            
            index = index + 1

    def limpiar(self):
        self.lexico.borrar()
        self.text1.delete("1.0", "end")
        for item in self.tabla.get_children():
            self.tabla.delete(item)

Interfaz()