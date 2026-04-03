"""Build the Psalms of Solomon flow file from parsed JSON data."""
import json
import re
import sys

with open('tools/pssol_parsed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

total_verses = 0
for ch_str in sorted(data.keys(), key=int):
    total_verses += len(data[ch_str])

out = []
out.append('"""')
out.append('Flow translations for Psalms of Solomon -- complete text.')
out.append('G. Buchanan Gray translation from R.H. Charles, APOT (1913), public domain.')
out.append('Source: Wesley Center Online (NNU).')
out.append('')
out.append('A collection of 18 psalms composed in the 1st century BC, likely in')
out.append("response to Pompey's conquest of Jerusalem (63 BC). Contains significant")
out.append('messianic expectations (Ps Sol 17-18) describing a Davidic king who will')
out.append('purge Jerusalem and rule the nations. Important background for NT')
out.append('messianic theology.')
out.append('')
out.append(f'Chapters: 18 | Verses: {total_verses}')
out.append('"""')
out.append('')
out.append('FLOW_PSALMS_OF_SOLOMON = {')

for ch_str in sorted(data.keys(), key=int):
    ch = int(ch_str)
    verses = data[ch_str]
    sorted_keys = sorted(verses.keys(), key=int)

    out.append(f'    {ch}: {{  # Psalm {ch}')
    for i, vk in enumerate(sorted_keys, 1):
        text = verses[vk]
        # Clean artifacts
        text = text.replace('[ ]', '').replace('< >', '').strip()
        text = re.sub(r'\(\)\s*', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        # Replace unicode dashes
        text = text.replace('\u2014', '--')
        text = text.replace('\u2013', '-')
        # Escape for Python single-quoted string
        text = text.replace('\\', '\\\\')
        text = text.replace("'", "\\'")
        out.append(f"        {i}: '{text}',")
    out.append('    },')

out.append('}')
out.append('')
out.append('NOTES_PSALMS_OF_SOLOMON = {}')
out.append('')

content = '\n'.join(out)

# Verify syntax
try:
    compile(content, 'flow_psalms_of_solomon.py', 'exec')
    print("Syntax check PASSED")
except SyntaxError as e:
    print(f"Syntax error at line {e.lineno}: {e}")
    lines = content.split('\n')
    print(f"  {lines[e.lineno - 1][:200]}")
    sys.exit(1)

with open('data/flow/flow_psalms_of_solomon.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Written {len(content)} bytes, 18 psalms, {total_verses} verses")
