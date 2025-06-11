import os
from dotenv import load_dotenv


class Config:

    def __init__(self):
        env_path = '/home/michael/git/video_game_diary/.env'
        load_dotenv(env_path, override=True)

        # API
        self.TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
        self.TRELLO_API_SECRET = os.getenv("TRELLO_API_SECRET")
        self.TRELLO_API_TOKEN = os.getenv("TRELLO_API_TOKEN")
        self.TRELLO_API_ENDPOINT = "https://api.trello.com/1/webhooks"

        # Webhooks
        self.TRELLO_WEBHOOK_SECRET = os.getenv("TRELLO_WEBHOOK_SECRET")
        self.TRELLO_WEBHOOK_CALLBACK = os.getenv("TRELLO_WEBHOOK_CALLBACK")

        # Boards
        self.TRELLO_BOARD_ID_GAMING = os.getenv("TRELLO_BOARD_ID_GAMING")

        # Lists
        self.TRELLO_LIST_STAGING_ID = os.getenv("TRELLO_LIST_STAGING_ID")
        self.TRELLO_LIST_TRIMUI_TO_PLAY_ID = os.getenv("TRELLO_LIST_TRIMUI_TO_PLAY_ID")
        self.TRELLO_LIST_RETROID_TO_PLAY_ID = os.getenv("TRELLO_LIST_RETROID_TO_PLAY_ID")
        self.TRELLO_LIST_ARCADE_TO_PLAY_ID = os.getenv("TRELLO_LIST_ARCADE_TO_PLAY_ID")
        self.TRELLO_LIST_MODERN_TO_PLAY_ID = os.getenv("TRELLO_LIST_MODERN_TO_PLAY_ID")
        self.TRELLO_LIST_PLAYING_ID = os.getenv("TRELLO_LIST_PLAYING_ID")
        self.TRELLO_LIST_PLAYED_ID = os.getenv("TRELLO_LIST_PLAYED_ID")
        self.TRELLO_LIST_COMPLETED_ID = os.getenv("TRELLO_LIST_COMPLETED_ID")

        # Map Device to List ID for sorting
        self.DEVICE_TO_LIST_ID = {
            # List Devices
            "Trimui Brick": self.TRELLO_LIST_TRIMUI_TO_PLAY_ID,
            "Retroid Pocket 5": self.TRELLO_LIST_RETROID_TO_PLAY_ID,
            "Arcade": self.TRELLO_LIST_ARCADE_TO_PLAY_ID,
            "Modern Consoles": self.TRELLO_LIST_MODERN_TO_PLAY_ID,
            # Devices for Trimui Brick
            "DOS": self.TRELLO_LIST_TRIMUI_TO_PLAY_ID,
            "NES": self.TRELLO_LIST_TRIMUI_TO_PLAY_ID,
            "SNES": self.TRELLO_LIST_TRIMUI_TO_PLAY_ID,
            "GB": self.TRELLO_LIST_TRIMUI_TO_PLAY_ID,
            "GBC": self.TRELLO_LIST_TRIMUI_TO_PLAY_ID,
            "GBA": self.TRELLO_LIST_TRIMUI_TO_PLAY_ID,
            "PS1": self.TRELLO_LIST_TRIMUI_TO_PLAY_ID,
            # Devices for Retroid Pocket 5
            "N64": self.TRELLO_LIST_RETROID_TO_PLAY_ID,
            "Xbox": self.TRELLO_LIST_RETROID_TO_PLAY_ID,
            "PS2": self.TRELLO_LIST_RETROID_TO_PLAY_ID,
            "GC": self.TRELLO_LIST_RETROID_TO_PLAY_ID,
            # Modern Systems - etc
            "PS3": self.TRELLO_LIST_MODERN_TO_PLAY_ID,
            "PS4": self.TRELLO_LIST_MODERN_TO_PLAY_ID,
            "PS5": self.TRELLO_LIST_MODERN_TO_PLAY_ID,
            "PC": self.TRELLO_LIST_MODERN_TO_PLAY_ID,
            "Xbox 360": self.TRELLO_LIST_MODERN_TO_PLAY_ID,
            "Xbox Series X": self.TRELLO_LIST_MODERN_TO_PLAY_ID,
        }
