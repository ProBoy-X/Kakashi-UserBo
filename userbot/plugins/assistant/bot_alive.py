import os
from telethon import events, Button, custom
from userbot.thunderconfig import Config

from userbot import ALIVE_NAME, bot 

currentversion = "2.1"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Kakashi UserBot"
ASSIS_PIC = os.environ.get("ASSIS_PIC", None)
if ASSIS_PIC is None:
     PM_IMG = "https://telegra.ph/file/f98d138354df7d2f914de.jpg"
else:
     PM_IMG = ASSIS_PIC


pm_caption = "      **Assɪsᴛᴀɴᴛ ɪs** `Oɴʟɪɴᴇ`\n\n"
pm_caption += "         **Sʏsᴛᴇᴍ Sᴛᴀᴛs**n"
pm_caption += "• **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ**► `1.15.0` \n"
pm_caption += f"• **Assɪsᴛᴀɴᴛ Vᴇʀsɪᴏɴ**► `{currentversion}`\n"
pm_caption += f"• **Mʏ Pᴇʀᴏᴏ Mᴀsᴛᴇʀ** ► {DEFAULTUSER} \n"
pm_caption += "• **Lɪᴄᴇɴᴄᴇ** ► [UserBot](https://github.com/ProBoy-X/Kakashi-UserBot/blob/master/LICENSE)\n"
pm_caption += "• **Cᴏᴘʏʀɪɢʜᴛ** ► [Kakashi UB](GitHub.com/ProBoy-X/Kakashi-userbot)\n"
light = [[Button.url("✨Rᴇᴘᴏ✨", "https://github.com/ProBoy-X/Kakashi-userbot"), Button.url("🤓Sᴜᴘᴘᴏʀᴛ🤓", "https://t.me/Kakashi_support")]]
light +=[[custom.Button.inline("✧Hᴇʟᴘ✧", data="gibcmd")]]
@tgbot.on(events.NewMessage(pattern="^/alive" , func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption, buttons=light)
