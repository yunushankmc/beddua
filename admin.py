import discord
from discord.ext import commands
import time

class admin:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context= True)
    async def clear(self, ctx, number):
        author = ctx.message.author
        author_avatar_url = author.avatar_url or author.default_avatar_url
        if ctx.message.author.permissions_in(ctx.message.channel).administrator:
            try:
                await self.client.delete_message(ctx.message)
                mgs = []
                number = int(number)
                async for x in self.client.logs_from(ctx.message.channel, limit=number):
                    mgs.append(x)
                await self.client.delete_messages(mgs)
                embed = discord.Embed(
                    title='Chat Cleaned!',
                    description='**{}** Messages deleted!'.format(number),
                    colour= discord.Colour.blue()
                )
                embed.set_author(name='Chat Deleted by {}'.format(author), icon_url=author_avatar_url)
                emo = await self.client.say(embed=embed)
                time.sleep(3)
                await self.client.delete_message(emo)
            except:
                self.client.say('I can\'t delete so many messages')
        else:
            await self.client.say("You Do Not Have Permission!")

def setup(client):
    client.add_cog(admin(client))
