import re
class ReadMe:
	def __init__(self,file_path, destination = None):
		self.file_obj = None
		self.html_string = None
		self.tags_map = {
			"#":"h1",
			"##":"h2",
			"###":"h3",
			"*":"li",
			"*word*":"i",
			"**word**":"b"
		}
		self.placeholder_patterns = ('#','*')
		self.placeholders = ('#+','\*')
		self.placeholders_re = '|'.join(self.placeholders)
		self.file_lines = []
		try:
			self.file_obj = open(file_path,"r")
		except Exception as er:
			print("There was an error trying to open the file")
			print(er)
		else:
			for line in self.file_obj.readlines():
				line = line.strip()
				if line:
					self.file_lines.append(line)
		finally:
			if self.file_obj is not None:
				self.file_obj.close()

	def convert_to_html(self):
		maps = []
		match = None
		
		line_number = 0
		while line_number < len(self.file_lines):
			match = re.match(self.placeholders_re,self.file_lines[line_number])
			holder = {}
			if self.file_lines[line_number].startswith(self.placeholder_patterns) and match is not None:
				placeholder = self.file_lines[line_number][match.start():match.end()]
				holder['tag'] = self.tags_map[placeholder]
				holder['text'] = self.file_lines[line_number][match.end():]
				maps.append(holder)
				line_number += 1
			else:
				holder['tag'] = 'p'
				holder['text'] = ''
				while line_number < len(self.file_lines) and re.match(self.placeholders_re,self.file_lines[line_number]) is None:
					print(self.file_lines[line_number])
					print("line number is ", line_number)
					holder['text'] += self.file_lines[line_number]
					maps.append(holder)
					line_number += 1
			match = None
		print(maps)



file = ReadMe("files/readme/test1.md")
file.convert_to_html()