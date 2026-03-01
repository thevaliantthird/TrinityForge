import os

def merge_files(output_file, prefix="part_"):
    # Get all files starting with the prefix
    parts = sorted([f for f in os.listdir(".") if f.startswith(prefix)])
    
    with open(output_file, "wb") as outfile:
        for part in parts:
            print(f"Merging {part}...")
            with open(part, "rb") as infile:
                outfile.write(infile.read())
    
    print(f"Merge complete! Output saved to {output_file}")

if __name__ == "__main__":
    merge_files("together_clean.pickle.enc")

