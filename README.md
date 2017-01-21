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
To export your your data to a json file, call the **.export("NameOfYourFileHere")** on your data object. The file will be saved in the same directory as the DataCreatoy.py file.
**Example:**
```Python
newDataObject.export("MyNewData")
```


## License
MIT License


Copyright (c) 2017 Jacob A. Gornall


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:


The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
