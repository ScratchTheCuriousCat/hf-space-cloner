import os
import time

os.system("color 6")
os.system("title Space Cloner")
os.system("cls")

print("Make sure you review the space's code before running")

space = input("Enter the HuggingFace space URL: ")
space_name = space.rstrip("/").split("/")[-1]

# get essentials

os.system(f"git clone {space}")
os.system(f"cd {space_name}")
os.system(f"python -m pip install -r requirements.txt")
print("Open space? (y/n)")
answer =  input("> ")
if answer == "y" or answer == "Y":
    os.system("exit")
    os.system("cls")
    os.system(f"cd {space_name}")
    os.system(f"python app.py")
else:
    print(f"done, execute  'cd {space_name}' and then 'python app.py' to run the cloned space.")
    print("about to exit in 10 seconds")
    time.sleep(10)
    os.system("exit")
