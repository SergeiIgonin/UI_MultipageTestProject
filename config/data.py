import faker, time


class Data:
    # EMAIL = "sergei3_ia@fakemail.com"
    # PASSWORD = "Sergei3!@#D7JkN"

    f = faker.Faker()
    EMAIL = f.email()
    PASSWORD = f.password()

    # EMAIL = str(time.time()) + "@fakemail.org"
    # PASSWORD = str(time.time()) + "Qw!"
