#!/usr/bin/env python3

"""
Nombre del programa: Mision2.py.py
Autor: Juan Sebastian Daleman Martinez
Curso: Fundamentos de robotica movil
Departamento de Ingeniería Mecánica y Mecatrónica
Universidad Nacional de Colombia - Sede Bogotá
Año: 2024-1S.

Programa para el control de un robot Ev3 usando el sistema ev3dev
para la solución de un laberinto con navegación autonoma con 
navegación basada en comportamiento 
"""

from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank, MediumMotor
from ev3dev2.sound import Sound
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor, ColorSensor
from ev3dev2.wheel import EV3EducationSetTire
import time

#Mensaje inicial para usuario
print("Bienvenido a la mision 2 \ntenemos que pasar el laberinto")
print()
print("**************************************")
print("\t __ __ __ __ __  S \t")
print("\tE   1   __   1   __1 \t")
print("\t 1__ __ __1__ __ __1 \t")
print("")
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
leds = Leds()

#Se declara el modo de uso de los sensores
Ulsonic.mode = "US-DIST-CM"
Color.mode = "COL-REFLECT"

# Definir el tipo de llanta usado
llanta = EV3EducationSetTire()

#Sonido
sound = Sound()

# Varibles
#####################################################

#Distancia en cm
Distance = None
CountsMotor = motor_a.count_per_rot

#Longitud de una celda en mm
Celda = 360

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

#Sonido para el cominenzo de la solución del laberinto
def SoundStartLaber():
    sound.tone([(Do, 350, 100), (Mi, 350, 100), (Sol, 350, 100),
                 (Fa, 350, 100), (Mi, 350, 100), (Sol, 350, 100), (La, 350)])

#Sonido de laberinto completado
def SoundFinishLaber():
    sound.tone([(La, 350, 100), (Si, 350, 100), (Sol, 350, 100),
                 (Mi, 350, 100), (Do, 350, 100), (Mi, 350, 100),
                 (Sol, 350, 100), (Fa, 450, 100), (Re, 450, 100), (Do, 350)])

#Sonido de escaneo de obstaculos
def SoundScanning():
    sound.tone([(Do, 350, 100), (Re, 350, 100), (Mi, 350, 100), (Fa, 350, 100), (Sol, 350)])

#Solución de obstaculo encontrado
def SolveObstacle():
    
    #Sonido de escaneo
    SoundScanning()

    #Obstaculos 
    ObstaculoDerecha = False
    ObstaculoIzquierda = False

    #Verificación de obstaculo a la derecha del robot
    motor_a.run_to_abs_pos(position_sp=90, speed_sp=50, stop_action="hold")
    motor_a.wait_until_not_moving()
    time.sleep(2)
    Distance = Ulsonic.distance_centimeters
    time.sleep(2)
    if Distance < 36:
        ObstaculoDerecha = True

    #Verificación de obstaculo a la izquierda del robot
    motor_a.run_to_abs_pos(position_sp=-90, speed_sp=50, stop_action="hold")
    motor_a.wait_until_not_moving()
    time.sleep(4)
    Distance = Ulsonic.distance_centimeters
    time.sleep(2)
    if Distance < 36:
        ObstaculoIzquierda = True

    #Reposicionamiento del motor para que el sensor vea al frente
    motor_a.run_to_abs_pos(position_sp=0, speed_sp=50, stop_action="hold")
    motor_a.wait_until_not_moving()
    time.sleep(2)

    #Solución caso de obstaculo
    if  ObstaculoDerecha:
        if  ObstaculoIzquierda:
            tank.turn_right(10, 180, True, 1)
            tank.wait_until_not_moving()
            return True

        tank.turn_left(5, 90, True, 2)
        tank.wait_until_not_moving()
        return False

    tank.turn_right(5, 90, True, 1)
    tank.wait_until_not_moving()
    return False

#Función para posicionamiento del robot en la entrada
def GoToEntry():

    #Cambio de luces de inicio
    leds.set_color("LEFT", "GREEN")
    leds.set_color("RIGHT", "GREEN")
    
    #Sonido de inicio
    SoundStart()

    #Bucle de busqueda de entrada
    while True:
        tank.on(30,30)

        if Color.reflected_light_intensity <= 10:
            tank.off(brake = True)
            break

def SolveLabyrinth():

    #Espera para que el usuario de inicio a la solución del robot
    input("Oprima enter para comenzar a solucionar el laberinto")

    #Distancia inicial
    Distance = Ulsonic.distance_centimeters
    
    #Luces de resolviendo el laberinto
    leds.set_color("LEFT", "ORANGE")
    leds.set_color("RIGHT", "ORANGE")

    # Calcular la cantidad de grados necesarios para recorrer la distancia por celda y evitar chocar con la pared incial
    Grados = ((Celda-100) / llanta.circumference_mm) * 360
    Grados2 = ((Celda) / llanta.circumference_mm) * 360

    #Sonido de inicio
    SoundStartLaber()

    #Mover a la primera celda
    tank.on_for_degrees(speed, speed, Grados)
    tank.wait_until_not_moving()
    Distance = Ulsonic.distance_centimeters
    time.sleep(2)

    while True:

        while True:
            
            #Medición de distancia al obstaculo
            Distance = Ulsonic.distance_centimeters

            #Verificación de aproximación al obstaculo
            if Distance <= 7:
                tank.off(brake = True)
                #print("Paraded detectada")
                break

            #Verificación de llegada a la meta
            if Color.reflected_light_intensity <= 10:
                tank.off(brake = True)
                print("Llegue a la meta")
                leds.set_color("LEFT", "GREEN")
                leds.set_color("RIGHT", "GREEN")
                break

            tank.on(speed, speed)


        if Color.reflected_light_intensity <= 10:
            tank.on_for_degrees(speed, speed, Grados2)
            tank.wait_until_not_moving()
            SoundFinishLaber()
            leds.animate_police_lights('YELLOW', 'GREEN', sleeptime=0.75, duration=10)
            leds.set_color("LEFT", "GREEN")
            leds.set_color("RIGHT", "GREEN")
            break

        Regreso = SolveObstacle()

        if Regreso:

            tank.on_for_degrees(speed, speed, Grados2)
            tank.wait_until_not_moving()

            Regreso = SolveObstacle()

        Distance = Ulsonic.distance_centimeters



def main():

    GoToEntry()

    SolveLabyrinth()
    


if __name__ == "__main__":
    main()
