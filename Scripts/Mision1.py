"""
Nombre del programa: Mision1.py
Autor: Juan Sebastian Daleman Martinez
Curso: Fundamentos de robotica movil
Departamento de Ingeniería Mecánica y Mecatrónica
Universidad Nacional de Colombia - Sede Bogotá
Año: 2024-1S.

Programa para el control de un robot Ev3 usando el sistema ev3dev
para la solución de una ruta con obstaculos con 
navegación basada en comportamiento 
"""

from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank, MediumMotor
from ev3dev2.sound import Sound
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor, ColorSensor, InfraredSensor
from ev3dev2.wheel import EV3EducationSetTire
import time


print("Bienvenido a la mision 1 \ntenemos que superar los obstaculos\n")
print()
print("**************************************")
print(" P2                                   ")
print("  \                                   ")
print("   \                                  ")
print("    \                                 ")
print("     \                                ")
print("      \                               ")
print("       \                              ")
print("        \                             ")
print("    _____\_______                     ")
print("   1            1                     ")
print("   1            1                     ")
print("   1     1______1                     ")
print("   1     1  \                         ")
print("   1     1   \                        ")
print("   1_____1    \                       ")
print("               \                      ")
print("                \                     ")
print("     ____________\____________        ")
print("     1                       1        ")
print("     1                       1        ")
print("     1_______________________1        ")
print("                     \                ")
print("                      \               ")
print("                       \              ")
print("                        \             ")
print("                         \            ")
print("                          \           ")
print("                          P1           ")
print("**************************************")
print()

#Se inicializan los motores y los sensores
motor_a = MediumMotor('outA')
motor_a.stop_action = "hold"
tank = MoveTank(OUTPUT_B, OUTPUT_C)
tank.gyro = GyroSensor()
gyro = GyroSensor()
Ulsonic = UltrasonicSensor()
Ulsonic.MODE_US_SI_CM
Color = ColorSensor()
Color.MODE_COL_REFLECT
InfRed = InfraredSensor()
InfRed.MODE_IR_PROX
leds = Leds()

#Se declara el modo de uso de los sensores
Ulsonic.mode = "US-DIST-CM"
Color.mode = "COL-REFLECT"
InfRed.mode = "IR-PROX"

# Definir el tipo de llanta usado
llanta = EV3EducationSetTire()

#Sonido
sound = Sound()

# Varibles
#####################################################

#Distancia en cm
CountsMotor = motor_a.count_per_rot

#Velocidad normal de los motores
speed = 30

#Notas
Do = 523.25
Re = 587.33
Mi = 659.26
Fa = 698.46
Sol = 783.99
La = 880
Si = 987.76

####################################################


#Cambio de luces de preparación
leds.set_color("LEFT", "AMBER")
leds.set_color("RIGHT", "AMBER")

# Calibrar el giroscopio
tank.gyro.calibrate()
print("Calibrando giro sensor... ")

# Esperar a que el giroscopio se calibre completamente
while tank.gyro.calibrate():
    time.sleep(0.1)
print("El giro sensor esta calibrado")

#Verificación y posicionamiento del motor_a adecuado
motor_a.run_to_abs_pos(position_sp=0, speed_sp=50, stop_action="hold")
motor_a.wait_until_not_moving()
time.sleep(2)


# Sonido para comienzo del movimiento
def SoundStart():
    sound.tone([(Do, 350, 100), (Mi, 350, 100), (Sol, 350)])

#Sonido para el cominenzo de la solución del contorno
def SoundStartContours():
    sound.tone([(Do, 350, 100), (Mi, 350, 100), (Sol, 350, 100),
                 (Fa, 350, 100), (Mi, 350, 100), (Sol, 350, 100), (La, 350)])

#Sonido de ruta completada
def SoundFinisRute():
    sound.tone([(La, 350, 100), (Si, 350, 100), (Sol, 350, 100),
                 (Mi, 350, 100), (Do, 350, 100), (Mi, 350, 100),
                 (Sol, 350, 100), (Fa, 450, 100), (Re, 450, 100), (Do, 350)])

#Sonido de contorno finalizado
def SoundFinishContours():
    sound.tone([(Do, 350, 100), (Re, 350, 100), (Mi, 350, 100), (Fa, 350, 100), (Sol, 350)])


