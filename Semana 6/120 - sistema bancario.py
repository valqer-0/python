class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente (Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        
        self.numero_cuenta = numero_cuenta
        self.balance = balance
        self.historial = []

    def __str__(self):
        return f"""
{'='*50}
INFORMACIÓN DEL CLIENTE
{'='*50}
Nombre: {self.nombre} {self.apellido}
Número de cuenta: {self.numero_cuenta}
Balance Actual: Q{self.balance:.2f}
{'='*50}
"""
    
    def depositar(self, monto):
        if monto <= 0:
            print("\nError: El monto debe ser positivo.")
            return False
        self.balance += monto
        self.historial.append(f"Depósito: Q{monto:.2f}")
        print(f"\nDepósito exitoso de Q.{monto:.2f}")
        print(f"Nuevo balance: Q.{self.balance:.2f}")
        return True

    def retirar(self, monto):
        if monto <= 0:
            print("\nError: El monto debe ser positivo.")
            return False
        if monto > self.balance:
            print("\nFondos insuficientes!")
            print(f"Balance actual: Q{self.balance:.2f}")
            print(f"Intentaste retirar: Q{monto:.2f}")
            return False
        else:
            self.balance -= monto
            self.historial.append(f"Retiro: Q{monto:.2f}")
            print(f"\nRetiro exitoso de Q{monto:.2f}")
            print(f"Nuevo balance: Q{self.balance:.2f}")
            return True

    def ver_historial(self):
        print("\n" + "-"*20 + " HISTORIAL " + "-"*20)
        if not self.historial:
            print("Sin transacciones.")
        else:
            for t in self.historial:
                print(t)
        print("-"*58)

    def transferir(self, destinatario, monto):
        if monto <= 0:
            print("\nError: El monto debe ser positivo.")
            return False
        if monto > self.balance:
            print("\nFondos insuficientes para la transferencia.")
            print(f"Balance actual: Q{self.balance:.2f}")
            return False
        self.balance -= monto
        destinatario.balance += monto
        self.historial.append(f"Transferencia enviada: Q{monto:.2f} -> {destinatario.numero_cuenta}")
        destinatario.historial.append(f"Transferencia recibida: Q{monto:.2f} <- {self.numero_cuenta}")
        print(f"\nTransferencia exitosa de Q{monto:.2f} a {destinatario.numero_cuenta}")
        return True

def crear_cliente():
    print("\n" + "="*50)
    print("BIENVENIDO AL BANCO FIBONACCI")
    print("="*50)
    print("\nPor favor, ingresa tus datos para crear tu cuenta:\n")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    numero_cuenta = input("Numero de cuenta: ")

    while True:
        try:
            deposito_inicial = float(input("Deposito inicial (presiona 0 para omitir): Q"))
            if deposito_inicial < 0:
                print("El depósito inicial no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Monto inválido. Ingresa un número.")

    cliente = Cliente(nombre, apellido, numero_cuenta, deposito_inicial)
    if deposito_inicial > 0:
        cliente.historial.append(f"Depósito inicial: Q{deposito_inicial:.2f}")

    print("\nCuenta creada exitosamente!")
    print(cliente)

    return cliente

def inicio():

    clientes = {}
    primero = crear_cliente()
    clientes[primero.numero_cuenta] = primero

    while True:
        print("\n" + "="*50)
        print("MENU PRINCIPAL")
        print("-"*50)
        print("1. Depositar")
        print("2. Retirar")
        print("3. Ver balance")
        print("4. Ver historial")
        print("5. Crear nueva cuenta")
        print("6. Transferir entre cuentas")
        print("7. Salir")

        opcion = input("\nSelecciona una opcion (1-7): ")
        if opcion == "1":
            cuenta = input("Número de cuenta: ")
            cliente = clientes.get(cuenta)
            if not cliente:
                print("Cuenta no encontrada.")
                continue
            try:
                monto = float(input("Monto a depositar : Q"))
            except ValueError:
                print("Monto inválido.")
                continue
            cliente.depositar(monto)

        elif opcion == "2":
            cuenta = input("Número de cuenta: ")
            cliente = clientes.get(cuenta)
            if not cliente:
                print("Cuenta no encontrada.")
                continue
            try:
                monto = float(input("Monto a retirar : Q"))
            except ValueError:
                print("Monto inválido.")
                continue
            cliente.retirar(monto)

        elif opcion == "3":
            cuenta = input("Número de cuenta: ")
            cliente = clientes.get(cuenta)
            if not cliente:
                print("Cuenta no encontrada.")
                continue
            print(cliente)

        elif opcion == "4":
            cuenta = input("Número de cuenta: ")
            cliente = clientes.get(cuenta)
            if not cliente:
                print("Cuenta no encontrada.")
                continue
            cliente.ver_historial()

        elif opcion == "5":
            nuevo = crear_cliente()
            if nuevo.numero_cuenta in clientes:
                print("Ya existe una cuenta con ese número. No se creó la cuenta.")
            else:
                clientes[nuevo.numero_cuenta] = nuevo

        elif opcion == "6":
            origen = input("Cuenta origen: ")
            destino = input("Cuenta destino: ")
            c_origen = clientes.get(origen)
            c_destino = clientes.get(destino)
            if not c_origen or not c_destino:
                print("Una o ambas cuentas no existen.")
                continue
            try:
                monto = float(input("Monto a transferir : Q"))
            except ValueError:
                print("Monto inválido.")
                continue
            c_origen.transferir(c_destino, monto)

        elif opcion == "7":
            print("\n" + "=" * 50)
            print("Gracias por usar Banco Fibonacci!")
            print("Cuentas registradas:")
            for c in clientes.values():
                print(c)
            print("¡Hasta pronto!")
            print("=" * 50)
            break
        else:
            print("\nOpción inválida. Selecciona una opción válida.")

if __name__ == "__main__":
    inicio()