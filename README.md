# Unmatched Power Switch (Powered by FT2232HL)

## How to connect

* Connect the sixth pin of the Front Panel Header on Unmatched Board to [0:7] ADBUS port.
* Connect the fifth pin of the Front Panel Header on Unmatched Board to GND.

## How to use

```bash
pip install -r ./requirements.txt
cp config.example.py config.py
python main.py --help
```

## The configuration

```python
# Detemine list of chats for bot to run
WHITELIST_CHAT = []
# The bot API token
TOKEN = ""

# The alias board name. Mapping: Board -> nth of the pin
BOARD_ADDR_ALIAS = {
    "magmortar": 2
}

# FTDI address to connect to
DEFAULT_FTDI_ADDR = "ftdi:///1"
```

