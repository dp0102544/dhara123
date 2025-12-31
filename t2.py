from datetime import datetime

# Get current date and time
now = datetime.now()

# Format date and time
formatted_datetime = now.strftime("%d-%m-%Y %H:%M:%S")

# Display
print("Current Date and Time:", formatted_datetime)
