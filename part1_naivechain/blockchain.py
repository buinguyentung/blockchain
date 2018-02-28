import hashlib
from datetime import datetime
from block import *

class BlockChain(object):
	# Storing the blockchain in a list
	lChain = []

	def __init__(self):
		lChain = []

	def printBlockInfo(self, blockIn):
		print '-------------------------------'
		print 'Info of block', blockIn.index
		print 'Hash          =', blockIn.sHash
		print 'Previous Hash =', blockIn.previousHash
		time = blockIn.timestamp
		print 'Creation time = ' + str(time.hour) + ':' + str(time.minute), '-', time.day, time.month, time.year
		print blockIn.data
		print '------------------------------'

	# Genesis block
	def createGenesisBlock(self):
		# sha256('Tung') = 'f97a02ba06587422d685927f0245114523b55578331b5eaa0c3d7f7ebb77fce0'
		genesisBlock = Block(0, 'f97a02ba06587422d685927f0245114523b55578331b5eaa0c3d7f7ebb77fce0', '', datetime.now(), "Tung's genesis block")
		#self.printBlockInfo(genesisBlock)
		self.lChain.append(genesisBlock)

	# Block hash
	def calculateHash(self, index, previousHash, timestamp, data):
		sha256 = hashlib.sha256()
		# TypeError: update() argument 1 must be string or buffer, not int or datetime
		sha256.update(str(index))
		sha256.update(previousHash)
		#sha256.update(str(timestamp))
		sha256.update(data)
		return sha256.hexdigest()

	def calculateHashForBlock(self, blockIn):
		return self.calculateHash(blockIn.index, blockIn.previousHash, blockIn.timestamp, blockIn.data)

	def getLastestBlock(self):
		return self.lChain[len(self.lChain) - 1]

	# Generating a block
	def generateNextBlock(self, nextBlockData):
		previousBlock = self.getLastestBlock()
		nextIndex = previousBlock.index + 1
		nextTimestamp = datetime.now()
		nextHash = self.calculateHash(nextIndex, previousBlock.sHash, nextTimestamp, nextBlockData)
		newBlock = Block(nextIndex, nextHash, previousBlock.sHash, nextTimestamp, nextBlockData)
		return newBlock

	# Adding new block into chain
	def addNewBlock(self, nextBlockData):
		self.lChain.append(self.generateNextBlock(nextBlockData))

	# Validating the integrity of blocks
	def isValidNewBlock(self, newBlock, previousBlock):
		if (previousBlock.index + 1 != newBlock.index):
			print 'invalid index'
			return False
		elif (previousBlock.sHash != newBlock.previousHash):
			print 'invalid previousHash'
			return False
		elif (self.calculateHashForBlock(newBlock) != newBlock.sHash):
			print 'invalid hash value'
			return False
		return True

	# Validating the structure of the block, so that malformed content sent by a peer won't crash our node
	def isValidBlockStructure(self, blockIn):
		# Type of index should be int
		# Type of sHash should be string
		# Type of previousHash should be string
		# Type of timestamp should be timedate
		# Type of data should be string
		return True

	# Checking for valid block chains
	def isValidBlockChain(self, lChainIn):
		for i in range(1, len(lChainIn)):
			# 1st check if valid block structure
			# ...
			# 2nd check if valid new block
			if (self.isValidNewBlock(lChainIn[i], lChainIn[i - 1]) == False):
				print 'Block ' + str(i) + ' is NOT valid!!!'
				return False
		print 'Block Chain is valid'
		return True

	# Choosing the longest chain
	def replaceChain(self, newChain):
		if (isValidBlockChain(newChain) == True & len(newChain) > len(lChain)):
			print 'Received blockchain is valid. Replacing current blockchain.'
			lChain = newChain
			# broadcastLatest()
		else:
			print 'Received BlockChain invalid'
