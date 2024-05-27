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

Cuando se habla de navegación planeada, esta hace referencia a la capacidad de un robot para determinar una ruta desde un punto de inicio hasta un destino final antes de comenzar el movimiento. Esta técnica se basa en la elaboracion previa de un mapa del entorno en el que se va a encontrar el dispositivo, y el uso de algoritmos de planificación de rutas que aseguren que el robot pueda evitar obstáculos y alcanzar su objetivo de manera eficiente. Los algoritmos más comunes para la planificación de rutas incluyen el algoritmo A*, el algoritmo Dijkstra, y otros métodos de búsqueda basados en grafos.

### Navegación basada en comportamientos

La navegación basada en comportamientos, es un enfoque distinto en donde el control del robot se divide en varios comportamientos simples que operan en paralelo. Cada comportamiento responde a estímulos específicos del entorno, y la combinación de estos comportamientos resulta en una navegación efectiva. Este enfoque es más reactivo y menos dependiente de un modelo preciso del entorno. Ejemplos de comportamientos incluyen seguir paredes, evitar obstáculos y seguir una línea. La gran ventaja que trae la navegacion basada en comportamientos es que nos quitamos la necesidad de desarrollar un mapa detallado de donde va cicular el robot, lo cual lo hace una tecnica mucho mas adaptativa a diferentes entornos.

### Investigaciones y desarrollode robots por Rodney Brooks y Mark Tilden

Rodney Brooks es conocido por su trabajo en robótica subsumida, un enfoque en el cual se construyen robots con múltiples capas de control, cada una encargada de tareas más complejas, desde lo básico como evitar obstáculos hasta tareas más avanzadas como la navegación completa. Este enfoque se utiliza en la serie de robots de la empresa iRobot, como las aspiradoras Roomba.

Mark Tilden, por su parte, es conocido por su trabajo en BEAM robotics (Biology, Electronics, Aesthetics, and Mechanics), que se centra en la creación de robots simples que imitan el comportamiento biológico mediante circuitos analógicos en lugar de microprocesadores. Los robots BEAM son autónomos y responden directamente a su entorno sin necesidad de programación compleja.

### Algoritmos de planeación de rutas para espación con obstáculos

Los algoritmos de planeación de rutas para espacios con obstáculos se diseñan para encontrar la mejor ruta posible desde un punto inicial a un destino, evitando colisiones. Entre los algoritmos más utilizados se encuentran:

#### Algoritmo A*
Este es un algoritmo de búsqueda de caminos que se utiliza ampliamente en la inteligencia artificial y la robótica para encontrar la ruta más corta entre dos puntos en un gráfico ponderado. Su eficiencia se debe a la utilización de una heurística que estima el costo restante para alcanzar el objetivo. A continuación se detallan sus componentes y funcionamiento:

- **Función de Costo**: A* utiliza una función de costo `f(n) = g(n) + h(n)`, donde:
  - `g(n)` es el costo acumulado desde el nodo inicial hasta el nodo `n`.
  - `h(n)` es la heurística que estima el costo desde el nodo `n` hasta el objetivo. La heurística debe ser admisible, es decir, nunca debe sobrestimar el costo real para garantizar que A* encuentre el camino óptimo.

- **Proceso**:
  1. Inicia en el nodo de inicio.
  2. Calcula `f(n)` para los nodos adyacentes.
  3. Selecciona el nodo con el menor valor de `f(n)` y lo expande.
  4. Repite el proceso hasta alcanzar el nodo objetivo o agotar todos los nodos.

- **Aplicaciones**: A* es ideal para entornos donde se puede calcular una heurística precisa, como juegos, robótica, y aplicaciones de navegación en mapas.

#### Algoritmo Dijkstra
El algoritmo de Dijkstra es un método clásico para encontrar el camino más corto desde un nodo inicial a todos los demás nodos en un gráfico con pesos no negativos. Es considerado uno de los algoritmos más importantes en la teoría de grafos y tiene las siguientes características:

- **Función de Costo**: A diferencia de A*, Dijkstra no utiliza una heurística. Se basa únicamente en el costo acumulado `g(n)`.

- **Proceso**:
  1. Inicializa el costo del nodo inicial a 0 y el de todos los demás nodos a infinito.
  2. Selecciona el nodo no visitado con el menor costo acumulado.
  3. Actualiza los costos de los nodos adyacentes.
  4. Marca el nodo actual como visitado.
  5. Repite hasta que todos los nodos hayan sido visitados.

