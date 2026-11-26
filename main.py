import os

ENTRY = "fridgehope: opening the fridge again, hoping a better snack magically appeared since you checked ten minutes ago."


def main():
    # Gate self-check: the scorer requires 1-140 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 140 and ENTRY.strip(), "entry fails the 140-character gate"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
