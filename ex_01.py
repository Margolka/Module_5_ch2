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

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.mail}"


# using Faker to create data for monkeys (allmost like humans) ;)
monkey_list = []
for _ in range(4):
    monkey_list.append(
        Human(
            first_name=monkey.first_name(),
            last_name=monkey.last_name(),
            firm=monkey.company(),
            position=monkey.job(),
            mail=monkey.email(),
        )
    )

[print(monkeys) for monkeys in monkey_list]

print("=== Sorted by first name ===")
by_first_name = sorted(monkey_list, key=lambda monkey: monkey.first_name)
[print(monkeys) for monkeys in by_first_name]

print("=== Sorted by last name ===")
by_last_name = sorted(monkey_list, key=lambda monkey: monkey.last_name)
[print(monkeys) for monkeys in by_last_name]

print("=== Sorted by e-mail ===")
by_mail = sorted(monkey_list, key=lambda monkey: monkey.mail)
[print(monkeys) for monkeys in by_mail]
