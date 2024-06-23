# ClassFinder
## INDEX
- Introducció
- Components
  - Components Elèctrics
  - Peces 3D
- Sistema Elèctric
- Algorisme Utilitzat
- Resultat Final
- Agraïments
- Autors

# Introducció
Classfinder és un projecte de l'assignatura de Robòtica del Grau enginyeria informàtica de la UAB.
El robot és un vehicle que utilitzant un sistema d'escàners i una càmera es guiarà al voltant de la facultat d'enginyeria. Se li demanarà per veu on es troba una aula concreta, q2 1005 per exemple, i el robot guiarà a la persona cap a aquella classe anant pel camí òptim.

# Components
### Components Elèctrics

- Motor Micro Metal LP con reductora 10:1

  <img src="https://tienda.bricogeek.com/288-thickbox_default/motor-micro-metal-lp-con-reductora-10-1.jpg" width="200" >

- Pareja de ruedas 80x10mm - Blanco

  <img src="https://tienda.bricogeek.com/933-thickbox_default/pareja-de-ruedas-80x10mm-blanco.jpg" width="200">

- Sensor de distancia por ultrasonidos HC-SR04

  <img src="https://tienda.bricogeek.com/2677-thickbox_default/sensor-de-distancia-por-ultrasonidos-hc-sr04.jpg" width="200">

- Raspberry Pi 3 B+

  <img src="https://tienda.bricogeek.com/4669-thickbox_default/kit-basico-raspberry-pi-zero-wifi-microsd-32gb.jpg" width="200">

- Cables dupond macho-macho

  <img src="https://tienda.bricogeek.com/7856-thickbox_default/cables-dupont-macho-macho-40-cm-40-unidades.jpg" width="200">

- Cables tipo DuPont Hembra - Hembra

  <img src="https://tienda.bricogeek.com/7856-thickbox_default/cables-dupont-macho-macho-40-cm-40-unidades.jpg" width="200">

- Altavoz 40mm / 3W

  <img src="https://tienda.bricogeek.com/7842-thickbox_default/altavoz-40mm-3w.jpg" width="200">

- Micrófono digital MEMS I2S SPH0645

  <img src="https://tienda.bricogeek.com/6556-thickbox_default/microfono-digital-mems-i2s-sph0645.jpg" width="200">

- Cámara Raspberry Pi v2 - 8 Megapixels

  <img src="https://tienda.bricogeek.com/3115-large_default/camara-raspberry-pi-v2-8-megapixels.jpg" width="200">

- Arduino Nano Every

  <img src="https://tienda.bricogeek.com/6397-large_default/arduino-nano-every.jpg" width="400" length="300">

### Peces 3D
  <img src="images/base_sense_forats.jpeg" width="400" height="200">
- Base i tapa del robot, peça sense forats. Fetes amb talladora laser

  <img src="images/columna.jpeg" width="150" height="300">
- Columna utilitzada per juntar la base i la tapa del robot. Fetes amb impresora 3D.

  <img src="images/ultraSound.jpeg" width="300" height="200">
- Peça feta per donar suport als sensors i que puguin estar ben orientats. Fetes amb impresora 3D.

# Sistema Elèctric
 foto del esquemita del arnau
# Algorisme Utilitzat
 Hem desenvolupat un robot que utilitza sensors d'ultrasons connectats a un Arduino per mesurar la distància entre el robot i els objectes del seu entorn. Aquesta informació es transmet des de l'Arduino a una Raspberry Pi a través d'un port sèrie. Quan s'inicialitza el sistema, es rep la distància de cada sensor.

L'algoritme de navegació del robot funciona de la següent manera:

Entrada de dades:

distàncies_sensors: Les distàncies mesurades per cada sensor d'ultrasons.
Càlcul del temps de desplaçament:

S'han realitzat mesures prèvies per determinar el temps que tarda el robot a anar d'un punt A a un punt B dins de cada passadís.
Aquest temps predefinit (temps_predefinit) es basa en la velocitat constant del robot i les distàncies entre els punts de referència (classes).
Gestió d'obstacles:

Si el robot detecta un obstacle, el sistema calcula el temps perdut (temps_perdut) degut a l'aturada i la maniobra necessària per esquivar l'obstacle.
Aquest temps perdut es suma al temps predefinit per ajustar el temps total de desplaçament (temps_total).
Càlcul del temps total:

El temps total es calcula com:
\text{temps_total} = \text{temps_predefinit} + \text{temps_perdut}
Sortida de dades:

El robot ajusta la seva ruta i el seu temps de desplaçament segons els obstacles detectats i la distància que encara ha de recórrer per arribar a la seva destinació.
Descripció del Funcionament
Quan el robot es mou cap a una destinació específica (una de les tres classes en cada passadís), utilitza els sensors d'ultrasons per detectar obstacles al seu camí. Si es troba amb un obstacle, el robot realitza els següents passos:

Es mesura el temps perdut degut a la detecció i l'esquiva de l'obstacle.
Aquest temps perdut s'afegeix al temps predefinit de desplaçament.
El robot continua el seu camí, ajustant el temps total segons sigui necessari per arribar al punt de destinació.
Aquest algoritme permet que el robot navegui de manera eficient i segura dins de l'edifici d'enginyeria, ajustant el seu temps de desplaçament segons les condicions reals del seu entorn.
# Resultat Final
 insertar foto de nuestra aberración
# Agraïments
Volem agrair a la UAB per poder facilitar la obtenció dels elements necesàris com per deixarnos les eines per fabricar i treballar amb ells. 
# Autors
- Arnau Ruzo 1597124 
- Marc Morillo 1600363
- Pol Muñoz 1601912
- David Feliu 1598106


