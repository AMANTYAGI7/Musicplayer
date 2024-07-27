import os
import pygame
from tkinter import Tk, Button, filedialog, messagebox

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x150")

        pygame.mixer.init()

        self.playlist = []
        self.current_song_index = 0
        self.paused = False

        Button(self.root, text="Select Folder", command=self.load_folder).pack(pady=10)
        Button(self.root, text="Play", command=self.play_music).pack(pady=10)
        Button(self.root, text="Pause/Unpause", command=self.pause_unpause_music).pack(pady=10)
        Button(self.root, text="Stop", command=self.stop_music).pack(pady=10)

    def load_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            print(f"Selected folder: {folder_path}")
            if os.path.isdir(folder_path):
                self.playlist = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('.mp3', '.wav', '.ogg'))]
                print(f"Playlist: {self.playlist}")
                if self.playlist:
                    self.current_song_index = 0
                    self.play_music()
                else:
                    messagebox.showerror("Error", "No playable music files found in the selected folder.")
            else:
                messagebox.showerror("Error", "Invalid folder path.")

    def play_music(self):
        if self.playlist:
            try:
                print(f"Playing: {self.playlist[self.current_song_index]}")
                pygame.mixer.music.load(self.playlist[self.current_song_index])
                pygame.mixer.music.play()
                self.paused = False
            except pygame.error as e:
                messagebox.showerror("Error", f"Failed to play the selected file: {e}")
                print(f"Failed to play the selected file: {e}")

    def pause_unpause_music(self):
        if self.playlist:
            if self.paused:
                pygame.mixer.music.unpause()
                print("Music unpaused")
            else:
                pygame.mixer.music.pause()
                print("Music paused")
            self.paused = not self.paused

    def stop_music(self):
        if self.playlist:
            pygame.mixer.music.stop()
            print("Music stopped")

if __name__ == "__main__":
    root = Tk()
    app = MusicPlayer(root)
    root.mainloop()

