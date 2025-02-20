# File Deletion Script

## Description

This script checks whether a specified file exists in the given directory path and deletes it if found. If the file does not exist, it informs the user.

## How It Works

1. The script defines a `file_path` variable, which should contain the full path of the file you want to delete.
2. It then checks if the file exists using Python's `os.path.isfile()` method.
3. If the file exists, it is removed using `os.remove()`.
4. If the file does not exist, a message is displayed stating that the file is not found.

## Prerequisites

- Python 3.x installed on your system.
- Ensure that the file path is correctly specified.
- The script must have permission to delete the specified file.

## Usage

1. Modify the `file_path` variable to include the full path of the file you want to delete.
2. Run the script using:

   ```bash
   python script.py

## Example

Modify the following line in the script:

  ```
   file_path = '/users/Downloads/example.txt'  # Replace with your actual file
  ```

Then run the script, and it will delete example.txt if it exists.

## Notes
- Be careful when specifying the file path, as this script will permanently delete the file without recovery.
- Ensure you have the correct permissions to delete the file.
- This script does not handle directories, only individual files.

## Disclaimer
- Use this script responsibly. The author is not responsible for any accidental data loss.
