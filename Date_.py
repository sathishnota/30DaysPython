from datetime import datetime

# Define the two dates (format: YYYY-MM-DD)
date1 = datetime.strptime("2025-03-01", "%Y-%m-%d")
date2 = datetime.strptime("2025-06-07", "%Y-%m-%d")

# Calculate the difference
difference = date2 - date1

# Print the number of days
print("Days between:", difference.days)
