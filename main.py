#!/anaconda/envs/aind/bin/python3

import pandas as pd
import datetime


# Read in the log file
big_log = pd.read_csv("./big_log.csv")

# Time variables
now = datetime.datetime.now()
now.strftime("%Y-%m-%d %H:%M")

# Populate new values to new entry
new_entry = pd.DataFrame(
    data={
        "Date": now.strftime("%Y-%m-%d %H:%M"),
        "Weight": input("Current weight?: "),
        "Type": input("Is this a run, bike, or log?: "),
        "Time": input("How long did you exercise?: "),
        "Pace": input("What was your pace?: "),
        "Comment": input("Comments?: "),
    },
    index=[0])

# Write out new log

# Append the result
sure = big_log.append(new_entry, ignore_index=True)

print(sure)
