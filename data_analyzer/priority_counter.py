import re


def count_priority(java_code):

    pattern = r'new\s+PriorityQueue\s*<.*>\s*\('
    matches = re.findall(pattern, java_code)

    return len(matches)