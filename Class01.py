class Player:
    id = 0
    levels = ["beginner", "intermediate", "advanced"]

    def __init__(self, name, age, city, level):
        self.name = name
        self.age = age
        self.city = city
        self.level = level
        Player.id += 1

    def show(self):
        print("I am the %dth player, my name is %s, I am %d years old, and I live in %s.my level is %s" % (
            self.id, self.name, self.age, self.city, self.level))

    def levelup(self):
        self.level = Player.levels[Player.levels.index(self.level) + 1]


tom = Player("Tom", 18, "Beijing", "beginner")
print(tom.name, tom.age, tom.city)
print(tom.__dict__)
tom.show()
tom.levelup()
tom.show()
