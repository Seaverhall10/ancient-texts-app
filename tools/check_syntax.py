"""Check all new OT book data files for Python syntax errors."""
import ast
import glob
import os

NEW_BOOKS = [
    "job", "proverbs", "ecclesiastes", "jeremiah", "ezekiel", "lamentations",
    "hosea", "joel", "amos", "obadiah", "jonah", "micah",
    "nahum", "habakkuk", "zephaniah", "haggai", "zechariah", "malachi",
    "songofsolomon", "1chronicles", "2chronicles", "ezra", "nehemiah", "esther"
]

errors = []
ok = 0

for book in NEW_BOOKS:
    book_dir = os.path.join("data", book)
    py_files = glob.glob(os.path.join(book_dir, "*.py"))
    for fpath in py_files:
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                source = f.read()
            ast.parse(source)
            ok += 1
        except SyntaxError as e:
            errors.append((fpath, e.lineno, e.msg))
            print(f"ERROR: {fpath}:{e.lineno} - {e.msg}")

print(f"\nTotal files: {ok + len(errors)}, OK: {ok}, Errors: {len(errors)}")