- **Limitaciones**: Si bien garantiza encontrar el camino más corto, puede ser ineficiente en gráficos grandes debido a su complejidad `O(V^2)` (donde V es el número de vértices). Sin embargo, utilizando estructuras de datos como colas de prioridad, la complejidad puede reducirse a `O(E \log V)` (donde E es el número de aristas).

- **Aplicaciones**: Es ampliamente utilizado en redes de comunicación, sistemas de información geográfica (SIG), y planificación de rutas.

#### RRT (Rapidly-exploring Random Trees)
El algoritmo de Árboles de Exploración Rápida (RRT) es un método de planificación de caminos diseñado para entornos complejos y de alta dimensión. Es especialmente útil para la planificación de rutas en tiempo real en espacios no estructurados y dinámicos.

- **Concepto Básico**: RRT explora el espacio de manera aleatoria, construyendo un árbol de rutas posibles desde el punto inicial hasta el objetivo.

- **Proceso**:
  1. Inicia en el nodo de inicio.
  2. Genera un punto aleatorio en el espacio de búsqueda.
  3. Encuentra el nodo en el árbol más cercano a este punto aleatorio.
  4. Extiende el árbol desde el nodo más cercano hacia el punto aleatorio, creando un nuevo nodo.
  5. Repite el proceso hasta que el nuevo nodo esté suficientemente cerca del objetivo o se alcance un límite de iteraciones.

- **Ventajas**:
  - **Exploración Rápida**: Explora rápidamente grandes áreas del espacio de búsqueda.
  - **Adaptabilidad**: Puede adaptarse fácilmente a diferentes entornos y restricciones dinámicas.

- **Limitaciones**: La ruta generada por RRT puede no ser la más corta ni la más suave. Sin embargo, variantes como RRT* (RRT estrella) mejoran la calidad de la ruta encontrando caminos óptimos asintóticamente.

- **Aplicaciones**: RRT es ideal para robótica móvil, manipulación robótica, y cualquier aplicación donde el entorno es desconocido o cambia con el tiempo.


### Algoritmos BUG
Los algoritmos BUG son una serie de métodos simples de navegación diseñados para que un robot se mueva desde un punto inicial a un punto final en presencia de obstáculos. Estos algoritmos son particularmente útiles en entornos desconocidos o parcialmente conocidos, donde el robot debe reaccionar a obstáculos inesperados durante su movimiento.

#### Bug 0
El algoritmo Bug 0 es el más básico de los algoritmos BUG. Su funcionamiento es sencillo y directo:

1. **Movimiento Inicial**: El robot se mueve en línea recta desde su posición inicial hacia el objetivo.
2. **Detección de Obstáculos**: Si el robot encuentra un obstáculo, cambia su estrategia.
3. **Bordeo del Obstáculo**: El robot bordea el obstáculo en una dirección predefinida (por ejemplo, en el sentido de las agujas del reloj) hasta que pueda continuar en línea recta hacia el objetivo.
4. **Reanudación del Movimiento**: Una vez que el obstáculo ha sido evitado, el robot retoma su movimiento en línea recta hacia el objetivo.

Este algoritmo es simple y fácil de implementar, pero puede no ser el más eficiente en términos de tiempo y distancia recorrida, especialmente en entornos con muchos obstáculos.

#### Bug 1
El algoritmo Bug 1 mejora la estrategia de Bug 0 al incluir un proceso de circunnavegación completa del obstáculo:

1. **Movimiento Inicial**: El robot se mueve en línea recta hacia el objetivo.
2. **Detección de Obstáculos**: Al encontrar un obstáculo, el robot marca el punto de colisión.
3. **Circunnavegación**: El robot circunvala completamente el obstáculo, manteniéndose en contacto con él, para encontrar el punto más cercano al objetivo desde el obstáculo.
4. **Reanudación del Movimiento**: Una vez que se ha determinado el punto más cercano al objetivo, el robot continúa su movimiento desde este punto en línea recta hacia el objetivo.

Este enfoque asegura que el robot siempre avanza hacia el objetivo de la manera más eficiente posible después de cada encuentro con un obstáculo.

#### Bug 2
El algoritmo Bug 2, también conocido como el algoritmo de la Pared Izquierda/Derecha, se basa en seguir una pared u obstáculo en una dirección específica:

