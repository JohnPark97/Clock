import os

# Path to the directory
directory = 'assets/img'

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file starts with 'cropped_' and ends with '.png'
    if filename.startswith('cropped_') and filename.endswith('.png'):
        # Create the new file name by removing the 'cropped_' prefix
        new_filename = filename.replace('cropped_', '', 1)
        
        # Full path for the old and new filenames
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_filepath, new_filepath)
