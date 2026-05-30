from datetime import datetime # Clock Library
import os

print("TASHWILL's Smart File Auto-Namer")
print("-" *36)

#1. Get the current date and time from my laptop 
now = datetime.now()

#2. Formating the into a text ( string)
timestamp = now.strftime("%Y-%m-%d %H-%M-%S")
print(f"Current Timestamp: {timestamp}")

#3. Create a unique filename for recording
base_filename = f"audio_record_{timestamp}.wav"
print(f"Generated Secure Filename:{base_filename}")
print("-" *36)

#4. Simulating saving the file to downloads folder
downloads_path = r"C:\Users\USER\Downloads"
full_destination = os.path.join(downloads_path, base_filename)

print("Simulating file creation sequence...")
print(f"Target Destination: {full_destination}")




