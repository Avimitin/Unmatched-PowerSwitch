from pyftdi.gpio import GpioController
import time
import log
import config

class UnmatchedPowerSwitch:
    def __init__(self, addr: str, pin_nth: int) -> None:
        self.gpio = GpioController()
        self.gpio.configure(addr, direction=0xFF)
        if pin_nth < 0 or pin_nth > 7:
            raise Exception("Invalid pin, only allow [0, 7]")
        self.pin = pow(2, pin_nth)

    def poweroff(self) -> None:
        self.gpio.write(0x00)

    def power_on(self) -> None:
        self.gpio.write(self.pin)
        time.sleep(0.5)
        self.gpio.write(0x00)
        time.sleep(0.5)
        self.gpio.write(self.pin)


def from_name(name: str) -> UnmatchedPowerSwitch | None:
    board_id = config.BOARD_ADDR_ALIAS.get(name)
    if board_id == None:
        return None
    gpio_ctrl = UnmatchedPowerSwitch(config.DEFAULT_FTDI_ADDR, board_id)
    return gpio_ctrl


def power_on_all(boards: list):
    for brd in boards:
        ctrl = from_name(brd)
        if ctrl is None:
            log.warn("Unknown board: {}".format(brd))
            return None
        ctrl.power_on()
        log.info("Board {} is power on".format(brd))

def power_off_all(boards: list):
    for brd in boards:
        ctrl = from_name(brd)
        if ctrl is None:
            log.warn("Unknown board: {}".format(brd))
            return None
        ctrl.poweroff()
        log.info("Board {} is power off".format(brd))

