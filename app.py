import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import joblib
import warnings


# Create a Tkinter GUI window
window = tk.Tk()
window.title("Turkish Letters Detection App")

# Ignore specific warning
warnings.filterwarnings("ignore", message="X does not have valid feature names")

# Load model
svm_model = joblib.load('model/TurkishLetterRecognition')

def preprocess_image(filepath):
    # Load image
    image = Image.open(filepath)
    # Convert to grayscale
    image = image.convert('L')
    # Resize image to 128x128
    image = image.resize((128, 128))
    # Convert to numpy array
    image_array = np.array(image)
    # Thresholding
    threshold = 128
    binary_image = np.where(image_array > threshold, 0, 1)
    # Flatten
    linear_array = binary_image.flatten()
    return linear_array.reshape(1, -1)

def predict_letter(filepath):
    """Predict the bill using the selected model."""
    try:
        features = preprocess_image(filepath)
        predicted_label = svm_model.predict(features)
        prediction_label.config(text=f"Predicted Label: {predicted_label[0]}", fg="blue", font=("Arial", 14, "bold"))
    except Exception as e:
        prediction_label.config(text=f"An error occurred: {str(e)}", fg="red", font=("Arial", 12, "italic"))

def open_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        display_image(filepath)
        predict_letter(filepath)

# Function to center the window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width / 2)
    y_coordinate = (screen_height / 2) - (height / 2)
    window.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

# Centering the window
center_window(window, 400, 400)

# Create a frame for image display
image_frame = tk.Frame(window)
image_frame.pack(pady=10)

# Create a label for displaying the image
image_label = tk.Label(image_frame)
image_label.pack()

# Function to display the uploaded image
def display_image(filepath):
    image = Image.open(filepath)
    image.thumbnail((200, 200))  # Resize image to fit within 200x200
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

# Create a label for displaying prediction
prediction_label = tk.Label(window, text="Upload an image to predict", font=("Arial", 12))
prediction_label.pack(pady=10)

# Create a green button to upload the image
upload_button = tk.Button(window, text="Upload Image", command=open_file, width=30, bg="green", fg="white")
upload_button.pack(pady=10)

# Run the GUI application
window.mainloop()