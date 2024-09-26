import os
import shutil
from collections import defaultdict

# Dictionary to classify file extensions into folders
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
    'Archives': ['.zip', '.tar', '.gz', '.7z', '.rar'],
    'Code': ['.py', '.java', '.cpp', '.js', '.html', '.css', '.php'],
    'Executables': ['.exe', '.bat', '.sh'],
    'Others': []
}

# Function to get the folder name based on file extension
def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return 'Others'

# Function to organize files into respective folders
def organize_directory(directory):
    if not os.path.exists(directory):
        print("The directory does not exist!")
        return

    # Create a dictionary to track categorized files
    file_map = defaultdict(list)
    
    # Loop through files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, ext = os.path.splitext(filename)
        category = get_category(ext.lower())

        # Ensure the category folder exists
        category_folder = os.path.join(directory, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        # Move the file to the appropriate folder
        new_location = os.path.join(category_folder, filename)
        shutil.move(file_path, new_location)
        file_map[category].append(filename)

    # Output the result
    for category, files in file_map.items():
        print(f"Moved {len(files)} file(s) to {category} folder.")

if __name__ == "__main__":
    # Get directory input from user
    user_directory = input("Enter the directory path to organize: ")
    organize_directory(user_directory)
