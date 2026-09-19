
time_secs = int(input("Ingrese su tiempo en segudos: "))

if time_secs < 600:
    spare_time = 600 - time_secs
    print("Esto es los segundos que faltan para llegar a 10 minutos:", spare_time)
elif time_secs > 600:
    print("Mayor.")
else:
    print("Igual.")