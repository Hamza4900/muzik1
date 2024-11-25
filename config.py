import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID","28503231"))
API_HASH = getenv("API_HASH","3f4f8597a1a8cfdd975eec20278c28b6")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","6037979897:AAFZM6xeUC8BgzbBSP-y_sADxjavz-IcSOA")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://Kingbrukh:kingkhan@kingbruh.ra3pjgm.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 360))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002028213552"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7784476491))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Hamza4900/muzik1",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/askkoleji")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/konnusanlar")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "AgCqQv7ajablJYlexNyCtCoFDFgjabVuJlPxZWGe5fciyg5X1Q7568P5kc3NAnO8gLmbyqWndX8g5bzTmopKH-6wtsZu4dwH5vYFeZ94iK8Hu3kc9MbtxrR4wfrm4Ks-U7OlYFrVDKyYUNqSlatXCY5GKzwq3qsQ6-YnIJ5XshsS0Jv6hukbeA_4BrEOZIyjo97AbfjvrxDWZnJ4w1paxiIUurAMM41CIJVK-dd-6HTxmOHudMoHOo9m4qq-Yy74iiTIU0m4msvlY7YlcmVAA2JQ81JyaJhwxv1XQPhvr-aUsordeqryT2vaiCAZ_rA2peG-9HJttqyAr2QeAt6eZTAAAAAc2wA6oA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/Yeni-11-29"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/Yeni-11-29"
)
PLAYLIST_IMG_URL = "https://telegra.ph/Eski-11-29"
STATS_IMG_URL = "https://telegra.ph/Eski-11-29"
TELEGRAM_AUDIO_URL = "https://telegra.ph/Eski-11-29"
TELEGRAM_VIDEO_URL = "https://telegra.ph/Eski-11-29"
STREAM_IMG_URL = "https://telegra.ph/Eski-11-29"
SOUNCLOUD_IMG_URL = "https://telegra.ph/Eski-11-29"
YOUTUBE_IMG_URL = "https://telegra.ph/Eski-11-29"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/Eski-11-29"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/Eski-11-29"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/Eski-11-29"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
