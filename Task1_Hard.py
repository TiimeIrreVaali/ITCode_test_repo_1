class Toy:
    def __init__(self, material, name, color, kind):
        self.name = name
        self.color = color
        self.kind = kind
        self.material = material

    def create(self):
        print(self.name)


class Plant(Toy):

    def __init__(self, material, name, color, kind):
        self.name = name
        self.color = color
        self.kind = kind
        self.material = material

    def materials(self):
        self.name = f'{self.name} {self.kind} made of {self.material}'

    def tailoring(self):
        self.name = f'tailored {self.name}'

    def dyeing(self):
        self.name = f'{self.color} {self.name}'


if __name__ == '__main__':
    george_toy = Plant('wool', 'George', 'black-and-white', 'cat')
    george_toy.create()