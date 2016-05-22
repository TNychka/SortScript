import os
import re

sortFolders = {
	"jpg" : "pictures",
	"png" : "pictures",
	"gif" : "pictures",

	"exe" : "programs",
	"cpp" : "programs",
	"hpp" : "programs"
}

renamingRules = {	
	"_by_.*" : "",
	" by .*" : "",
	"tumblr.*" : "unnamed",
	"_" : " ",	
}


def rename(fileName):
	for regex in renamingRules:
		p = re.compile(regex)
		fileName = re.sub(regex, renamingRules[regex], fileName)
	return fileName



def sortFile(directory, file, prefix, extention):

	if extention in sortFolders:
		sortFolder = sortFolders[extention]
	else:
		sortFolder = "Unknown"

	sortFolderExists = os.path.exists(os.path.join(directory,sortFolder))
	fileLocation = os.path.join(directory,file)
	fileDestination = fileLocation
	prefix = rename(prefix)
	fileNameExists = os.path.exists(os.path.join(directory,sortFolder,prefix+"."+extention))

	if not sortFolderExists:							#check to see if folder for extention exists
		os.makedirs(os.path.join(directory,sortFolder))
		fileDestination = os.path.join(directory,sortFolder,prefix+"."+extention)
	elif fileNameExists:								#Prevent overwriting duplicate names																			#If duplicate exists, rename to multiple	
		n = 1	
		temp = ' ('+str(n)+')'
		while os.path.exists(os.path.join(directory,sortFolder,prefix+temp+"."+extention)):
			n += 1									#renames a multiple of the original name
			temp = ' ('+str(n)+')'
		fileDestination = os.path.join(directory,sortFolder,prefix+temp+"."+extention)
	else:
		fileDestination = os.path.join(directory,sortFolder,prefix+"."+extention)
	
	if not fileDestination == fileLocation:
		os.rename(fileLocation, fileDestination) #move file into new folder, duplicates will not occur since the folder is empty


def organize(directory):
	list_of_file = os.listdir(directory)
	for file in list_of_file:									#Search through file and place all major extentions in a directory 
		file_prefix = os.path.splitext(file)[0]
		file_extention = os.path.splitext(file)[1]
		if (not file_extention == ''
			and not file == "sort.py"):
			sortFile(directory, file, file_prefix, file_extention.replace(".", ""))


def main():
	current_directory = os.getcwd()
	print (current_directory)
	organize(current_directory)


main()
