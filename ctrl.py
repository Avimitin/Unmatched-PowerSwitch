from pyftdi.gpio import GpioController
import time
import log
import config

# A class wrapper to operate on specific pin on ADBUS
class UnmatchedPowerSwitch:
    # Create a new wrapper to operate on the specific pin
    #
    # :param str addr: the ftdi address to connnect
    # :param int pin_nth: the nth pin to operate, must be in range [0, 8)
    def __init__(self, addr: str, pin_nth: int) -> None:
        self.gpio = GpioController()
        self.gpio.configure(addr, direction=0xFF)
        if pin_nth < 0 or pin_nth > 7:
            raise Exception("Invalid pin, only allow [0, 7]")
        self.pin = pow(2, pin_nth)

    # Monitor pressing the button
    def poweroff(self) -> None:
        self.gpio.write(self.pin)
        time.sleep(3)
        self.gpio.write(0x00)

    # Monitor a quick click
    def power_on(self) -> None:
        self.gpio.write(self.pin)
        time.sleep(0.5)
        self.gpio.write(0x00)
        time.sleep(0.5)
        self.gpio.write(self.pin)

    # Close the gpio connection
    def close(self) -> None:
        # FIXME: Why don't we just reuse the connection?
        self.gpio.close()


# Get the gpio pin from alias
#
# :param str name: the alias name
def from_name(name: str) -> UnmatchedPowerSwitch | None:
    board_id = config.BOARD_ADDR_ALIAS.get(name)
    if board_id == None:
        return None
    gpio_ctrl = UnmatchedPowerSwitch(config.DEFAULT_FTDI_ADDR, board_id)
    return gpio_ctrl


# Try power on all the given boards
#
# :param list boards: list of alias name
def power_on_all(boards: list):
    for brd in boards:
        ctrl = from_name(brd)
        if ctrl is None:
            log.warn("Unknown board: {}".format(brd))
            return None
        ctrl.power_on()
        log.info("Poweron signal is sent".format(brd))
        ctrl.close()


# Try power off all the given boards
#
# :param list boards: list of alias name
def power_off_all(boards: list):
    for brd in boards:
        ctrl = from_name(brd)
        if ctrl is None:
            log.warn("Unknown board: {}".format(brd))
            return None
        ctrl.poweroff()
        log.info("Poweroff signal is sent".format(brd))
        ctrl.close()

