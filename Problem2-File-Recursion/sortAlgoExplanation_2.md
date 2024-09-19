Task
The task is to write a Python function that searches through a specified directory and all of its subdirectories to find and return a list of all files that end with the ".c" extension.

Explanation
os.path.isfile and os.path.isdir are used to determine with a boolean response whethere a file or directory exist,
if so then they are connected with the os.path.join method.

The time complexity of this function is O(n), where n is the total number of files and directories in the given path. 
This is because the function recursively traverses through all directories and files to find the files with the specified suffix.
The space complexity of this function is also O(n), as the function uses recursion to traverse through directories and maintains a list of results. 
The space complexity is directly proportional to the number of files and directories in the given path.