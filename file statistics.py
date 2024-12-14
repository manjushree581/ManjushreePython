mport os
import time
file_path = '/content/DoG!!.jpg'
file_stats = os.stat(file_path)
print(f"File size: {file_stats.st_size} bytes")
print(f"Last modified time: {time.ctime(file_stats.st_mtime)}")
print(f"Creation time: {time.ctime(file_stats.st_ctime)}")
print(f"Last accessed time: {time.ctime(file_stats.st_atime)}")
