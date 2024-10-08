from discord import (
	Cog, Bot, ApplicationContext, Interaction
)
from discord import option
from discord.ext.commands import slash_command as command
from psutil import cpu_freq, virtual_memory, disk_usage, cpu_count, cpu_percent
from cpuinfo import get_cpu_info
from platform import platform
from math import floor
from os import getcwd
import sys

sys.path.append(getcwd()+'/../')

from utils.functions import log

class Utils(Cog):
	def __init__(self, bot: Bot):
		log('[Utils] Loading extension \'Utils\'...')
		super().__init__()
		self.bot: Bot = bot
		log('[Utils] Extension \'Utils\' loaded.')
		return
	
	# Command /ping
	@command(
		name = 'ping',
		description = 'BotサーバーとのPingを確認します [Extension: Utils]'
	)
	async def __ping(self, ctx: ApplicationContext) -> None:
		latency = floor(self.bot.latency * 1000)
		spacing = ""
		for i in range(0, 8 + 11 + len(str(latency))):
			spacing = spacing + " "
		await ctx.respond("```\n+-----+%s+--------+\n| You |%s| ==  == | \n+--+--+ <===== %s ms =====> | Server |\n   |   %s| ==  == |\n---+---%s+--------+\n```" % (spacing, spacing, latency, spacing, spacing))
		return
	
	# Command /server
	@command(
		name = "server",
		description = "サーバー情報を返します [Module: General]"
	)
	async def __server(self, ctx: ApplicationContext) -> None:
		msg: Interaction = await ctx.respond("```\n[%s@localhost ~] $ serverinfo\n[ServerInfo]Loading server information..._\n```" % (ctx.interaction.user.display_name))
		CPUFreq = cpu_freq()
		mem = virtual_memory()
		disk = disk_usage(path="/")
		CPUBrand = get_cpu_info()["brand_raw"]
		await msg.edit_original_response(content="```\n[%s@localhost ~] $ serverinfo\n[ServerInfo] - Server Information -\n[ServerInfo] Platform : %s\n[ServerInfo]\n[ServerInfo] CPU      : '%s' %s GHz (%s - %s) (C/T: %s / %s) (Usage: %s %%)\n[ServerInfo] Memory   : %s GBytes / %s GBytes (Free: %s GBytes) (Usage: %s %%)\n[ServerInfo] Disk     : %s GBytes / %s GBytes (Free: %s GBytes) (Usage: %s %%)\n[ServerInfo]\n[ServerInfo] ### Success.\n[%s@localhost ~] $ _\n```" % (
			ctx.interaction.user.display_name,
			platform(),
			CPUBrand, round(CPUFreq.current / 1024, 1), round(CPUFreq.min / 1024, 1), round(CPUFreq.max / 1024, 1), cpu_count(logical=False), cpu_count(logical=True), cpu_percent(interval=1),
			round(mem.used / 1073741824, 2), round(mem.total / 1073741824, 2), round(mem.free / 1073741824, 2), mem.percent,
			round(disk.used / 1073741824, 2), round(disk.total / 1073741824, 2), round(disk.free / 1073741824, 2), disk.percent,
			ctx.interaction.user.display_name
		))
		return

def setup(bot: Bot) -> None:
	bot.add_cog(Utils(bot=bot))
	return