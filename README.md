# Minify Script

This script is designed to minify HTML or JavaScript files by removing unnecessary whitespace and newlines. For JavaScript files, it also strips out both single-line (//) and multi-line (/* */) comments before minification. The resulting output is a compact version of the original file, which can be useful for reducing file size for deployment.

## Features

- Whitespace Removal: Collapses multiple whitespace characters (spaces, tabs, newlines) into a single space.
- Comment Removal: For JavaScript files (.js), the script removes both single-line and multi-line comments.
- Output File Naming: If no output file is specified, the script automatically generates a name by appending _minified to the original file name.

## Requirements

- Python 3.x
- Standard Python libraries: argparse, os, and re

## Usage

Run the script from the command line:

```
./minify.py input_file [output_file]
```
- input_file: The path to the file you want to minify (HTML or JS).
- output_file (optional): The path for the minified output. If omitted, the script appends _minified to the original file name.

## Examples

Minify a JavaScript file and specify an output file:

```
./minify.py script.js minified_script.js
```
Minify an HTML file without specifying an output file:

```
./minify.py index.html
```
Output file will be named index_minified.html by default.

## How It Works

1. File Reading: The script reads the entire content of the input file.
2. Comment Removal (JS Only): If the input file is a JavaScript file, it removes:
- Single-line comments (using //).
- Multi-line comments (using /* */).
3. Whitespace Collapsing: It replaces any sequence of whitespace with a single space, ensuring that the content remains syntactically correct.
4. File Writing: The minified content is written to the output file.
5. Notification: The script prints a confirmation message indicating the location of the minified file.
