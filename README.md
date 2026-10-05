# IT Automation Scripts

This is a repository where I save Python scripts I write to automate everyday IT and systems administration tasks. 

## 🛠️ Script 1: IT Support Ticket Sorter (`ticket_sorter.py`)
This script automatically looks through a folder of incoming IT support tickets (saved as text files) and sorts them into different directories based on how urgent they are.

### How it works:
* It reads the text inside every new support ticket file.
* If it catches serious keywords like **"error"**, **"critical"**, or **"crash"**, it immediately flags the ticket and escalates it to a `critical_alerts` folder.
* All other general questions or requests are neatly moved to a `general_requests` folder.

### Key concepts I practiced:
* Working with the file system using Python's `os` and `shutil` modules.
* Handling file input/output (`open()` and `read()`).
* String manipulation and logical filtering in Python loops.
