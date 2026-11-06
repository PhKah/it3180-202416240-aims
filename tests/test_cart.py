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

        def test_total_cost_with_discount(self):
            cart = Cart()
            dvd = DigitalVideoDisc("DVD 1", "Category", "Director", 90, 100.0)
            cart.add_dvd(dvd)
            
            self.assertEqual(cart.total_cost_with_discount(20), 80.0)
            
            with self.assertRaises(ValueError):
                cart.total_cost_with_discount(150)
    
    def test_sort_by_title(self):
        cart = Cart()
        d1 = DigitalVideoDisc("B Title", "Cat", "Dir", 90, 20.0)
        d2 = DigitalVideoDisc("A Title", "Cat", "Dir", 90, 10.0)
        cart.add_dvd(d1)
        cart.add_dvd(d2)
        cart.sort_by_title()
        self.assertEqual(cart.items[0].title, "A Title")

    def test_sort_by_cost(self):
        cart = Cart()
        d1 = DigitalVideoDisc("DVD 1", "Cat", "Dir", 90, 10.0)
        d2 = DigitalVideoDisc("DVD 2", "Cat", "Dir", 90, 50.0)
        cart.add_dvd(d1)
        cart.add_dvd(d2)
        cart.sort_by_cost()
        self.assertEqual(cart.items[0].cost, 50.0)
if __name__ == "__main__":
    unittest.main()
