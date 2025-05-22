def max_file_system_depth(fs):
    if not isinstance(fs, dict) or not fs:
        return 0
    return 1 + max((max_file_system_depth(sub) for sub in fs.values()), default=0)
#time complexity: o(n)