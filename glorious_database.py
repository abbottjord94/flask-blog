import os
import json

class Database():
	_data = {}
	_filename = ""
	_dirpath = ""

	def __init__(self, _fn="database.json", _dp=os.path.dirname(__file__)):
		self._filename = os.path.join(_dp, _fn)
		if not os.path.exists(self._filename):
			with open(self._filename, 'w+') as outfile:
				outfile.write("{}")
				outfile.close()
		else:
			with open(self._filename) as json_file:
				self._data = json.load(json_file)
				json_file.close()

	def load(self):
		with open(self._filename) as json_file:
			self._data = json.load(json_file)
			json_file.close()

	def save(self):
		with open(self._filename, 'w+') as outfile:
			json.dump(self._data, outfile)
			outfile.close()

	def insert(self,key,obj):
		self.load()
		self._data[key] = obj
		self.save()

	def delete(self,key):
		self.load()
		self._data.pop(key, None)
		self.save()

	def data(self):
		self.load()
		return self._data
