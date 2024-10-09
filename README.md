# WPDomainChecker

<p align="center">
  <img src="https://github.com/user-attachments/assets/26114272-ae8e-4ecd-8123-bc3090303809">
</p>

**WPDomainChecker** is a simple command-line tool that checks a list of domains to identify which ones are powered by WordPress. This tool leverages HTTP requests to examine the presence of key WordPress components in the site's HTML content.

## Features

- Checks multiple domains concurrently for faster performance.
- Normalizes domain formats (handles `http://`, `https://`, and no prefix).
- Provides user-friendly error messages for failed requests.
- Outputs results to the console and optionally saves them to a file.

## Requirements

- Python 3.x
- Requests library (install via `pip install requests`)

## Installation

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/cyberasset/WPDomainChecker.git
   cd WPDomainChecker
2. Install the required dependencies:
   ```bash
   pip install requests

## Usage

To use the tool, run the following command in your terminal:
```bash
python WPDomainChecker.py -l /path/to/your/subdomains.txt -o output.txt
```
## Options

- -l, --list: The path to the text file containing the list of domains to check (one domain per line).
- -o, --output: Optional path to save the list of WordPress domains found.

## Example

1. Create a text file named subdomains.txt with the following content:
  ```bash
  http://example.com
  blog.example.com
  https://another-example.com
  ```
2. Run the command:
  ```bash
  python WPDomainChecker.py -l subdomains.txt -o wp_domains.txt
  ```
3. The results will be displayed in the console and saved to wp_domains.txt.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
