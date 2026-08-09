import os
import math

def split_file(input_path: str, n: int):
    """
    Split a binary file into n sequential parts.
    Creates files named: original.part0, original.part1, ..., original.part(n-1)
    """
    if n not in (3, 4, 5, 6):
        raise ValueError("n must be 3, 4, 5 or 6")

    file_size = os.path.getsize(input_path)
    chunk_size = math.ceil(file_size / n)

    with open(input_path, "rb") as f:
        for i in range(n):
            data = f.read(chunk_size)
            if not data:
                break
            part_name = f"{input_path}.part{i}"
            with open(part_name, "wb") as part:
                part.write(data)
            print(f"Created: {part_name} ({len(data)} bytes)")

    print(f"\nDone. Split into {n} parts.")


# Example usage
if __name__ == "__main__":
    split_file("accumulated_new.zip.enc", 4)   # change 4 to 3, 5 or 6 as needed