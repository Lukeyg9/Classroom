class Bird:
    def __init__(self, species, habitat):
        self.species = species
        self.habitat = habitat

    def make_sound(self):
        raise NotImplementedError("Subclass must use make_sound.")

class Owl(Bird):
    def __init__(self, species, habitat, nocturnal=True):
        super().__init__(species, habitat)
        self.nocturnal = nocturnal

    def make_sound(self):
        return "Hoot!"

class Dodo(Bird):
    def __init__(self, species, habitat, extinct=True):
        super().__init__(species, habitat)
        self.extinct = extinct

    def make_sound(self):
        return "Silence..."

owl = Owl("Owl", "Forest")
dodo = Dodo("Dodo", "Island")

birds = [owl, dodo]
for bird in birds:
    print(f"{bird.species} lives in {bird.habitat}. Sound: {bird.make_sound()}")
