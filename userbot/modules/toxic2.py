from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.lewat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1.2)
    await typew.edit("**Ikan Bandeng**")
    sleep(1.2)
    await typew.edit("**Makan Kawat**")
    sleep(1.2)
    await typew.edit("**Misii Orang ganteng mau lewat π€**")
# Create by myself @localheart


@register(outgoing=True, pattern='^.ndaklevel(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1.3)
    await typew.edit("**Buah Apel di Air Payau**")
    sleep(1.3)
    await typew.edit("**Ndak Level LahYauuuu**")
# Create by myself @localheart


@register(outgoing=True, pattern='^.awkwok(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**BABI!!**")
    sleep(1)
    await typew.edit("**MUKA LU KAYA BABI**")
    sleep(1)
    await typew.edit("**OTAK LU TUH KAYA KONTOL**")
    sleep(1)
    await typew.edit("**MUKA LU HINA BANGET**")
    sleep(1)
    await typew.edit("**OTAK LU KAYA BATU**")
    sleep(1)
    await typew.edit("**HAHAHAHA**")
    sleep(1)
    await typew.edit("**MAKANYA JANGAN SANGEAN MULU**")
    sleep(1)
    await typew.edit("**KONTOL LU AJA MASIH BENGKOK**")
    sleep(1)
    await typew.edit("**EHHH SANGE NYA MAU DAPAT YANG CANTIK**")
    sleep(1)
    await typew.edit("**HAHAHAHA**")
# Create by myself @localheart

CMD_HELP.update({
    "toxic2":
    "πΎπ€π’π’ππ£π: `.ngentot`\
    \nβ³ : Lu Coba Sendiri Aja."
    "πΎπ€π’π’ππ£π: `.goblok`\
    \nβ³ : Lu Coba Sendiri Aja."
    "πΎπ€π’π’ππ£π: `.ngatain`\
    \nβ³ : Lu Coba Sendiri Aja."
})
