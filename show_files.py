import os
import fnmatch


def read_gitignore_patterns(path_to_gitignore):
    """Read and parse .gitignore, returning a list of patterns."""
    patterns = []
    with open(path_to_gitignore, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            if line and not line.startswith('#'):
                patterns.append(line)
    return patterns


def match_patterns(path, patterns):
    """Check if a path matches any of the .gitignore patterns or is the .git folder."""
    for pattern in patterns:
        if fnmatch.fnmatch(path, pattern) or fnmatch.fnmatch(os.path.basename(path), pattern):
            return True
    return False


def list_files(startpath, patterns):
    for root, dirs, files in os.walk(startpath, topdown=True):
        # Explicitly exclude the .git directory
        dirs[:] = [d for d in dirs if not match_patterns(os.path.join(root, d), patterns) and d != '.git']
        files = [f for f in files if not match_patterns(os.path.join(root, f), patterns)]


        # Limit to first 20 directories and files
        dirs = dirs[:10]
        files = files[:10]

        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)

        for d in dirs[:10]:  # Show only up to 20 directories
            print(f'{subindent}{d}/')
        if len(dirs) > 10:
            print(f'{subindent}... and more directories')

        for f in files[:10]:  # Show only up to 20 files
            print(f'{subindent}{f}')
        if len(files) > 10:
            print(f'{subindent}... and more files')


if __name__ == '__main__':
    project_path = '.'  # Adjust as needed
    gitignore_path = os.path.join(project_path, '.gitignore')
    patterns = ['.git']  # Explicitly add .git to patterns to ensure it's excluded
    if os.path.exists(gitignore_path):
        patterns += read_gitignore_patterns(gitignore_path)
    list_files(project_path, patterns)
