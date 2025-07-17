#interface class Practice
from abc import ABC, abstractmethod

class Playable(ABC):
    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def pause(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class MediaInfo(ABC):
    @abstractmethod
    def get_title(self):
        pass
    
    @abstractmethod
    def get_duration(self):
        pass
    
    @abstractmethod
    def get_info(self):
        pass
def duration_converter(duration):
    # Convert duration to a more readable format (e.g., minutes:seconds)
    minutes = duration // 60
    seconds = (duration % 60) 
    return f"{minutes}:{seconds:02}"  # Return the duration in minutes and seconds format with seconds as 2 digits

# Create implementations
class Song(Playable, MediaInfo):
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    def play(self):
        return f"Playing song: {self.title}"
    def pause(self):
        return f"Paused song: {self.title}"
    def stop(self):
        return f"Stopped song: {self.title}"
    def get_title(self):
        return self.title
    def get_duration(self):
        return self.duration
    def get_info(self):
        return f"Song: {self.title} by {self.artist} ({duration_converter(self.duration)})"

class Video(Playable, MediaInfo):
    def __init__(self, title, resolution, duration):
        self.title = title
        self.resolution = resolution
        self.duration = duration
    def play(self):
        return f"Playing video: {self.title}"
    def pause(self):
        return f"Paused video: {self.title}"
    def stop(self):
        return f"Stopped video: {self.title}"
    def get_title(self):
        return self.title
    def get_duration(self):
        return self.duration
    def get_info(self):
        return f"Video: {self.title} ({self.resolution}) ({duration_converter(self.duration)})"

# Create the media player
class MediaPlayer:
    def __init__(self):
        self.current_media = None
    def set_media(self, media):
        self.current_media = media
    def play(self):
        return self.current_media.play()
    def pause(self):
        return self.current_media.pause()
    def stop(self):
        return self.current_media.stop()
    

# Test your implementation - DO NOT MODIFY THIS TEST CODE
song = Song("Bohemian Rhapsody", "Queen", 355)
video = Video("Python Tutorial", "1080p", 1800)
player = MediaPlayer()

# Test with song
player.set_media(song)
print(player.current_media.get_info())
print(player.play())
print(player.pause())
print(player.stop())
print()  # Empty line for readability

# Test with video
player.set_media(video)
print(player.current_media.get_info())
print(player.play())
print(player.pause())
print(player.stop())