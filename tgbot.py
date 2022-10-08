from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import log
import ctrl
import asyncio

try:
    import config
except ImportError:
    print("Copy the config.example.py to config.py file and restart")
    quit(1)


def filter_machine(machines: list[str]) -> tuple[list, list]:
    board = config.BOARD_ADDR_ALIAS.keys()
    exist = []
    non_exist = []
    for m in machines:
        if m in board:
            exist.append(m)
        else:
            non_exist.append(m)
    return (exist, non_exist)


async def reboot(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_message is None:
        return

    if not update.effective_message.chat.id in config.WHITELIST_CHAT:
        log.warn("Somebody: (%s) try to reboot", update.message.from_user.first_name)
        return

    if ctx.args is None:
        await update.effective_message.reply_text("At least one machine name is required")
        return

    machines = ctx.args
    if len(machines) < 1:
        await update.effective_message.reply_text("At least one machine name is required")

    (exist_machine, non_exist_machine) = filter_machine(machines)
    log.info("New request for rebooting. Reboot boards: {}, Request User: {}", " ".join(machines), update.effective_message.from_user.first_name)

    await update.effective_message.reply_text("Those machine doesn't exist: {}".format(" ,".join(non_exist_machine)))

    ctrl.power_off_all(exist_machine)
    await asyncio.sleep(1.0 * len(exist_machine))
    ctrl.power_on_all(exist_machine)

    await update.effective_message.reply_text("Machines: {} is rebooted".format(" ,".join(exist_machine)))

async def list(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_message is None:
        return
    await update.effective_message.reply_text("Available boards: {}".format('\n'.join(config.BOARD_ADDR_ALIAS.keys())))

def init_bot():
    app = ApplicationBuilder().token(config.TOKEN).build()
    app.add_handler(CommandHandler("reboot", reboot))
    app.add_handler(CommandHandler("list", list))

    return app
