from playlist import Playlist

class Song:
    def __init__(self,title:str,releaseData:str,artist:str):
        self.title = title
        self.releaseData = releaseData
        self.artist = artist

    def getTitle(self):
        return self.title
    def getArtist(self):
        return self.artist

song_one = Song('Title of Song One', '10/10/2024','Mila')
song_two = Song('Title of Song Two', '1/12/2020','Mehrin')
song_three = Song('Title of Song Three', '2/06/1980','Kishor')

collectionOne:list[Song] = [song_one,song_two,song_three]

playListOne = Playlist(songs=collectionOne)


for s in playListOne.getSongs():
    print(f"Title: {s.title}")
    print(f"Artist: {s.artist}")