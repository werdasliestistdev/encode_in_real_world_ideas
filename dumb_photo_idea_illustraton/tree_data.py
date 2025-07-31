
#!/usr/bin/env python3
"""
tree_data.py  –  Minimal prototype for “data‑on‑objects” using a single reference image
=====================================================================

Usage examples
--------------
# 1) Make a fingerprint from an image
python tree_data.py fingerprint tree.jpg

# 2) Store a message keyed by that fingerprint
python tree_data.py store tree.jpg "goodbye world" db.json

# 3) Read the message back later (from same tree photo)
python tree_data.py read tree.jpg db.json
"""

import cv2
import hashlib
import json
import os
import sys
from pathlib import Path

################################################################################
# Fingerprint utilities
################################################################################

def fingerprint_image(path, size=256):
    """Deterministically fingerprint an image file.

    The pipeline is intentionally simple: grayscale → resize → flatten → SHA‑256.
    You can swap this for a fancier, rotation‑invariant version later.
    """
    img = cv2.imread(str(path))
    if img is None:
        raise FileNotFoundError(f"Could not read image '{path}'.")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (size, size), interpolation=cv2.INTER_AREA)
    token = hashlib.sha256(resized.flatten().tobytes()).hexdigest()
    return token


################################################################################
# Lightweight JSON key‑value store helpers
################################################################################

def load_db(db_path):
    if not Path(db_path).exists():
        return {}
    with open(db_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(db_path, data):
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


################################################################################
# CLI commands
################################################################################

def cmd_fingerprint(argv):
    if len(argv) != 2:
        print("USAGE: tree_data.py fingerprint <image_path>")
        return 1
    token = fingerprint_image(argv[1])
    print(token)
    return 0

def cmd_store(argv):
    if len(argv) != 4:
        print("USAGE: tree_data.py store <image_path> <message> <db.json>")
        return 1
    img_path, message, db_path = argv[1:]
    token = fingerprint_image(img_path)
    db = load_db(db_path)
    db[token] = message
    save_db(db_path, db)
    print(f"Stored message under token: {token}")
    return 0

def cmd_read(argv):
    if len(argv) != 3:
        print("USAGE: tree_data.py read <image_path> <db.json>")
        return 1
    img_path, db_path = argv[1:]
    token = fingerprint_image(img_path)
    db = load_db(db_path)
    message = db.get(token)
    if message is None:
        print("No entry found for this object.")
        return 1
    print(message)
    return 0


def main():
    if len(sys.argv) < 2:
        print("Available commands: fingerprint | store | read")
        return 1
    cmd = sys.argv[1].lower()
    cmds = {
        "fingerprint": cmd_fingerprint,
        "store": cmd_store,
        "read": cmd_read,
    }
    if cmd not in cmds:
        print(f"Unknown command '{cmd}'. Available: {', '.join(cmds)}")
        return 1
    return cmds[cmd](sys.argv[1:])

if __name__ == "__main__":
    sys.exit(main())
