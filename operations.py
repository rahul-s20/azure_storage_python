import os
from azure.storage.blob import ContainerClient, BlobClient, BlobServiceClient, ContentSettings

class FileIO:
    def __init__(self, connection_string: str, container_name: str):
        self.container_client = ContainerClient.from_connection_string(connection_string, container_name)
        self.blob_service_client =  BlobServiceClient.from_connection_string(connection_string)
        self.my_container = self.blob_service_client.get_container_client(container_name)

    def save_blob(self,download_path: str, file_name: str, file_content: bytes):
        download_file_path = os.path.join(download_path, file_name)
        os.makedirs(os.path.dirname(download_file_path), exist_ok=True)
        with open(download_file_path, "wb") as file:
            file.write(file_content)

    def upload(self, files):
        print("Started uploading....")
        for file in files:
            blob_client = self.container_client.get_blob_client(file.name)
            with open(file.path, "rb") as data:
                blob_client.upload_blob(data)
                print(f"{file.name} uploaded successfully.")

    def download_all_blobs_in_container(self, download_path: str):
        print("Started downloading....")
        my_blobs = self.my_container.list_blobs()
        for blob in my_blobs:
            print(blob.name)
            bytes = self.my_container.get_blob_client(blob).download_blob().readall()
            self.save_blob(download_path, blob.name, bytes)    
            print("Download finished successfully.")        