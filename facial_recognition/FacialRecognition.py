import cv2
import os

# Load the pre-trained face detection model (you might need to download the model)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Get the path of the current script (facial_recognition/FacialRecognition.py)
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the path to the directory containing your images (in the root directory)
image_directory = os.path.join(script_directory, '..', 'images')  # Go up one level to the root directory

# Define the directory to save extracted faces (in the root directory)
output_directory = os.path.join(script_directory, '..', 'faces')

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Iterate through image files
for filename in os.listdir(image_directory):
    if filename.endswith(('.jpg', '.png', '.jpeg')):  # Add more image extensions if needed
        # Load the image
        image_path = os.path.join(image_directory, filename)
        image = cv2.imread(image_path)

        # Check if the image was loaded successfully
        if image is not None:
            # Convert the image to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Process and save each detected face
            for i, (x, y, w, h) in enumerate(faces):
                # Extract the face from the image
                face = image[y:y + h, x:x + w]

                # Save the face to a separate file in the output_directory
                face_filename = f'{filename}_face_{i}.jpg'
                face_output_path = os.path.join(output_directory, face_filename)
                cv2.imwrite(face_output_path, face)

                # Display a success message
                print(f"Success: Face extracted from {filename} and saved as {face_filename}")
        else:
            print(f"Error: Unable to load the image {filename}")
