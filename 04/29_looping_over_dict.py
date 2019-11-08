

film = {'name': 'Forrest Gump',
        'made': 1994,
        'director': 'Robert Zemeckis',
        'soundtrack': 'Multiple',
        'starring': 'Tom Hanks',
        'fun_fact': '''The house used in Forrest Gump is
                    the same house used in The Patriot
                    (2000). Some paneling was changed
                    for interior shots  in the latter
                    film.'''}

while film:
    key, value = film.popitem()
    print('Key: ', key, ' | Value: ', value)
