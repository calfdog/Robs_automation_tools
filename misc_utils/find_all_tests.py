"""
Rob Marchetti
Description: recursively find all python test_ file names and get the total count
Example: Find all python "test_*" files under the your project or test directory
"""

from pathlib import Path
import os


all_py_files = Path(r"{YourProjectDirectory}").rglob("test_*.py")

test_count = 0
test_paths = [os.path.split(paths) for paths in all_py_files]

for test_name in test_paths:
    print(f"test name: {test_name[1]}")
    test_count = test_count+1
print(f"total test count: {test_count}")

