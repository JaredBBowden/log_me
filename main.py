#!/anaconda/envs/aind/bin/python3

import pandas as pd
import datetime

now = datetime.datetime.now()
now.strftime("%Y-%m-%d %H:%M")


# Init the data frame to log to
starting_out = pd.DataFrame(columns={
    "Date": [],
    "Type": [],
    "Weight": [],
    "Time": [],
    "Pace": [],
    "Comment": []
})
starting_out.to_csv("./big_log.csv")

another = pd.DataFrame(data={
    "Date": now.strftime("%Y-%m-%d %H:%M"),
    "Weight": input("What is your name? "),
    "Type": input("Is this a run, bike, or log? "),
    "Time": input("How long did you exercise? "),
    "Pace": input("What was your pace? "),
    "Comment": input("Comments? ")
})

# Append the result
sure = starting_out.append(another, ignore_index=True)

input("What is your name? ")

another = pd.DataFrame(data={
    "Date": [1],
    "Weight": [1],
    "Type": [1],
    "Time": [1],
    "Pace": [1],
    "Comment": [1]
})

print(sure)


now.strftime("%Y-%m-%d %H:%M")
