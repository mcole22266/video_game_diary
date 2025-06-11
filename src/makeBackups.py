# Pulls data from the Trello Board and stores the raw JSON as
# `board_data_raw.json`. Additionally, converts the raw JSON
# board data into only attributes we care about for easy
# viewing/editing/etc

import json
from models.TrelloBoard import TrelloBoard
from config import Config

config = Config()


def main():
    print("Fetching board data")
    board = TrelloBoard()
    board_data = board.get_board()

    print("Writing raw board data to file")
    with open('./resources/board_data_raw.json', 'w') as f:
        json.dump(board_data, f, indent=2)

    print("Converting card data")
    card_data = {}
    for lst, cards in board_data.items():
        print(f"- Cards in {lst}")
        card_data[lst] = {}
        # If the list is one belonging to a device, store the device
        device = ""
        if lst.replace(" - To Play", "") in config.DEVICE_TO_LIST_ID.keys():
            device = lst.split("-")[0].strip()  # Stored as `Device - To Play`
        for card in cards:
            boardId = card.get("idBoard", "")
            cardId = card.get("id", "")
            shortUrl = card.get("shortUrl", "")
            name = card.get("name", "")
            desc = card.get("desc", "")

            # If the name is in the form YYYY-MM-DD - System - Title, extract
            release = ""
            system = ""
            title = ""
            if len(name.split(" - ")) == 3:
                release, system, title = name.split(" - ")
            else:
                title = name

            card_data[lst][name] = {
                "Description": desc,
                "Device": device,
                "BoardId": boardId,
                "CardId": cardId,
                "ShortUrl": shortUrl,
                "Release Date": release.strip(),
                "System": system.strip(),
                "Title": title.strip()
            }
    
    print("Writing card data to file")
    with open('./resources/board_data.json', 'w') as f:
        json.dump(card_data, f, indent=2)


if __name__ == "__main__":
    main()
    print("Done")