1. **Movimiento Inicial**: El robot se mueve en línea recta hacia el objetivo.
2. **Detección de Obstáculos**: Al encontrar un obstáculo, el robot sigue la pared en una dirección predefinida (izquierda o derecha).
3. **Seguimiento de la Pared**: El robot continúa siguiendo la pared hasta encontrar un punto donde pueda reanudar su movimiento hacia el objetivo.
4. **Reanudación del Movimiento**: Una vez que se ha encontrado un punto donde el camino hacia el objetivo está libre, el robot se aleja de la pared y continúa su trayectoria directa hacia el objetivo.

Este método es eficiente para evitar quedar atrapado en ciclos infinitos, siempre y cuando el entorno esté simplemente conectado (es decir, no haya áreas cerradas donde el robot no pueda escapar).

### Algoritmo de Solución de un Laberinto (Maze Algorithm)

Los algoritmos de solución de laberintos permiten a los robots encontrar una salida en un entorno de laberinto. Estos algoritmos son esenciales para la navegación en entornos complejos y desconocidos, donde el robot debe explorar y decidir en tiempo real la mejor manera de avanzar. A continuación, se describen algunos de los algoritmos más comunes:

#### Algoritmo de Trémaux
El algoritmo de Trémaux es un método eficiente para resolver laberintos que garantiza encontrar la salida si existe. Su funcionamiento se basa en marcar los caminos mientras el robot avanza:

1. **Movimiento Inicial**: El robot comienza a moverse desde el punto de entrada del laberinto.
2. **Marcado de Caminos**: A medida que el robot avanza, marca el camino recorrido. Si encuentra una bifurcación, elige un nuevo camino y lo marca.
3. **Evitación de Ciclos**: Si el robot encuentra un camino ya marcado dos veces, significa que ese camino lleva a un ciclo o a un callejón sin salida, y no debe ser recorrido de nuevo.
4. **Retorno y Cambio de Dirección**: Si el robot llega a un callejón sin salida, regresa al último punto de decisión y toma una nueva dirección no explorada.
5. **Salida del Laberinto**: El proceso continúa hasta que el robot encuentra la salida del laberinto.

El algoritmo de Trémaux es simple y asegura que el robot no quede atrapado en ciclos infinitos, encontrando eventualmente la salida si existe.

#### Algoritmo de Pledge
El algoritmo de Pledge es útil para resolver laberintos que pueden contener ciclos o bucles, permitiendo al robot salir de estos ciclos y encontrar la salida:

1. **Movimiento Inicial**: El robot se mueve en línea recta hasta encontrar un obstáculo.
2. **Contador de Ángulos**: El robot utiliza un contador de ángulos para rastrear el número de giros realizados. Inicializa el contador a cero.
3. **Giro y Seguimiento de Pared**: Al encontrar un obstáculo, el robot gira en una dirección predefinida (por ejemplo, a la izquierda) y comienza a seguir la pared.
4. **Actualización del Contador**: Por cada giro, el robot actualiza el contador de ángulos:
   - Gira 90° a la izquierda: decrementa el contador en 90.
   - Gira 90° a la derecha: incrementa el contador en 90.
5. **Condición de Salida de Ciclos**: El robot continúa siguiendo la pared hasta que el contador de ángulos vuelva a cero, momento en el cual se puede mover en línea recta nuevamente.
6. **Reanudación del Movimiento**: El proceso se repite hasta que el robot encuentra la salida del laberinto.

El algoritmo de Pledge es particularmente útil para laberintos con múltiples ciclos, asegurando que el robot no quede atrapado en un bucle infinito.

#### Algoritmo de la Mano Izquierda/Derecha
El algoritmo de la Mano Izquierda/Derecha es uno de los métodos más intuitivos y fáciles de implementar para resolver laberintos simplemente conectados (sin islas):

1. **Movimiento Inicial**: El robot comienza a moverse desde el punto de entrada del laberinto.
2. **Seguimiento de Pared**: El robot mantiene su mano izquierda o derecha en contacto con la pared del laberinto.
   - Mano Izquierda: El robot sigue la pared a su izquierda.
   - Mano Derecha: El robot sigue la pared a su derecha.
3. **Exploración Continua**: El robot sigue moviéndose a lo largo de la pared, girando en las esquinas y siguiendo cualquier camino disponible mientras mantiene el contacto con la pared.
4. **Salida del Laberinto**: Eventualmente, el robot encontrará la salida del laberinto si el laberinto está simplemente conectado.

