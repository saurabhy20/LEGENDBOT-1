import os

from typing import Set

from telethon.tl.types import ChatBannedRights

from validators.url import url

class Config(object):

    LOGGER = True

    # MUST NEEDED VARS

    # set this value with your name

    ALIVE_NAME = os.environ.get("SHAHID DON", None)

    AUTONAME = os.environ.get("SHAHID DON", None)

    # Get the values for following 2 from my.telegra>

    APP_ID = int(os.environ.get("21037364", 6))

    API_HASH = os.environ.get("5968b33e9b46440617378380668e0de2") or None

    # Datbase url heroku sets it automatically else >

    DB_URI = os.environ.get("DATABASE_URL", None)

    # Get this value by running python3 stringsetup.>

    LEGEND_STRING = os.environ.get("1AZWarzwBu3wP_LBLqecA6eq0K6G0qRA5JaYyFDuE-dp5UE8jVYR0hVCpEq7achjkRZrL-GP6gNMfzaH3ozbA1aMHY9FwxUzTURRoXJUXgFfFKDQ4FB5qLvMx611atnjSdyrdT7GNwpKU76sx5Eh2wTEoQ9f5W92TBFbpj7nlcg1pZoXD8vrq1eZTkmFnBKQZkYXej4qbmCH3SPHmgmYORAlHQ1k4MFXZnZxyovzUa4a-dpbxXcrIQVjHsUhHwbeSUJ9pH5q-Ye0ahPkcwbqvKcjkSIeId46oZso8xzYNTDL1XIUO0b6Jkja-xei8VH_DkuyzzAjoP_KDfsulOwMAFNBykWsoDqc=", >

    # Telegram BOT Token and bot username from @BotF>

    BOT_TOKEN = os.environ.get("6167734236:AAFNK8tVKFY6egBPRdR1F2S5I4W96ri2ApY") or os.en>

    BOT_USERNAME = shahiddon_bot

    # get this value from http://www.timezoneconvert>

    TZ = os.environ.get("TZ", "Asia/Kolkata")
