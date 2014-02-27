#!/usr/bin/env python3

import urllib.request # to download HTML source
import sys # to access CLI arguments
from bs4 import BeautifulSoup # to parse HTML source

version = 0.01

def printUsageInfo():
	helpMsg = """Usage:
	sjp.py <word>
	sjp.py (-h | --help | /?)
	sjp.py (-v | --version)"""
	print(helpMsg)

def printVersionInfo():
	versionMsg = "sjp.py " + str(version)
	print(versionMsg)

def getDefinition(word):
	url = 'http://sjp.pl/' + word
	html = urllib.request.urlopen(url).read()

	soup = BeautifulSoup(html)

	# checks if definition is in dictionary:
	if soup.find_all('span', style="color: #e00;"):
	  print("[Error] \"" + word + "\" not found")
	  exit()

	# definition is in dictionary, continue:
	ex = soup.find_all('p', style="margin-top: .5em; font-size: medium; max-width: 30em; ")[0]
	return ex.contents[0::2] # returns a list of lines of definition

def main():
	if len(sys.argv) > 1:
		if sys.argv[1] in ["-h", "--help", "/?"]:
			printUsageInfo()
			exit()
		elif sys.argv[1] in ["-v", "--version"]:
			printVersionInfo()
			exit()
		else:
			print('\n'.join(getDefinition(sys.argv[1])))
	else:
		printUsageInfo()
		exit()
	
if __name__ == "__main__":
	main()