import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(color=0xc33952)
        embed.set_author(name="Chizuru", icon_url="https://cdn.discordapp.com/avatars/826020514308030474/e0a11d526f8417aa2c989273465efdac.png?size=1024")
        embed.add_field(name="""__**Basic Commands**__", value="Basic commands, just random stuff.\n\u200b\n **Ping** - Test if the bot is online will respond with Pong!\n
        """, inline=False)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Help(bot))