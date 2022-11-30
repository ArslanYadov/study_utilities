class Human:
    """Класс человека."""
    def __init__(
        self, fname: str = None,
        lname: str = None,
        age: int = 0
    ) -> None:
        self.fname = fname
        self.lname = lname
        self.age = age

    def get_full_name(self) -> str:
        """Получить полное имя."""
        return self.fname + ' ' + self.lname
    
    def __repr__(self) -> str:
        return 'My name is {}. I\'m {} y.o.'.format(
            self.get_full_name(), self.age
        )
