import os
import shutil

# Define the source directory (current directory) and destination directory
source_dir = '.'
dest_dir = 'model improvements'

# Create the destination directory if it doesn't exist
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Iterate through all files in the source directory
for filename in os.listdir(source_dir):
    # Check if the file starts with "weights-improvement"
    if filename.startswith('weights-improvement'):
        # Construct full file paths
        source_file = os.path.join(source_dir, filename)
        dest_file = os.path.join(dest_dir, filename)
        
        # Move the file
        shutil.move(source_file, dest_file)
        print(f"Moved: {filename}")

print("All weights-improvement files have been moved to the 'model improvements' folder.")