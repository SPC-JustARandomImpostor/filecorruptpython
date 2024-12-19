import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages
required_packages = [
    "tk"
]

for package in required_packages:
    install(package)

print("All required dependencies have been installed.")
