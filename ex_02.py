from faker import Faker

monkey = Faker("pl_PL")


class Human:
    def __init__(self, first_name, last_name, firm, position, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.firm = firm
        self.position = position
        self.mail = mail
        pass

        # Variables
        self._length = 0

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.mail}"

    @property
    def length(self):
        return len(f"{self.first_name} {self.last_name}")

    def contact(self):
        return f"Kontaktuj się z {self.first_name} {self.last_name} {self.position} {self.mail}- długość {self.length}"


monkey_01 = Human(
    first_name=monkey.first_name(),
    last_name=monkey.last_name(),
    firm=monkey.company(),
    position=monkey.job(),
    mail=monkey.email(),
)
print(monkey_01.contact())
