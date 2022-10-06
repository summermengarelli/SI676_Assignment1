

### This script is designed to create an inventory of the files
### contained in the 'data' folder and their associated metadata.

import os
from datetime import datetime
import hashlib
import csv


### Find the directory ##########

datapath = os.path.join(os.getcwd(),'networked-services-labs','data')


### checksums function ##########

def get_checksum(filePath, checksum_type):
    '''This is a helper function to create a checksum.
    In this example we will focus on MD5, which can be used to check data integrity.

    The filePath value argument be a string representing a valid path.
    The checksum_type argument should be a valid type of checksum.

    The function returns the string of characters for an MD5 or SHA256 checksum.
    The is function only allows you to create MD5 or SHA 256 and will result in an error for other types.'''
    checksum_type = checksum_type.lower().replace(' ', '')

    with open(filePath, 'rb') as f:
        bytes = f.read()
        if checksum_type == 'md5':
            hash_string = hashlib.md5(bytes).hexdigest()
        elif checksum_type == 'sha256':
            hash_string = hashlib.sha256(bytes).hexdigest()
        else:
            raise('{} is not a hash function supported by this program. You must ask for MD5.')
    return hash_string


### Script ##########

file_list = list()
headers = ['filename', 'absolute_path', 'file_extension', 'size_bytes', 'modify_datetime', 'md5_checksum', 'sha256_checksum']


for folder_name, subfolders, filenames in os.walk(datapath):
    for file in filenames:
        file_path = os.path.join(os.path.abspath(folder_name), file)
        if os.path.isfile(file_path):
           file_info = {
            'filename' : os.path.basename(file),
            'absolute_path' : os.path.abspath(os.path.join(folder_name, file)),
            'file_extension' : os.path.splitext(file)[1],
            'size_bytes' : os.path.getsize(file_path),
            'modify_datetime' : datetime.strftime(datetime.fromtimestamp(os.path.getmtime(file_path)), "%Y-%m-%dT%H:%M:%S"),
            'md5_checksum' : get_checksum(os.path.join(folder_name, file), 'md5'),
            'sha256_checksum' : get_checksum(os.path.join(folder_name, file), 'sha256')}
        file_list.append(file_info)



with open('data_directory-file-manifest.csv', 'w') as csvfile:
    fileManifest = csv.DictWriter(csvfile, fieldnames=headers)
    fileManifest.writeheader()
    for file in file_list:
        fileManifest.writerow(file)






