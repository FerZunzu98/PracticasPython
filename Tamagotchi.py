from random import randint
from time import sleep

class Tamagotchi:
    def __init__(self, nombre):
        #Parametro
        self.nombre = nombre
        #Atributos cuidado
        self.hambre = 0
        self.aburrimiento = 0
        self.cansancio = 0
        self.suciedad= 0
        
        self.comida = 2
        self.dormido = False
        self.vivo = True
        
    def comer(self):
        if(self.comida):
            self.comida -= 1
            self.hambre -= randint(1,4)
            print(f"Tu tamagochi {self.nombre} ha comido")
        else:
            print("No hay comida disponible")
            
        if self.hambre < 0:
            self.hambre = 0
        
    def jugar(self):
        num_random = randint(0,2)
        print(f"{self.nombre} quiere jugar...")
        respuesta= int(input("Elige uno:\n 0: Piedra\n 1: Papel\n 2: Tijeras "))

        valores = {
            0:"Piedra",
            1:"Papel",
            2:"Tijeras"
        }

        print(num_random)
        print(respuesta)

        if num_random == respuesta: 

            print(f"{self.nombre} y tu habeis empatado")
        
        else:

            if (num_random == 0 and respuesta == 1) or (num_random == 1 and respuesta == 2) or (num_random == 2 and respuesta == 0):
                print(f"{self.nombre} ha sacado {valores[num_random]}, has ganado!")
                self.aburrimiento -= 1

            
            else:
    
                print(f"{self.nombre} ha sacado {valores[num_random]}, te ha ganado!")
                self.aburrimiento -= 3
                
        if self.aburrimiento < 0:
            self.aburrimiento = 0

        print("Quieres jugar otra?")
        otra = int(input("1: Si\n0: No\n"))

        if otra:
            self.jugar()

        
    def dormir(self):
        self.dormido = True
        self.cansancio = 0 if self.cansancio - 3 < 0 else self.cansancio - 3  
        self.aburrimiento = 0 if self.aburrimiento - 2 < 0 else self.aburrimiento - 3
        print(f"{self.nombre} esta durmiendo...")
        
    def despertar(self):
        num = randint(0,2) 
        
        if num == 0:
            print(f"{self.nombre} se ha despertado")
            self.dormido = False
            self.aburrimiento = 0
        else:
            print(f"{self.nombre} sigue durmiendo")
            self.dormir()
            
    def ducha(self):
        
        self.suciedad = 0
        print(f"{self.nombre} ha tomado una ducha")
    
    def buscar_comida(self):
        comida_encontrada = randint(0,4)
        self.comida += comida_encontrada
        self.suciedad += 2
        print(f"{self.nombre} ha encontrado {comida_encontrada} comidas!")
        
    def mostrar_valores(self):

        print(f"Nombre: {self.nombre}")
        print(f"Hambre: {self.hambre}")
        print(f"Aburrimiento: {self.aburrimiento}")
        print(f"Cansancio: {self.cansancio}")
        print(f"Comida: {self.comida}")
        print(f"Dormido: {self.dormido}")
        print(f"Suciedad: {self.suciedad}")
        
    def dificultad(self,nivel = 1):
        if(nivel < 1 | nivel > 5):
            print("Nivel no valido, prueva de nuevo")
            return
        
        self.hambre += randint(0,nivel)
        self.suciedad += randint(0,nivel)
        if not(self.dormido):
            self.aburrimiento += randint(0,nivel)
            self.cansancio += randint(0,nivel)
            
    def morir(self):
        if self.hambre >= 10:
            print(f"{self.nombre} murio de hambre")
            self.vivo = False
        
        if self.suciedad >= 10:
            print(f"{self.nombre} murio de una infección")
            self.vivo = False
            
        if self.aburrimiento >= 10:
            print(f"{self.nombre} está muy aburrido y ser durmió")
            self.aburrimiento = 10
            self.dormido = True
        
        if self.cansancio >= 10:
            print(f"{self.nombre} está muy cansado y se durmió")
            self.cansancio = 10
            self.dormido = True
            

def mostrar_menu (tamagotchi):
    if not(tamagotchi.dormido):
        print("""
                Presiona 1: Comer
                Presiona 2: Jugar
                Presiona 3: Dormir
                Presiona 4: Ducha
                Presiona 5: Buscar Comida
                """)
        
        option = input()
        if option.isnumeric():
            option = int(option)
            if not(option in [1,2,3,4,5]):
                return
        else:
            print("Opción no valida")
            return
    
        return option
    else:
        print(f"{tamagotchi.nombre} esta dormido... Presiona 6")
        option = input()
        
        if option != "6": option = "6"
        
        return int(option)
    

def llamar_accion(tamagotchi,option):
    if option == 1:
        tamagotchi.comer()
    elif option == 2:
        tamagotchi.jugar()
    elif option == 3:
        tamagotchi.dormir()
    elif option == 4:
        tamagotchi.ducha()
    elif option == 5:
        tamagotchi.buscar_comida()
    elif option == 6:
        tamagotchi.despertar()
    else:
        print("OPCIÓN NO VALIDA")

def pedir_nivel ():
    
    while True:
        
        nivel = input("Introduce el nivel de dificultad del 1 al 5 : ")
        
        if nivel in ["1","2","3","4","5"]:
            
            print("Nivel establecido en "+nivel)
            return int(nivel)
        
        else:
            print("Entrada no válida, intentalo de nuevo!")
            

def main():

    print("Tamagotchi en Python ")
    print("En este proyecto he programado un tamagotchi basico para el manejor de funciones y clases en python")

    nivel  =  pedir_nivel()

    nombre = input("Introducce el nombre de tu tamagotchi: ")

    mi_tamagotchi = Tamagotchi(nombre)

    mi_tamagotchi.mostrar_valores()

    ronda = 1

    mi_tamagotchi.vivo = True

    while mi_tamagotchi.vivo:
        print("**********************")
        print(f"Esta es la ronda {ronda}")

        mi_tamagotchi.mostrar_valores()

        print("      ****************")
        llamar_accion(mi_tamagotchi, mostrar_menu(mi_tamagotchi))
        print("      *****************")

        print(f"Ronda nº: {ronda}")

        mi_tamagotchi.mostrar_valores()

        sleep(3)

        mi_tamagotchi.dificultad(nivel)

        mi_tamagotchi.morir()

        print("**********************")

        ronda +=1


main()