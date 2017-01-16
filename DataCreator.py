import random, string

DATA_BLANK = "{{ \"{dataTitle}\": [{dataContent}] }}"
ITEM_BLANK = "{{ \"{itemName}\": {{ {itemContent} }} }}"
ITEM_CONTENT = "\"{contentName}\": {data}"

class DataCreator:

	DATA = ""

	def __init__(self, dataTitle="data", numItemsToGenerate=10, dataTypeArr=[["integer", "IntDataTitle", [0, 100]], ["string", "StringDataTitle", [1, 15]], ["boolean", "BoolDataTitle"]]):
		print "Generating Data..."

		items = ""
		for x in range(numItemsToGenerate):
			itemContent = ""
			print "____Generating Item#" + str(x) + "..."

			for index, i in enumerate(dataTypeArr):
				print "________Generating Item#" + str(x) + " " + i[1] + " data..."

				if (i[0] == "integer" or i[0] == "int" or i[0] == "Int" or i[0] == "Integer"):
					data = random.randint(i[2][0], i[2][1])

				elif (i[0] == "string" or i[0] == "str" or i[0] == "String" or i[0] == "Str"):
					data = '"' + ''.join(random.choice(string.lowercase) for a in range(random.choice([i[2][0], i[2][1]]))) + '"'

				elif (i[0] == "boolean" or i[0] == "bool" or i[0] == "Boolean" or i[0] == "Bool"):
					data = random.choice(["true", "false"])

				elif (i[0] == "float" or i[0] == "Float"):
					data = random.uniform(i[2][0], i[2][1])

				else:
					raise ValueError('Invalid Type...')

				itemContent += ITEM_CONTENT.format(contentName=i[1], data=str(data))
				if index < len(dataTypeArr) - 1:
					itemContent += ", "
			items += ITEM_BLANK.format(itemName="Item" + str(x), itemContent=itemContent)
			if x < numItemsToGenerate - 1:
				items += ", "

		self.DATA = DATA_BLANK.format(dataTitle=dataTitle, dataContent=items)
		print self.DATA


	def export(self, filename):
		print "Exporting " + filename + ".json"
		with open(filename + ".json", "w") as f:
			f.write(self.DATA)
		
