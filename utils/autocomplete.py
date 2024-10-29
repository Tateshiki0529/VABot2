from discord import (
	AutocompleteContext
)
from json import load
from os import getcwd

from .version_manager import VersionInfo

class AutoComplete:
	async def getExtensions(self, ctx: AutocompleteContext) -> list[str]:
		return [extension for extension in ctx.bot.extensions.keys() if ctx.value in extension]
	
	async def getVersion(self, ctx: AutocompleteContext) -> list[str]:
		version_info = VersionInfo()
		return [version for version in version_info.getVersions() if ctx.value in version]
	
	async def getCPNameListAsync(self, ctx: AutocompleteContext) -> list[str]:
		with open('./cp-list.json', 'r') as fp:
			json = load(fp)
		
		return [row['name'] for row in json if ctx.value in row['name']]

	def getCPNameList() -> list[str]:
		with open('./cp-list.json', 'r') as fp:
			json = load(fp)
		
		return [row['name'] for row in json]