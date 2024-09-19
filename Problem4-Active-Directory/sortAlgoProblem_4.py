class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    if user in group.get_users():
        return True
    for subgroup in group.get_groups():
        if is_user_in_group(user, subgroup):
            return True
    return False

# Test Case 1: Empty Input
empty_group = Group("empty_group")
empty_user = ""
assert is_user_in_group(empty_user, empty_group) == False, "Test Case 1 Failed"

# Test Case 2: User Not Found in Group
new_group = Group("new_group")
new_user = "new_user"
assert is_user_in_group(new_user, new_group) == False, "Test Case 2 Failed"

# Test Case 3: User Not Having Any Parent
assert is_user_in_group(sub_child_user, parent) == True, "Test Case 3 Failed"

# Test Case 4: User in Group
assert is_user_in_group("sub_child_user", parent) == True

# Test Case 5
large_group = Group("large")
for i in range(1000):
    large_group.add_user(f"user_{i}")
assert is_user_in_group("user_500", large_group) == True
