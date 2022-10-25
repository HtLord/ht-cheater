import fire


class Hello(object):
	def run(self,
			speed=1, # assign a default value means it can be optional flag for cli
			who, # none default args mean required flag for cli
			):
		pass

	def stop(self):
		pass


if __name__ == '__main__':
	"""
	This example will create followed clis
	python fire run who=alice
	python fire run speed=2 who=bob
	python fire stop
	"""
	fire.Fire(Hello)

