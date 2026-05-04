# moja_lista_na_sok=['banan', 'marchew', 'młotek']
# print(moja_lista_na_sok)
#
# moja_lista_na_sok.pop(2)
# print(moja_lista_na_sok)
#
# moja_lista_na_sok.remove('banan')
# print(moja_lista_na_sok)

users: list = [
    {'username': 'oliwia', 'location': 'łódź', 'posts': 1,
     'usermessage': ['życzenia1', 'kocham legie', 'sprzeam opla', 'kiwi1']},
    {'username': 'paweł', 'location': 'ostróda', 'posts': 2,
     'usermessage': ['życzenia2', 'kocham legie1', 'sprzeam opla1']},
    {'username': 'eliza', 'location': 'radom', 'posts': 3, 'usermessage': ['życzenia3', 'kocham legie2']},
    {'username': 'filip', 'location': 'dęblin', 'posts': 4,
     'usermessage': ['życzenia4', 'kocham legie3', 'sprzeam opla3', 'kiwi3']},
]


# print(users)
# users.remove({'username': 'oliwia', 'location': 'łódź', 'posts': 1,
#      'usermessage': ['życzenia1', 'kocham legie', 'sprzeam opla', 'kiwi1']})

def update_user(users_data: list) -> None:
    name = input('Podaj imię użytkownika do zmiany: ')

    for user in users_data:
        if user['username'] == name:
            user['username'] = input('Podaj nowe imię: ')
            user['location'] = input('Podaj nową lokalizację: ')
            user['posts'] = int(input('Podaj liczbę postów: '))


update_user(users)
print(users)
