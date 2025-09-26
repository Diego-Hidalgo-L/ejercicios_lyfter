
games_list = [
    {'Nombre': 'Grand Theft Auto IV',
    'Género': 'Acción',
    'Desarrollador': 'Rockstar Games',
    'Clasificación': 'M'}
    ,
    {'Nombre': 'The Elder Scrolls IV: Oblivion',
    'Género': 'RPG',
    'Desarrollador': 'Bethesda',
    'Clasificación': 'M'}
    ,
    {'Nombre': "Tony Hawk's Pro Skater 2",
    'Género': 'Deportes',
    'Desarrollador': 'Activision',
    'Clasificación': 'T'}
    ]


for i, game in enumerate(games_list):
    for value in game.values():
        if value == "M":
            print(games_list[i]['Nombre'])