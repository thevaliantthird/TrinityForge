import os
import math

def split_file(input_path: str, n: int):
    """
    Split a binary file into n sequential parts.
    Creates files named: original.part00, original.part01, ..., original.part(n-1)
    """
    if n < 2:
        raise ValueError("n must be at least 2")

    file_size = os.path.getsize(input_path)
    chunk_size = math.ceil(file_size / n)

    # Zero-pad part numbers so filenames sort correctly once n >= 10
    width = len(str(n - 1))

    with open(input_path, "rb") as f:
        for i in range(n):
            data = f.read(chunk_size)
            if not data:
                break
            part_name = f"{input_path}.part{i:0{width}d}"
            with open(part_name, "wb") as part:
                part.write(data)
            print(f"Created: {part_name} ({len(data)} bytes)")

    print(f"\nDone. Split into {n} parts.")


if __name__ == "__main__":
    split_file("neer_strat.zip.enc", 50)