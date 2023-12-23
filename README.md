# AI-Enhanced Wildlife Monitoring System

This project aims to develop a basic AI system to help in wildlife conservation efforts by monitoring animal populations and behaviors using camera trap images. The system identifies different animal species and analyzes the time and frequency of animal appearances to infer patterns in wildlife behavior. The collected data is visualized in a user-friendly dashboard.

## Key Features

1. **Animal Species Identification:** Utilize a simple machine learning model to identify different animal species captured in camera trap images.
2. **Behavioral Analysis:** Analyze the time and frequency of animal appearances to infer patterns in wildlife behavior.
3. **Data Visualization:** Create a user-friendly dashboard to display the collected data, showing trends and insights about wildlife activities.

## Technology Requirements

- Python for development, with libraries like Pandas and Matplotlib for data analysis and visualization.
- A beginner-friendly machine learning platform like Google's Teachable Machine or AutoML for model training.
- Cloud storage (like Google Cloud Storage) for storing camera trap images and data.
- Basic knowledge of cloud computing for setting up and managing the cloud environment.

## Installation

To install the required libraries, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the project, execute the following command:

```bash
python main.py
```

## Project Structure

- `requirements.txt`: Contains the necessary Python libraries required for this project.
- `data_collection.py`: Contains the code for collecting and uploading camera trap images to cloud storage.
- `model_training.py`: Contains the code for training the machine learning model for animal species identification.
- `data_analysis.py`: Contains the code for analyzing the collected data to infer patterns in wildlife behavior.
- `dashboard.py`: Contains the code for creating a user-friendly dashboard to visualize the collected data.
- `main.py`: The main script that ties all the other scripts together.

## Note

Please replace `'your-bucket-name'` in the scripts with the name of your Google Cloud Storage bucket.

## License

This project is licensed under the terms of the MIT license.
