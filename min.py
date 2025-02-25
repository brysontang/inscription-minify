#!/usr/bin/env python3
import argparse
import os
import re

def remove_js_comments(content):
    # Remove single line comments
    content = re.sub(r'//.*?\n', '', content)
    # Remove multi-line comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    return content

def minify_file(input_file, output_file):
    # Read the entire content from the input file
    with open(input_file, "r", encoding="utf-8") as infile:
        content = infile.read()
    
    # Get file extension
    _, ext = os.path.splitext(input_file)
    
    # If JS file, remove comments first
    if ext.lower() == '.js':
        content = remove_js_comments(content)
    
    # Remove newlines and collapse any sequence of whitespace into a single space.
    # This preserves a space where needed while removing unnecessary whitespace.
    minified_content = re.sub(r'\s+', ' ', content).strip()
    
    # Write the minified content to the output file
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(minified_content)
    
    print(f"Minified content written to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Minify a file by removing newlines and extra whitespace, safe for HTML/JS."
    )
    parser.add_argument("input_file", help="Path to the input file (e.g., an HTML or JS file)")
    parser.add_argument("output_file", nargs="?", help="Optional output file name. If omitted, '_minified' is appended to the original file name.")
    
    args = parser.parse_args()
    
    # Generate a default output file name if not provided
    if not args.output_file:
        base, ext = os.path.splitext(args.input_file)
        args.output_file = f"{base}_minified{ext}"
    
    minify_file(args.input_file, args.output_file)
