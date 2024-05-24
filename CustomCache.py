import os

# Define the custom cache directory
custom_cache_dir = "/home/dcsadmin/Documents/PGreeting/"

# Set the environment variable
os.environ['HF_HOME'] = custom_cache_dir

# Ensure the directory exists
os.makedirs(custom_cache_dir, exist_ok=True)

