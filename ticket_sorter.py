import os
import shutil

# Define our directories for processing IT tickets
incoming_dir = "./incoming_tickets"
critical_dir = "./critical_alerts"
general_dir = "./general_requests"

# Automatically create the directories if they don't exist yet
for folder in [incoming_dir, critical_dir, general_dir]:
    if not os.path.exists(folder):
        os.makedirs(folder)

print("--- Starting IT Support Ticket Sorter ---")

# Scan the incoming directory for text file tickets
if os.path.exists(incoming_dir):
    for file_name in os.listdir(incoming_dir):
        if file_name.endswith(".txt"):
            file_path = os.path.join(incoming_dir, file_name)
            
            # Read the file to scan for urgent keywords
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read().lower()
            
            # Sort based on priority keywords
            if "error" in content or "critical" in content or "crash" in content:
                shutil.move(file_path, os.path.join(critical_dir, file_name))
                print(f"🚨 Escalated to Critical: {file_name}")
            else:
                shutil.move(file_path, os.path.join(general_dir, file_name))
                print(f"✅ Sorted to General: {file_name}")

print("--- Sorting Process Finished ---")
