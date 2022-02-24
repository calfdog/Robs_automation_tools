"""Quick Example of getting a list of PID and name works on mac and Windows"""

import psutil

# Print a list of pid's and names
process = psutil.process_iter()
for i in process:
    print(i.name, i.pid)



