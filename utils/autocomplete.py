from discord import (
	AutocompleteContext
)

class AutoComplete:
	async def getExtensions(self, ctx: AutocompleteContext) -> list[str]:
		return [extension for extension in ctx.bot.extensions.keys() if ctx.value in extension]