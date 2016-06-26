import kronos

from .functions import create_random_key


@kronos.register('01 0 * * *')
def generate_keys():
    """
    Cron task used to generate keys at 0:0 o'clock every day.
    """
    for i in range(100):
        create_random_key()

