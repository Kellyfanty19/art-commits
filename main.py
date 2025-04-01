from datetime import datetime, timedelta
import subprocess
import os

commits = [
    "    *    ",
    "   ***   ",
    "*********",
    "  *****  ",
    " *** *** ",
    "**     **",
    "         ",
]

def generateCommit(mapCommit, sunday):
    # commits = {}
    result = {}
    width = len(mapCommit[0])
    count = 7 * width
    current_Date = sunday
    week_Day = 0
    for day in range(count):
        week = day // 7
        char = mapCommit[week_Day][week]
        if char != ' ':
            date = current_Date.strftime('%Y-%m-%d')
            result[date] = 10 if char == '*' else 0
        current_Date += timedelta(days=1)
        week_Day = (week_Day + 1) % 7
    return result

date = datetime(2025, 3, 30)
commits_data = generateCommit(commits, date)
print(commits_data)
for date_str, count in commits_data.items():
    for i in range(count):
        with open("commit.log", "a", encoding="utf-8") as f:
            f.write(f"Commit {i} on {date_str}\n")
        subprocess.run(["git", "add", "commit.log"], check=True)
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = f"{date_str} 12:00:00"
        env["GIT_COMMITER_DATE"] = f"{date_str} 12:00:00"

        subprocess.run(
            ["git", "commit", "-m", f"Auto commit for {date_str}"],
            env=env,
            check=True,
            stdout=subprocess.DEVNULL
        )