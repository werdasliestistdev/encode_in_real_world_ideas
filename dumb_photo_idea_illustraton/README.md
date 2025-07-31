
# 1) Generate the canonical fingerprint for a tree-cross-section photo
python tree_data.py fingerprint download-6.jpg
# → 8b4e2572dd6eb2eee9a649a4f5d93873363843c6ba0ec211d7eb8c11ea2d5373

# 2) Store a payload keyed by that fingerprint
python tree_data.py store download-6.jpg "goodbye world" db.json

# 3) Later, read the payload from a fresh photo of the same object
python tree_data.py read download-6.jpg db.json
# → goodbye world

