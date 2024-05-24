# Robotica-movil-Lab3
Juan Sebastian Daleman

Juan David Chica Garcia

Luis Alejandro Duran Espitia

Santiago Olaya Castaño

Tabla de Contenidos
---
- [Objetivos](#objetivos)
- [Consulta bibliografica](#consulta-bibliografica)
  - [Navegación planeada](#navegación-planeada)
  - [Navegación basada en comportamientos](#navegación-basada-en-comportamientos)
  - [Investigaciones y desarrollode robots por Rodney Brooks y Mark Tilden](#investigaciones-y-desarrollode-robots-por-rodney-brooks-y-mark-tilden)
  - [Algoritmos de planeación de rutas para espación con obstáculos](#algoritmos-de-planeación-de-rutas-para-espación-con-obstáculos)
  - [Algoritmos BUG](#algoritmos-bug)
  - [Algoritmo de solución de un laberinto (maze algorithm)](#algoritmo-de-solución-de-un-laberinto-maze-algorithm)
- [Misiones de funcionamiento](#misiones-de-funcionamiento)
- [Misión 1](#misión-1)
  - [Resultados](#resultados)
  - [Solución presentada](#solución-presentada)
  - [Algoritmo usado](#algoritmo-usado)
  - [Video](#video)
- [Misión 2](#misión-2)
  - [Resultados](#resultados-1)
  - [Solución presentada](#solución-presentada-1)
  - [Algoritmo usado](#algoritmo-usado-1)
  - [Video](#video-1)
- [Conclusiones](#conclusiones)

## Objetivos
- Identificar las características de los tipos de navegación.
- Identificar los algoritmos BUG y de soluci´on del laberinto.
- Aplicar al menos dos algoritmos por comportamientos.

## Consulta bibliografica

### Navegación planeada

### Navegación basada en comportamientos

### Investigaciones y desarrollode robots por Rodney Brooks y Mark Tilden

### Algoritmos de planeación de rutas para espación con obstáculos

### Algoritmos BUG

- **Bug 0**
- **Bug 1**
- **Bug 3**

### Algoritmo de solución de un laberinto (maze algorithm)

## Misiones de funcionamiento
Se deben resolver con navegación basada en comportamientos

### Misión 1
**Objetivo:** Usar uno de los algoritmos BUG para navegar de la posición 1 (P1) o partida hasta la posició 2 (P2) o meta.

**Materiales:**
- Robot EV3 y acesorios
- Catón paja para formar obstaculos
- ev3devcon micro SD y antena wi-fi

**Reto**
Crear un espacio de trabajo que contenga al menos dos obstáculos que intercepten una línea recta entre la posición 1 y la posición 2. Con tamaño adecuado para el paso del EV3 entre obstáculos.

![image](https://github.com/JSDaleman/Robotica-movil-Lab3/assets/70998067/edcf715b-1347-41a3-afc5-14447c42d69e)

**Consideraciones**
Como el algoritmo requiere el conocimiento de la pose del robot en su recorrido se puede usar odometría visual, odometría por las ruedas, reconocimiento por imásgenes. Una alternativa permitida es combinar el algoritmo BUG con un seguidor de línea. La línea puede ser parte de la prepacion de la zona de operación del robot.

#### Resultados

#### Solución presentada

#### Algoritmo usado

#### Video


### Misión 2
**Objetivo:** Usar uno de los algoritmos MAZE para ir de la entrada P1 hasta la salida P2 del laberinto.

**Materiales:**
- Robot EV3 y accesorios
- Tabla o piso
- Tablillas y postes para formar obstáculos
- IDE EV3

**Reto**
Montar el laberinto que debe tener como mínimo 6L x 2L, donde L debe ser entre 1,5 y 2,0 veces el largo del EV3.

Se puede un mundo diferente al mostrado. El laberinto debe tener una entrada y una salida marcadas.

![image](https://github.com/JSDaleman/Robotica-movil-Lab3/assets/70998067/18513a13-9a28-485c-827c-2071517ba26d)

**Consideraciones**
Al cumplir la misión, el algoritmo debe resolver al menos una vez cada una de las situaciones presentadas.

![image](https://github.com/JSDaleman/Robotica-movil-Lab3/assets/70998067/4143672e-bb7a-4414-a97e-a3d1ece56136)


#### Resultados
Los materiales empleados fueron:
- Robot EV3 y acesorios
- Catón paja, cinta y plastilina para formar obstáculos
- micro SD y antena wi-fi
- Software: ev3dev y visual studio code

**Mundo utilizado**

Se planeo un mundo de 6L*2L en donde L tendria el valor de 36cm ya que seria de 1.5 del largo del robot el cual es de 24cm.

![Plano laberintro](https://github.com/JSDaleman/Robotica-movil-Lab3/assets/70998067/b9b3df13-bfa7-4b24-b716-d7b8876badf7)

El cual una vez implementado se vio asi

![Imagen de WhatsApp 2024-05-23 a las 22 22 23_9b6e7f54](https://github.com/JSDaleman/Robotica-movil-Lab3/assets/70998067/04f1df4e-42b2-4f9c-b12a-963e7787fffd)

![Imagen de WhatsApp 2024-05-23 a las 22 22 22_03894511](https://github.com/JSDaleman/Robotica-movil-Lab3/assets/70998067/3848e016-8468-4bce-acdd-da471f243976)

![Imagen de WhatsApp 2024-05-23 a las 22 22 22_af62a34c](https://github.com/JSDaleman/Robotica-movil-Lab3/assets/70998067/5f6cfe3c-500c-415b-b022-f5972fddc0c6)

![Imagen de WhatsApp 2024-05-23 a las 22 22 23_4ac6df53](https://github.com/JSDaleman/Robotica-movil-Lab3/assets/70998067/bba23b56-22fc-4280-8c8c-52970b7c6299)

#### Solución presentada

El algoritmo creado utiliza una combinación de detección de obstáculos y búsqueda de rutas alternativas para navegar por el laberinto. Se basa principalmente en la detección de obstáculos con el sensor ultrasónico y en la detección de líneas negras con el sensor de color para identificar la entrada y la salida del laberinto. La estrategia de solución de obstáculos implica girar en dirección opuesta a los obstáculos detectados, similar a una regla de seguimiento de pared. El uso de sonidos y luces proporciona retroalimentación visual y auditiva sobre el estado y las acciones del robot durante todo el proceso. En este algoritmo se combinaron dos tecnicas de solución la cuales fueron algoritmo de la mano Derecha/Izquierda (Right/Left Hand Rule) y búsqueda en Profundidad (Depth-First Search, DFS). El algoritmo tiene elementos de la regla de la mano derecha/izquierda en la función SolveObstacle(), donde el robot comprueba y responde a los obstáculos a su derecha e izquierda. Dependiendo de las detecciones, toma giros a la izquierda o derecha, lo cual es característico de este tipo de algoritmos. Además de elementos de búsqueda en Profundidad El robot avanza hasta que encuentra un obstáculo y luego retrocede para probar otro camino, lo cual es un enfoque típico de la búsqueda en profundidad. La función SolveLabyrinth() ejemplifica este comportamiento, donde el robot sigue un camino hasta que encuentra una barrera, retrocede y prueba otra dirección.

**Aspectos Clave del Algoritmo**

- **Seguimiento de Pared (Wall Following) y Reglas de la Mano:**
  - SolveObstacle(): La función verifica obstáculos a la derecha e izquierda y decide girar según los resultados.
  - El robot usa un sensor ultrasónico para medir distancias a los lados y determina los giros basándose en estas mediciones.
  - Esto es similar a las reglas de la mano derecha/izquierda y algoritmo de Wall Follower, donde el robot sigue una pared para encontrar la salida.
  
-  **Búsqueda Exhaustiva y Movimientos Lineales:**
  - SolveLabyrinth(): El robot avanza en línea recta hasta encontrar un obstáculo o llegar al final del laberinto.
  - Este comportamiento es similar a una búsqueda en profundidad (DFS), ya que el robot explora un camino hasta encontrar un obstáculo y luego retrocede para intentar una ruta diferente.


#### Algoritmo usado
El código usado fue [Mision2.py](https://github.com/JSDaleman/Robotica-movil-Lab3/blob/main/Scripts/Mision2.py) el cual tiene la siguiente estructura:

```
Inicio
    Mostrar mensaje de bienvenida y laberinto

    Inicializar motores y sensores
    Definir variables y constantes
    Configurar modos de sensores

    Configurar colores de luces de preparación
    Calibrar giroscopio

    Verificar y posicionar motor_a en la posición adecuada

    Definir funciones de sonido:
        SoundStart() - reproducir tono de inicio
        SoundStartLaber() - reproducir tono de inicio de solución de laberinto
        SoundFinishLaber() - reproducir tono de finalización de laberinto
        SoundScanning() - reproducir tono de escaneo de obstáculos

    Definir función SolveObstacle()
        Reproducir sonido de escaneo
        Escanear derecha
        Si hay obstáculo a la derecha:
            Marcar ObstaculoDerecha como verdadero

        Escanear izquierda
        Si hay obstáculo a la izquierda:
            Marcar ObstaculoIzquierda como verdadero

        Reposicionar motor_a al frente

        Si hay obstáculos en ambos lados:
            Girar 180 grados a la derecha
            Retornar verdadero (indicando que se necesita retroceder)
        Si hay obstáculo solo a la derecha:
            Girar 90 grados a la izquierda
            Retornar falso
        Si no hay obstáculos a la derecha:
            Girar 90 grados a la derecha
            Retornar falso

    Definir función GoToEntry()
        Configurar luces de inicio
        Reproducir sonido de inicio

        Mientras no se detecte la línea de entrada (color):
            Avanzar hacia adelante

        Detener motores al detectar la línea

    Definir función SolveLabyrinth()
        Esperar entrada del usuario para comenzar

        Medir distancia inicial con sensor ultrasónico
        Configurar luces de resolución de laberinto
        Calcular grados para recorrer una celda menos un margen

        Reproducir sonido de inicio de laberinto

        Moverse a la primera celda
        Medir distancia con sensor ultrasónico

        Mientras no se llegue al final del laberinto:
            Mientras no se detecte un obstáculo o la meta:
                Si la distancia medida es menor o igual a 7 cm:
                    Detener motores
                    Salir del bucle

                Si se detecta la meta (color):
                    Detener motores
                    Mostrar mensaje de llegada
                    Configurar luces de meta
                    Salir del bucle

                Continuar avanzando hacia adelante

            Si se detecta la meta (color):
                Avanzar a la siguiente celda
                Reproducir sonido de finalización del laberinto
                Animar luces de policía
                Configurar luces de meta
                Salir del bucle principal

            Llamar a SolveObstacle() para decidir el próximo movimiento
            Si SolveObstacle() retorna verdadero:
                Avanzar a la siguiente celda
                Llamar nuevamente a SolveObstacle()

    Definir función main()
        Llamar a GoToEntry()
        Llamar a SolveLabyrinth()

    Ejecutar función main() si el script es ejecutado como el programa principal

Fin
```

#### Video
[Video de resultado misión 2](https://www.youtube.com/watch?v=qZ1mem_wqYo)

## Conclusiones

* **Limitación en la velocidad de solución:** Por la excatitud del giro usando el giro sensor y el posicionamiento adecuado del sensor de ultra sonido para la mediciones de distancia generan limitantes en la velocidad angular para el giro para evitar acumulacion de errores donde el robot perdera su correcta orientación y la necesidad de tiempos de espera para tener correctos posicionamientos de los elementos del robot.

* **Eficacia en la navegación:** El algoritmo demuestra eficacia en la navegación y solución de un laberinto utilizando sensores básicos disponibles en el kit EV3. La combinación de sensores ultrasónico y de color permite al robot detectar obstáculos y la meta con precisión.
  
* **Simplicidad y robustez:** Utiliza una estrategia simple pero robusta basada en la detección de obstáculos y la búsqueda de rutas alternativas. Este enfoque hace que el algoritmo sea relativamente fácil de implementar y depurar, especialmente en un entorno educativo.
  
* **Adaptabilidad:** El algoritmo puede adaptarse a diferentes configuraciones de laberinto y tipos de obstáculos. La capacidad del robot para girar en varias direcciones según las lecturas de los sensores le permite ajustarse dinámicamente a diferentes situaciones. Siendo una limitante en el algoritmo que las ramas no pueden ser mayores a una celda lo cual podria adaptarse facilmente para evitar esta limitante.
  
* **Feedback visual y auditivo:** La integración de señales visuales y auditivas mejora la interacción humano-robot, proporcionando retroalimentación inmediata sobre el estado del robot y sus acciones. Esto es especialmente útil en entornos educativos para facilitar el aprendizaje y la comprensión de los procesos robóticos.
  
* **Limitaciones de sensores:** A pesar de su eficacia general, el algoritmo depende en gran medida de la precisión y el rango de los sensores. Las limitaciones en la precisión de los sensores ultrasónico y de color pueden afectar la capacidad del robot para detectar obstáculos y la línea de meta en ciertos escenarios.

* **Tiempo de calibración:** La necesidad de calibrar el giroscopio y posicionar el sensor ultrasónico al inicio del proceso es crucial para asegurar movimientos precisos. Esto añade un paso adicional pero necesario para la correcta ejecución del algoritmo.

* **Estrategia de obstáculos:** La estrategia de resolución de obstáculos es similar a la regla de la mano derecha o izquierda (Right/Left Hand Rule), ya que el robot escanea ambos lados y elige una dirección basada en la presencia de obstáculos. Esto asegura que el robot siempre tenga un plan de acción para evitar quedarse atascado.

* **Aplicabilidad en entornos reales:** Aunque el algoritmo está diseñado para un entorno controlado como un laberinto, los principios subyacentes pueden aplicarse a escenarios más complejos de navegación robótica. Las técnicas de detección y evasión de obstáculos son fundamentales en robótica móvil.

* **Experiencia de usuario:** La inclusión de sonidos y efectos de luces mejora significativamente la experiencia del usuario, haciendo que la interacción con el robot sea más intuitiva y agradable. Este tipo de feedback es valioso en aplicaciones educativas y demostraciones interactivas.

* **Potencial educativo:** El algoritmo es una excelente herramienta educativa para enseñar principios básicos de programación, robótica y algoritmos de búsqueda. Los estudiantes pueden aprender sobre la integración de hardware y software, la lógica de control y la importancia de la calibración y la precisión en sistemas robóticos. En resumen, el algoritmo proporciona una solución efectiva y educativa para la navegación de laberintos con robots EV3. Su simplicidad, junto con la robustez y la capacidad de proporcionar retroalimentación visual y auditiva, lo convierte en una excelente herramienta tanto para principiantes como para usuarios avanzados en el campo de la robótica.
