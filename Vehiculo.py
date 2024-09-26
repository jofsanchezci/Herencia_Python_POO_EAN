# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Kilometraje: {self.kilometraje} km"

# Clase derivada Auto que hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, kilometraje, numero_puertas):
        super().__init__(marca, modelo, año, kilometraje)  # Llama al constructor de Vehiculo
        self.numero_puertas = numero_puertas

    def mostrar_informacion(self):
        info = super().mostrar_informacion()  # Llama al método mostrar_informacion() de Vehiculo
        return f"{info}, Número de puertas: {self.numero_puertas}"

# Clase derivada Motocicleta que hereda de Vehiculo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, kilometraje, tipo_motor):
        super().__init__(marca, modelo, año, kilometraje)
        self.tipo_motor = tipo_motor

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Tipo de motor: {self.tipo_motor}"

# Clase derivada Camion que hereda de Vehiculo
class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, kilometraje, capacidad_carga):
        super().__init__(marca, modelo, año, kilometraje)
        self.capacidad_carga = capacidad_carga

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Capacidad de carga: {self.capacidad_carga} toneladas"

# Ejemplo de uso
auto = Auto("Toyota", "Corolla", 2020, 30000, 4)
moto = Motocicleta("Honda", "CBR", 2019, 12000, "Combustión")
camion = Camion("Volvo", "FH", 2021, 50000, 18)

# Mostrar información
print(auto.mostrar_informacion())
print(moto.mostrar_informacion())
print(camion.mostrar_informacion())
