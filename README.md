
# SRT to Text Converter

This Python script converts subtitle files in SRT format to plain text. It reads an SRT file, removes all SRT formatting and timing information, and outputs the plain text into a new file. Additionally, the script copies the resulting plain text to the clipboard for immediate use.

## Features

- Strip timing and numeric formatting from SRT files.
- Output clean text to a new `.txt` file.
- Automatically copy the converted text to the clipboard.

## Prerequisites

Before you run the script, ensure you have Python installed on your system. Additionally, you need to install the `pyperclip` module, which the script uses to copy text to the clipboard. You can install this module using pip:

```bash
pip install pyperclip
```

## Usage

1. Save the script as `srt2txt.py`.
2. Run the script using Python:

```bash
python srt2txt.py
```

3. When prompted, enter the filename of your SRT file. If you don't include the `.srt` extension, it will be appended automatically.
4. The script will attempt to convert the SRT file to text and will print "Success!!!" if everything went correctly. If the file cannot be processed, it will print "not working".
5. Check the script's directory for the output `.txt` file named after the original with its extension replaced by `.txt`.

## Example

Suppose you have an SRT file named `example.srt`. Run the script, enter `example.srt` when prompted, and after successful execution, you will find `example.txt` in the same directory. The contents of `example.srt` will also be copied to your clipboard.

## Error Handling

If the script encounters an issue (e.g., the file does not exist, or there's a permission error), it will output "not working". Ensure that the filename is correct and that you have the appropriate permissions to read the file and write to the directory.

## License

This script is released under the MIT License.
