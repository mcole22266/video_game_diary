# Updates the Trello Cards such that games are organized placed in their
# respective lists and various details are updated
import os
import json
from dotenv import load_dotenv
from models.TrelloBoard import TrelloBoard

load_dotenv()

# Map Device to List ID for sorting
DEVICE_TO_LIST_ID = {
    "Trimui Brick": os.getenv("TRELLO_LIST_TRIMUI_TO_PLAY_ID"),
    "Retroid Pocket 5": os.getenv("TRELLO_LIST_RETROID_TO_PLAY_ID"),
    "Modern Consoles": os.getenv("TRELLO_LIST_MODERN_TO_PLAY_ID"),
    "Arcade": os.getenv("TRELLO_LIST_ARCADE_TO_PLAY_ID")
}


def main():
    board = TrelloBoard()

    # Read Board Data in
    with open("./resources/board_data.json", "r") as f:
        boardData = json.load(f)

    for lst, card in boardData.items():
        print(f"Updating {len(lst)} cards in list {lst}")
        for name, data in card.items():
            currentCard = board.get_card(data.get("CardId"))
            cardId = data.get("CardId")
            description = data.get("Description", "")

            # Find the List to place the item in
            device = data["Device"]
            target_list_id = DEVICE_TO_LIST_ID.get(device)
            if not target_list_id:
                print(f"Skipping card '{name}' due to Unknown device '{device}'")
                continue

            # Update the Card
            # - Name
            if currentCard.get("name", "") != name:
                print(f"Updating card {currentCard.get('name', '')} Name to {name}")
                board.update_card_name(cardId, name)
            # - Description
            if currentCard.get("desc", "") != description:
                print(f"Updating card {currentCard.get('name', '')} Description to {description}")
                board.update_card_desc(cardId, description)
            # - List
            if currentCard.get("idList", "") != target_list_id:
                # We only want to move the item if it's not Playing, Completed, or Played Lists
                if currentCard.get("idList", "") not in [
                    os.getenv("TRELLO_LIST_PLAYING_ID"),
                    os.getenv("TRELLO_LIST_COMPLETED_ID"),
                    os.getenv("TRELLO_LIST_PLAYED_ID")
                ]:
                    print(f"Updating card {currentCard.get('name', '')} List to {target_list_id}")
                    board.move_card_to_list(cardId, target_list_id)


if __name__ == "__main__":
    main()
