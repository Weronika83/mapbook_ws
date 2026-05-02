def read_data(user_data: list) -> None:
    for user in user_data:
        print(
            f'twój znajomy {user['username']} z miejscowości {user['location']} opublikował {user['posts']} wiadomości. Ostatnia wiaomość {user['usermessage'][-1]}')

