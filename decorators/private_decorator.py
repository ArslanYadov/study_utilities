"""
Декоратор класса.
Делает атрибуты класса, указанные в аргументах декоратора, приватными.

Перегрузка операций вида __x__ все ещё доступна,
т.к. __getattr__ пропускает подобные методы и они ищутся в
декорируемом классе.

__debug__ добавлен для возможности запуска файла
с ключом оптимизации python3 [-O] main.py,
убирая траты на работу декоратора.

Пример использования:

1    @private('name')
2    class Person:
3
4        def __init__(self, name):
5            self.name = name
6
7        def get_name(self):
8            return self.name

Таким образом, из класса Person, экземпляр класса
может получить атрибут name только через метод get_name()

з.ы. либо через расширенное имя класса:
    person._Instance__wrapped.name
"""


def private(*private_attributes):
    def decorator(cls):
        if not __debug__:
            return cls

        class Instance:

            def __init__(self, *args, **kwargs) -> None:
                self.__wrapped = cls(*args, **kwargs)

            def __getattr__(self, name):
                if name in private_attributes:
                    raise TypeError('[{}] is private attribute!'.format(name))

                return getattr(self.__wrapped, name)

            def __setattr__(self, name, value):
                if name == '_Instance__wrapped':
                    self.__dict__[name] = value

                if name in private_attributes:
                    raise TypeError('[{}] is private attribute!'.format(name))

                return setattr(self.__wrapped, name, value)

        return Instance
    return decorator
