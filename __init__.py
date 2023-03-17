import re

import discord

import breadcord
from breadcord.module import ModuleCog


class MoyaiPlusPlus(breadcord.module.ModuleCog):
    def __init__(self, module_id: str):
        super().__init__(module_id)
        
    @ModuleCog.listener()
    async def on_message(self, message: discord.Message):
        for reaction in selfsettings.reactions:
            if re.findall(reaction.key, message.content.lower()):
                try:
                    await message.add_reaction(reaction.value)
                except discord.errors.HTTPException as exception:
                    if exception.text == "Unknown Emoji":
                        raise ValueError(f'Invalid Emoji "{reaction.value}" In Module Settings') from exception
                    else:
                        raise exception

async def setup(bot: breadcord.Bot):
    await bot.add_cog(MoyaiPlusPlus("moyai_plus_plus"))
