from contextlib import contextmanager
import logging


def my_function():
    logging.debug("debug")
    logging.error("warn")


@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)

    try:
        yield
    finally:
        logger.setLevel(old_level)


with debug_logging(logging.DEBUG):
    print("inside")
    my_function()

print("after")
my_function()
