import time

from userbot import ALIVE_NAME, CMD_HELP, Lastupdate
from userbot.Config import Var
from userbot.plugins import telever
from userbot.utils import lightning_cmd, sudo_cmd


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
PM_IMG = Var.ALIVE_IMAGE
pm_caption = "➥ **Kᴀᴋᴀsʜɪ Usᴇʀʙᴏᴛ ɪs** `ᴏɴʟɪɴᴇ`\n\n"
pm_caption += "➥            **✘ Sʏsᴛᴇᴍ sᴛᴀᴛs ✘**\n"
pm_caption += "➥ **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ** »» `1.15.0` \n"
pm_caption += "➥ **Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ** »» `3.7.4` \n"
pm_caption += f"➥ **Pɪɴɢ** »» `Pᴏɴɢ:- {uptime}` \n"
pm_caption += "➥ **Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛᴜs** »» `Fᴜɴᴄᴛɪᴏɴᴀʟ`\n"
pm_caption += f"➥ **Bᴏᴛ ᴠᴇʀsɪᴏɴ** »» `Uᴘ ᴛᴏ ᴅᴀᴛᴇ`\n"
pm_caption += f"➥ **👑Oᴡɴᴇʀ👑** »» {DEFAULTUSER} \n"
pm_caption += "➥ **Lɪᴄᴇɴsᴇ** »» [PʀᴏBᴏʏ-x](https://github.com/ProBoy-X/Kakashi-UserBot)\n"
pm_caption += "➥ **Cᴏᴘʏʀɪɢʜᴛ** »» [PʀᴏBᴏʏ-x](GitHub.com/JassManak1125)\n"
pm_caption +=           "Dᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ [Kᴀᴋᴀsʜɪ Uʙ](https://github.com/ProBoy-X/Kakashi-UserBot)"


@borg.on(lightning_cmd(pattern=r"fralive"))
@borg.on(sudo_cmd(pattern=r"fralive", allow_sudo=True))
async def friday(alive):
    await alive.get_chat()
    """ For .salive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CMD_HELP.update(
    {
        "salive": "**sLive**\
\n\n**Syntax : **`.salive`\
\n**Usage :** Check if UserBot is salive"
    }
)
