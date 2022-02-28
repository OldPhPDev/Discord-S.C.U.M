class Logger:
	@staticmethod
	def log(text, color=None, log={"console":True, "file":False}):
		if isinstance(log, bool):
			log = {"console":log, "file":False}
		if log["console"]:
			if color:
				string = color + text + '\033[m'
			else:
				string = text
			print(string)
		if log["file"]:
			with open(log["file"], 'a+') as f:
				f.write(text + '\n\n')