import os
import getpass

def install_package():
	try:
		package_name = input("Enter the package name to be installed")
		os.system(f"sudo yum install -y {package_name}")
	except Exception as e:
		print(f"Failed to install {package_name}\n{e}")

