import pygame,os,random

class Music:
    def __init__(self):
        self.music_amplitude = 0.5
        self.__load_tracks()
    def __play(self):
        pygame.mixer.music.load(self.track)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.music_amplitude)
    def __load_tracks(self):
        self.mp3_files = []
        for root, dirs, files in os.walk("music"):
            for file in files:
                if file.endswith(".mp3"):
                    self.mp3_files.append(os.path.join(root, file))
    def choose_track(self):
        self.track = random.choice(self.mp3_files)
        self.__play()
    def vol_up(self):
        current_vol = pygame.mixer.music.get_volume()
        if current_vol < 1.0:
            pygame.mixer.music.set_volume(min(1.0,current_vol + 0.1))
    def vol_down(self):
        current_vol = pygame.mixer.music.get_volume()
        if current_vol > 0.0:
            pygame.mixer.music.set_volume(max(0.0,current_vol - 0.1))
