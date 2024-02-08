# import matplotlib.pyplot as plt
# import csv

# # Lists to store the data
# dates = []
# volumes = []

# # Open the CSV file and read the data
# with open('data.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         dates.append(row['date'])
#         volumes.append(float(row['volume']))

# # Plot the data
# plt.figure(figsize=(10,  6)) # Optional: set the figure size
# plt.bar(dates, volumes, color='blue', alpha=0.5)
# plt.xlabel('Date')
# plt.ylabel('Volume')
# plt.title('Stock Volume Over Time')
# plt.xticks(rotation=45) # Rotate x-axis labels for better visibility
# plt.tight_layout() # Adjust the layout to prevent clipping of labels
# plt.show()


import numpy as np
from scipy.io.wavfile import write
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
# Read the CSV file
import pandas as pd
filename = 'data2.csv'
df = pd.read_csv(filename)

# Normalize the volume data to the range  0-1
normalized_volumes = (df['volume'] - df['volume'].min()) / (df['volume'].max() - df['volume'].min())

# Generate a simple tone for each volume level
fs =  1000  # Sample rate
duration = len(df) / fs  # Duration in seconds
frequency = 100  # Frequency of the tone

# Create a time array
t = np.linspace(0, duration, int(fs * duration), False)

# Generate the sound wave
sound_wave = normalized_volumes * np.sin(2 * np.pi * frequency * t)
print(sound_wave)
# Write the sound wave to a WAV file
write('output2.wav', fs, sound_wave)

# import numpy as np
# from scipy.io.wavfile import write
# import warnings
# warnings.filterwarnings("ignore", category=FutureWarning)

# # Read the CSV file
# import pandas as pd
# filename = 'data.csv'
# df = pd.read_csv(filename)

# # Normalize the volume data to the range   0-1
# normalized_volumes = (df['volume'] - df['volume'].min()) / (df['volume'].max() - df['volume'].min())

# # Generate a simple tone for each volume level
# fs =  44100  # Sample rate
# duration =  1  # Duration in seconds
# frequency =  100  # Lower frequency for clearer sound

# # Create a time array
# t = np.linspace(0, duration, int(fs * duration), False)

# # Generate the sound wave
# sound_wave = normalized_volumes * np.sin(2 * np.pi * frequency * t)

# # Write the sound wave to a WAV file
# write('output.wav', fs, (sound_wave *  32767).astype(np.int16))
