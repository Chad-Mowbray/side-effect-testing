import unittest
from guesser import Guesser


class TestGuesser(unittest.TestCase):
    
    def test_game_over(self):
        g = Guesser()
        g.guesses = [1,2,3,4]
        is_over = g.is_game_over()
        self.assertTrue(is_over)
    
    def test_valid_input(self):
        g = Guesser()
        with self.assertRaises(ValueError):
            g.validate_input("ee")
        self.assertEqual(g.validate_input("3"), 3)
        
    def test_get_input(self):
        g = Guesser()
        inp = g.get_input("hi", lambda x: "there")
        self.assertEqual(inp, "there")
        
    def test_display(self):
        g = Guesser()
        msg = g.display_msg("hi", lambda x: x)
        self.assertEqual(msg, "hi")
        
if __name__ == "__main__":
    unittest.main()