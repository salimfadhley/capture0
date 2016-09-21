import unittest


class TestModules(unittest.TestCase):
    def test_import(self):
        from capture0.main import hello_world
        assert (hello_world)


if __name__ == "__main__":
    unittest.main()
