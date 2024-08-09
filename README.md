![modernfetch01](https://github.com/user-attachments/assets/ad28a005-2b3a-4834-a0c0-4c3b43c59abc)

# System Information Tool

A modern Python tool for displaying system information in a rich, formatted output. It supports both JSON and table formats and features a stylized animated logo.

## Features

- Displays comprehensive system information including OS, kernel version, CPU, RAM, and more.
- Supports output in JSON or table format.
- Features a visually appealing panel with a gradient border and a centered title.
- Includes an animated logo for a dynamic presentation.

## Installation

Ensure you have Python 3 installed. Install the required Python packages using pip:

```bash
pip install rich psutil
```

# Usage
You can run the tool from the command line. By default, it will display information in a table format. Use the --format argument to switch between JSON and table formats.

# Example
To display system information in table format, run:

```bash
python system_info.py
```
To display system information in JSON format, run:
```bash
python system_info.py --format json
```
# Code Overview
- get_cpu_info(): Retrieves CPU information.
- get_system_info(): Collects and formats system information.
- print_info(info, output_format): Displays system information in the specified format.
- display_logo(): Shows an animated logo.

# Contribution
Feel free to fork the repository and submit pull requests. Contributions are welcome!

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
- Rich for the rich text and formatting.
- Psutil for system information utilities.






