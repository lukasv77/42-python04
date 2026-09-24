#!/usr/bin/env python3


def secure_archive(filename: str, mode: str = "r",
                   content: str = "") -> tuple[bool, str]:
    if mode == "r":
        if content:
            return (False, "Content not allowed in read mode")
        try:
            with open(filename, mode) as file:
                data = file.read()
                return (True, data)
        except (OSError, UnicodeError) as error:
            return (False, str(error))
    if mode == "w":
        try:
            with open(filename, mode) as file:
                file.write(content)
                if content != "":
                    return (True, 'Content successfully written to file')
                else:
                    return (True, 'Empty file created')
        except OSError as error:
            return (False, str(error))
    return (False, 'Unsupported mode')


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))

    print("\nUsing 'secure_archive' to read with content:")
    print(secure_archive("/noname", "r", "Hello 42!"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "w", result[1]))

    print("\nUsing 'secure_archive' to write empty string to a new file:")
    print(secure_archive("empty_file.txt", "w"))


if __name__ == "__main__":
    main()
