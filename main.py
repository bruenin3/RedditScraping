import os
import subprocess

# Get the root directory of your project
root_directory = os.path.dirname(os.path.abspath(__file__))

# Define the paths to your separate scripts relative to the root directory
reddit_scraper_script = os.path.join(root_directory, 'scraping', 'RedditScraper.py')
face_extraction_script = os.path.join(root_directory, 'facial_recognition', 'FacialRecognition.py')

# Run the Reddit scraper script
subprocess.run(['python', reddit_scraper_script])

# Run the face extraction script
subprocess.run(['python', face_extraction_script])
