class Counter(object):
	""" this is my first Python Module """

	instances = 0

	def __init__(self):
		Counter.instances += 1
		self.reset()

	""" this is my first Python Module """
	def reset(self):
		self.willen = 0

	""" this is my first Python Module """
	def increment(self, a=1):
		self.willen += a
	
	""" this is my first Python Module """
	def decrement(self, a=1):
		self.willen -= a

	def getValue(self):
		return self.willen

	def __str__(self):
		return str(self.willen)

	def __eq__(self, other):
		if self is other: return True
		elif type(self) != type(other): return False
		else: return self.willen == other.willen
