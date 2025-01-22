import os

def get_size(start_path):
    """
    Calculate the total size of a directory or a file.
    """
    total_size = 0
    if os.path.isfile(start_path):  # If it's a file, get its size directly
        return os.path.getsize(start_path)
    for dirpath, _, filenames in os.walk(start_path):
        for f in filenames:
            try:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
            except (FileNotFoundError, PermissionError):
                pass  # Ignore inaccessible files
    return total_size

def get_sorted_sizes(drive_path):
    """
    List and sort all files/directories in the drive based on their size.
    """
    if not os.path.exists(drive_path):
        print(f"The path '{drive_path}' does not exist.")
        return
    
    items = []
    for item in os.listdir(drive_path):
        item_path = os.path.join(drive_path, item)
        size_in_gb = get_size(item_path) / (1024 ** 3)  # Convert size to GB
        items.append((item, size_in_gb))

    # Sort items by size (largest first)
    items.sort(key=lambda x: x[1], reverse=True)
    
    # Print the sorted list
    print(f"\nItems in '{drive_path}' sorted by size:")
    print(f"{'Name':<50} {'Size (GB)':>10}")
    print("-" * 60)
    for name, size in items:
        print(f"{name:<50} {size:>10.2f} GB")

if __name__ == "__main__":
    # Replace this with the drive or directory path you want to check
    drive = input("Enter the drive or directory path to scan (e.g., C:/, /mnt/data): ")
    get_sorted_sizes(drive)
