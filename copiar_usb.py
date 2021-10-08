import shutil
import os

def src_to_dst(src, dst):
	cpy_files = 0
	with os.scandir(src) as songs:
		for song in songs:
			if song.is_file():
				if str(song.name) not in dst:
					shutil.copy2(song, dst)
					cpy_files += 1
	return cpy_files

copied_files = src_to_dst("C:/Users/Eduardo/Desktop/Music", "E:/Music")

if copied_files != 0:
	print("The songs has been sucessfully copied!\nCopied Elements: {number}".format(number=copied_files))
else:
	print("Something went wrong in the process :/\nCopied Elements: {number}".format(number=copied_files))