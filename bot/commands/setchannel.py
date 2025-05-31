from bot.instance import bot
from bot.utils import state

@bot.command()
async def setchannel(ctx):
    state.set_read_channel(ctx.guild.id, ctx.channel.id)
    await ctx.send(f"📢 このチャンネルを読み上げ対象に設定しました")