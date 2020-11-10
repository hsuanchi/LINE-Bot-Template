import os

from dotenv import load_dotenv

from bot import create_app

dotenv_path = os.path.join(os.path.dirname(__file__), ".flaskenv")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path, override=True)


app = create_app()


@app.cli.command()
def test():
    import sys
    import unittest

    tests = unittest.TestLoader().discover("tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.errors or result.failures:
        sys.exit(1)
