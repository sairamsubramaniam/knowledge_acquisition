
import subprocess
import sys

def dump(url):
    try:
        return subprocess.Popen(["mysqldump", url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)
