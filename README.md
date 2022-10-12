# Unmatched Power Switch (Powered by FT2232HL)

## How to connect

* Connect the sixth pin of the Front Panel Header on Unmatched Board to [0:7] ADBUS port.
* Connect the fifth pin of the Front Panel Header on Unmatched Board to GND.

## How to use

```bash
pip install -r ./requirements.txt
# Use environment variable to configure
vim .env
python main.py --help
```

## The configuration

```bash
# Detemine list of chats for bot to run, separate by comma
export POWERSWITCH_WHITELIST_CHAT=123456,7890123

# The bot API token
export POWERSWITCH_TGBOT_TOKEN=abcdeg:123511341

# The alias board name. Form: board_name:pin, separate by comma
export POWERSWITCH_BOARD_ALIAS=magmortar:2,larvesta:3

# FTDI address to connect to, optional, default "ftdi:///1"
export POWERSWITCH_FTDI_ADDR=ftdi:///1
```

