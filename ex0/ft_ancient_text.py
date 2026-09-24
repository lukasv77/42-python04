#!/usr/bin/env python3

import sys
import typing


def read_archive(filename: str) -> str | None:
    try:
        file: typing.IO[str] = open(filename)
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return None
    try:
        content = file.read()
    except (OSError, UnicodeDecodeError) as error:
        print(f"Error reading file '{filename}': {error}")
        file.close()
        return None
    file.close()
    return content


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print(f"=== Cyber Archives Recovery ===\n"
              f"Accessing file '{sys.argv[1]}'")
        content = read_archive(sys.argv[1])
        if content is not None:
            print("---\n")
            print(content)
            print("---")
            print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    main()
