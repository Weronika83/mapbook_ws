users: list=[
    {'username':'oliwia', 'location':'łódź','posts':1,'usermessage':['życzenia1','kocham legie', 'sprzeam opla', 'kiwi1']},
    {'username':'paweł', 'location':'ostróda','posts':2,'usermessage':['życzenia2','kocham legie1', 'sprzeam opla1']},
    {'username':'eliza', 'location':'raom','posts':3,'usermessage':['życzenia3','kocham legie2']},
    {'username': 'filip', 'location': 'dęblin','posts':4, 'usermessage':['życzenia4','kocham legie3', 'sprzeam opla3', 'kiwi3']},
]

for user in users[1:]:
    print(f'twój znajomy {user['username']} z miejscowości {user['location']} opublikował {user['posts']} wiadomości. Ostatnia wiaomość {user['usermessage'][-1]}')
