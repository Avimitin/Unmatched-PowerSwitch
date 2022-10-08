import argparse
import tgbot
import log
import ctrl

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="The GPIO way to shutdown the Unmatched board")
    parser.add_argument("-n", "--on", type = str, nargs="+", metavar="board_id", default = None, help = "Power on the specfic board")
    parser.add_argument("-f", "--off", type = str, nargs="+", metavar="board_id", default = None, help = "Power off the specfic board")
    parser.add_argument("--bot", action=argparse.BooleanOptionalAction, help ="Run a telegram bot in background")
    parser.set_defaults(bot=False)

    args = parser.parse_args()

    if args.bot == True:
        app = tgbot.init_bot()
        log.info("Bot started")
        app.run_polling()
        # Quit when this script is ran as daemon
        quit(0)

    if args.on != None and len(args.on) != 0:
        ctrl.power_on_all(args.on)

    if args.off != None and len(args.off) != 0:
        ctrl.power_off_all(args.off)
