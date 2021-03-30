from database.profiledb import ProfileDB

import discord
from discord.ext import commands

db = ProfileDB()

class Banking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def balance(self, ctx):
        user = ctx.author

        db.open_account(ctx.author.id)

        bal = db.get_bank_data(ctx.author.id)

        embed=discord.Embed(description=f'{bal}')
        embed.set_author(name=f'{user} Balance', icon_url=f'{user.avatar_url}')
        await ctx.send(embed=embed)

    @commands.command()
    async def add(self, ctx, deltamoney):
        db.open_account(ctx.author.id)

        delmoney = int(deltamoney)

        db.change_money(ctx.author.id, delmoney)

        await ctx.send("Pog")


def setup(bot):
    bot.add_cog(Banking(bot))