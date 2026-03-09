# SONNET SESSION HANDOFF — Ancient Texts Study App

## READ THIS FIRST

You are picking up work on the **Ancient Texts Study App** — a single-file HTML biblical study tool.

**User**: Seaver Hall @ Firmatek LLC (NOT Sean)
**Project Location**: `E:\My Drive\ANCIENT_TEXTS Study App\`
**Desktop Mirror**: `C:\Users\SeaverHall\Desktop\ANCIENT_TEXTS_APP\`

## CONTEXT

This app is built by `build.py` which compiles Python data files + CSS + JS into ONE self-contained HTML file (~30MB). The build output goes to `output/AncientTextsStudy.html` and is also copied to Desktop.

### Key Architecture
- `manifest.json` — defines all texts (books) and their eras (sections)
- `data/{book}/info.py` — introduction/metadata for each book (TEXT_INFO dict)
- `data/{book}/era_*.py` — chapter content (CHAPTERS list of dicts)
- `src/css/styles.css` — dark theme CSS
- `src/js/app.js` — all application JS
- `build.py` — the build system

### The Thesis
This is NOT a systematic theology app. It reveals the **governance architecture of Scripture** through the divine council worldview (Michael Heiser lens). Every book should connect to: delegated authority, cosmic rebellion, covenant, the council.

### NT Books Use Greek (Not Hebrew)
NT era files use the `hebrew_terms` key for Greek terms (same key name for compatibility). The language is "greek" with Aramaic for Jesus' spoken words.

## YOUR TASKS (in order)

### Task 1: Inventory What Exists
```bash
# Check what files exist in each NT directory
for dir in matthew mark luke john acts romans 1corinthians 2corinthians galatians ephesians philippians colossians 1thessalonians 2thessalonians 1timothy 2timothy titus philemon hebrews james 1peter 2peter 1john 2john 3john jude revelation; do
    echo "=== $dir ==="
    ls "E:/My Drive/ANCIENT_TEXTS Study App/data/$dir/"*.py 2>/dev/null || echo "(no .py files)"
done
```

### Task 2: Write Missing info.py Files
For any NT book directory missing `info.py`, create one. Use `data/genesis/info.py` or `data/hebrews/info.py` as template. Each needs:
```python
TEXT_INFO = {
    'title': 'Book Name',
    'author': 'Author (with scholarly notes)',
    'date_composed': 'Date range',
    'original_language': 'Greek (Koine)',
    'manuscript_tradition': 'Key manuscripts',
    'theological_framework': 'Divine council connection',
    'key_themes': ['theme1', 'theme2', ...],
    'reader_notes': [
        {'heading': 'Confusing Term Explained', 'body': 'Full explanation...'},
        ...
    ]
}
```

### Task 3: Write Missing era_*.py Files
For any NT book without era files, create them. Use existing OT eras as template. Each chapter dict needs ALL 14 keys:
```python
CHAPTERS = [
    {
        'type': 'chapter',
        'title': 'Chapter Title',
        'ref': 'Book X:Y-Z',
        'period': 'ca. 50-60 AD',
        'summary': 'Brief summary...',
        'body': 'Full scholarly body text with divine council lens...',
        'hebrew_terms': [  # Greek terms for NT, kept as hebrew_terms for compat
            {'term': 'Greek term', 'transliteration': 'romanized', 'meaning': 'Full explanation...'}
        ],
        'sections': [
            {'heading': 'Section Title', 'body': 'Section content...'}
        ],
        'ane_context': 'Ancient Near East / Greco-Roman context...',
        'second_temple': 'Second Temple Jewish background...',
        'divine_council_note': 'How this connects to the divine council framework...',
        'cross_refs': [
            {'ref': 'Related passage', 'note': 'How it connects'}
        ],
        'historical_note': 'Historical background...',
        'reader_note': 'Helpful note for first-time readers...'
    },
    ...
]
```

### Task 4: Add Era Entries to manifest.json
For every era_*.py file in NT directories, add a matching era entry to manifest.json. Insert after the Daniel eras (before 1 Enoch eras). Format:
```json
{
    "id": "unique_era_id",
    "text": "book_id",
    "name": "Era Display Name",
    "chapters": "Book X-Y",
    "color": "#hex_from_text_entry",
    "icon": "I",
    "data_file": "era_filename_without_py",
    "themes": ["theme1", "theme2"]
}
```

### Task 5: Build and Fix
```bash
cd "E:/My Drive/ANCIENT_TEXTS Study App" && python build.py
```
Fix any errors. Target: 0 warnings. After successful build, verify chapter count increased from ~562.

### Task 6: Sync to Desktop
```bash
# Copy all new/modified files to Desktop mirror
for dir in matthew mark luke john acts romans 1corinthians 2corinthians galatians ephesians philippians colossians 1thessalonians 2thessalonians 1timothy 2timothy titus philemon hebrews james 1peter 2peter 1john 2john 3john jude revelation; do
    cp -r "E:/My Drive/ANCIENT_TEXTS Study App/data/$dir/"* "C:/Users/SeaverHall/Desktop/ANCIENT_TEXTS_APP/data/$dir/" 2>/dev/null
done
```

## IMPORTANT RULES
1. **Dark theme**: Background #0c0e14, gold accent #c9a84c, cream text #e0ddd5. ALL colors muted earth tones.
2. **No bright colors**: No pure red, green, blue, pink. Everything subdued.
3. **Divine council lens**: EVERY chapter must connect to governance, delegated authority, council
4. **Proactive reader notes**: Explain EVERY confusing term (Greek words, historical context, theological concepts)
5. **Don't over-engineer**: Keep it simple, follow existing patterns
6. **Research before inventing**: Read existing era files before writing new ones

## COLOR PALETTE FOR NT BOOKS (from manifest.json)
- Matthew: #5b7d9f  Mark: #6a5a4a  Luke: #5a7a6a  John: #7a6a5a
- Acts: #6a7a8a  Romans: #8a6a5a  1 Cor: #7a7a6a  2 Cor: #7a7a6a
- Galatians: #6a8a6a  Ephesians: #5a6a8a  Philippians: #7a6a7a  Colossians: #8a6a7a
- 1-2 Thess: #7a8a7a  1-2 Tim: #8a8a6a  Titus: #8a8a6a  Philemon: #8a7a8a
- Hebrews: #c9a84c  James: #6a8a6a  1-2 Peter: #6a7a8a
- 1-3 John: #7a6a5a  Jude: #8a6a6a  Revelation: #a0845a

## STATUS LOG
- Write what you completed in `SONNET_HANDOFF/STATUS.md`
- Note any issues or decisions made