#Función de busqueda de linea
def SearchLine():

    #Ciclo de busqueda
    while True:

        #Giro a la izquierda con velocidad de 10% y objetivo de 5 grados 
        tank.turn_left(10, 5)

        #Verificación de linea alcanzada y parada
        if Color.reflected_light_intensity <= 10:
            tank.off(brake = True)
            break

#Funcion de seguidor de linea
def LineFollower():
    
    #Ciclo de funcionamiento 
    while True:

        #Medición de distancia al obstaculo
        Distance = Ulsonic.distance_centimeters

        #Verificación de aproximación al obstaculo
        if Distance <= 7:
            tank.off(brake = True)
            return True, True

        #Algoritmo de seguimiento bang bang
        if Color.reflected_light_intensity <= 16:
            tank.on(5, 20)
        else:
            if Color.reflected_light_intensity < 55:
                tank.on(20, 5)
        
        #Busqueda de obejtivo final
        if Distance >= 126 and Distance <= 130:
            tank.off(brake = True)
            return False, False 
        
            

def SolveObstacle():

    #Sonido de resolucion de obstaculo
    SoundStartContours()

    #Giro con corrección a la izquierda para contorno
    tank.turn_left(5, (90+gyro.angle), True, 1)
    tank.wait_until_not_moving()
    time.sleep(0.5)

    #Ciclo de seguimiento contorno del obstaculo
    while True:

        #Medición de distancia al obstaculo
        Distance = Ulsonic.distance_centimeters

        #Verificación de aproximación al obstaculo y correcion de orientacion 
        if Distance <= 5:
            tank.off(brake = True)
            tank.wait_until_not_moving()
            move(10, False)
            time.sleep(0.5)
            tank.turn_left(5, 90, True, 2)
            tank.wait_until_not_moving()
        
        #Control bang bang para mantener distacia del obstaculo
        if InfRed.proximity <= 19:
            tank.on(5, 10)

        elif InfRed.proximity < 27:
            tank.on(10, 5)

        #Verificacion llegada a la linea y correcion de orientacion para seguir la linea
        if Color.reflected_light_intensity <= 10:
            tank.off(brake = True)
            move(50, False)
            tank.turn_left(5, 90, True, 2)
            tank.wait_until_not_moving()
            time.sleep(0.5)
            SearchLine()
            time.sleep(0.5)
            return False
        
#Funcion para movimiento dando una determinada distancia y se se decia una disancia de seguridad
def move(Distance, safe = True, DisSafe = 100):
    
    # Calcular la cantidad de grados necesarios para recorrer la distancia indicada con un margen de seguridad o no
    DistanceSafe = 0
    if safe:
        DistanceSafe = DisSafe
    Grados = ((Distance-DistanceSafe) / llanta.circumference_mm) * 360

    #Mover distancia definida
    tank.on_for_degrees(speed, speed, Grados)
    tank.wait_until_not_moving()
    time.sleep(2)


def main():

    try:
        #Espera para que el usuario de inicio a la solución del robot
        input("Oprima enter para comenzar a solucionar la ruta")
        
        #Busqueda de la linea inicial
        SearchLine()

        #Luces de modo solución 
        leds.set_color("LEFT", "ORANGE")
        leds.set_color("RIGHT", "ORANGE")
    
        #Sonido de inicio
        SoundStart()

        Solucionando = True
        #Ciclo de solucion de ruta
        while Solucionando:

            #Condicion de terminacion de solucion y de obstaculo encontrado
            Obstaculo, Solucionando = LineFollower()

            if Obstaculo:
               
               #Solucion con algoritmo Bug
               Obstaculo = SolveObstacle()

               #Verificacion terminacion algoritmo 
               if not Obstaculo:
                SoundFinishContours()

        #Cambio de luces de llegada a meta
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")

        #Parada de motores
        tank.off(brake = True)
        print("Fin de la ruta")

        #Sonido de finalizacion
        SoundFinisRute()

        #Luces de celebracion
        leds.animate_police_lights('AMBER', 'GREEN', sleeptime=0.75, duration=10)
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")

    #Intrrupcion de teclado dada por el usuario
    except KeyboardInterrupt:
        print("\nMision abortada") 
        tank.off(brake = True)  


if __name__ == "__main__":
    main()
