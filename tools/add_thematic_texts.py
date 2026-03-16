"""Add 4 new thematic texts + eras to manifest.json"""
import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
manifest_path = os.path.join(BASE, "manifest.json")

m = json.load(open(manifest_path, encoding="utf-8"))

new_texts = [
    {
        "id": "sheol_resurrection",
        "name": "Death, Sheol & the Resurrection Hope",
        "category": "thematic",
        "language": "multi",
        "chapters": 12,
        "color": "#7a6e8a",
        "data_dir": "sheol_resurrection",
        "content_type": "html_fragment",
        "interlinear": None,
        "description": "What the Hebrew texts actually say about death, the soul, bodily resurrection, and why the new creation is not the heaven you were taught"
    },
    {
        "id": "prophetic_sequence",
        "name": "The Prophetic Matrix",
        "category": "thematic",
        "language": "multi",
        "chapters": 10,
        "color": "#b85c3a",
        "data_dir": "prophetic_sequence",
        "content_type": "html_fragment",
        "interlinear": None,
        "description": "The eight-stage prophetic sequence from current age to new creation \u2014 what the texts actually say vs. what you were told"
    },
    {
        "id": "canon_septuagint",
        "name": "The Bible You Read & the One They Wrote",
        "category": "thematic",
        "language": "multi",
        "chapters": 10,
        "color": "#5a7a9a",
        "data_dir": "canon_septuagint",
        "content_type": "html_fragment",
        "interlinear": None,
        "description": "LXX vs Masoretic, Dead Sea Scrolls confirmation, canon formation, 1 Enoch, Jubilees, and the texts that shaped the world the apostles lived in"
    },
    {
        "id": "reward_bema",
        "name": "What You Do Now Has Eternal Weight",
        "category": "thematic",
        "language": "multi",
        "chapters": 12,
        "color": "#c9a84c",
        "data_dir": "reward_bema",
        "content_type": "html_fragment",
        "interlinear": None,
        "description": "Salvation vs reward, the bema seat, five crowns, the parable of the minas, and your role in the new creation \u2014 the reward system the church stopped teaching"
    }
]

