import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i}", "Category", "Director", 90, 10.0)
            self.assertTrue(cart.add_dvd(dvd))
        
        overflow_dvd = DigitalVideoDisc("DVD 21", "Category", "Director", 90, 10.0)
        self.assertFalse(cart.add_dvd(overflow_dvd))

if __name__ == "__main__":
    unittest.main()
