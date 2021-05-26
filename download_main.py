from config import load_config, get_files
from operations import FileIO



if __name__ == '__main__':
    configuration = load_config()
    upload_object = FileIO(configuration["connection_string"], configuration["storage_container_name"])
    upload_object.download_all_blobs_in_container(configuration['download_file_path'])
