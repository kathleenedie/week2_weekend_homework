class Guest:

    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def guest_has_entry_fee(self, room, guest):
        if room.entry_fee <= self.wallet:
            return "Yes, warbling for me"
        else:
            return "Singing in the shower tonight"