
# Programación Orientada a Objetos con Python

La Programación Orientada a Objetos (POO) en Python es un paradigma que permite organizar el código en torno a **objetos**. Un objeto es una instancia de una **clase**, que agrupa atributos y métodos para representar y manipular datos y comportamientos.

## Conceptos clave en POO con Python:

### 1. Clases y Objetos
- Una **clase** es un plano o plantilla que define los atributos (variables) y métodos (funciones) de un tipo de objeto. 
- Un **objeto** es una instancia de una clase, y puede tener sus propios valores para los atributos definidos en la clase.

```python
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} ha arrancado.")

# Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla")
mi_coche.arrancar()
```

### 2. Encapsulamiento
Consiste en ocultar los detalles internos de un objeto y exponer solo lo necesario. Python no tiene un sistema de encapsulamiento estricto, pero los atributos o métodos pueden indicarse como "privados" usando un guion bajo `_` o doble guion bajo `__` para limitar su acceso.

```python
class Coche:
    def __init__(self, marca, modelo):
        self._marca = marca  # atributo "protegido"
        self.__modelo = modelo  # atributo "privado"

    def mostrar_info(self):
        return f"{self._marca} {self.__modelo}"
```

### 3. Herencia
La herencia permite crear una nueva clase que reutilice o extienda el comportamiento de una clase existente. Esto facilita la creación de nuevas clases basadas en clases preexistentes.

```python
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def mover(self):
        print(f"El vehículo {self.marca} está en movimiento.")

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} ha arrancado.")

mi_coche = Coche("Honda", "Civic")
mi_coche.arrancar()  # Usa métodos de Coche
mi_coche.mover()     # Usa métodos heredados de Vehículo
```

### 4. Polimorfismo
Permite que diferentes objetos respondan de manera distinta al mismo método o acción. Las clases hijas pueden redefinir métodos de la clase base.

```python
class Vehiculo:
    def mover(self):
        print("El vehículo se está moviendo.")

class Bicicleta(Vehiculo):
    def mover(self):
        print("La bicicleta está pedaleando.")

class Coche(Vehiculo):
    def mover(self):
        print("El coche está acelerando.")

# Polimorfismo en acción
vehiculos = [Bicicleta(), Coche()]
for vehiculo in vehiculos:
    vehiculo.mover()  # Diferentes comportamientos según el tipo de vehículo
```

### 5. Abstracción
Permite definir una interfaz para las clases sin preocuparse por los detalles de implementación. Python no tiene clases abstractas estrictamente, pero puedes usar el módulo `abc` para crearlas.

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto
```

### 6. Composición
En lugar de heredar de una clase, la composición permite crear objetos utilizando otras clases como atributos.

```python
class Motor:
    def encender(self):
        print("El motor está encendido.")

class Coche:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        self.motor.encender()
        print("El coche está en marcha.")
```

## Ventajas de la POO:
- **Modularidad**: Se puede organizar el código en clases reutilizables y fácilmente mantenibles.
- **Reutilización**: A través de la herencia y la composición, se pueden reutilizar clases ya definidas.
- **Facilidad de mantenimiento**: Se pueden hacer cambios en el código más fácilmente al tener un diseño bien estructurado.


# Sistema de Gestión de Vehículos en Python

Este proyecto implementa un sistema básico de gestión de vehículos utilizando el concepto de **herencia** en Programación Orientada a Objetos (POO) en Python. 

## Conceptos Clave

- **Herencia**: Permite que una clase hija (derivada) herede atributos y métodos de una clase padre (base). Esto permite reutilizar código y evitar duplicación.
- **Polimorfismo**: Las clases derivadas pueden sobrescribir los métodos de la clase base para personalizarlos, manteniendo un comportamiento coherente.

## Estructura del Código

1. **Clase base `Vehiculo`**: Contiene atributos comunes a todos los vehículos, como `marca`, `modelo`, `año`, y `kilometraje`.
2. **Clases derivadas**:
   - `Auto`: Añade el atributo específico `numero_puertas`.
   - `Motocicleta`: Añade el atributo específico `tipo_motor`.
   - `Camion`: Añade el atributo específico `capacidad_carga`.

Cada una de estas clases derivadas hereda de la clase base `Vehiculo` y sobrescribe el método `mostrar_informacion()` para agregar información adicional específica.

## Ejemplo de Uso

```python
# Crear instancias de cada tipo de vehículo
auto = Auto("Toyota", "Corolla", 2020, 30000, 4)
moto = Motocicleta("Honda", "CBR", 2019, 12000, "Combustión")
camion = Camion("Volvo", "FH", 2021, 50000, 18)

# Mostrar información
print(auto.mostrar_informacion())
print(moto.mostrar_informacion())
print(camion.mostrar_informacion())
```

### Resultado:

```plaintext
Marca: Toyota, Modelo: Corolla, Año: 2020, Kilometraje: 30000 km, Número de puertas: 4
Marca: Honda, Modelo: CBR, Año: 2019, Kilometraje: 12000 km, Tipo de motor: Combustión
Marca: Volvo, Modelo: FH, Año: 2021, Kilometraje: 50000 km, Capacidad de carga: 18 toneladas
```