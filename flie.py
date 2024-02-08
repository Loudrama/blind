import numpy as np
from scipy.io.wavfile import write
import pandas as pd

# Read the CSV file
filename = 'data2.csv'
df = pd.read_csv(filename)

# Normalize the volume data to the range   0-1
normalized_volumes = (df['volume'] - df['volume'].min()) / (df['volume'].max() - df['volume'].min())

# Check if the normalized volumes are all zeros
if np.all(normalized_volumes ==  0):
    raise ValueError("All volume values are zero.")

# Generate a simple tone for each volume level
fs =   1000  # Sample rate
duration =   1  # Duration of each sound in seconds
num_samples = fs * duration  # Total number of samples per sound

# Function to generate a sound wave for a given volume level
def generate_sound_wave(volume, num_samples, fs):
    frequency =   100 + (900 * volume)  # Map volume to a frequency between   100 and   1000 Hz
    t = np.linspace(0, duration, num_samples, False)
    # Multiply by a constant to increase amplitude if needed
    return (volume * np.sin(2 * np.pi * frequency * t)).astype(np.int16)

# Generate the full audio file by concatenating individual sound waves
full_audio = []
for volume in normalized_volumes:
    sound_wave = generate_sound_wave(volume, num_samples, fs)
    print(sound_wave)  # Debugging line to print each sound wave
    full_audio.extend(sound_wave)

# Convert the list to a NumPy array and specify the data type
full_audio_np = np.array(full_audio, dtype=np.int16)

# Write the full audio to a WAV file
write('output2.wav', fs, full_audio_np)
