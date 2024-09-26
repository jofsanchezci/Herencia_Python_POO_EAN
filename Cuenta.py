class Cuenta:
    def __init__(self, saldo, tasa_anual):
        self._saldo = saldo
        self._tasa_anual = tasa_anual
        self._consignaciones = 0
        self._retiros = 0
        self._comision = 0

    def consignar(self, monto):
        self._saldo += monto
        self._consignaciones += 1

    def retirar(self, monto):
        if monto <= self._saldo:
            self._saldo -= monto
            self._retiros += 1
            return True
        return False

    def calcular_interes_mensual(self):
        interes_mensual = (self._saldo * self._tasa_anual / 100) / 12
        self._saldo += interes_mensual
        return interes_mensual

    def extracto_mensual(self):
        self._saldo -= self._comision
        interes = self.calcular_interes_mensual()
        return self._saldo, self._comision, interes

    def imprimir(self):
        print(f"Saldo: {self._saldo}")
        print(f"Comisión mensual: {self._comision}")
        print(f"Número de transacciones - Consignaciones: {self._consignaciones}, Retiros: {self._retiros}")

class CuentaDeAhorros(Cuenta):
    def __init__(self, saldo, tasa_anual):
        super().__init__(saldo, tasa_anual)
        self._activa = saldo < 10000

    def consignar(self, monto):
        if self._activa:
            super().consignar(monto)

    def retirar(self, monto):
        if self._activa:
            return super().retirar(monto)

    def extracto_mensual(self):
        if self._retiros > 4:
            self._comision += 1000
        self._activa = self._saldo < 10000
        return super().extracto_mensual()

class CuentaCorriente(Cuenta):
    def __init__(self, saldo, tasa_anual, sobregiro):
        super().__init__(saldo, tasa_anual)
        self._sobregiro = sobregiro

    def retirar(self, monto):
        if monto <= self._saldo + self._sobregiro:
            self._saldo -= monto
            self._retiros += 1
            if self._saldo < 0:
                self._sobregiro += self._saldo
            return True
        return False

    def consignar(self, monto):
        super().consignar(monto)
        if self._sobregiro > 0 and monto > self._sobregiro:
            monto -= self._sobregiro
            self._sobregiro = 0
            super().consignar(monto)

    def extracto_mensual(self):
        return super().extracto_mensual()

def main():
    cuenta_ahorros = CuentaDeAhorros(5000, 3)
    cuenta_ahorros.consignar(2000)
    cuenta_ahorros.retirar(1000)
    cuenta_ahorros.extracto_mensual()
    cuenta_ahorros.imprimir()

    cuenta_corriente = CuentaCorriente(2000, 3, 1000)
    cuenta_corriente.consignar(500)
    cuenta_corriente.retirar(2500)
    cuenta_corriente.extracto_mensual()
    cuenta_corriente.imprimir()

main()
