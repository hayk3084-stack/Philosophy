from philosophers import Philosopher


class Argument:
    def __init__(self, philosopher, name, description, refutes=None, former_arg=None):
        self.philosopher = philosopher
        self.argument_name = name
        self.__description = description
        self.__refutes = refutes
        self.__former_arg = former_arg

    def __str__(self):
        if self.__former_arg is None:
            return f"The {self.argument_name} argument of {self.philosopher.name} is: {self.__description}"
        else:
            return f"The {self.argument_name} argument of {self.philosopher.name}, which is based on his former {self.__former_arg.argument_name} argument, is: {self.__description}"

    def refute_arg(self):
        return f"The {self.argument_name} argument refutes the {self.__refutes.argument_name} argument of {self.__refutes.philosopher.name}"


if __name__ == "__main__":
    descartes = Philosopher("René Descartes", "France", 1596, 1650, "Rationalism", "I think therefore I am")
    cogito = Argument(descartes, "Cogito", "Even if the demon deceives me about everything, "
                                            "in order to deceive me I must exist. "
                                            "Doubt itself is a form of thinking, and whoever thinks exists. "
                                            "In the Second Meditation, Descartes puts it this way: "
                                            "the proposition “I am, I exist” is necessarily true whenever it is put forward by me or conceived in my mind.")
    dualism = Argument(descartes, "Dualism", "Having established that he exists as a thinking thing, he notes that he can clearly and distinctly conceive of himself as a being whose entire essence is to think, without any extension. "
    "At the same time, he can clearly and distinctly conceive of body as something purely extended in space, without any thought. "
    "Since whatever he can clearly and distinctly understand apart can, at least by God's power, exist apart, mind and body must be two really distinct substances. "
    "The mind is a thinking, non-extended thing, and the body is an extended, non-thinking thing. "
    "He adds a supporting argument from divisibility: the body, like everything extended, can be divided into parts, whereas the mind cannot. "
    "This is because it is the same single 'I' that wills, understands and perceives, and a thing cannot be both divisible and indivisible.", former_arg=cogito)
    print(dualism)
