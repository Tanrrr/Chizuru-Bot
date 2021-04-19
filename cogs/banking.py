from discord.ext.commands import cooldowns
from database.profiledb import ProfileDB

import discord
from discord.ext import commands

db = ProfileDB()



class Banking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,ctx, member):
        user = member

        db.open_account(ctx.guild.id, user.id)

    @commands.command(aliases=['b', 'bal'])
    async def balance(self, ctx):
        user = ctx.author

        db.open_account(ctx.guild.id, ctx.author.id)

        bal = db.get_bank_data(ctx.guild.id, ctx.author.id)

        embed=discord.Embed(title=f' {bal} $')
        embed.set_author(name=f"{user}'s Balance", icon_url=f'{user.avatar_url}')
        await ctx.send(embed=embed)

    @commands.command()
    async def add(self, ctx, deltamoney: int):

        db.open_account(ctx.guild.id, ctx.author.id)

        db.change_money(ctx.guild.id, ctx.author.id, deltamoney)

        await ctx.send(f"Added {deltamoney}$ to account!")

def setup(bot):
    bot.add_cog(Banking(bot))