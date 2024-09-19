import os
def find_files(suffix, path):
    if not os.path.isdir(path):
        return []
    
    results = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path) and item_path.endswith(suffix):
            results.append(item_path)
        elif os.path.isdir(item_path):
            results.extend(find_files(suffix, item_path))
    
    return results

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

# Test Case 1: Normal case
print(find_files(".c", "/testdir"))

# Test Case 2: Invalid input path
print(find_files('.txt', 'invalid_path'))  # Output: []

# Test Case 3: No files found for the given extension
print(find_files('.pdf', '/path/to/directory/with/no_pdf_files'))  # Output: []

# Test Case 4: Valid path with files found
print(find_files('.txt', '/path/to/directory/with/txt_files'))  # Output: ['/path/to/directory/with/txt_files/file1.txt', '/path/to/directory/with/txt_files/file2.txt']
