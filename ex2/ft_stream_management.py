#!/usr/bin/env python3

import sys
import typing


def save_content(content: str) -> None:
    try:
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        filename = sys.stdin.readline().strip()
    except KeyboardInterrupt:
        sys.stdout.flush()
        print("\n[STDERR] KeyboardInterrupt", file=sys.stderr)
        return None
    if not filename:
        print("Not saving data.")
        return None
    print(f"Saving data to '{filename}'")
    try:
        file = open(filename, "w")
    except OSError as error:
        sys.stdout.flush()
        print(f"[STDERR] Error opening file '{filename}': {error}",
              file=sys.stderr)
        print("Data not saved.")
        return None
    try:
        file.write(content)
        file.close()
        print(f"Data saved in file '{filename}'.")
    except OSError as error:
        sys.stdout.flush()
        print(f"[STDERR] Error writing file '{filename}': {error}",
              file=sys.stderr)
        print("Data not saved.")
        file.close()
        return None


def read_archive(filename: str) -> str | None:
    try:
        file: typing.IO[str] = open(filename)
    except OSError as error:
        sys.stdout.flush()
        print(f"[STDERR] Error opening file '{filename}': {error}",
              file=sys.stderr)
        return None
    try:
        content = file.read()
    except (OSError, UnicodeDecodeError) as error:
        sys.stdout.flush()
        print(f"[STDERR] Error reading file '{filename}': {error}",
              file=sys.stderr)
        file.close()
        return None
    file.close()
    return content


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return None
    print(f"=== Cyber Archives Recovery & Preservation ===\n"
          f"Accessing file '{sys.argv[1]}'")
    content = read_archive(sys.argv[1])
    if content is None:
        return None
    print("---\n")
    print(content)
    print("---")
    print(f"File '{sys.argv[1]}' closed.")
    content = content.replace("\n", "#\n")
    print("\nTransform data:\n---\n")
    print(content)
    print("---")
    save_content(content)


if __name__ == "__main__":
    main()
