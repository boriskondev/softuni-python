class NameTooShortError(Exception):
    def __init__(self, message):
        self.message = message


class MustContainAtSymbolError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidDomainError(Exception):
    def __init__(self, message):
        self.message = message


domains = ["com", "bg", "org", "net"]

while True:
    email = input()
    if email == "End":
        break
    if "@" in email:
        name, host_and_domain = email.split("@")
        domain = host_and_domain.split(".")[1]
        if len(name) < 4:
            raise NameTooShortError("Name must be more than 4 characters")
        elif domain not in domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        else:
            print("Email is valid")
    else:
        raise MustContainAtSymbolError("Email must contain @")
