from discord import (
	Cog, Bot, Intents, ApplicationContext
)
from discord import option
from discord.ext.commands import slash_command as command
from dotenv import load_dotenv
from os import getenv
from emoji import emojize

from utils.functions import log, is_owner
from utils.autocomplete import AutoComplete

load_dotenv()

class VABot(Cog):
	def __init__(self, bot: Bot):
		super().__init__()
		self.bot: Bot = bot
		log('[Core] Loading extensions...')
		log('[Core] All extensions loaded!')
		return
	
	@Cog.listener()
	async def on_ready(self) -> None:
		log('[Core] Bot %s#%s is active!' % (self.bot.user.display_name, self.bot.user.discriminator))
		return

	@Cog.listener()
	async def on_application_command(self, ctx: ApplicationContext) -> None:
		log('[Core] %s@%s issued: /%s' % (ctx.interaction.user.display_name, ctx.interaction.user.name, ctx.command.qualified_name))
		return
	
	@Cog.listener()
	async def on_disconnect(self) -> None:
		log('[Core] Connection closed. Bot stopped.')
		return
	
	# Command /reload <extension_name>
	@command(
		name = 'reload',
		description = '拡張機能をリロードします [Module: Core] [Admin]'
	)
	@option(
		name = 'extension_name',
		type = str,
		description = 'リロードする拡張機能名',
		autocomplete = AutoComplete.getExtensions,
		required = True
	)
	async def __reload(self, ctx: ApplicationContext, extension_name: str) -> None:
		if not is_owner(ctx):
			await ctx.respond('Error: このコマンドは管理者以外使用できません。')
			return
		if extension_name in self.bot.extensions.keys():
			self.bot.reload_extension(extension_name)
			await ctx.respond('拡張機能 `%s` をリロードしました！' % extension_name)
			return
		else:
			await ctx.respond('Error: 拡張機能名 `%s` は利用できません！' % extension_name)
			return
	
	# Command /stop-server
	@command(
		name = 'stop-server',
		description = 'Botを停止します [Module: Core] [Admin]'
	)
	async def __stop_server(self, ctx: ApplicationContext) -> None:
		if not is_owner(ctx):
			await ctx.respond('Error: このコマンドは管理者以外使用できません。')
			return
		await ctx.respond(emojize(':wave:'))
		cogs = [c for c in self.bot.cogs]
		for cog in cogs:
			self.bot.remove_cog(cog)
		await self.bot.close()
		return
	
if __name__ == '__main__':
	log('[System] Initializing...')
	discord_token = getenv('DISCORD_TOKEN')
	target_guild_id = getenv('DISCORD_GUILD_ID')
	bot = Bot(auto_sync_commands=True, intents=Intents().all(), debug_guilds=[target_guild_id])
	log('[System] Loading module \'Core\'...')
	bot.add_cog(VABot(bot=bot))
	log('[System] Module \'Core\' loaded!')
	log('[System] Connecting to Discord server...')
	bot.run(discord_token)