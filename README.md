# SI676_Assignment1

This readme file was generated on 2022-10-05 by Summer Mengarelli (smengare).

### GENERAL INFORMATION

Title of Dataset: **File Inventory for 'Data' Directory, SI676 Assignment 1**

**Author/PI**
Name: Summer Mengarelli
Institution: University of Michigan School of Information
Email: smengare@umich.edu

**Dates of data collection:**
Data source directory was cloned from Github (source below) on 2022-10-05.
File inventory was generated on 2022-10-05.


### SHARING/ACCESS INFORMATION

**Licenses/restriction placed on this data:** None.

**Publicly accessible location of the data source:** https://github.com/morskyjezek/networked-services-labs/tree/main/data

**Recommended citation for this dataset:** #enter here after generated in github


### DATA & FILE OVERVIEW

**File List:**
    data_directory-file-manifest.csv | CSV dataset.
    mengarelli_676_HW1.py | The Python script used to generate the inventory data.
    README.md | This file, the readme.
    CITATION.cff | Plain text file to allow citation widget on Github repo hosting this dataset.


### METHODOLOGICAL INFORMATION

**Description of methods used for collection/generation of data:**

Data was generated by cloning Jesse Johnston's Github repository, then creation of a Python script that access the target directory, iterated through its subdirectories, checked for files, and created dictionaries containing those files' metadata. Metadata was then written out to the final CSV file.

**Methods:**

1. Downloading the source data from Jesse Johnston's Github repository was executed using the 'git clone' command line command.

2. The Python script used to generate the data inventory used the 'os', 'datetime', 'hashlib', and 'csv' modules. The script set a file path to the 'data' directory. The function 'get_checksum' was sourced from SI676 course materials and was used to generate MD5 and SHA526 checksums for each file in the 'data' directory. The 'os' function 'os.walk()' was used to iterate through the 'data' directory and its subdirectories and construct the dictioanries containing each file's metadata. Finally, 'csv.DictWriter()' from the 'csv' module was used to write the inventory data out to the CSV dataset found in this repository.

**Instrument/Software-Specific Information:**
    Software used to write script: Python 3.9.13
    Python modules: os, datetime, hashlib, csv


### DATA-SPECIFC INFORMATION FOR: data_directory-file-manifest.csv

**Number of fields:** 7
**Number of rows:** 50

**Field List:**
    filename | the basename of a file in the 'data' directory
    absolute_path | the absolute path of a file in the 'data' directory
    file_extension | the extension (.*) of a file in the 'data' directory
    size_bytes | the size, in bytes, of a file in the 'data' directory
    modify_datetime | the last time and date of modification of a file in the 'data' directory, formatted following ISO 8601
    md5_checksum | the MD5 hash checksum for a file in the 'data' directory
    sha256_checksum | the SHA-256 hash checksum for a file in the 'data' directory

Missing data codes?