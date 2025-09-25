
# Cree un diccionario que guarde la siguiente información sobre un hotel:
    # nombre.
    # numero_de_estrellas.
    # habitaciones.
# El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
    # numero.
    # piso.
    # precio_por_noche.

mi_hotel = {
    'nombre' : 'Four Seasons',
    'numero_de_estrellas' : 5,
    'habitaciones' : [
        {
            'numero' : 304,
            'piso' : 3,
            'precio_por_noche' : '$225'
        },
        {
            'numero' : 207,
            'piso' : 2,
            'precio_por_noche' : '$175'
        },
        {
        'numero' : 408,
        'piso' : 4,
        'precio_por_noche' : '$250'
        }
    ]
}

print(mi_hotel['habitaciones'][2]['numero'])