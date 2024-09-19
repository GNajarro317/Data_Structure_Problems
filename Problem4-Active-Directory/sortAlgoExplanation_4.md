Task
The task is to implement a system that simulates user and group management in a hierarchical structure similar to Windows Active Directory. In this system, groups can contain both users (identified by unique strings representing their IDs) and other groups. The task is to create a function that efficiently checks if a user is a member of a specified group.

Explanation
Under the function is_user_in_group, the if else condition statment is utilized to determine if user is in the group or if its false.
The for loop is  used to go through the list of users and groups for the if else condition statement.

The time complexity of the is_user_in_group function is O(n), where n is the total number of users in all groups within the parent group. 
This is because the function recursively checks each user in the group and its subgroups to see if the user is present.
The space complexity of the is_user_in_group function is also O(n), as the function uses recursion to traverse through all groups and users within the parent group, 
potentially creating a recursive call stack of size n.