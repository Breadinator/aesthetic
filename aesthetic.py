# Licensed under the Copyfree Open Innovation License, which can be found in the next comment.
# http://copyfree.org/content/standard/licenses/coli/license.txt
# (Doesn't really need a license, but #YOLO am i rite?)

import sys

def strToAesthetic(ugly): #pass in a string
	aesthetic = ""
	
	for n, i in enumerate(ugly):
		if n == len(ugly) - 1:
			aesthetic += str(i).lower() + "   "
		else:
			aesthetic += str(i).lower() + " "

	return aesthetic

if __name__ == "__main__":
	ret = ""
	for n, i in enumerate(sys.argv):
		if n == 0:
			continue
		ret += strToAesthetic(sys.argv[n])
	print(ret)