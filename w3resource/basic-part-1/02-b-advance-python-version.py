# This script will display detailed information of the python version being used.

# Import modules.

import platform
import sys

# Detect the python version and display it.

py_version=platform.python_version()
print(f"Python version: {py_version}")

# Detect the git tag and display it.

git_tag=sys.version.split("(")[1].split(",")[0]
print(f"Git Tag: {git_tag}")

# Detect the release date and time and display it.

release_date=sys.version.split(",")[1].strip()
release_time=sys.version.split(",")[2].split(")")[0].strip()
print(f"Release date and time: {release_date}, {release_time}")

# Detect the major, miinor, micro release numbers and release level and display it.

print(f"Major release number: {sys.version_info.major}")
print(f"Minor release number: {sys.version_info.minor}")
print(f"Micro release number: {sys.version_info.micro}")
print(f"Release level: {sys.version_info.releaselevel}")
