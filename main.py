import discord
from discord.ext.commands import Bot
from discord.ext import commands
import time
import sys
import subprocess
import json
import random

bot = discord.Client()
bot = commands.Bot(command_prefix="!", pm_help=None, description='Bot')

exceptions =['cmd','admin']




@bot.event
async def on_ready():
    print("<=-----------------------------=>")
    print("   Name: {}".format(bot.user.name))
    print("   ID: {}".format(bot.user.id))
    print("<=-----------------------------=>")
    await bot.change_presence(game=discord.Game(name='Beddua Okuyor...',url='https://www.twitch.tv/komocii', type=1))


@bot.command(hidden= True,pass_context=True)
async def restart(ctx):
    BotOwner = "289453428701396992"
    await bot.delete_message(ctx.message)
    if ctx.message.author.id == BotOwner:
        msga = await bot.say("Restaring")
        msg = await bot.say("█▒▒▒▒▒▒▒▒▒ %01")
        time.sleep(0.01)
        await bot.edit_message(msga, "Restaring")
        await bot.edit_message(msg,"███▒▒▒▒▒▒▒ %10")
        time.sleep(0.01)
        await bot.edit_message(msga, "Restaring")
        await bot.edit_message(msg,"█████▒▒▒▒▒ %30")
        time.sleep(0.01)
        await bot.edit_message(msga, "Restaring")
        await bot.edit_message(msg,"███████▒▒▒ %50")
        time.sleep(0.01)
        await bot.edit_message(msga, "Restaring")
        await bot.edit_message(msg,"██████████ %100")
        time.sleep(0.1)
        await bot.delete_message(msga)
        await bot.delete_message(msg)
        await bot.logout()
        subprocess.call([sys.executable, "main.py"])
    else:
        await bot.say("**Bu komutu Sadece <@289453428701396992> Kullanabilir!**")

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Büygeç")
    await bot.add_roles(member, role)
    embed = discord.Embed(
                title='**B Ü Y Ü L E N D İ N İ Z**',
                description= member.mention,
                colour= discord.Colour.blue()
            )
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_author(name='Hoş Geldin')
    channel = discord.utils.get(member.server.channels, name="büyülendin")
    await bot.send_message(channel, embed=embed)

if __name__ == '__main__':
    for exception in exceptions:
        try:
            bot.load_extension(exception)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(exception, error))


    bot.run("NTc5NDUzMTc4NDQxODkxODY5.XPbKlA.uu3zV5s3bbbSqQJozVoGs3DNl4g")
