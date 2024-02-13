import random
class GeneratorName:
    @staticmethod
    def random_name():
        name = random.choice(['Nick','Andrew', 'Bob', 'Joe', 'Peter'])
        return name
        
generate = GeneratorName()
generate.random_name()

