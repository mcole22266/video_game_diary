# Video Game Diary

My personal tool for managing my video game backlog and tracking my gaming journey through time.

## Overview

This project helps me organize and automate my video game collection through Trello. It's specifically designed to maintain my "Gaming Through Time" board, where I track games chronologically from the early days of gaming to modern releases.

## Setup

### Environment Configuration

The `.env` file needs to contain Trello credentials:

```
# API
TRELLO_API_KEY=XXX
TRELLO_API_SECRET=XXX
TRELLO_API_TOKEN=XXX

# Boards
TRELLO_BOARD_ID_GAMING=XXX

# Lists
TRELLO_LIST_STAGING_ID=XXX
TRELLO_LIST_TRIMUI_TO_PLAY_ID=XXX
TRELLO_LIST_RETROID_TO_PLAY_ID=XXX
TRELLO_LIST_ARCADE_TO_PLAY_ID=XXX
TRELLO_LIST_MODERN_TO_PLAY_ID=XXX
TRELLO_LIST_PLAYING_ID=XXX
TRELLO_LIST_PLAYED_ID=XXX
TRELLO_LIST_COMPLETED_ID=XXX
```

## Scripts

| Script | Purpose |
|--------|---------|
| `makeBackups.py` | Pulls all lists and cards from Trello Board and stores in JSON _- in two files. More details below_ |
| `updateTrelloCards.py` | Updates the name, description, and which list to be placed of all Trello Cards based on `board_data.json` |

## Resources

The `resources` directory contains JSON files with my structured game data:
- `board_data_raw.json`: The raw JSON output of fetching the Trello Board
- `board_data.json`: Specific attributes both pulled from raw and computed in a JSON format. This is used in `updateTrelloCards.py` to inform the script how to update the cards

## Project Purpose

This is my personal tool for managing my extensive video game backlog. As I work through games from different eras, this helps me:

1. Track my progress through gaming history in my "Gaming Through Time" Trello board
2. Organize games by platform, release date, and completion status
3. Maintain details about each game including which of my devices is best suited for playing them:
   - Trimui Brick (for retro games without analog controls)
   - Retroid Pocket 5 (for games up to PS2/GameCube era)
   - Modern Consoles (for newer games)
   - Arcade (for arcade-style games)

This automation saves me time managing my collection and helps me decide what to play next on my gaming journey.
