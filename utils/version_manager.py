class VersionInfo:
	def __init__(self) -> None:
		self.version_text: dict[str, str] = {
			'5.1.0': '''以下の機能を実装しました:
・`Core`モジュール
　- 新しいコマンドの実装
　　- `/version` コマンド
''',
			'5.0.0': '''以下の機能を実装しました:
・`Core`モジュール
　- ベースモジュールの実装
　- 新しいコマンドの実装
　　- `/reload` コマンド
　　- `/stop-server` コマンド
'''
		}
		self.latest_version = list(self.version_text.keys())[0]
		return

	def getVersion(self, version: str|None = None) -> str|bool:
		if not version:
			return self.version_text[self.latest_version]
		else:
			if not self.version_text[version]:
				return False
			else:
				return self.version_text[version]
			
	def getVersions(self) -> list[str]:
		return list(self.version_text.keys())