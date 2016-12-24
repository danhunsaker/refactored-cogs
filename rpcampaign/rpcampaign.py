# Discord
import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils import checks
# Essentials
import os


class RPCampaign:
    """RPG Campaign - formal roleplaying channels and commands"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json('data/rpcampaign/settings.json')

    @commands.group(pass_context=True, no_pm=True)
    async def createcampaign(self, ctx):
        """Create RPG Campaign channels"""
        server = ctx.message.server
        if server.id not in self.settings:
            self.settings[server.id] = {}
            self.save_json()
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)


def check_folder():
    f = 'data/rpcampaign'
    if not os.path.exists(f):
        os.makedirs(f)


def check_file():
    f = 'data/rpcampaign/settings.json'
    if dataIO.is_valid_json(f) is False:
        dataIO.save_json(f, {})


def setup(bot):
    check_folder()
    check_file()
    n = RPCampaign(bot)
    bot.add_cog(n)
