# A POC to Communicate with Azure storage by using python

First we need to install the requirements.txt file : pip install -r requirements.txt

The config.yaml contains necessary environment variable such as :

connection_string: "string...."
storage_container_name: "string"
local_file_path: "D:/Projects/azure/azure_storage/files_upload"
download_file_path: "D:/Projects/azure/azure_storage/downloaded_files"

In order to upload files to blob container run upload_main.py
In order to download all the files from the container run download_main.py
