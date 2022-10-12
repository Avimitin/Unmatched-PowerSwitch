WHITELIST_CHAT = []
TOKEN = ""
BOARD_ADDR_ALIAS = {}
DEFAULT_FTDI_ADDR = ""

try:
    import dotenv
    dotenv.load_dotenv()
except ImportError:
    pass

from os import getenv as env
from sys import exit

def load_config() -> None:
    whitelist_chat = env("POWERSWITCH_WHITELIST_CHAT")
    if whitelist_chat is None:
        exit("Please provide a list of chat that have permission to reboot. Set by env `POWERSWITCH_WHITELIST_CHAT`, separate by comma `,`")
    chats = whitelist_chat.split(",")
    whitelist_chat = []
    for c in chats:
        whitelist_chat.append(int(c))
    if len(whitelist_chat) == 0:
        exit("No chat id provided")
    global WHITELIST_CHAT
    WHITELIST_CHAT = whitelist_chat

    token = env("POWERSWITCH_TGBOT_TOKEN")
    if token is None:
        exit("Please provide a tgbot token. Set by env `POWERSWITCH_TGBOT_TOKEN`")
    global TOKEN
    TOKEN = token

    board_addr_alias = env("POWERSWITCH_BOARD_ADDR_ALIAS")
    if board_addr_alias is None:
        exit("Please provide the alias from board name to pin. Set by env `BOARD_ADDR_ALIAS`, in `name:pin` form, separate by comma `,`")
    pairs = board_addr_alias.split(",")
    alias = {}
    for p in pairs:
        tmp = p.split(":")
        alias[tmp[0]] = tmp[1]
    global BOARD_ADDR_ALIAS
    BOARD_ADDR_ALIAS = alias

    ftdi_addr = env("POWERSWITCH_FTDI_ADDR", "ftdi:///1")
    global DEFAULT_FTDI_ADDR
    DEFAULT_FTDI_ADDR = ftdi_addr

load_config()

if __name__ == "__main__":
    assert len(WHITELIST_CHAT) > 1
    assert TOKEN != ""
    assert len(BOARD_ADDR_ALIAS.keys()) > 1
    assert DEFAULT_FTDI_ADDR != ""
