from base_class.human import Human

def throw_age(method):
    """Декоратор уменьшает возраст для метода класса."""
    def wrapper(self):
        new_age = self.age
        new_age -= 3
        return new_age
    return wrapper


class Woman(Human):
    """Класс женщины."""
    def __init__(self, fname, lname, age, sex='Female') -> None:
        super().__init__(fname, lname, age)
        self.sex = sex

    @throw_age
    def lie_about_age(self):
        return self.age

    def __repr__(self) -> str:
        super().__repr__()
        return 'My name is {}. I\'m {} y.o.. Sex: {}.'.format(
            self.get_full_name(), self.age, self.sex
        )


def test() -> None:
    """Тесты."""
    em = Woman('Elena', 'Muntyanu', 29)
    assert em.__repr__() == 'My name is Elena Muntyanu. I\'m 29 y.o.. Sex: Female.'
    assert em.lie_about_age() == 26
    assert em.age != 26

if __name__ == '__main__':
    test()
