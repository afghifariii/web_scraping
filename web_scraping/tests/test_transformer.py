import unittest
from web_scraping import transformer


class TestTransformer(unittest.TestCase):
    def test_is_money_miliar_when_string_money_contains_miliar(self):
        string_money = "35.5 miliar"
        actual = transformer.is_money_miliar(string_money)

        self.assertTrue(string_money)
    
    
    def test_is_money_miliar_when_string_money_not_contains_miliar(self):
        string_money = "980 juta"
        actual = transformer.is_money_miliar(string_money)

        self.assertFalse(actual)
    
    
    def test_transform_money_format_when_money_is_juta(self):
        string_money = "980 Juta"
        actual = transformer.transform_money_format(string_money)

        self.assertEqual(actual, "980")
    

    def test_transform_money_format_when_money_is_miliar(self):
        string_money = "35.5 miliar"
        actual = transformer.transform_money_format(string_money)

        self.assertEqual(actual, "35.5")
    

    def test_transform_money_format_when_money_contains_comma(self):
        string_money = "35,5 miliar"
        actual = transformer.transform_money_format(string_money)

        self.assertEqual(actual, "35.5")


if __name__ == "__main__":
    unittest.main()