import glob
import os

def merge_file(input_path: str, output_path: str = None):
    """
    Reassemble a file previously split by split_file().
    Looks for files named: input_path.part00, input_path.part01, ...
    and concatenates them in numeric order into output_path
    (defaults to input_path itself if not given).
    """
    if output_path is None:
        output_path = input_path

    pattern = f"{input_path}.part*"
    parts = glob.glob(pattern)

    if not parts:
        raise FileNotFoundError(f"No part files found matching: {pattern}")

    # Sort numerically by the suffix after "part", not alphabetically,
    # so this works regardless of zero-padding width.
    def part_index(p):
        suffix = p[len(f"{input_path}.part"):]
        return int(suffix)

    parts.sort(key=part_index)

    total_bytes = 0
    with open(output_path, "wb") as out:
        for part_name in parts:
            with open(part_name, "rb") as part:
                data = part.read()
                out.write(data)
                total_bytes += len(data)
            print(f"Merged: {part_name} ({len(data)} bytes)")

    print(f"\nDone. Reassembled {len(parts)} parts into {output_path} ({total_bytes} bytes total).")


if __name__ == "__main__":
    merge_file("init_fx_ranker.zip.enc")