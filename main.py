#!/anaconda/envs/aind/bin/python3

import pandas as pd
import datetime
import cv2
import sys

def photo_booth(the_date):

    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

        cv2.imshow('frame', rgb)
        if cv2.waitKey(1) & 0xFF == ord('q'):

            # FIXME return this, and remove the date argument
            cv2.imwrite("./images/" + str(the_date) + ' capture.jpg', frame)
            break

    cap.release()
    cv2.destroyAllWindows()


def log_me(log_type):

    # Read in the log file
    big_log = pd.read_csv("./big_log.csv")

    # Time variables
    now = datetime.datetime.now()
    the_date = now.strftime("%Y-%m-%d %H:%M")

    photo_booth(the_date)

    # Save and backup
    big_log.to_csv("./data_backup/" + the_date + " " + "big_log.csv")

    if log_type == "doogie":
        new_entry = pd.DataFrame(
            data={
                "Date": the_date,
                "Comment": input("Comments?: "),
            },
            index=[0])
    elif log_type == "weight":
        new_entry = pd.DataFrame(
            data={
                "Date": the_date,
                "Weight": input("Current weight?: "),
                "Comment": input("Comments?: "),
            },
            index=[0])
    else:
        # Populate new values to new entry
        new_entry = pd.DataFrame(
            data={
                "Date": the_date,
                "Weight": input("Current weight?: "),
                "Type": input("Is this a run, bike, or log?: "),
                "Distance": input("How far did you go?: "),
                "Pace": input("What was your pace?: "),
                "Comment": input("Comments?: "),
            },
            index=[0])

    # Append the result
    to_out = big_log.append(new_entry, ignore_index=True)

    # FIXME write to file here -- with the new test argument...

    # Write out new log
    to_out.to_csv("./big_log.csv", index=False)


if __name__ == "__main__":
    print("###########################################################")
    print("#                         LOG ME                          #")
    print("###########################################################")

    # TODO Let's clean this up a little
    try:
        log_type = sys.argv[1]
    except:
        log_type = "sure"

    log_me(log_type)
