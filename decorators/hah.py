def mult_elem():
    """kek"""
    mult = 2
    def we():
        def need():
            def to_go():
                def deeper():
                    return lambda n: n * mult
                return deeper
            return to_go
        return need
    return we


def test_cases(data: dict) -> None:
    """Тест кейсы."""
    for args, expected in data.items():
        assert mult_elem()()()()()(args) == expected


def main() -> None:
    data: dict = {
        3: 6,
        0: 0,
        -5: -10,
        10: 20,
        'spam': 'spamspam',
    }
    test_cases(data)


if __name__ == '__main__':
    main()