new_eras = [
    # sheol_resurrection eras
    {"id": "sheol_hebrew", "text": "sheol_resurrection", "name": "Part I: Sheol \u2014 The Hebrew Understanding", "chapters": "Chapters 1\u20132", "color": "#7a6e8a", "icon": "I", "data_file": "era_sheol_hebrew", "themes": ["Sheol", "Hebrew death concepts", "Universal destination"]},
    {"id": "nephesh_soul", "text": "sheol_resurrection", "name": "Part II: Nephesh \u2014 You ARE a Soul", "chapters": "Chapters 3\u20134", "color": "#7a6e8a", "icon": "II", "data_file": "era_nephesh_soul", "themes": ["Nephesh", "Hebrew anthropology", "Platonic dualism"]},
    {"id": "resurrection_hope", "text": "sheol_resurrection", "name": "Part III: The Resurrection Hope", "chapters": "Chapters 5\u20136", "color": "#7a6e8a", "icon": "III", "data_file": "era_resurrection_hope", "themes": ["Bodily resurrection", "1 Corinthians 15", "Last enemy"]},
    {"id": "intermediate_state", "text": "sheol_resurrection", "name": "Part IV: Between Death & Resurrection", "chapters": "Chapters 7\u20138", "color": "#7a6e8a", "icon": "IV", "data_file": "era_intermediate_state", "themes": ["Intermediate state", "Absent from body", "Paradise"]},
    {"id": "purgatory_dismantled", "text": "sheol_resurrection", "name": "Part V: Purgatory Dismantled", "chapters": "Chapters 9\u201310", "color": "#7a6e8a", "icon": "V", "data_file": "era_purgatory_dismantled", "themes": ["Purgatory", "Tetelestai", "Hebrews 10:14"]},
    {"id": "new_creation", "text": "sheol_resurrection", "name": "Part VI: The New Creation", "chapters": "Chapters 11\u201312", "color": "#7a6e8a", "icon": "VI", "data_file": "era_new_creation", "themes": ["New heavens and earth", "Physical resurrection", "God dwelling with humanity"]},

    # prophetic_sequence eras
    {"id": "rapture_origins", "text": "prophetic_sequence", "name": "Part I: What Everyone Was Told", "chapters": "Chapters 1\u20132", "color": "#b85c3a", "icon": "I", "data_file": "era_rapture_origins", "themes": ["Rapture doctrine", "Darby 1830", "Dispensationalism"]},
    {"id": "one_return", "text": "prophetic_sequence", "name": "Part II: One Return", "chapters": "Chapters 3\u20134", "color": "#b85c3a", "icon": "II", "data_file": "era_one_return", "themes": ["Apantesis", "1 Thessalonians 4", "Single visible return"]},
    {"id": "eight_stages", "text": "prophetic_sequence", "name": "Part III: The Eight Stages", "chapters": "Chapters 5\u20136", "color": "#b85c3a", "icon": "III", "data_file": "era_eight_stages", "themes": ["Prophetic sequence", "Tribulation", "First resurrection"]},
    {"id": "millennium", "text": "prophetic_sequence", "name": "Part IV: The Millennium", "chapters": "Chapters 7\u20138", "color": "#b85c3a", "icon": "IV", "data_file": "era_millennium", "themes": ["Millennium", "Isaiah 11", "Premillennialism"]},
    {"id": "new_creation_destiny", "text": "prophetic_sequence", "name": "Part V: New Creation", "chapters": "Chapters 9\u201310", "color": "#b85c3a", "icon": "V", "data_file": "era_new_creation_destiny", "themes": ["Gog-Magog", "Great White Throne", "New Jerusalem"]},

    # canon_septuagint eras
    {"id": "lxx_mt", "text": "canon_septuagint", "name": "Part I: Two Text Traditions", "chapters": "Chapters 1\u20132", "color": "#5a7a9a", "icon": "I", "data_file": "era_lxx_mt", "themes": ["Septuagint", "Masoretic Text", "Deut 32:8"]},
    {"id": "dss_confirmation", "text": "canon_septuagint", "name": "Part II: Dead Sea Scrolls Verdict", "chapters": "Chapters 3\u20134", "color": "#5a7a9a", "icon": "II", "data_file": "era_dss_confirmation", "themes": ["4QDeutj", "Qumran", "Textual criticism"]},
    {"id": "canon_history", "text": "canon_septuagint", "name": "Part III: How We Got Our Bible", "chapters": "Chapters 5\u20136", "color": "#5a7a9a", "icon": "III", "data_file": "era_canon_history", "themes": ["Jerome", "Council of Trent", "Ethiopian Orthodox"]},
    {"id": "enoch_tradition", "text": "canon_septuagint", "name": "Part IV: 1 Enoch", "chapters": "Chapters 7\u20138", "color": "#5a7a9a", "icon": "IV", "data_file": "era_enoch_tradition", "themes": ["1 Enoch", "Jude 14-15", "Three-tier framework"]},
    {"id": "other_texts", "text": "canon_septuagint", "name": "Part V: Jubilees, Giants & Beyond", "chapters": "Chapters 9\u201310", "color": "#5a7a9a", "icon": "V", "data_file": "era_other_texts", "themes": ["Jubilees", "Book of Giants", "4 Ezra"]},

    # reward_bema eras
    {"id": "salvation_vs_reward", "text": "reward_bema", "name": "Part I: The Critical Distinction", "chapters": "Chapters 1\u20132", "color": "#c9a84c", "icon": "I", "data_file": "era_salvation_vs_reward", "themes": ["Salvation vs reward", "Grace", "Works evaluated"]},
    {"id": "bema_seat", "text": "reward_bema", "name": "Part II: The Judgment Seat", "chapters": "Chapters 3\u20134", "color": "#c9a84c", "icon": "II", "data_file": "era_bema_seat", "themes": ["Bema", "2 Corinthians 5:10", "Fire testing"]},
    {"id": "five_crowns", "text": "reward_bema", "name": "Part III: The Five Crowns", "chapters": "Chapters 5\u20136", "color": "#c9a84c", "icon": "III", "data_file": "era_five_crowns", "themes": ["Stephanos", "Crown of life", "Crown of glory"]},
    {"id": "minas_parable", "text": "reward_bema", "name": "Part IV: The Parable of the Minas", "chapters": "Chapters 7\u20138", "color": "#c9a84c", "icon": "IV", "data_file": "era_minas_parable", "themes": ["Luke 19", "Ten cities", "Faithful stewardship"]},
    {"id": "reigning_with_christ", "text": "reward_bema", "name": "Part V: Reigning With Christ", "chapters": "Chapters 9\u201310", "color": "#c9a84c", "icon": "V", "data_file": "era_reigning_with_christ", "themes": ["Divine council replacement", "Judge angels", "Revelation 22:5"]},
    {"id": "treasures_new_creation", "text": "reward_bema", "name": "Part VI: Treasures & the New Creation", "chapters": "Chapters 11\u201312", "color": "#c9a84c", "icon": "VI", "data_file": "era_treasures_new_creation", "themes": ["Thesauros", "Differentiated glory", "Nations and kings"]},
]

# Insert new texts after last thematic text
last_thematic = max(i for i, t in enumerate(m["texts"]) if t.get("category") == "thematic")
for j, nt in enumerate(new_texts):
    m["texts"].insert(last_thematic + 1 + j, nt)

# Append new eras
m["eras"].extend(new_eras)

# Save
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(m, f, ensure_ascii=False)

print(f"Added {len(new_texts)} texts and {len(new_eras)} eras")
print(f"Total texts: {len(m['texts'])}, Total eras: {len(m['eras'])}")

# Verify
thematic_count = sum(1 for t in m["texts"] if t["category"] == "thematic")
print(f"Thematic texts now: {thematic_count}")
for t in m["texts"]:
    if t["category"] == "thematic":
        era_count = sum(1 for e in m["eras"] if e["text"] == t["id"])
        print(f"  {t['id']}: {era_count} eras")
