#utilises the fitparse package to uncompress files
import fitparse
import pandas as pd

# Load the FIT file
file_path = './sample_data/Activity1.fit'  # Replace with your .fit file path
fitfile = fitparse.FitFile(file_path)

# Initialize an empty list to store records
data = []

# Iterate over all messages in the file
for record in fitfile.get_messages('record'):
    record_data = {}
    for data_field in record:
        record_data[data_field.name] = data_field.value
    data.append(record_data)

# Convert the list of records to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to CSV
csv_file_path = './sample_data/ConvertedFile.csv'  # Specify your desired CSV output path
df.to_csv(csv_file_path, index=False)

print(f"FIT file successfully converted to CSV and saved as {csv_file_path}")