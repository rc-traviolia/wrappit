import os
from gitignore_parser import parse_gitignore
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def load_gitignore_patterns(executing_directory):
    gitignore_file = os.path.join(executing_directory, '.gitignore')
    if os.path.isfile(gitignore_file):
        return parse_gitignore(gitignore_file)  # Ensure to pass patterns, not file path
    return None

def print_directory_structure():
    def print_tree(path, gitignore_parser, prefix=''):
        if not os.path.isdir(path):
            return
        
        entries = sorted(os.listdir(path))
        
        # Separate files and directories
        files = [entry for entry in entries if os.path.isfile(os.path.join(path, entry))]
        directories = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
        
        # Print files first
        for index, entry in enumerate(files):
            full_path = os.path.join(path, entry)
            
            if gitignore_parser and not gitignore_parser(full_path):
                connector = '└── ' if index == len(files) - 1 and not directories else '├── '
                entry_color = Fore.BLUE
                print(f"{prefix}{connector}{entry_color}{entry}")
        
        # Print directories
        for index, entry in enumerate(directories):
            full_path = os.path.join(path, entry)

            # Explicitly check for '.git' directory to include it in the results
            if gitignore_parser and (entry == '.git' or gitignore_parser(full_path)):
                continue
            
            connector = '└── ' if index == len(directories) - 1 else '├── '
            entry_color = Fore.YELLOW
            print(f"{prefix}{connector}{entry_color}{entry}/")
            new_prefix = prefix + ('    ' if index == len(directories) - 1 else '│   ')
            print_tree(full_path, gitignore_parser, new_prefix)
    
    executing_directory = os.getcwd()
    gitignore_parser = load_gitignore_patterns(executing_directory)
    # Print the base folder first
    print(f"{Fore.YELLOW}{os.path.basename(executing_directory)}/")
    print_tree(executing_directory, gitignore_parser)

if __name__ == "__main__":
    print_directory_structure()
