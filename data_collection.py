```python
# Import necessary libraries
import os
import pandas as pd
from google.cloud import storage

# Define constants
BUCKET_NAME = 'your-bucket-name'  # Replace with your bucket name
IMAGE_DIR = 'camera_images'  # Directory where images are stored locally
CSV_FILE = 'image_data.csv'  # CSV file to store image metadata

# Initialize a storage client
storage_client = storage.Client()

def list_files(directory):
    """List all files in a directory"""
    files = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            files.append(filename)
    return files

def upload_to_bucket(blob_name, path_to_file, bucket_name):
    """Upload data to a bucket"""
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)

    print(f"File {blob_name} uploaded to {bucket_name}.")

def collect_data():
    """Main function to collect and upload data"""
    # List all image files
    image_files = list_files(IMAGE_DIR)

    # Create a DataFrame to store image metadata
    df = pd.DataFrame(image_files, columns=['image_file'])

    # Upload each image to the cloud storage
    for image_file in image_files:
        upload_to_bucket(image_file, os.path.join(IMAGE_DIR, image_file), BUCKET_NAME)

    # Save image metadata to a CSV file
    df.to_csv(CSV_FILE, index=False)

if __name__ == "__main__":
    collect_data()
```
