# Grok Map Enhancement Tasks

## Priority 1: High-Resolution Historical Boundaries (GeoJSON)

Create ACCURATE GeoJSON polygons for these empires/kingdoms at their maximum extent.
These need REAL geographic coordinates, not simplified shapes.

### Required Empires (chronological):
1. **Sumerian City-States** (~3500-2334 BC) — Southern Mesopotamia
2. **Akkadian Empire** (~2334-2154 BC) — Sargon's empire
3. **Third Dynasty of Ur** (~2112-2004 BC) — Neo-Sumerian
4. **Old Babylonian Empire** (~1894-1595 BC) — Hammurabi
5. **Egyptian New Kingdom** (~1550-1070 BC) — Thutmose III maximum
6. **Hittite Empire** (~1600-1178 BC) — Anatolia to Syria
7. **Mitanni Kingdom** (~1500-1300 BC) — Upper Mesopotamia
8. **Ugaritic Kingdom** (~1450-1185 BC) — coastal Syria
9. **Kingdom of Israel (United)** (~1000-930 BC) — David/Solomon
10. **Northern Kingdom (Israel)** (~930-722 BC)
11. **Southern Kingdom (Judah)** (~930-586 BC)
12. **Phoenician City-States** (~1200-332 BC) — coastal trade network
13. **Neo-Assyrian Empire** (~911-612 BC) — Tiglath-Pileser through fall
14. **Neo-Babylonian Empire** (~626-539 BC) — Nebuchadnezzar
15. **Achaemenid Persian Empire** (~550-330 BC) — Cyrus to Darius III
16. **Alexander's Empire** (~334-323 BC)
17. **Ptolemaic Egypt** (~305-30 BC)
18. **Seleucid Empire** (~312-63 BC)
19. **Hasmonean Kingdom** (~140-63 BC)
20. **Roman Republic/Empire** (~264 BC - 476 AD)
21. **Herod's Kingdom** (~37-4 BC)
22. **Byzantine Empire** (~330-1453 AD, max extent under Justinian)
23. **Rashidun/Umayyad Caliphate** (~632-750 AD)
24. **Crusader States** (~1099-1291 AD)
25. **Ottoman Empire** (~1299-1922, max extent ~1683)
26. **British Mandate Palestine** (~1920-1948)
27. **Modern Israel** (1949 Armistice lines)
28. **Modern Israel** (post-1967, including occupied territories)

### Format Required:
```json
{
  "name": "Neo-Assyrian Empire (~745-612 BC)",
  "color": "#c0392b",
  "period_start": -745,
  "period_end": -612,
  "description": "Maximum extent under Tiglath-Pileser III, Sargon II, Sennacherib",
  "biblical_refs": "2 Kings 15-19; Isaiah 10; Nahum",
  "coords": [[lat, lng], [lat, lng], ...]
}
```

## Priority 2: More Megalithic Sites (Target: 100+)

Current count: ~30 sites. Target: 100+ globally.

### Missing Regions:
- **Korean Peninsula** — 30,000+ dolmens (largest concentration on Earth)
- **Indian subcontinent** — Megaliths of South India, Mahabalipuram
- **China** — Longyou Caves, terracotta army area megaliths
- **Southeast Asia** — Plain of Jars (Laos), Bada Valley (Sulawesi)
- **Russia/Caucasus** — Dolmens of Western Caucasus, Arkaim
- **Northern Africa** — Djenne-Djenno, Mzora Ring (Morocco)
- **Scandinavia** — Ale's Stones, Anundshög, Jelling Stones
- **Central Europe** — Externsteine, Goseck Circle
- **Australia/Oceania** — Wurdi Youang, Hawaiian heiau
- **Caribbean** — Stonehenge-like structures in Belize
- **North America** — Serpent Mound, Cahokia Mounds, Mystery Hill/America's Stonehenge

### Format:
```json
{
  "cat": "megalith",
  "name": "Site Name",
  "lat": 37.2236,
  "lng": 38.9217,
  "desc": "Factual description (what it is, when built, key stats)",
  "refs": "Biblical cross-references if any",
  "note": "Interesting connections, alternative theories, giant legends",
  "alt_theory": "The 'tin foil' speculation (labeled clearly as speculation)"
}
```

## Priority 3: More Journey Routes

### Missing Biblical Journeys:
- **Ruth's Journey** — Moab to Bethlehem
- **Jonah's Flight** — Joppa to Tarshish (failed) + Nineveh
- **Ezra's Return** — Babylon to Jerusalem
- **Nehemiah's Journey** — Susa to Jerusalem
- **Jesus' Ministry** — Bethlehem → Egypt → Nazareth → Jordan → Galilee → Jerusalem
- **Paul's Missionary Journeys** (3 routes + journey to Rome)
- **Philip's Ministry** — Samaria → Gaza road → Caesarea
- **Peter's Journeys** — Jerusalem → Joppa → Caesarea → Antioch → Rome

## Priority 4: Ancient Trade Routes
- **King's Highway** — Egypt to Damascus via Transjordan
- **Via Maris (Way of the Sea)** — Egypt to Mesopotamia via coast
- **Incense Route** — South Arabia to Mediterranean
- **Silk Road** (western terminus) — connection to Rome/Antioch

## Output Format
All data should be in JSON format, ready to be integrated into the Leaflet map.
Coordinates must be [latitude, longitude] in decimal degrees (WGS84).
