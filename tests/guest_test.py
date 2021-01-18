import unittest

from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Yeller Young", 25.00, "The Chain")
        self.guest_2 = Guest("Tuneful Tina", 32.00, "Dancing Queen")
        self.guest_3 = Guest("Metal Mickey", 10.00, "Enter Sandman")
        self.room_1 = Room("Party Palace", 10, 6.00)
        self.room_2 = Room("Cosy Coop", 2, 14.00)
    
    def test_guest_has_name(self):
        self.assertEqual("Yeller Young", self.guest_1.name)

    def test_guest_wallet_amount(self):
        self.assertEqual(32.00, self.guest_2.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Enter Sandman", self.guest_3.favourite_song)

    def test_guest_has_entry_fee(self):
        self.assertEqual("Yes, warbling for me", self.guest_1.guest_has_entry_fee(self.room_1, self.guest_1))
    
    