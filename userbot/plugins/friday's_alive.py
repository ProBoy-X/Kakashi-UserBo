"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor
import os
import time

from userbot import ALIVE_NAME, Lastupdate
from userbot.plugins import currentversion
from userbot.utils import lightning_cmd, sudo_cmd

FRI_IMAGE = os.environ.get("FRI_IMAGE", None)
if FRI_IMAGE is None:
    FRI_IMG = "https://telegra.ph/file/f98d138354df7d2f914de.jpg"
else:
    FRI_IMG = FRI_IMAGE


# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"

pm_caption = "         **Kᴀᴋᴀsʜɪ UsᴇʀBᴏᴛ ɪs** »» `Oɴʟɪɴᴇ`\n\n"
pm_caption += "              **Sʏsᴛᴇᴍ Sᴛᴀᴛs**\n"
pm_caption += "➥ **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ** »» `1.21.0` \n"
pm_caption += "➥ **Pʏᴛʜᴏɴ** »» `3.9.0` \n"
pm_caption += f"➥ **Uᴘᴛɪᴍᴇ** »» `{uptime}` \n"
pm_caption += "➥ **Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛᴜs** »» `Functional`\n"
pm_caption += "➥ **Cᴜʀʀᴇɴᴛ Bʀᴀɴᴄʜ** »» `master`\n"
pm_caption += f"➥ **Vᴇʀsɪᴏɴ** »» `{currentversion}`\n"
pm_caption += f"➥ **Mʏ Mᴀsᴛᴇʀ** :»» {DEFAULTUSER} \n"
pm_caption += "➥ **Lɪᴄᴇɴsᴇ** :»» [Kᴀᴋᴀsʜɪ UB](https://github.com/ProBoy-X/Kakashi-UserBot/master/LICENSE)\n"
pm_caption += "➥ **Cᴏᴘʏʀɪɢʜᴛ** :»» [PʀᴏBᴏʏ-X](GitHub.com/ProBoy-X)\n"




@borg.on(lightning_cmd(pattern=r"falive"))
@borg.on(sudo_cmd(pattern=r"falive", allow_sudo=True))
async def friday(falive):
    await falive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(falive.chat_id, FRI_IMG, caption=pm_caption)
    await falive.delete()
