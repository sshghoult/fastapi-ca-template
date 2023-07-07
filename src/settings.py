from os import environ

EXAMPLE = environ.get("EXAMPLE_ENV_VARIABLE", "default")
DEBUG = environ.get("DEBUG", "False") == "True"

STAGE = environ.get("STAGE", "LOCAL")
if STAGE not in ("LOCAL", "TEST", "PRODUCTION"):
    raise ValueError
