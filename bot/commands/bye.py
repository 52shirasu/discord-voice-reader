from bot.instance import bot

@bot.command()
async def bye(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("👋 切断しました")
    else:
        await ctx.send("⚠️ 接続されていません")