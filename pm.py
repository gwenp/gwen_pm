#! /usr/bin/env python
import os,ConfigParser,commands,sys

directory = "."

def scanrec(dirname):
	found = 0
	for f in os.listdir(dirname):
		if(f==".projectroot"):
			return os.path.abspath(dirname)
			found = 1
	if(os.path.abspath(dirname)!="/" and found==0):
		return scanrec(dirname+"/..")

projectFile=scanrec(directory)

def config_value_subsitution(text):
	text = text.replace("{rootDir}", projectFile)
	return text

if(projectFile):
	if (len(sys.argv) > 1):
		projectFile
		config = ConfigParser.RawConfigParser()
		config.read(projectFile + "/.projectroot")
		
		if( sys.argv[1] == 'build' ):
			print os.system(config_value_subsitution(config.get('Building', 'build_command')))
		elif( sys.argv[1] == 'compile' ):
			print os.system(config_value_subsitution(config.get('Building', 'compile_command')))
		elif( sys.argv[1] == 'execute' ):
			print os.system(config_value_subsitution(config.get('Building', 'execute_command')))
		else:
			print projectFile
	else:
		print projectFile
else:
	print "pas de fichier .projectroot"
