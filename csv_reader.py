import sys
from os import linesep

class CSVParser:
	def __init__(self, file_path, separator = ','):
		if not file_path.strip():
			print("You must provide a valid file path")
			return
		self.file_path = file_path.strip()
		self.separator = separator
		self.data_table = []
		self.file = None
		try:
			self.file = open(self.file_path, "r", encoding="utf-8")
		except Exception as er:
			print("There was an error trying to instantiate the parser")
			print(er)

	def toJSON(self, file_destination = 'to.json', fields = []):
		if self.file:
			object_keys = []
			for line_number, line in enumerate(self.file.readlines()):
				line = line.replace(linesep, '').split(self.separator)
				if line_number == 0:
					object_keys = fields if len(fields) > 0 else line 
					continue
				row = {}
				for index,key in enumerate(object_keys):
					row[key] = line[index]
				print(row)
				self.data_table.append(row)

	@property 
	def data(self):
		return self.data_table

parser = CSVParser("files/tech_funding.csv",",")
parser.toJSON()
#print(parser.data)

"""
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
"""
#read_csv("files/tech_funding.csv",",")


