#Organize files
import os
#current_directory = os.getcwd()									#get the current directory
current_directory = "E:\\Users\\Tyler\\Downloads"

def sortFile(directory, file, prefix, extention):
	
	print("Detected "+ extention)
	
	folder = extention.replace(".","")+"s"
	
	if not os.path.exists(os.path.join(directory,folder)):					#check to see if folder for extention exists
		os.makedirs(os.path.join(directory,folder))
		os.rename(os.path.join(directory,file), os.path.join(directory,folder,file))    #move file into new folder, duplicates will not occur since the folder is empty
	elif not os.path.exists(os.path.join(directory,folder,file)):				#Prevent overwriting duplicate names
		os.rename(os.path.join(directory,file), os.path.join(directory,folder,file))
	else:
		n = 1
		temp = '('+str(n)+')'
		while os.path.exists(os.path.join(directory,folder,prefix+temp+extention)):
			n = n+1										#renames a multiple of the original name
			temp = '('+str(n)+')'
		os.rename(os.path.join(directory,file), os.path.join(directory,folder,prefix+temp+extention))


def organize(directory):
	n=0
	temp=""
	list_of_file = os.listdir(directory)
	for file in list_of_file:									#Search through file and place all major extentions in a directory 
		#print("Now sorting " + file)
		file_prefix = os.path.splitext(file)[0]
		file_extention = os.path.splitext(file)[1]
		if not file_extention == '':
			sortFile(directory, file, file_prefix, file_extention)
		
#print (current_directory)
#print (os.listdir(current_directory))
organize(current_directory)
