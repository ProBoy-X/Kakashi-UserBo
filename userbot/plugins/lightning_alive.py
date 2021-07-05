import asyncio
import os

from telethon import __version__ 
from userbot import ALIVE_NAME, TG_CHANNEL, TG_GRUP
from userbot.thunderconfig import Config
from userbot.utils import lightning_cmd

LIGHTNING_ALV_IMG = os.environ.get("LIGHTNING_ALV_IMG", None)
if not LIGHTNING_ALV_IMG:
    ALV_LIGHTNING = "https://telegra.ph/file/784150ba339df72b89728.mp4"
else:
    ALV_LIGHTNING = LIGHTNING_ALV_IMG


version = "4.5"
python_version = "3.8.5"

# Functions
def lightning_Read_time(seconds: int) -> str:
    count = 0
    kirsh = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            lol_hehehe, result = divmod(seconds, 60)
        else:
            lol_hehehe, result = divmod(seconds, 24)
        if seconds == 0 and lol_hehehe == 0:
            break
        time_list.append(int(result))
        seconds = int(lol_hehehe)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        kirsh += time_list.pop() + ", "

    time_list.reverse()
    kirsh += ":".join(time_list)

    return kirsh

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Kᴀᴋᴀsʜɪ UsᴇʀBᴏᴛ"

TG = str(TG_GRUP) if TG_GRUP else "Not  Yet😁😁"
TG_CHANN = str(TG_CHANNEL) if TG_CHANNEL else "Not Yet😁😁"


from userbot import CMD_LIST

pm_caption = "**☠ Kᴀᴋᴀsʜɪ UsᴇʀBᴏᴛ ɪs Oɴʟɪɴᴇ ☠**\n\n"
pm_caption =         "**⚡Wᴏʀᴋɪɴɢ ᴀs ɢᴏᴏᴅ ᴀs ɪ sʜᴀʟʟ..⚡**\n\n"
pm_caption += f"• **♛ Oᴡɴᴇʀ ♛** »» {DEFAULTUSER}\n"
pm_caption += "• **`Vᴇʀsɪᴏɴ`**  »»  `1.17.5`\n"
pm_caption += "• **`Sᴜᴅᴏ`**    »»  `ᴛʀᴜᴇ`  
pm_caption += "• **`Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ`**  »» [Kᴀᴋᴀsʜɪ Uʙ](https://t.me/Kakashi_Support_Official)\n"
pm_caption += "• **`Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ`**  »» [Kᴀᴋᴀsʜɪ Uʙ](https://t.me/kakashi_support)\n\n"
pm_caption += "        **Dᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ [Kᴀᴋᴀsʜɪ ᴜsᴇʀʙᴏᴛ](https://github.com/ProBoy-X/Kakashi-UserBot)"


@borg.on(lightning_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def lightning(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, file=ALV_LIGHTNING, caption=pm_caption)
    await alive.delete()
