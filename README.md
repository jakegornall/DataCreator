# DataCreator
### *DataCreator is a python tool for quickly generating random data for testing your applications.*


## Installation
```shell
$ git clone https://github.com/jakegornall/DataCreator
```
*NOTE:  If using DataCreator within your application, make sure you copy "DataCreator.py" into your application's root directory.*



## Usage
**First, import the DataCreator class.**
```Python
from DataCreator import DataCreator
```
**Next, create a new DataCreator object/instance with your desired parameters.**

**The DataCreator object takes the following parameters:**
* dataTitle: a string indicating the name of your data.
* numItemsToGenerate: an integer indicating how many items you want to create.
* dataTypeArr: an array where each element of the array is a description of an items properties.
	* example dataTypeArr element:  ["integer", "Quantity", [0, 25]]
	* index 0 takes a string "integer", "string", "boolean".
	* index 1 takes a string indicating the name of the data.
	* index 2 takes an array of two numbers indicating a range. the above will generate an integer between 0-25 called "Quantity".

**Example:**
```Python
newDataObject = DataCreator(
	dataTitle="MyData",
	numItemsToGenerate= 10,
	dataTypeArr=[
		["integer", "IntDataTitle", [0, 100]],
		["string", "StringDataTitle", [10, 15]],
		["boolean", "BoolDataTitle"]
	])
```
To export your your data to a json file, call the **.export("NameOfYourFileHere")** method on your data object. The file will be saved in the same directory as the DataCreatoy.py file.
**Example:**
```Python
newDataObject.export("MyNewData")
```

Use the **.getData()** method on your data object to return your data as a python dictionary.

The **.getDataString()** method returns your data as a json string.
