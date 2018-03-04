#*-*coding:utf-8*-*
#  SCRIPT QUE COMPARA LLAVES
# Script Realizado por Diego Alberto Parra Garzón, Esto es software libre
#con licencia GPL3, Bogotá, Colombia
#_____________________________________________________________________
#Al cargar la clase:
#            CompararUsuario().build()
#carga inmediatamente la base de datos de usuarios.
#______________________________________________________________________
# Para Comparar un usuario con la base de Datos se invoca a la función
#            self.CompararArray(NUID_QUE_SE_QUIERE_COMPARAR)
# Trabaja como un ciclo en un hilo
#______________________________________________________________________
# Para Revisar el estado de comparación se invoca a la función:
#            estadoCom():
# La cual devuelve:
# "1" si esta comparando,
# "2" si se encontro coincidencia en la base de datos,
# "3" si no esta en la base de datos.
# Es un ciclo en un hilo, trabajar con un while o un clock.schedule
#______________________________________________________________________
#Para añadir un usuario se invoca primero la función
#             CompararArray(NUID_QUE_SE_QUIERE_COMPARAR_PARA_AGREGAR)
# y luego se invoca
#            estadoCom():
# Si estadoCom devuelve 3, invocar la función:
#           agregarUsuario(nuid, name, codigoIdentificacion)
# Esta recibe 3 parametros: la nuid"ID de la llave RFID",
# name"Nombre completo del usuario",
# codigoIdentificacion"El código de asignación dado por la empresa.".
#_______________________________________________________________________
#Para quitar un usuario se invoca primero la función
#             CompararArray(NUID_QUE_SE_QUIERE_COMPARAR_PARA_BORRAR)
# y luego se invoca
#            estadoCom():
# Si estadoCom devuelve 2 , invocar la función:
#            quitarUsuario()
#_____________________________________________________________________

from kivy.clock import Clock
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App

class CompararUsuario(RelativeLayout):
        
    def CargarArray(self):
        global array
        array = []

        #        with open("DataBase.text", "r") as f:
        with open("Datos/DataBase.text", "r") as f:
            for line in f:
                array.append(line)
        print array

    def CompararArray(self, valorAcomparar):
        global nuid
        self.item = 2
        nuid = str(valorAcomparar)
        print "Llamando a compara"
        self.estadocomparacion = 1
        self.estadoCom()
        Clock.schedule_interval(self.compara, 0.01)

        
    def compara(self, dt):
        NUID =  array[self.item].split(",")
        print self.item
        print NUID[0]
        Nuid = str(NUID[0])
        if ( Nuid == nuid):
            print "El NUID coincide"
            Clock.unschedule(self.compara)
            self.estadocomparacion = 2
            self.Vitem = self.item - 1
            self.estadoCom()
        
        if ( Nuid != nuid):
            print "El NUID no coincide"
            self.estadocomparacion = 1
            self.estadoCom()
            self.Vitem = self.item    -1                        
            self.item = self.item+1
            
        if (self.item == len(array) ):
            if ( Nuid == nuid):
                print "El NUID coincide"
                Clock.unschedule(self.compara)
                self.estadocomparacion = 2
                self.Vitem = self.item
                self.estadoCom()
                
            if ( Nuid != nuid):
                print "El NUID no coincide"
                Clock.unschedule(self.compara)
                self.estadocomparacion = 3
                self.Vitem =  "nada"
                self.estadoCom()
            
    def estadoCom(self):
        #devuelve 1 si esta comparando
        #devuelve 2 si esta en la base de datos
        #devuelv 3 si no esta en la base de datos
        eC = self.estadocomparacion
        print "Estado de comparacion es: "
        if eC ==1:
            print "Comparando actualmente el item: "  + str(self.item)
        if eC ==2:
            print "Se encontro una coincidencia, script terminado"
        if eC ==3:
            print "No se encontro ninguna coincidencia script terminado"
        return eC

    
    def quitarUsuario(self):
        arrayCambiado = []
        for i in range(0, len(array),1):
            if (i == (int(self.Vitem) +1)):
                pass
            if (i != (int(self.Vitem)+1)) :
                arrayCambiado.append(array[i])
                
        print str(arrayCambiado)
        var = open("Datos/DataBase.text", "w")
        for i in range(0,len(arrayCambiado), 1):
            var.write(str(arrayCambiado[i]))
        var.close()
        
    def agregarUsuario(self, nuid, name, codigoIdentificacion):
        variable = str(nuid)+","+str(name)+","+str(codigoIdentificacion)
#        var = open("DataBase.text", "a")
        var = open("Datos/DataBase.text", "a")
        var.write(variable)
        var.close()    
        self.CargarArray()

    def build(self):
        rl = RelativeLayout()
        print "Cargando la base de datos."
        self.CargarArray()
        print "Base de datos cargada."
#        self.CompararArray("C0C67A53")
#        self.agregarUsuario("101324456","Diego parra Garzón","101010")
        return rl

#class CompararUSER(App):
class CompararUSER(RelativeLayout):    
    def build(self):
        return CompararUsuario().build()
    


#if __name__ == "__main__" :
 #   CompararUSER().run()

