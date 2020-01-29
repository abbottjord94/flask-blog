import os
import json

class Database():
	_data = []
	_filename=os.path.join(os.path.dirname(__file__)) + "/database.json"

	def load(self):
		with open(self._filename) as json_file:
			self._data = json.load(json_file)

	def save(self):
		with open(self._filename, 'w') as outfile:
			json.dump(self._data, outfile)

	def insert(self,key,obj):
		self.load()
		self._data[key] = obj
		self.save()

	def delete(self,key):
		self.load()
		self._data.pop(key, None)
		self.save()

	def data(self):
		return self._data
