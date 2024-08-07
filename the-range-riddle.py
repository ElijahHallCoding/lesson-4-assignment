# Task 1: Your Mood Today

import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm"]

# List of days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through each day of the week using range
for i in range(len(days_of_week)):
    # Select a random mood
    mood = random.choice(moods)
    # Print the mood for the current day
    print(f"On {days_of_week[i]}, you were feeling {mood}.")