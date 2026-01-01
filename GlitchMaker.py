import os
import random
import argparse
from pathlib import Path

def glitch_jpeg(input_path, output_path, amount=10, seed=None, mode="swap"):
    with open(input_path, 'rb') as f:
        data = bytearray(f.read())

    # JPEG Start of Scan (SOS)
    header_end = data.find(b'\xFF\xDA') + 2
    if header_end <= 2:
        raise ValueError("Invalid JPEG (SOS marker not found)")

    # JPEG End of Image (EOI)
    eoi = data.rfind(b'\xFF\xD9')
    glitch_range_end = eoi if eoi > 0 else len(data)

    if seed is not None:
        random.seed(seed)

    if mode == "swap":
        for _ in range(amount):
            i = random.randint(header_end, glitch_range_end - 2)
            j = i + random.randint(1, 10)
            if j < glitch_range_end:
                data[i], data[j] = data[j], data[i]

    elif mode == "shift":
        chunk_size = 64
        for _ in range(amount):
            start = random.randint(header_end, glitch_range_end - chunk_size - 1)
            shift = random.randint(-16, 16)
            new_start = max(
                header_end,
                min(glitch_range_end - chunk_size - 1, start + shift)
            )
            chunk = data[start:start + chunk_size]
            data[new_start:new_start + chunk_size] = chunk

    else:
        raise ValueError("Unknown glitch mode")

    with open(output_path, 'wb') as f:
        f.write(data)


# -----------------------------
# CLI ARGUMENTS
# -----------------------------

parser = argparse.ArgumentParser(description="JPEG Glitch Tool")
parser.add_argument(
    "--intensity",
    choices=["low", "medium", "high"],
    default="medium",
    help="Glitch intensity level"
)
parser.add_argument(
    "--mode",
    choices=["swap", "shift", "random"],
    default="random",
    help="Glitch mode"
)
parser.add_argument(
    "--seed",
    type=int,
    default=None,
    help="Random seed (optional)"
)

args = parser.parse_args()

# -----------------------------
# INTENSITY MAPPING
# -----------------------------

INTENSITY_MAP = {
    "low": 5,
    "medium": 15,
    "high": 40
}

glitch_amount = INTENSITY_MAP[args.intensity]

# -----------------------------
# DYNAMIC PATHS
# -----------------------------

pictures_dir = Path.home() / "Pictures"
output_dir = pictures_dir / "glitched"
output_dir.mkdir(exist_ok=True)

# -----------------------------
# PROCESS FILES
# -----------------------------

processed = 0

for file in pictures_dir.iterdir():
    if not file.is_file():
        continue

    if file.suffix.lower() not in (".jpg", ".jpeg"):
        continue

    if "_glitch" in file.stem.lower():
        continue

    output_file = output_dir / f"{file.stem}_glitch.jpg"

    try:
        glitch_jpeg(
            input_path=file,
            output_path=output_file,
            amount=glitch_amount,
            seed=args.seed or random.randint(0, 100),
            mode=random.choice(["swap", "shift"]) if args.mode == "random" else args.mode
        )
        print(f"Glitched: {file.name} → {output_file.name}")
        processed += 1
    except Exception as e:
        print(f"Skipped {file.name}: {e}")

print(f"\nDone! ({processed} files glitched)")
