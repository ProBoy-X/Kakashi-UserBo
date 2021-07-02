"""Check if userbot awake or not . 

"""
from userbot import ALIVE_NAME
from userbot.Config import Var
from userbot.utils import lightning_cmd
import os
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)
if ALIVE_PHOTTO is None:
    ALIVE_PHOTTO = "https://telegra.ph/file/f98d138354df7d2f914de.jpg"
else:
    ALIVE_PHOTTO = ALIVE_PHOTTO


DEFAULTUSER = (
    str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
)

ALIVE_MESSAGE = Var.ALIVE_MESSAGE
if not ALIVE_MESSAGE:
    ALIVE_MESSAGE = "**✨Yᴜᴘᴘ.. I'ᴍ ᴀᴡᴀᴋᴇ✨ \n\n\n**"
    ALIVE_MESSAGE +=       " `Bᴏᴛ Sᴛᴀᴛᴜs \n\n\n`"
    ALIVE_MESSAGE += f"`Tᴇʟᴇᴛʜᴏɴ ==> Tᴇʟᴇᴛʜᴏɴ-15.0.0 \n\n`"
    ALIVE_MESSAGE += f"`Pʏᴛʜᴏɴ ==> Pʏᴛʜᴏɴ-3.8.5 \n\n`"
    ALIVE_MESSAGE += "`I'ʟʟ Bᴇ Wɪᴛʜ Yᴏᴜ Mᴀsᴛᴇʀ Tɪʟʟ Mʏ Dʏɴᴏ Eɴᴅs!!😉 \n\n`"
    ALIVE_MESSAGE += f"`Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ` ==>  @Kakashi_Support \n\n"
    ALIVE_MESSAGE += f"`Mʏ Pᴇᴇʀᴏᴏ Mᴀsᴛᴇʀ` ==> {DEFAULTUSER} \n\n "
else:
    ALIVE_MESSAGE = ALIVE_MESSAGE

# @command(outgoing=True, pattern="^.awake$")
@borg.on(lightning_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete()
    await borg.send_file(awake.chat_id, ALIVE_PHOTTO, caption=ALIVE_MESSAGE)

from userbot import CMD_HELP

CMD_HELP.update( {
    ".awake": "**USAGE** Check If Userbot Alive ."
})
