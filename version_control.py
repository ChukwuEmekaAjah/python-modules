import hashlib 
import sys
import os
import pickle 
def version_control(file_path):
	file = None
	try:
		file = open(file_path,'r')
	except Exception as e:
		print("there was an error ouch")
		print(e)
	else:
		file_map = {}
		for (line_number, line) in enumerate(file.readlines()):
			#print(line)
			#print("ewoooo")
			line_hash = hashlib.md5(bytes(line,'utf-8')).hexdigest()
			file_map[line_hash] = line_number 
		storage = open("dump.txt","wb")
		pickle.dump(file_map,storage)
	finally:
		if(file is not None):
			file.close()
# this is a fucking comment
# and this one too
def compare(file_path):
	file = None
	source = open("dump.txt","rb")
	old_map = pickle.load(source)
	difference = {}
	try:
		file = open(file_path,'r')
	except Exception as e:
		print("there was an error")
		print(e)
	else:
		file_map = {}
		for (line_number, line) in enumerate(file.readlines()):
			#print(line)
			line_hash = hashlib.md5(bytes(line,'utf-8')).hexdigest()
			file_map[line_hash] = line_number 
		file_map_keys = file_map.keys()
		for (key, value) in file_map.items():
			if old_map.get(key):
				print(key + " : "+str(value))
			else:
				print("New lines "+str(value))
	finally:
		if(file is not None):
			file.close()

#version_control("version_control.py")
compare("version_control.py")