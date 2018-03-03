import pandas as pd

neat = input("What is your name? ")

print("I found: " + neat)

starting_out = pd.DataFrame(columns={
    "Date": [],
    "Type": [],
    "Weight": [],
    "Time": [],
    "Pace": [],
    "Comment": []
})


starting_out.to_csv("./big_log.csv", index=False)


#!/anaconda/envs/aind/bin/python3
import pandas as pd

neat = input("What is your name? ")

print("I found: " + neat)

# This is just some stuff that I use to populate a new (EMPTY!) frame
starting_out = pd.DataFrame(columns={
    "Date": [],
    "Type": [],
    "Weight": [],
    "Time": [],
    "Pace": [],
    "Comment": []
})

starting_out.to_csv("./big_log.csv", index=False)


big_log = pd.read_csv("./big_log.csv")
big_log
