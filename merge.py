import os
import glob

def merge_files(output_path: str, n: int = None):
    """
    Merge sequential .part0, .part1, ... files back into one file.
    
    If n is given, it looks for exactly that many parts.
    If n is None, it automatically finds all consecutive .partN files.
    """
    # Find all part files
    base = output_path
    # Remove any existing extension so we can rebuild correctly
    if base.endswith(".bin") or base.endswith(".exe") or "." in os.path.basename(base):
        # Keep the original name the user wants
        pass

    parts = []
    i = 0
    while True:
        part_name = f"{output_path}.part{i}"
        if not os.path.exists(part_name):
            break
        parts.append(part_name)
        i += 1
        if n is not None and i >= n:
            break

    if not parts:
        raise FileNotFoundError(f"No part files found for {output_path}")

    print(f"Found {len(parts)} parts. Merging...")

    with open(output_path, "wb") as outfile:
        for part in parts:
            with open(part, "rb") as infile:
                data = infile.read()
                outfile.write(data)
                print(f"  Added {part} ({len(data)} bytes)")

    print(f"\nMerged successfully → {output_path}")
    print(f"Final size: {os.path.getsize(output_path)} bytes")


# Example usage
if __name__ == "__main__":
    # After splitting "yourfile.bin" you would run:
    merge_files("yourfile.bin")          # auto-detects number of parts
    # or
    # merge_files("yourfile.bin", n=4)   # if you want to force exactly 4 parts