import unittest

from src.room import Room
from src.guest import Guest
from src.songs import Songs

class TestRoom (unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Party Palace", 10, 6.00)
        self.room_2 = Room("Cosy Coop", 2, 14.00)
        self.guest_1 = Guest("Yeller Young", 25.00, "The Chain")
        self.guest_2 = Guest("Tuneful Tina", 32.00, "Dancing Queen")
        self.guest_3 = Guest("Metal Mickey", 10.00, "Enter Sandman")
        self.song_1 = Songs("The Chain", "Fleetwood Mac")
        self.song_2 = Songs("Club Tropicana", "Wham!")
        self.song_3 = Songs("Wind of Change", "Scorpion")
    
    def test_room_has_name(self):
        self.assertEqual("Party Palace", self.room_1.name)

    def test_room_capacity(self):
        self.assertEqual(2, self.room_2.capacity)

    def test_room_entry_fee(self):
        self.assertEqual(6.00, self.room_1.entry_fee)

    def test_room_check_in_guests(self):
        self.room_1.check_in_guests(self.guest_1)
        self.room_1.check_in_guests(self.guest_2)
        self.assertEqual(2, len(self.room_1.guests))
    
    def test_room_check_in_out_guests(self):
        self.room_1.check_in_guests(self.guest_1)
        self.room_1.check_in_guests(self.guest_2)
        self.room_1.check_in_guests(self.guest_3)
        self.room_1.check_out_guests(self.guest_1)
        self.assertEqual(2, len(self.room_1.guests))

    def test_room_playlist_song_number(self):
        self.room_1.add_songs_to_playlist(self.song_1)
        self.room_1.add_songs_to_playlist(self.song_2)
        self.room_1.add_songs_to_playlist(self.song_3)
        self.assertEqual(3, len(self.room_1.playlist))

    def test_room_capacity_for_guest_yes(self):
        self.room_1.check_in_guests(self.guest_1)
        self.room_1.check_in_guests(self.guest_2)
        self.assertEqual("Come on in!", self.room_1.check_capacity_for_guests(self.room_1))

    def test_room_capacity_for_guest_no(self):
        self.room_2.check_in_guests(self.guest_1)
        self.room_2.check_in_guests(self.guest_2)
        self.room_2.check_in_guests(self.guest_3)
        self.assertEqual("Sorry, too many here!", self.room_2.check_capacity_for_guests(self.room_2))

    # def test_guest_favourite_song_in_playlist_yes(self):
    #     self.room_1.add_songs_to_playlist(self.song_1)
    #     self.room_1.add_songs_to_playlist(self.song_2)
    #     self.assertEqual("Whoo hoo!", self.room_1.guest_favourite_song_in_playlist(self.guest_1))

    def test_guest_favourite_song_in_playlist_yes(self):
        self.room_1.add_songs_to_playlist(self.song_1)
        self.room_1.add_songs_to_playlist(self.song_2)
        self.assertEqual("Whoo hoo!", self.room_1.guest_favourite_song_in_playlist(self.guest_1))