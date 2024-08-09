![modernfetch01](https://github.com/user-attachments/assets/ad28a005-2b3a-4834-a0c0-4c3b43c59abc)

# System Information Tool

A modern Python tool for displaying system information in a rich, formatted output. It supports both JSON and table formats and features a stylized animated logo.

## Features

- Displays comprehensive system information including OS, kernel version, CPU, RAM, and more.
- Supports output in JSON or table format.
- Features a visually appealing panel with a gradient border and a centered title.
- Includes an animated logo for a dynamic presentation.

## Installation

Download the repository:

```bash
git clone https://github.com/Cedaleon/modernfetch.git
```

# Usage
You can run the tool from the command line. By default
```bash
cd modernfetch
chmod +x modernfetch
./modernfetch.py
```
# For ease of execution, move the script to a directory in PATH:
```bash
sudo mv modernfetch.py /usr/local/bin/modernfetch
modernfetch
```

# Code Overview
- get_cpu_info(): Retrieves CPU information.
- get_system_info(): Collects and formats system information.
- print_info(info, output_format): Displays system information in the specified format.
- display_logo(): Shows an animated logo.

# Contribution
Feel free to fork the repository and submit pull requests. Contributions are welcome!

# Acknowledgments
- Rich for the rich text and formatting.
- Psutil for system information utilities.






