#!/bin/bash

# Clone the repository
git clone https://github.com/Skuldur/Classical-Piano-Composer.git

# Navigate to the cloned repository
cd Classical-Piano-Composer

# Create the destination directory if it doesn't exist
mkdir -p ../ai-music-project/midi_songs

# Copy the .mid files to the destination directory
cp midi_songs/*.mid ../ai-music-project/midi_songs/

# Go back to the original directory
cd ..

# Optionally, remove the cloned repository if no longer needed
rm -rf Classical-Piano-Composer
