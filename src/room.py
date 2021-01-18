class Room:

    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.playlist = []

    def check_in_guests(self, guest):
        self.guests.append(guest)

    def check_out_guests(self, guest):
        self.guests.remove(guest)

    def add_songs_to_playlist(self, song):
        self.playlist.append(song)
        print(self.playlist)
    
    def check_capacity_for_guests(self, room_name):
        if self.capacity >= len(self.guests):
            return "Come on in!"
        else:
            return "Sorry, too many here!"
    
    # def guest_favourite_song_in_playlist(self, guest):
    #         if self.playlist [0] == guest.favourite_song:
    #             return "Whoo hoo!"
    #         else:
    #             return "It's just ok"

    # def guest_favourite_song_in_playlist(self, guest):
    #     for play in self.playlist:
    #         if guest.favourite_song in self.playlist:
    #             return "whoo hoo!"
    #         else: 
    #             return "It's just ok"
    
    # def guest_favourite_song_in_playlist(self, guest):
    #     for play in self.playlist:
    #         if guest in self.playlist:
    #             return "whoo hoo!"
    #         else: 
    #             return "It's just ok"
    
    def guest_favourite_song_in_playlist(self, guest):
        for song in self.playlist:
            if guest.favourite_song in song.title:
                return "Whoo hoo!"
        else: 
            return "It's just ok"