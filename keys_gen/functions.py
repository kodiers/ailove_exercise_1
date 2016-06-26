import random
from .models import Keys


SYMBOLS = '1 2 3 4 5 6 7 8 9 0 Q W E R T Y U I O P A S D F G H J K L Z X C V B N M q w e r t y u i o p a s d f g h j k l z x c v b n m'


def generate_random_string(symbols, length):
    """
    Generate string from symbols.
    :param symbols: String of symbols divided by space.
    :param length: Length of generated string
    :return: String
    """
    sym_list = symbols.split()
    str_list = random.sample(sym_list, length)
    gen_string = ''.join(str_list)
    return gen_string


def create_random_key():
    """
    Create unique key object.
    :return: Keys object
    """
    key_obj = None
    key = generate_random_string(SYMBOLS, 4)
    try:
        key_obj = Keys.objects.create(key=key)
    except Exception:
        key_obj = create_random_key()
    return key_obj