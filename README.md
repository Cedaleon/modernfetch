![modernfetch01](https://github.com/user-attachments/assets/ad28a005-2b3a-4834-a0c0-4c3b43c59abc)

# System Information Tool

A modern Python tool for displaying system information in rich, formatted output. It supports JSON and table formats and features a stylized editable ASCII logo.

## Features

- Shows complete system information including operating system, kernel version, CPU, RAM and more.
- Supports output in JSON or table format.
- Features a visually attractive panel.
- Includes a logo in customizable ASCII format for a dynamic presentation.

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

# Contribution
Feel free to fork the repository and submit pull requests. Contributions are welcome!

# Acknowledgments
- ChatGPT
- Candy - my cat







