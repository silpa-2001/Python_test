import os

direct="Silpa"
part_dir="C:/Users/Admin/Desktop/Python"
path=os.path.join(part_dir,direct)
try:
    os.mkdir(path)
    print("Directory '%s' created successfully." % direct)
except FileExistsError:
    print("Directory '%s' already exists." % direct)
except Exception as e:
    print("An error occurred while creating the directory: %s" % e)

print("List of directories:")
try:
    contents = os.listdir(part_dir)
    for item in contents:
        print(item)
except FileNotFoundError:
    print("Directory '%s' not found." % part_dir)
except Exception as e:
    print("An error occurred while listing the directory contents: %s" % e)

print("Searching for a .py file ....")
try:
    for file in os.listdir(part_dir):
        if file.endswith(".py"):
            print(file)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("An Error had occured :( --",e)

print("Removing a particular file:")
try:
    if os.path.exists("C:/Users/Admin/Desktop/Python/test2.txt"):
        os.remove("C:/Users/Admin/Desktop/Python/test2.txt")
        print("File is removed successfully.")
    else:
        print("File does not exist.")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("An Error had occured :( --",e)