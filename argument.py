from philosophers import Philosopher
class Argument:
    def __init__(self, philosopher, name, description ):
        self.__philosopher = philosopher
        self.argument_name = name
        self.__description = description

    def __str__(self):
            return f"The {self.argument_name} argument of {self.__philosopher.name} is: {self.__description}"

if __name__ == "__main__":
    descartes = Philosopher("René Descartes", "France", 1596, 1650, "Rationalism", "I think therefore I am")
    cogito = Argument(descartes,"Cogito", "Even if the demon deceives me about everything, "
                                            "in order to deceive me I must exist. "
                                            "Doubt itself is a form of thinking, and whoever thinks exists. "
                                            "In the Second Meditation, Descartes puts it this way: "
                                            "the proposition “I am, I exist” is necessarily true whenever it is put forward by me or conceived in my mind.")
    print(cogito)
