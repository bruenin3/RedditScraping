import praw
import requests
import os

# Get the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the path to the "images" folder in the root directory
root_directory = os.path.dirname(script_directory)
image_folder = os.path.join(root_directory, 'images')

# Create the folder if it doesn't exist
os.makedirs(image_folder, exist_ok=True)

# Update your app credentials
reddit = praw.Reddit(
client_id='client_id',
client_secret='client_secret',
user_agent='user_agent',
username = 'username',
password = 'password'
)

# Access the r/pics subreddit
subreddit = reddit.subreddit('pics')

# Retrieve the top 50 posts
top_posts = subreddit.top(limit=50)

# Loop through the posts, download the image, and save post info
for post in top_posts:
    try:
        # Download the image
        image_url = post.url
        response = requests.get(image_url)
        response.raise_for_status()  # Check for connection or HTTP errors

        # Save the image with a filename based on the post's ID
        image_filename = os.path.join(image_folder, f"{post.id}.jpg")
        with open(image_filename, 'wb') as f:
            f.write(response.content)

        # Print post information
        print(f"Title: {post.title}")
        print(f"Score (Upvotes): {post.score}")
        print(f"Image saved as: {image_filename}")
        print("------------")

    except requests.exceptions.RequestException as e:
        # Handle connection or HTTP errors
        print(f"Skipping post due to error: {str(e)}")
        continue
