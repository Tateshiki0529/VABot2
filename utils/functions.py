from stringcolor import cs
from discord import ApplicationContext, Embed
from datetime import datetime as dt, timezone as tz, timedelta as td

class LOGLEVEL:
	INFO = 0
	WARN = 1
	ERROR = 2
	DEBUG = -1

def log(message: str, log_level: int = LOGLEVEL.INFO) -> None:
	now = dt.now().astimezone(tz(td(hours=9)))
	match log_level:
		case LOGLEVEL.INFO:
			print('[%s][%s] %s' % (cs(now.strftime('%Y/%m/%d %H:%M:%S'), 'teal'), cs('INFO', 'seagreen3'), message))
			return
		case LOGLEVEL.WARN:
			print('[%s][%s] %s' % (cs(now.strftime('%Y/%m/%d %H:%M:%S'), 'teal'), cs('WARN', 'yellow2'), message))
			return
		case LOGLEVEL.ERROR:
			print('[%s][%s] %s' % (cs(now.strftime('%Y/%m/%d %H:%M:%S'), 'teal'), cs('ERROR', 'red2'), message))
			return
		case LOGLEVEL.DEBUG:
			print('%s%s%s%s%s' % (cs('[', 'grey7'), cs(now.strftime('%Y/%m/%d %H:%M:%S'), 'teal'), cs('][', 'grey7'), cs('DEBUG', 'lightslategrey'), cs('] %s' % message, 'grey7')))
			return
		case _:
			print('[%s][%s] %s' % (cs(now.strftime('%Y/%m/%d %H:%M:%S'), 'teal'), cs('INFO', 'seagreen3'), message))
			return

def is_owner(ctx: ApplicationContext) -> bool:
	return ctx.interaction.user == ctx.interaction.guild.owner

def addFields(embed: Embed, fields: list[tuple[str, str, bool]]) -> Embed:
	for field in fields:
		embed.add_field(name=field[0], value=field[1], inline=field[2])
	return embed