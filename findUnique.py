#Script to create a new file with only unique elements

import argparse
result = "unique.txt"
parser = argparse.ArgumentParser(description = "Script that creates a File with only unique elements!!")

parser.add_argument("b",help = "The base record file to be used for matching")
parser.add_argument("s", help = "Source file for matching against the records")
parser.add_argument("-r","--result",help = "Name of the output file !!")
parser.add_argument("--wc",help = "No of words in the output file")
args = parser.parse_args()
#Reading from base file
base_ = open(args.b)
inp_ = open(args.s)
out_ = open(args.result, "w")
base_dict = set()
for word in base_.read().split('\n'):
	base_dict.add(word)

for word in inp_.read().split('\n'):
	if word not in base_dict: out_.write(word+'\n')

base_.close()
inp_.close()
out_.close()

if args.wc :
	out_ = open(args.result)
	print("words :",len(out_.read().split('\n')))
	out_.close()
print("--Complete--")








