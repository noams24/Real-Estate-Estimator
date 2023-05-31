import os
import pandas as pd

# Define the folder path containing the CSV files
folder_path = "scraped_files/sales"

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Iterate through all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):
        # Read the CSV file into a DataFrame
        file_path = os.path.join(folder_path, file_name)
        data = pd.read_csv(file_path)
        
        # Append the data to the combined DataFrame
        combined_data = combined_data.append(data, ignore_index=True)

# Save the combined data to a new CSV file
combined_file_path = os.path.join("tables", "sales.csv")
combined_data.to_csv(combined_file_path, index=False)

print("Combined CSV file created successfully!")
