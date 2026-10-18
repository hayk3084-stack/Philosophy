class Philosopher:

    def __init__(self, name, country, birth_year, death_year, school, catch_phrase):  # constructor
        self.__name = name
        self.__country = country
        self.__birth_year = birth_year
        self.__death_year = death_year
        self.__school = school
        self.__catch_phrase = catch_phrase

    def philosophy_it(self):
        return f"As {self.__name} from {self.__country} always says: {self.__catch_phrase}"

    def __str__(self):
        return f"{self.__name} from the school {self.__school}"


if __name__ == "__main__":
    descartes = Philosopher("René Descartes", "France", 1596, 1650, "Rationalism", "I think therefore I am")
    print(descartes)
