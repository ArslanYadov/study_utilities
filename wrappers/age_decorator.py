def throw_age(method):
    def wrapper(self):
        new_age = self.age
        new_age -= 3
        return new_age
    return wrapper
