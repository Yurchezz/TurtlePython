class Turtle:
    sensei = "Splinter"

    science_naming = ""
    actual_name = ""
    weight = 0
    swimming_speed = 0
    living_place = ""
    weapon = ""
    battle_style = ""

    def to_string(self):
        print("-----------------------"
              , "\nActual Name:", self.actual_name
              , "\nScientific Name:", self.science_naming
              , "\nWeight:", self.weight
              , "\nSwimming Speed:", self.swimming_speed
              , "\nWeapon:", self.weapon
              , "\nBattle Style: " + self.battle_style
              , "\n-----------------------")

    def __init__(
            self,
            actual_name="Ninja Turtle",
            science_naming="Terrapene carolina",
            weight=10000,
            swimming_speed=1,
            weapon="Fists",
            battle_style="Street"
    ):
        self.actual_name = actual_name
        self.science_naming = science_naming
        self.weight = weight
        self.swimming_speed = swimming_speed
        self.weapon = weapon
        self.battle_style = battle_style

    @staticmethod
    def show_sensei():
        print("Sensei: ", Turtle.sensei)

    def __del__(self):
        print("Destructor have been invoked")


def main():

    rafael = Turtle(
        "Rafael",
        "cherepahus rafaelus",
        1200,
        15,
        "Sais",
        "Karate")

    donatello = Turtle(
        "Donatello",
        "cherepahus donatellus",
        1000,
        13,
        "Bo Staff",
        "Karate")

    leonardo = Turtle(
        "Leonardo",
        "cherepahus leonardus",
        1000,
        14,
        "Katanas",
        "Karate")

    leonardo.to_string()
    donatello.to_string()
    rafael.to_string()

    Turtle.show_sensei()


if __name__ == "__main__":
    main()


