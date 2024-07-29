import json

file_path = r"C:\Users\imiwu\OneDrive\Documents\CARLA-Simulation-2\.ipynb_checkpoints\T17_Normal_8min_Fog.json"

# Load data from JSON file
with open(file_path, 'r') as json_file:
    data = json.load(json_file)

# Initialize arrays for x, y, lat, and lon
x_array = []
y_array = []
lat_array = []
lon_array = []

# Extract data into arrays
for entry in data:
    if 'accelerometer' in entry:
        x_array.append(entry['accelerometer']['x'])
        y_array.append(entry['accelerometer']['y'])
    if 'lat' in entry and 'lon' in entry:
        lat_array.append(entry['lat'])
        lon_array.append(entry['lon'])

# Save arrays to text files
def save_array_to_txt(array, filename):
    with open(filename, 'w') as txt_file:
        for item in array:
            txt_file.write(f"{item}\n")

save_array_to_txt(x_array, 'T17_x_array.txt')
save_array_to_txt(y_array, 'T17_y_array.txt')
save_array_to_txt(lat_array, 'T17_lat_array.txt')
save_array_to_txt(lon_array, 'T17_lon_array.txt')

print("Data has been extracted and saved to text files.")