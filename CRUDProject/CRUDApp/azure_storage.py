from azure.storage.blob import BlobServiceClient

# Your connection string and container name
connection_string = "AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;DefaultEndpointsProtocol=http;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;"
container_name = "storagecommoncontainer"
file_path = "C:\Users\vasudev pareek\Downloads\MyDownloadedFile"  # Replace with your file path
blob_name = "my_uploaded_test.jpg"  # Name in Azure Storage

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Get the container client
container_client = blob_service_client.get_container_client(container_name)

# Upload the file
with open(file_path, "rb") as data:
    container_client.upload_blob(name=blob_name, data=data, overwrite=True)

print(f"File '{file_path}' uploaded to container '{container_name}' as '{blob_name}'")
