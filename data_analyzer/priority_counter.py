import re


def count_priority(java_code):
    # Use a regular expression to find all direct instantiations of PriorityQueue in the Java code
    pattern = r'new\s+PriorityQueue\s*<.*>\s*\('
    matches = re.findall(pattern, java_code)

    # Return the number of instantiations found
    return len(matches)