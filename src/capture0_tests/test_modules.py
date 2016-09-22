import unittest


class TestModules(unittest.TestCase):

    def test_import(self):
        from capture0.main import home_page
        assert home_page

    def test_import(self):
        import capture0_static
        assert capture0_static


if __name__ == "__main__":
    unittest.main()
