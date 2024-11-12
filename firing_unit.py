import ctypes
import os
import platform

# check OS and load library (RNG)
if platform.system() == 'Windows':
    lib = ctypes.CDLL(os.path.abspath("rng_models/libmtrand.dll"))
else:
    lib = ctypes.CDLL(os.path.abspath("rng_models/libmtrand.so")) 

# specify return types
lib.initialise_random.restype = None
lib.get_random_value.restype = ctypes.c_double

# initialise the random number generator
lib.initialise_random()


def simulate_engagement(pk: int) -> bool:
    """Generates random number from a uniform distribution,
    using the c library for the Mersenne Twister random number generator.
    Checks if this number is less than or equal to the Pk. Returns Boolean.

    :param pk: Probability of kill.
    :type pk: int
    :return: Whether the random number generated is larger or equal to the Pk.
    :rtype: bool
    """
    # calls RNG c function.
    random_value = lib.get_random_value()
    return random_value <= pk
