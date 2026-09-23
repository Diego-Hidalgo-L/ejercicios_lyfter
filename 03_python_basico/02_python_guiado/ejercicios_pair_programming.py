
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))

tarifa_por_hora = int(input("Ingrese su tarifa por hora: "))

salario = horas_trabajadas * tarifa_por_hora
print(f'Su salario es de: {salario}')

# TypeError: can't multiply sequence by non-int of type 'str'
# input() interpreta los números como strings, aunque sean integers.
# Para resolver esto, hay que utilizar el nombre corto que aparece en nuestra tabla (S4: Resumen - Tipos de datos).
# En este caso, vamos a utilizar int().

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
dominio_de_empresa = input("Ingrese el dominio de la empresa: ")

print(nombre + '.' + apellido + '@' + dominio_de_empresa + '.com')
print(f'{nombre}.{apellido}@{dominio_de_empresa}.com')

# La segunda respuesta (F string) es mejor que la segunda.
# Si en la primera utilizamos int's en vez de strings, el programa se confundiría.
# No sabe qué hacer en caso de sumer int's + strings.