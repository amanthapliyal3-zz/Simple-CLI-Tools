import argparse

parser = argparse.ArgumentParser()
parser.add_argument("f", help = "Input file !!")
args = parser.parse_args()

try :
	file = open(args.f)
except :
	print("File do not exist !!!")
	exit()

print("Words in output File --->>> " ,len(file.read().split('\n')))
