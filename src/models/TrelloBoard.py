import requests
from config import Config


class TrelloBoard:
    """
    Object Model for a Trello Board providing Private and Public Methods for interacting
    with the Trello REST API
    """
    def __init__(self):
        config = Config()
        self.api_key = config.TRELLO_API_KEY
        self.token = config.TRELLO_API_TOKEN
        self.secret = config.TRELLO_API_SECRET
        self.board_id = config.TRELLO_BOARD_ID_GAMING
        self.base_url = "https://api.trello.com/1"

    def _build_params(self, params=None):
        """
        Private Method for building the parameters for the Trello API
        """
        if params is None:
            params = {}
        params.update({
            'key': self.api_key,
            'token': self.token
        })
        return params

    def _handle_response(self, response):
        """
        Private Method for handling the response from the Trello API
        """
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.text}")
            response.raise_for_status()

    def _get(self, endpoint, params=None):
        """
        Private Method for a GET Request on the Trello Board
        """
        params = self._build_params()
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        return self._handle_response(response)

    def _put(self, endpoint, data=None):
        """
        Private Method for a PUT Request on the Trello Board
        """
        params = self._build_params()
        response = requests.put(f"{self.base_url}{endpoint}", params=params, data=data)
        return self._handle_response(response)

    def _post(self, endpoint, data=None):
        """
        Private Method for a POST Request on the Trello Board
        """
        params = self._build_params()
        response = requests.post(f"{self.base_url}{endpoint}", params=params, data=data)
        return self._handle_response(response)

    def get_board(self):
        """
        Fetch all Card Data from the Trello Board
        """
        board_data = {}
        lists = self.get_lists()
        for list_data in lists:
            list_id = list_data['id']
            list_name = list_data['name']
            print(f"Fetching cards in list {list_name}")
            cards = self.get_cards_in_list(list_id)
            board_data[list_name] = cards

        return board_data

    def get_card(self, card_id):
        """
        Get a specific card's data
        """
        endpoint = f"/cards/{card_id}"
        return self._get(endpoint)

    def update_card_name(self, card_id, new_name):
        """
        Update the name of a Trello Card
        """
        endpoint = f"/cards/{card_id}/name"
        data = {'value': new_name}
        return self._put(endpoint, data)

    def update_card_desc(self, card_id, new_desc):
        """
        Update the description of a Trello Card
        """
        endpoint = f"/cards/{card_id}/desc"
        data = {'value': new_desc}
        return self._put(endpoint, data)

    def move_card_to_list(self, card_id, list_id):
        """
        Move a Trello Card to a specific list
        """
        endpoint = f"/cards/{card_id}/idList"
        data = {'value': list_id}
        return self._put(endpoint, data)

    def get_lists(self):
        """
        Get all lists in a board
        """
        endpoint = f"/boards/{self.board_id}/lists"
        return self._get(endpoint)

    def get_cards_in_list(self, list_id):
        """
        Get all cards in a list
        """
        endpoint = f"/lists/{list_id}/cards"
        return self._get(endpoint)
