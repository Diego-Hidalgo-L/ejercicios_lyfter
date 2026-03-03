

class SaldoInsuficiente(Exception):
    pass


def retirar_dinero(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficiente()
    else:
        saldo -= monto
    return saldo


def main():
    saldo = 500_000
    try:
        monto = float(input("Ingrese el monto que desea retirar: "))
        saldo = retirar_dinero(saldo, monto)

        print("\nRetiro realizado correctamente.")
        print("El saldo es de:", saldo)

    except SaldoInsuficiente:
        print("El saldo es insuficiente.")
    except ValueError:
        print("Ingrese valores válidos.")


main()