Este método es simple y efectivo para laberintos donde todas las paredes están conectadas a la periferia, pero puede no funcionar en laberintos con islas (áreas desconectadas de las paredes exteriores).

## Misiones de funcionamiento
Se deben resolver con navegación basada en comportamientos

### Misión 1
**Objetivo:** Usar uno de los algoritmos BUG para navegar de la posición 1 (P1) o partida hasta la posició 2 (P2) o meta.

**Materiales:**
- Robot EV3 y accesorios
- Tabla o piso
- Tablillas y postes para formar obstáculos
- IDE EV3
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

Se planeo un mundo de 6L*2L en donde L tendria el valor de 36cm ya que seria de 1.5 del largo del robot el cual es de 24cm y con una altura de pared de 26 cm

![Plano laberintro](https://github.com/JSDaleman/Robotica-movil-Lab3/assets/70998067/49bb2ebb-1402-4488-a8a0-0c16f2e3ec3d)

El cual una vez implementado se vio asi

![Imagen de WhatsApp 2024-05-23 a las 22 22 23_9b6e7f54](https://github.com/JSDaleman/Robotica-movil-Lab3/assets/70998067/04f1df4e-42b2-4f9c-b12a-963e7787fffd)

![Imagen de WhatsApp 2024-05-23 a las 22 22 22_03894511](https://github.com/JSDaleman/Robotica-movil-Lab3/assets/70998067/3848e016-8468-4bce-acdd-da471f243976)

![Imagen de WhatsApp 2024-05-23 a las 22 22 22_af62a34c](https://github.com/JSDaleman/Robotica-movil-Lab3/assets/70998067/5f6cfe3c-500c-415b-b022-f5972fddc0c6)

![Imagen de WhatsApp 2024-05-23 a las 22 22 23_4ac6df53](https://github.com/JSDaleman/Robotica-movil-Lab3/assets/70998067/bba23b56-22fc-4280-8c8c-52970b7c6299)

**Configuración robot**
![Imagen de WhatsApp 2024-05-27 a las 09 16 32_e451ce4d](https://github.com/JSDaleman/Robotica-movil-Lab3/assets/70998067/766e187f-27cb-4908-b454-86f6f7eadbea)

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


## Bibliografia
* Zamora, M. A., & Tomás-Balibrea, L. M. (2000). Navegación planificada de un robot móvil en entornos interiores desconocidos. *ResearchGate*. Recuperado de https://www.researchgate.net/publication/244222675_Navegacion_Planificada_de_un_Robot_Movil_en_Entornos_Interiores_Desconocidos
* Cruz, J. D., Londoño, S. H., & Velasco, J. R. (2012). Control de navegación basado en comportamientos para pequeños robots móviles. *Revista Politécnica*, 8(15), 79-85. Recuperado de https://revistas.elpoli.edu.co/index.php/pol/article/view/382/548
* Robotnik®. (2013). Nueva Generación de Robots Industriales que se Autoadaptan al Entorno. Recuperado de "https://robotnik.eu/es/nueva-generacion-de-robots-industriales-que-se-autoadaptan-al-entorno/"
* LibreTexts Español. (2011). Bibliotecas LibreTexts: una colaboración multiinstitucional para desarrollar la próxima generación de textos de acceso abierto para mejorar la educación postsecundaria. Recuperado de "https://espanol.libretexts.org/Ingenieria/Ingenier%C3%ADa_Mec%C3%A1nica/Introducci%C3%B3n_a_los_Robots_Aut%C3%B3nomos_(Correll)/04%3A_Planeaci%C3%B3n_de_caminos/4.02%3A_Algoritmos_de_planificaci%C3%B3n_de_rutas"
* Mario Serna H., Abraham Sánchez L., Martín Estrada A., Ma. Beatríz Bernábe L., Elberfeld E. Pérez G. (2019)  Navegación de robots móviles utilizando algoritmos Bugs extendidos. Recuperado de "https://rcs.cic.ipn.mx/2019_148_8/Navegacion%20de%20robots%20moviles%20utilizando%20algoritmos%20Bugs%20extendidos.pdf"
* Beanz Magazine. (2024). Maze-Solving Algorithms. Recuperado de "https://kidscodecs.com/maze-solving-algorithms/"
