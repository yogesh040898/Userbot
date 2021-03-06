# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from telethon import events
import asyncio
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Module doesn't exist or Module name is invalid**š")
    else:
        await event.edit("\nAvailable Modules:"
"\n\nā¢ šš±šŗš¶š»: `admin`, `chat`"
"\nā¢ šØš½š±š®šš²šæ: `update`, `update now`"
"\nā¢ š š²šŗš²š: `memes`, `deepfry`, `dfry`, `dice`, `basketball`, `dart`, `waifu`, `random`, `carbon`,"
"\nā¢ šš»š±šæš¼š¶š±: `android`, `magisk`"
"\nā¢ šš³šø: `afk`"
"\nā¢ š§š¼š¼š¹š: `all`, `antivirus`, `dictionary`,`dogbin`, `listmyusernames`, `ocr`,`qr`, `currency`, `wiki`, `ud`, `tts`, `trt`, `yt`, `imdb`, `ss`, `telegraph`, `compress`, `rbg`, `barcode`, `quotly`"  
"\nā¢ š”š¼šš²š: `notes`, `filter`, `snips`"
"\nā¢ š§š²šš-š§šæš®š»šš³š¼šæšŗ:`figlet`, `sticklet_un`, `base64`, `hash`, `textx`"
"\nā¢ š£š : `logpms`, `nopm`, `pmpermit`"
"\nā¢ ššµš®š: `chatinfo`, `create`, `invite`, `profile`, `welcome`, `stats` `raw`, `purge`, `purgeme`, `del`, `edit`, `sd`, `whois`"  
"\nā¢ š„š²šš®šæš±š²š±: `lydia`, `repeat`,  `spam`, `sed`"
"\nā¢ ššš®š¹š®šš¼šæš: `eval`, `exec`, `term`, `pip`"
"\nā¢ šš¶ššµššÆ: `git`, `gcommit`, `heroku`, `repo`, `myrepo`"
"\nā¢ šŖš²šÆ: `google` `reverse`, `img`, `w3m`, `weather`, `speed`, `dc`, `ping`, `instagram`"
"\nā¢ šØš½š¹š¼š®š± šš¼šš»š¹š¼š®š±: `direct`, `aria`, `aria2`, `gdrive`, `mega`, `rip`, `download`, `webupload`"
"\nā¢ šš¼šš¶š±: `cod`"
"\nā¢ šØšš²šæšÆš¼š: `useitoub`, `sleep`, `shutdown`, `restart`, `anti_spambot`, `sysd`, `botver`, `alive`, `dbs`,  `creator`,  `readme`,  `time`,  `date`"
"\nā¢ š¦šš¶š°šøš²šæš:  `stickers`"
"\nā¢ š ššš¶š°:  `song`,  `lyrics`"
"\n  --  \n"
f"ā¢ **Please specify which module do you want help for !!**\n"
f"**Usage:** `.help <module name> to know how it works`")
