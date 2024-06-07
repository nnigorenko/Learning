from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    users = []
    videos = []

    def __init__(self, users, videos, current_user):
        self.users = (User)
        self.videos = [Video]
        self.current_user = current_user

    def log_in(self, login, password):
        for i in range(len(self.users)):
            if login in self.users[i]:
                if hash(password) in self.users[i]:
                    self.current_user = login
                    print(f'Wellcome back, {login}!')
                    break
                else:
                    print('Incorrect password')
                    break
            else:
                continue
        print(f'User {login} not found')







# for i in range(1, 11):
#     sleep(1)
#     print(i, end=' ')

# ur = UrTube()
# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
# ur.add(v1, v2)

# Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
# watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)

# Попытка воспроизведения несуществующего видео
# watch_video('Лучший язык программирования 2024 года!')
