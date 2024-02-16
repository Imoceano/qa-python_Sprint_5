import random
class GeneratorPassword:
    @staticmethod
    def random_password():
        number = random.randint(100000,999999)
        return number

