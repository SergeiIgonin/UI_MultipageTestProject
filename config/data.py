import faker


class Data:

    f = faker.Faker()
    EMAIL = f.email()
    PASSWORD = f.password()
