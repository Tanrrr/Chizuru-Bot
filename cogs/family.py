import asyncio
import discord
from discord.ext import commands
from discord.ext.commands.core import check
from database.profiledb import ProfileDB
from database.familydb import FamilyDB

db = ProfileDB()
fdb = FamilyDB()

class Family(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def marry(self, ctx, target: discord.User):
        target_id = int(target.id)

        db.open_account(ctx.guild.id, ctx.author.id)

        db.open_account(ctx.guild.id, target_id)

        if not fdb.check_married(ctx.guild.id, ctx.author.id):
            msg = await ctx.send(f"<@{target_id}> do you want to marry <@{ctx.author.id}>")

            await msg.add_reaction('✅')

            def check(reaction, user):
                return user == target and str(reaction.emoji) == '✅'

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send("Ran out of time, please try again.")
            else:
                fdb.marry(ctx.guild.id, ctx.author.id, target_id)

                msg.delete()

                await ctx.send("Married Them!")
        else:
            await ctx.send("You are already married.")
                
    @commands.command()
    async def divorce(self, ctx):
        db.open_account(ctx.guild.id, ctx.author.id)

        if fdb.check_married:
            msg = await ctx.send(f"<@{ctx.author.id}> are you sure you want to divorce?")

            await msg.add_reaction('✅')

            def check(reaction, user):
                return user == user and user != msg.author and str(reaction.emoji) == '✅'

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0, check=check)

            except asyncio.TimeoutError:
                await ctx.send("Ran out of time, please try again.")

            else:

                fdb.divorce(ctx.guild.id, ctx.author.id)

                await ctx.send("Divorced Them")

                msg.delete()
        else:
            await ctx.send("You arent married to anyone.")


    @commands.command()
    async def family(self, ctx):
        
        fam = fdb.check_family(ctx.guild.id, ctx.author.id)

        if fam == 'None':
            await ctx.send('You have no family')
        else:
            await ctx.send(f'You are married to **<@{fam}>** ')



def setup(bot):
    bot.add_cog(Family(bot))