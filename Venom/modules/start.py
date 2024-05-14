import asyncio
import random
import asyncio
import random
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton
from pyrogram import Client
from pyrogram import filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import EMOJIOS, IMG, STICKER
from Venom import VenomX
from Venom.database.chats import add_served_chat
from Venom.database.users import add_served_user
from Venom.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)



channel_ids = [-1002019851310]




async def check_channels_membership(user_id):
    for channel_id in channel_ids:
        if not await VenomX.get_chat_member(channel_id, user_id):
            return False
    return True

@VenomX.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)

@VenomX.on_message(filters.private & filters.command(["start", "aistart"]))
async def start_command(_, m: Message):
    user_id = m.from_user.id
    try:
        if await check_channels_membership(user_id):
            # User is member of all channels, execute start command
            if m.chat.type == ChatType.PRIVATE:
                accha = await m.reply_text(
                    text=random.choice(EMOJIOS),
                )
                await asyncio.sleep(1.3)
                await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ ѕтαятιиg..__")
                await asyncio.sleep(0.2)
                await accha.edit("__ᴅιиg ᴅσиg ꨄ sтαятιиg.....__")
                await asyncio.sleep(0.2)
                await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ sтαятιиg..__")
                await asyncio.sleep(0.2)
                await accha.delete()
                umm = await m.reply_sticker(sticker=random.choice(STICKER))
                await asyncio.sleep(2)
                await umm.delete()
                await m.reply_photo(
                    photo=random.choice(IMG),
                    caption=f"""**๏ ʜᴇʏ, ɪ ᴀᴍ {VenomX.name}**\n**➻ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.**\n**──────────────**\n**➻ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ]**\n<b>||๏ ʜɪᴛ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ||</b>""",
                    reply_markup=InlineKeyboardMarkup(DEV_OP),
                )
                await add_served_user(m.from_user.id)
            else:
                await m.reply_photo(
                    photo=random.choice(IMG),
                    caption=START,
                    reply_markup=InlineKeyboardMarkup(HELP_START),
                )
                await add_served_chat(m.chat.id)
        else:
            # User is not a member of all channels, handle this case
            await m.reply_text(
                "You must join all our channels first!"
            )
    except UserNotParticipant:
        
        # User is not a member of all channels, send message with button
        await m.reply_text(
            "You must join all our channels first!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Join",
                            url="https://t.me/thanosprosss"
                        ),
                        InlineKeyboardButton(
                            "join",
                            url="https://t.me/thanosprosss"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "join",
                            url="https://t.me/thanosprosss"
                        ),
                        InlineKeyboardButton(
                            "join",
                            url="https://t.me/thanosprosss"
                        )
                    ]
                ]
            )
        )
# Add other commands and functions here

# Run the client
                


@VenomX.on_cmd("help")
async def help(client: VenomX, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)



@VenomX.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)
