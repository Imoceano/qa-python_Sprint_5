import random
class GeneratorEmail:
    @staticmethod
    def random_email():
        name = 'konstantingolovin'
        number = random.randint(1,1999)
        mail = random.choice(['ya','yandex','gmail','mail'])
        domain = random.choice(['ru','com','net','eng','org'])
        return f'{name}{number}@{mail}.{domain}'
