import sys
def read_csv(file_path,separator = ',',fields={}):
	if not file_path.strip():
		print("You must provide a valid file path")
		return
	container = []
	file = None
	try:
		file = open(file_path, "r")
		object_keys = []
		for counter,line in enumerate(file.readlines()):
			line = line.replace('\n', '')
			line = line.split(separator)
			if counter == 0:
				object_keys = line
				continue
			row = {}
			for index,key in enumerate(object_keys):
				row[key] = line[index]
			container.append(row)
			#print(container)
	except Exception as er:
		print(er)
	finally:
		print(container[0:10] if len(container) > 10 else {})
		if file is not None:
			file.close()

	if __name__ == '__main__':
		print(sys.argv)

read_csv("files/tech_funding.csv",",")


