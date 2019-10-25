class Simple1Exception(Exception):
    pass


class Simple2Exception(Exception):
    pass


def abc():
    try:
        raise Simple1Exception
    except Simple1Exception as e:
        raise Simple2Exception from e


abc()
