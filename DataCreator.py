# MIT License
#
# Copyright (c) 2017 Jacob A. Gornall
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import random, string, os, json

base_dir = os.path.dirname(__file__)

DATA_BLANK = "{{ \"{dataTitle}\": [{dataContent}] }}"
ITEM_BLANK = "{{ \"{itemName}\": {{ {itemContent} }} }}"
ITEM_CONTENT = "\"{contentName}\": {data}"

class DataCreator:

	DATA = ""

	def __init__(self, dataTitle="data", numItemsToGenerate=10, dataTypeArr=[["integer", "IntDataTitle", [0, 100]], ["string", "StringDataTitle", [10, 15]], ["boolean", "BoolDataTitle"]]):
		'''Generates new data set when a new DataCreator object is created.'''
		print "Generating Data..."

		items = ""
		for x in range(numItemsToGenerate):
			itemContent = ""
			for index, i in enumerate(dataTypeArr):
				if i[0].lower() in ["integer", "int"]:
					data = random.randint(i[2][0], i[2][1])

				elif i[0].lower() in ["string", "str"]:
					data = '"' + ''.join(random.choice(string.lowercase) for a in range(random.choice([i[2][0], i[2][1]]))) + '"'

				elif i[0].lower() in ["boolean", "bool"]:
					data = random.choice(["true", "false"])

				elif i[0].lower() == "float":
					data = random.uniform(i[2][0], i[2][1])
				else:
					raise ValueError('Invalid Type: ' + '"' + i[0] + '"')

				itemContent += ITEM_CONTENT.format(contentName=i[1], data=str(data))
				if index < len(dataTypeArr) - 1:
					itemContent += ", "
			items += ITEM_BLANK.format(itemName="Item" + str(x), itemContent=itemContent)
			if x < numItemsToGenerate - 1:
				items += ", "

		self.DATA = DATA_BLANK.format(dataTitle=dataTitle, dataContent=items)
		print "Data Creation Complete..."


	def getData(self):
		'''Returns json data as dictionary.'''
		if self.DATA != "":
			return json.loads(self.DATA)
		else:
			raise ValueError('No data to return...')


	def getRawDataString(self):
		'''Returns DATA as string.'''
		return self.DATA


	def export(self, filename):
		'''Exports DATA to a json file.'''
		print "Exporting " + filename + ".json"
		with open(filename + ".json", "w") as f:
			f.write(self.DATA)
		print "File Saved At: " + base_dir + "\\" + filename + ".json"
