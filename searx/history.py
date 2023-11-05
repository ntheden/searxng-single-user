import datetime
from pathlib import Path


def write_to_history(json_string):
    # Get current date and time as strings in YYYY-MM-DD format and HH:MM:SS format, respectively
    now = datetime.datetime.now()
    history_dir = Path(f'history/{now.strftime("%Y-%m-%d")}')

    # Check if a folder for the current date exists, and create it otherwise
    history_dir.mkdir(parents=True, exist_ok=True)

    # Find the highest numbered log file in the current day's folder, or 0 if there are none.
    max_number = -1
    for fpath in history_dir.iterdir():
        try:
            number = int(fpath.name[len("log_"):-5]) # Extract the number from the file name and convert to an integer
            if number > max_number:
                max_number = number
        except ValueError: # Ignore any non-numeric files in the folder (like .gitignore)
            pass

    # Create a new log file with the highest number plus 1, or 0 if there are none.
    fpath = history_dir / f"log_{(max_number+1):03d}.json"
    with open(fpath, "a") as f:

        # Write the log message and timestamp to the file
        f.write(json_string)
