class Block(object):
	def __init__(self, index, sHash, previousHash, timestamp, data):
		self.index = index
		self.sHash = sHash
		self.previousHash = previousHash
		self.timestamp = timestamp
		self.data = data

	def getIndex(self):
		return self.index
