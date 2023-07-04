import os


class Config:
    API_ID = 27885485  # Change 12345 to your API_ID
    API_HASH = "7dd9974c713787410beae4a295cc1e2d"  # Change None to your API_HASH
    BOT_TOKEN = "6314663611:AAHPIGrhUU5ieN25ujs0pMW1_y9_NGsS4Cg"  # Change None to your BOT_TOKEN
    OWNER_ID = int(os.environ.get("OWNER_ID", 0))  # Change 0 to your OWNER_ID
    OWNER_NAME = os.environ.get("OWNER_NAME", None)  # Change None to your OWNER_NAME

    # For Local Deploys edit above 5 lines.
    # Put your API_ID and OWNER_ID (without comma) and API_HASH,BOT_TOKEN n OWNER_NAME (with commas) below.
    # If got any problem ask in @MysteryBotsChat.
