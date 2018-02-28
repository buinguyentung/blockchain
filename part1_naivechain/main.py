import sys
import pickle
from blockchain import *


def main():
	print "CREATING A CHAIN OF BLOCKS..."

	bChain = BlockChain()
	# Generate block 0
	bChain.createGenesisBlock()

	# Generate block 1
	blockData1 = 'Satoshi sent Tung 100000btc; '
	bChain.addNewBlock(blockData1)

	# Generate block 2
	blockData2 = 'Tung sent his mom 1000btc; ' + 'Tung sent his sister 10000btc; '
	bChain.addNewBlock(blockData2)

	bChain.isValidBlockChain(bChain.lChain)

	for i in range(0, len(bChain.lChain)):
		bChain.printBlockInfo(bChain.lChain[i])

if __name__ == '__main__':
	main()
