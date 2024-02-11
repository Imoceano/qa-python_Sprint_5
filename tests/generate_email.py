import random
class GeneratorEmail:
    @staticmethod
    def random_email():
        name = random.choice(['Nick','Andrew', 'Bob', 'Joe', 'Peter'])
        number = random.randint(1,999)
        mail = random.choice(['ya','yandex','gmail','mail'])
        domain = random.choice(['ru','com','net','eng','org'])
        return f'{name}{number}@{mail}.{domain}'
        
generate = GeneratorEmail()
generate.random_email()

