import pywhatkit as kit
from datetime import datetime

# Input phone number and message
phone_number = input("Enter phone number (with country code, e.g., +1234567890): ")
message = input("Enter message: ")

# Get current time and add at least 2 minutes
now = datetime.now()
hour = now.hour
minute = now.minute + 2  # At least 2 minutes ahead to avoid time sync issues

# If the minute exceeds 59, adjust the hour and minute accordingly
if minute >= 60:
    hour += 1
    minute = minute % 60

# Send the message
kit.sendwhatmsg(phone_number, message, hour, minute)