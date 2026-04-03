"""
bible_analysis.py — Structured data for the Bible Analysis tab.
Contains 70 book entries across 7 sections.
Parsed from docs/bible_study_reference.html.
"""

THEME_FILTERS = [
    {"code": 'SEED', "label": 'SEED'},
    {"code": 'COV', "label": 'COVENANT'},
    {"code": 'DC', "label": 'DIVINE COUNCIL'},
    {"code": 'REBEL', "label": 'REBELLION'},
    {"code": 'EXILE', "label": 'EXILE'},
    {"code": 'SPIRIT', "label": 'SPIRITUAL WAR'},
    {"code": 'KING', "label": 'KINGSHIP'},
    {"code": 'PRIEST', "label": 'PRIESTHOOD'},
    {"code": 'TYPE', "label": 'TYPOLOGY'},
    {"code": 'NATIONS', "label": 'NATIONS'},
    {"code": 'WOMEN', "label": 'WOMEN'},
    {"code": 'REMNANT', "label": 'REMNANT'},
]

BOOK_SECTIONS = [
    {"id": 'pentateuch', "title": 'The Pentateuch (Torah)'},
    {"id": 'historical-books', "title": 'Historical Books'},
    {"id": 'wisdom-books', "title": 'Wisdom & Poetry'},
    {"id": 'major-prophets', "title": 'Major Prophets'},
    {"id": 'minor-prophets-section', "title": 'The Twelve — Minor Prophets'},
    {"id": 'new-testament', "title": 'The New Testament'},
    {"id": 'non-canonical', "title": 'Non-Canonical Texts'},
]

BOOK_ENTRIES = [
    {
        "id": 'genesis',
        "section": 'pentateuch',
        "title": 'Book 1: Genesis (Bereshit)',
        "themes": 'SEED COV DC REBEL EXILE IMAGE TYPE HOLY SPIRIT WOMEN REVERSAL NATIONS DREAM',
        "era_count": 8,
        "chapters": 50,
        "grade": 'A+',
        "meta_text": '8 era files &middot; 50 chapters &middot; Grade: A+',
        "body_html": '''<h4>Major Themes</h4>
  <div class="theme-grid">
    <span class="badge badge-theme">SEED</span><span class="badge badge-theme">COVENANT</span><span class="badge badge-theme">DIVINE COUNCIL</span><span class="badge badge-theme">THREE REBELLIONS</span><span class="badge badge-theme">IMAGE OF GOD</span><span class="badge badge-theme">EXILE-RETURN</span>
  </div>
  <p><strong>SEED (Gen 3:15)</strong> <span class="badge badge-critical">CRITICAL</span> — The thesis statement. Every genealogy tracks the seed line: Seth &rarr; Noah &rarr; Shem &rarr; Abraham &rarr; Isaac &rarr; Jacob &rarr; Judah &rarr; David &rarr; Christ.</p>
  <p><strong>COVENANT (berit)</strong> <span class="badge badge-major">MAJOR</span> — Three covenants: Noahic (Gen 9, universal), Abrahamic (Gen 15/17, unilateral — God alone passes through the cut animals), Circumcision (Gen 17, sign).</p>
  <p><strong>DIVINE COUNCIL</strong> <span class="badge badge-critical">CRITICAL</span> — "Let US make man" (1:26). "Like one of US" (3:22). bene ha'elohim take wives (6:1-4). "Let US go down" (11:7). YHWH + two malakim visit Abraham (18-19).</p>
  <p><strong>THREE REBELLIONS</strong> — Eden (ch. 3, nachash/guardian cherub). Hermon (ch. 6, 200 Watchers). Babel (ch. 11, nations allotted to lesser elohim per Deut 32:8).</p>

  <h4>Contested Words</h4>
  <table class="ref-table">
    <tr><th>Hebrew</th><th>Issue</th><th>Severity</th></tr>
    <tr><td><strong>elohim</strong></td><td>"God" vs. "gods" vs. "divine beings" — same word for YHWH and the council. English translations obscure the plurality.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>bene ha'elohim</strong> (6:2)</td><td>"Sons of God" = divine beings, NOT "sons of Seth." Sethite view introduced 3rd c. AD, zero Hebrew support.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>nephilim</strong> (6:4)</td><td>From naphal (to fall)? Giants, fallen ones. LXX: gigantes. Offspring of Watchers + human women.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>nachash</strong> (3:1)</td><td>Three roots with same consonants: snake, shine, divine. Isa 14 and Ezek 28 use "shining" sense.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>zera</strong> (3:15)</td><td>Seed — singular (Christ) or collective? Paul argues singular (Gal 3:16).</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>tselem</strong> (1:26)</td><td>"Image" but literally carved statue. ANE kings placed tselem in territory. Functional vs. ontological.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>berit</strong> (15:18)</td><td>Covenant — "cut" (karat berit). Unilateral or bilateral? Shapes whether God's promises are conditional.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>ruach</strong> (1:2)</td><td>"Spirit of God" or "wind of God" or "mighty wind"?</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>tohu wabohu</strong> (1:2)</td><td>Formless and void, chaos. Pre-existing chaos or created state? Gap theory.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>hesed</strong> (24:27)</td><td>Steadfast love, mercy, loyalty — no single English word captures covenant faithfulness.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
  </table>

  <h4>Unusual Characters</h4>
  <ul>
    <li><strong>Melchizedek</strong> (14:18) — King of Salem + priest of El Elyon. No genealogy. Serves bread and wine. Abraham tithes to him. &rarr; Ps 110:4, Heb 5-7.</li>
    <li><strong>Enoch</strong> (5:24) — "Walked with God and was not." Didn't die. &rarr; Heb 11:5, Jude 14-15 (quotes 1 Enoch).</li>
    <li><strong>The Nachash</strong> (ch. 3) — NOT a snake. A "shining one" / guardian cherub in Eden (Ezek 28:13-15). &rarr; Rev 12:9, 20:2.</li>
    <li><strong>Hagar</strong> (16, 21) — The ONLY person in the Bible who NAMES God ("El Roi" — the God who sees me).</li>
    <li><strong>Tamar</strong> (ch. 38) — Forces Judah to fulfill levirate duty. "She is more righteous than I." In Jesus' genealogy (Matt 1:3).</li>
  </ul>

  <h4>Conspicuous Silences</h4>
  <ul>
    <li>Satan never named — the nachash is never called "Satan" in Genesis (identified in Rev 12:9)</li>
    <li>No afterlife details — people die but Genesis says nothing about where they go</li>
    <li>Why God chose Abraham — Gen 12:1 starts mid-sentence with no explanation</li>
    <li>The 400-year gap — Genesis 50 to Exodus 1 is a black hole</li>
    <li>Enoch's story — one verse (5:24) for the man 1 Enoch gives 108 chapters</li>
  </ul>

  <h4>Cross-References</h4>
  <p class="xref">Genesis <span class="arrow">&rarr;</span> <span class="badge badge-ot">Exodus</span> <span class="badge badge-ot">Deuteronomy</span> <span class="badge badge-nt">Romans</span> <span class="badge badge-nt">Galatians</span> <span class="badge badge-nt">Hebrews</span> <span class="badge badge-dss">1 Enoch</span> <span class="badge badge-nt">Revelation</span> <span class="badge badge-ot">Job</span> <span class="badge badge-ot">Psalms</span></p>''',
        "key_claim": "Genesis 3:15 is the thesis statement of the entire Bible — every genealogy, every covenant, every conflict from Cain to Christ tracks the seed line and the war between the serpent's offspring and the woman's.",
        "contested_words": [
            {"word": "elohim", "hebrew": "אֱלֹהִים", "issue": "'God' vs. 'gods' vs. 'divine beings' — same word for YHWH and the council. English translations obscure the plurality.", "severity": "CRITICAL"},
            {"word": "bene ha'elohim", "hebrew": "בְּנֵי הָאֱלֹהִים", "issue": "'Sons of God' = divine beings, NOT 'sons of Seth.' Sethite view introduced 3rd c. AD, zero Hebrew support.", "severity": "CRITICAL"},
            {"word": "nephilim", "hebrew": "נְפִילִים", "issue": "From naphal (to fall)? Giants, fallen ones. LXX: gigantes. Offspring of Watchers + human women.", "severity": "CRITICAL"},
            {"word": "nachash", "hebrew": "נָחָשׁ", "issue": "Three roots with same consonants: snake, shine, divine. Isa 14 and Ezek 28 use 'shining' sense.", "severity": "CRITICAL"},
            {"word": "zera", "hebrew": "זֶרַע", "issue": "Seed — singular (Christ) or collective? Paul argues singular (Gal 3:16).", "severity": "CRITICAL"},
            {"word": "tselem", "hebrew": "צֶלֶם", "issue": "'Image' but literally carved statue. ANE kings placed tselem in territory. Functional vs. ontological.", "severity": "MAJOR"},
            {"word": "berit", "hebrew": "בְּרִית", "issue": "Covenant — 'cut' (karat berit). Unilateral or bilateral? Shapes whether God's promises are conditional.", "severity": "MAJOR"},
            {"word": "ruach", "hebrew": "רוּחַ", "issue": "'Spirit of God' or 'wind of God' or 'mighty wind'?", "severity": "MAJOR"},
            {"word": "tohu wabohu", "hebrew": "תֹהוּ וָבֹהוּ", "issue": "Formless and void, chaos. Pre-existing chaos or created state? Gap theory.", "severity": "MAJOR"},
            {"word": "hesed", "hebrew": "חֶסֶד", "issue": "Steadfast love, mercy, loyalty — no single English word captures covenant faithfulness.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "exodus", "why": "Passover lamb typology begins with God clothing Adam/Eve in skins (3:21) and Abraham's 'God will provide the lamb' (22:8)"},
            {"target": "deuteronomy", "why": "Babel scattering (Gen 11) directly sets up the Deut 32:8 allotment of nations to lesser elohim"},
            {"target": "romans", "why": "Adam-Christ typology (Rom 5:12-21) and Abraham's faith-righteousness (Rom 4, cf. Gen 15:6)"},
            {"target": "galatians", "why": "Paul argues zera (seed) in Gen 3:15/12:7 is singular = Christ (Gal 3:16)"},
            {"target": "hebrews", "why": "Melchizedek priesthood (Gen 14:18) becomes the anchor of Christ's superior priesthood (Heb 5-7)"},
            {"target": "1enoch", "why": "Genesis 6:1-4 is the compressed account; 1 Enoch 6-16 provides the full Watcher narrative"},
            {"target": "revelation", "why": "The nachash of Eden (Gen 3) is identified as Satan/the dragon (Rev 12:9, 20:2); Eden restored in Rev 21-22"},
            {"target": "job", "why": "bene ha'elohim appear in the divine council (Job 1:6, 2:1) — same phrase as Gen 6:2"},
            {"target": "psalms", "why": "Melchizedek reappears in Ps 110:4; divine council in Ps 82; creation theology in Ps 8, 104"},
        ],
        "what_it_doesnt_say": [
            "Satan never named — the nachash is never called 'Satan' in Genesis (identified in Rev 12:9)",
            "No afterlife details — people die but Genesis says nothing about where they go",
            "Why God chose Abraham — Gen 12:1 starts mid-sentence with no explanation",
            "The 400-year gap — Genesis 50 to Exodus 1 is a black hole",
            "Enoch's story — one verse (5:24) for the man 1 Enoch gives 108 chapters",
        ],
        "unusual_characters": [
            {"name": "Melchizedek", "ref": "14:18", "detail": "King of Salem + priest of El Elyon. No genealogy. Serves bread and wine. Abraham tithes to him.", "connections": ["psalms", "hebrews"]},
            {"name": "Enoch", "ref": "5:24", "detail": "Walked with God and was not. Didn't die.", "connections": ["hebrews", "jude", "1enoch"]},
            {"name": "The Nachash", "ref": "3:1", "detail": "NOT a snake. A 'shining one' / guardian cherub in Eden (Ezek 28:13-15).", "connections": ["isaiah", "ezekiel", "revelation"]},
            {"name": "Hagar", "ref": "16:13", "detail": "The ONLY person in the Bible who NAMES God ('El Roi' — the God who sees me).", "connections": ["galatians"]},
            {"name": "Tamar", "ref": "38:6", "detail": "Forces Judah to fulfill levirate duty. 'She is more righteous than I.' In Jesus' genealogy.", "connections": ["ruth", "matthew"]},
        ],
        "patterns": [
            "Toledot structure: 'These are the generations of...' appears 11 times, organizing the entire book",
            "Chiasm in the Flood narrative (Gen 6-9): 'God remembered Noah' at the center",
            "First-mention principle: first occurrence of key words (covenant, love, worship, prophet) sets the pattern for the rest of Scripture",
            "Seven-fold patterns: 7 days of creation, 7 'good' declarations, Lamech's 77-fold vengeance vs. 7-fold for Cain",
            "Reversal of primogeniture: younger chosen over older repeatedly (Isaac over Ishmael, Jacob over Esau, Joseph over brothers, Ephraim over Manasseh)",
        ],
        "mistranslations": [
            {"english": "God", "original": "elohim", "issue": "Hides divine council plurality — same word used for YHWH, angels, and the council"},
            {"english": "serpent", "original": "nachash", "issue": "Hides the 'shining one' meaning — reduces a divine being to an animal"},
            {"english": "giants", "original": "nephilim", "issue": "Obscures the 'fallen ones' etymology and connection to divine-human hybridization"},
        ],
    },
    {
        "id": 'exodus',
        "section": 'pentateuch',
        "title": 'Book 2: Exodus (Shemot)',
        "themes": 'SEED COV DC TYPE HOLY PRIEST BLOOD WOMEN NATIONS SPIRIT',
        "era_count": 8,
        "chapters": 40,
        "grade": 'A+',
        "meta_text": '8 era files &middot; 40 chapters &middot; Grade: A+',
        "body_html": '''<h4>Major Themes</h4>
  <div class="theme-grid">
    <span class="badge badge-theme">YHWH REVEALED</span><span class="badge badge-theme">COSMIC WARFARE</span><span class="badge badge-theme">PASSOVER TYPOLOGY</span><span class="badge badge-theme">HARDENING</span><span class="badge badge-theme">SINAI COVENANT</span><span class="badge badge-theme">TABERNACLE</span><span class="badge badge-theme">GOLDEN CALF</span>
  </div>
  <p><strong>YHWH REVEALED</strong> <span class="badge badge-critical">CRITICAL</span> — God reveals his personal name (3:14-15). ehyeh asher ehyeh — "I AM WHO I AM" or "I WILL BE WHAT I WILL BE." The LORD (all caps) in English hides the divine name from readers.</p>
  <p><strong>PLAGUES AS COSMIC WARFARE</strong> <span class="badge badge-major">MAJOR</span> — Ex 12:12: "Against all the gods of Egypt I will execute judgments." Each plague targets a specific Egyptian deity. YHWH dismantles the spiritual powers behind Egypt's pantheon.</p>
  <p><strong>PASSOVER TYPOLOGY</strong> <span class="badge badge-critical">CRITICAL</span> — Unblemished lamb (12:5) &rarr; Christ "without blemish" (1 Pet 1:19). Blood on doorposts &rarr; blood of Christ. No bones broken (12:46) &rarr; John 19:36. "Christ our Passover" (1 Cor 5:7).</p>
  <p><strong>HARDENING</strong> <span class="badge badge-critical">CRITICAL</span> — Three different Hebrew words all translated "harden": chazaq (strengthen), kaved (make heavy), qashah (stiffen). Pharaoh hardens his OWN heart first (chs. 7-8), then God hardens it (chs. 9-14).</p>
  <p><strong>TABERNACLE AS REVERSE-EDEN</strong> <span class="badge badge-major">MAJOR</span> — Portable Eden. Cherubim guard the Holy of Holies just as cherubim guard Eden. Built from a heavenly "pattern" (tavnit). 7 speeches of instruction mirror 7 days of creation.</p>

  <h4>Contested Words</h4>
  <table class="ref-table">
    <tr><th>Hebrew</th><th>Issue</th><th>Severity</th></tr>
    <tr><td><strong>YHWH</strong> (3:14-15)</td><td>The divine name itself — meaning, pronunciation, origin all debated. "LORD" hides it.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>ehyeh asher ehyeh</strong> (3:14)</td><td>"I AM WHO I AM" or "I WILL BE WHAT I WILL BE"? Self-existence or promise of presence?</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>pesach</strong> (12:13)</td><td>"Pass over" or "hover over/protect"? Does God skip the house or guard the door?</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>yam suph</strong> (13:18)</td><td>"Red Sea" or "Reed Sea"? suph = reeds. LXX translated it "Red Sea" and it stuck.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>mashchit</strong> (12:23)</td><td>"The destroyer" — a distinct being, NOT YHWH. A divine council agent executing the decree.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>nacham</strong> (32:14)</td><td>"Relented" or "repented" or "changed his mind"? Does God change his mind? Used 30+ times.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
  </table>

  <h4>Unusual Characters</h4>
  <ul>
    <li><strong>The Destroyer (mashchit)</strong> (12:23) — A distinct being executing the 10th plague, NOT YHWH himself. Divine council agent.</li>
    <li><strong>Bezalel</strong> (31:1-5) — First person "filled with the Spirit of God" — for CRAFTSMANSHIP, not prophecy.</li>
    <li><strong>Pharaoh</strong> (unnamed) — The text NEVER names the exodus Pharaoh. Deliberate damnatio memoriae.</li>
    <li><strong>Five women of Exodus 1-2</strong> — Shiphrah, Puah, Jochebed, Miriam, Pharaoh's daughter: they outwit the most powerful man on earth.</li>
  </ul>''',
        "key_claim": "The plagues are not random natural disasters but targeted strikes against Egypt's gods — YHWH systematically dismantles an entire pantheon to demonstrate his supremacy over the spiritual powers behind the nations.",
        "contested_words": [
            {"word": "YHWH", "hebrew": "יהוה", "issue": "The divine name itself — meaning, pronunciation, origin all debated. 'LORD' hides it.", "severity": "CRITICAL"},
            {"word": "ehyeh asher ehyeh", "hebrew": "אֶהְיֶה אֲשֶׁר אֶהְיֶה", "issue": "'I AM WHO I AM' or 'I WILL BE WHAT I WILL BE'? Self-existence or promise of presence?", "severity": "CRITICAL"},
            {"word": "nacham", "hebrew": "נָחַם", "issue": "'Relented' or 'repented' or 'changed his mind'? Does God change his mind? Used 30+ times.", "severity": "CRITICAL"},
            {"word": "pesach", "hebrew": "פֶּסַח", "issue": "'Pass over' or 'hover over/protect'? Does God skip the house or guard the door?", "severity": "MAJOR"},
            {"word": "yam suph", "hebrew": "יַם סוּף", "issue": "'Red Sea' or 'Reed Sea'? suph = reeds. LXX translated it 'Red Sea' and it stuck.", "severity": "MAJOR"},
            {"word": "mashchit", "hebrew": "מַשְׁחִית", "issue": "'The destroyer' — a distinct being, NOT YHWH. A divine council agent executing the decree.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "genesis", "why": "Passover lamb fulfills the pattern of substitutionary sacrifice begun with the skins in Gen 3:21 and the ram for Isaac in Gen 22"},
            {"target": "leviticus", "why": "The tabernacle instructions (Ex 25-40) set up the entire sacrificial system codified in Leviticus"},
            {"target": "hebrews", "why": "The tabernacle as 'copy and shadow' of heavenly reality (Heb 8:5, cf. Ex 25:40 tavnit/pattern)"},
            {"target": "revelation", "why": "The plagues of Exodus reappear in Revelation's trumpet and bowl judgments; the exodus pattern of cosmic liberation repeated"},
            {"target": "1corinthians", "why": "'Christ our Passover lamb has been sacrificed' (1 Cor 5:7) — direct Passover typology"},
            {"target": "john", "why": "Jesus crucified at Passover; 'not a bone shall be broken' (John 19:36, cf. Ex 12:46)"},
        ],
        "what_it_doesnt_say": [
            "Pharaoh is never named — deliberate damnatio memoriae, the most powerful man on earth denied identity",
            "No explanation of how Israel maintained identity for 400 years in Egypt",
            "The burning bush is never explained — what kind of fire doesn't consume?",
            "Moses' 40 years in Midian are compressed into a few verses",
            "No account of how Israel learned to build the tabernacle's sophisticated structures",
        ],
        "unusual_characters": [
            {"name": "The Destroyer (mashchit)", "ref": "12:23", "detail": "A distinct being executing the 10th plague, NOT YHWH himself. Divine council agent.", "connections": ["2samuel", "1chronicles", "revelation"]},
            {"name": "Bezalel", "ref": "31:1-5", "detail": "First person 'filled with the Spirit of God' — for CRAFTSMANSHIP, not prophecy.", "connections": []},
            {"name": "Pharaoh", "ref": "1:8", "detail": "The text NEVER names the exodus Pharaoh. Deliberate damnatio memoriae.", "connections": ["romans"]},
            {"name": "Shiphrah and Puah", "ref": "1:15", "detail": "Hebrew midwives who defy Pharaoh's genocide order — named when Pharaoh is not.", "connections": []},
        ],
        "patterns": [
            "Seven speeches of tabernacle instruction mirror the seven days of creation — tabernacle as new Eden",
            "Hardening escalation: Pharaoh hardens his OWN heart first (chs. 7-8), then God hardens it (chs. 9-14) — three different Hebrew words: chazaq, kaved, qashah",
            "Plagues follow a 3x3+1 structure: three sets of three plagues with escalating severity, then the 10th as climax",
            "Chiasm in the Song of the Sea (Ex 15): YHWH as warrior at the center",
        ],
        "mistranslations": [
            {"english": "LORD", "original": "YHWH", "issue": "Hides the personal divine name behind a title — readers never learn God's actual name"},
            {"english": "Red Sea", "original": "yam suph", "issue": "Obscures 'Sea of Reeds' — LXX mistranslation that stuck for 2,000 years"},
            {"english": "hardened", "original": "chazaq/kaved/qashah", "issue": "Collapses three distinct Hebrew concepts (strengthen/make heavy/stiffen) into one English word"},
        ],
    },
    {
        "id": 'leviticus',
        "section": 'pentateuch',
        "title": 'Book 3: Leviticus (Vayikra)',
        "themes": 'HOLY PRIEST BLOOD COV TYPE',
        "era_count": 5,
        "chapters": 27,
        "grade": 'A',
        "meta_text": '5 era files &middot; 27 chapters &middot; Grade: A',
        "body_html": '''<h4>Major Themes</h4>
  <div class="theme-grid">
    <span class="badge badge-theme">HOLINESS</span><span class="badge badge-theme">SACRIFICE</span><span class="badge badge-theme">AZAZEL</span><span class="badge badge-theme">PRIESTHOOD</span><span class="badge badge-theme">JUBILEE</span>
  </div>
  <p><strong>HOLINESS CODE</strong> <span class="badge badge-critical">CRITICAL</span> — "Be holy (qadosh) for I YHWH your God am holy" (19:2). Holiness = separation + consecration. Not moralism but ontological distinction.</p>
  <p><strong>DAY OF ATONEMENT / AZAZEL</strong> <span class="badge badge-critical">CRITICAL</span> — Lev 16: Two goats. One sacrificed to YHWH, one sent to Azazel in the wilderness. Azazel = a specific imprisoned Watcher (1 Enoch 10:4-6). The scapegoat sends sins BACK to their originator.</p>
  <p><strong>FIVE OFFERINGS</strong> — Burnt (olah), grain (minchah), peace (shelamim), sin (chattat), guilt (asham). Each addresses a different dimension of the God-human relationship.</p>
  <p><strong>JUBILEE</strong> (ch. 25) <span class="badge badge-major">MAJOR</span> — Every 50th year: land reverts, slaves freed, debts cancelled. Economic reset rooted in divine ownership: "The land is mine; you are strangers and sojourners with me" (25:23). Jesus' inaugural sermon (Luke 4:18-19) declares Jubilee fulfilled.</p>

  <h4>Key Contested Words</h4>
  <table class="ref-table">
    <tr><th>Hebrew</th><th>Issue</th><th>Severity</th></tr>
    <tr><td><strong>azazel</strong> (16:8)</td><td>"Scapegoat" or proper name of a Watcher/demon? 1 Enoch 10:4-6 names Azazel as the imprisoned Watcher leader.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>kaphar</strong> (16:30)</td><td>"Atone" — but does it mean cover, cleanse, or ransom? Shapes entire atonement theology.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>qadosh</strong> (19:2)</td><td>"Holy" — separated/set apart. Not moral perfection but ontological distinction.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>se'irim</strong> (17:7)</td><td>"Goat demons" — hairy ones. Israel sacrificing to actual spiritual entities in the wilderness.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
  </table>''',
        "key_claim": "The Day of Atonement (Lev 16) sends one goat to YHWH and one to Azazel — a specific imprisoned Watcher — returning sins to their originator, not merely symbolizing removal.",
        "contested_words": [
            {"word": "azazel", "hebrew": "עֲזָאזֵל", "issue": "'Scapegoat' or proper name of a Watcher/demon? 1 Enoch 10:4-6 names Azazel as the imprisoned Watcher leader.", "severity": "CRITICAL"},
            {"word": "kaphar", "hebrew": "כָּפַר", "issue": "'Atone' — but does it mean cover, cleanse, or ransom? Shapes entire atonement theology.", "severity": "CRITICAL"},
            {"word": "qadosh", "hebrew": "קָדוֹשׁ", "issue": "'Holy' — separated/set apart. Not moral perfection but ontological distinction.", "severity": "MAJOR"},
            {"word": "se'irim", "hebrew": "שְׂעִירִים", "issue": "'Goat demons' — hairy ones. Israel sacrificing to actual spiritual entities in the wilderness.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "1enoch", "why": "Azazel in Lev 16 is the same being named in 1 Enoch 10:4-6 as the Watcher leader imprisoned in the wilderness"},
            {"target": "hebrews", "why": "The entire sacrificial system is 'a shadow of good things to come' (Heb 10:1); Day of Atonement fulfilled in Christ's once-for-all sacrifice"},
            {"target": "exodus", "why": "The tabernacle built in Exodus is the setting for every sacrifice prescribed in Leviticus"},
            {"target": "romans", "why": "kaphar (atonement/propitiation) connects to hilasterion in Rom 3:25 — the mercy seat"},
            {"target": "luke", "why": "Jesus' inaugural sermon (Luke 4:18-19) declares Jubilee (Lev 25) fulfilled"},
        ],
        "what_it_doesnt_say": [
            "No explanation of WHY blood atones — 'the life is in the blood' (17:11) but the mechanism is never explained",
            "Azazel is never identified — the text assumes the audience knows who/what Azazel is",
            "No rationale for the clean/unclean animal distinctions — the categories are given without explanation",
            "The Jubilee — no record that Israel ever actually observed it",
        ],
        "unusual_characters": [
            {"name": "Azazel", "ref": "16:8", "detail": "The scapegoat's destination — a being in the wilderness. 1 Enoch identifies him as the Watcher leader who taught humans warfare and cosmetics.", "connections": ["1enoch"]},
            {"name": "Nadab and Abihu", "ref": "10:1-2", "detail": "Aaron's sons who offer 'strange fire' and are consumed. God's holiness is lethal when boundaries are violated.", "connections": ["numbers", "2samuel"]},
        ],
        "patterns": [
            "Five offerings address five dimensions: burnt (dedication), grain (provision), peace (fellowship), sin (purification), guilt (restitution)",
            "Holiness gradient: camp → court → holy place → holy of holies mirrors the access structure of Eden",
            "Clean/unclean binary structures the entire book — everything is categorized, nothing is neutral",
            "Jubilee cycle (7x7+1 = 50 years) mirrors the creation week pattern at a macro scale",
        ],
        "mistranslations": [
            {"english": "scapegoat", "original": "azazel", "issue": "Turns a proper name (a specific Watcher) into a generic concept — hides the divine council backstory"},
            {"english": "atonement", "original": "kaphar", "issue": "English theological abstraction hides the concrete Hebrew: cover, smear, ransom"},
            {"english": "holy", "original": "qadosh", "issue": "English implies moral perfection; Hebrew means 'set apart, other' — ontological category, not ethical"},
        ],
    },
    {
        "id": 'numbers',
        "section": 'pentateuch',
        "title": 'Book 4: Numbers (Bamidbar)',
        "themes": 'REBEL SPIRIT DC HOLY PRIEST EXILE',
        "era_count": 6,
        "chapters": 36,
        "grade": 'A',
        "meta_text": '6 era files &middot; 36 chapters &middot; Grade: A',
        "body_html": '''<h4>Major Themes</h4>
  <div class="theme-grid">
    <span class="badge badge-theme">REBELLION</span><span class="badge badge-theme">WILDERNESS</span><span class="badge badge-theme">BALAAM</span><span class="badge badge-theme">PRIESTLY BLESSING</span><span class="badge badge-theme">NEPHILIM REMNANTS</span>
  </div>
  <p><strong>BALAAM</strong> <span class="badge badge-critical">CRITICAL</span> — Pagan diviner hired to curse Israel, compelled by YHWH to bless instead. "A star shall come out of Jacob" (24:17) — messianic oracle from a non-Israelite. His donkey sees the Angel of YHWH before he does. Later leads Israel into sexual sin (25:1-3, Rev 2:14).</p>
  <p><strong>PRIESTLY BLESSING</strong> (6:24-26) — "YHWH bless you and keep you; YHWH make his face shine on you." The oldest biblical text found in archaeology (Ketef Hinnom silver scrolls, ~600 BC). Fulfilled in Rev 22:4: "They will see his face."</p>
  <p><strong>NEPHILIM IN CANAAN</strong> (13:33) — The spies report Nephilim/Anakim in the land. The post-Flood giant clans are real. This is why conquest requires divine intervention.</p>
  <p><strong>BRONZE SERPENT</strong> (21:8-9) — "Moses made a bronze serpent (nachash nechoshet) and set it on a pole." Jesus interprets this: "As Moses lifted up the serpent in the wilderness, so must the Son of Man be lifted up" (John 3:14). The NACHASH becomes the symbol of salvation.</p>''',
        "key_claim": "Balaam — a pagan diviner — delivers the clearest messianic oracle in the Torah ('A star shall come out of Jacob,' 24:17), proving YHWH's sovereignty extends beyond Israel's borders and uses even hostile agents.",
        "contested_words": [
            {"word": "nephilim", "hebrew": "נְפִילִים", "issue": "The spies report Nephilim/Anakim in Canaan (13:33) — post-Flood giant clans are real, not exaggeration.", "severity": "CRITICAL"},
            {"word": "nachash nechoshet", "hebrew": "נְחַשׁ נְחֹשֶׁת", "issue": "Bronze serpent — wordplay on nachash (serpent/shining one) and nechoshet (bronze/copper). The shining nachash becomes salvation.", "severity": "CRITICAL"},
            {"word": "cherem", "hebrew": "חֵרֶם", "issue": "'Devoted to destruction' — consecrated to God, not ethnic cleansing. Religious category.", "severity": "MAJOR"},
            {"word": "qesem", "hebrew": "קֶסֶם", "issue": "Divination — Balaam practices qesem (22:7) yet YHWH speaks through him. Pagan methods overridden by divine sovereignty.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "john", "why": "Jesus directly interprets the bronze serpent: 'As Moses lifted up the serpent... so must the Son of Man be lifted up' (John 3:14)"},
            {"target": "revelation", "why": "Balaam reappears as archetype of false teaching (Rev 2:14) — the one who taught Balak to entice Israel"},
            {"target": "joshua", "why": "The Nephilim/Anakim reported by the spies are the targets of Joshua's conquest campaigns"},
            {"target": "deuteronomy", "why": "Moses' final speeches in Deuteronomy recapitulate and interpret the wilderness failures recorded in Numbers"},
            {"target": "2peter", "why": "Balaam becomes the paradigm of prophets-for-hire: 'the way of Balaam' (2 Pet 2:15)"},
        ],
        "what_it_doesnt_say": [
            "Why 38 years of wilderness wandering are almost entirely skipped — from ch. 19 to ch. 20, decades vanish",
            "How the Nephilim survived the Flood — the spies see them but no origin explanation is given",
            "What Balaam actually saw when the donkey stopped — his spiritual blindness vs. an animal's sight",
            "Why Moses striking the rock (20:11) instead of speaking to it warranted exclusion from the Promised Land",
        ],
        "unusual_characters": [
            {"name": "Balaam", "ref": "22:5", "detail": "Pagan diviner hired to curse Israel, compelled by YHWH to bless instead. Delivers messianic prophecy. Later leads Israel into sin.", "connections": ["revelation", "2peter", "jude"]},
            {"name": "Balaam's donkey", "ref": "22:28", "detail": "Sees the Angel of YHWH before the professional seer does. God opens its mouth to rebuke a prophet.", "connections": []},
            {"name": "Zelophehad's daughters", "ref": "27:1-7", "detail": "Five women challenge inheritance law and win — God changes the legal code in their favor.", "connections": []},
            {"name": "The bronze serpent", "ref": "21:9", "detail": "The nachash on a pole becomes the instrument of healing — the very image of the enemy becomes salvation.", "connections": ["john", "2kings"]},
        ],
        "patterns": [
            "Census-rebellion-judgment cycle: the book is structured around two censuses (chs. 1, 26) with rebellion filling the gap between them",
            "Escalating rebellion: complaining (11) → Miriam/Aaron challenge Moses (12) → spies refuse the land (13-14) → Korah challenges priesthood (16) → Moses fails (20)",
            "The nachash wordplay in 21:8-9: nachash (serpent) made of nechoshet (bronze) — the instrument of the curse becomes the instrument of healing",
            "Balaam's oracles follow a 4-oracle structure with escalating scope: Israel → Messiah → nations",
        ],
        "mistranslations": [
            {"english": "giants", "original": "nephilim/anakim", "issue": "Reduces the theological category of divine-human hybrid 'fallen ones' to a mere physical description"},
            {"english": "bronze serpent", "original": "nachash nechoshet", "issue": "Misses the deliberate wordplay connecting the serpent-being (nachash) to the bronze/shining material"},
        ],
    },
    {
        "id": 'deuteronomy',
        "section": 'pentateuch',
        "title": 'Book 5: Deuteronomy (Devarim)',
        "themes": 'COV DC REBEL EXILE KING RIV HOLY SEED NATIONS',
        "era_count": 6,
        "chapters": 34,
        "grade": 'A+',
        "meta_text": '6 era files &middot; 34 chapters &middot; Grade: A+',
        "body_html": '''<h4>Major Themes</h4>
  <div class="theme-grid">
    <span class="badge badge-theme">DEUT 32:8 ALLOTMENT</span><span class="badge badge-theme">SHEMA</span><span class="badge badge-theme">TREATY STRUCTURE</span><span class="badge badge-theme">BLESSINGS/CURSES</span><span class="badge badge-theme">PROPHET LIKE MOSES</span><span class="badge badge-theme">HEART CIRCUMCISION</span>
  </div>
  <p><strong>DEUT 32:8-9 — THE DIVINE COUNCIL ALLOTMENT</strong> <span class="badge badge-critical">CRITICAL</span> — The single most important text for the app's theological framework. After Babel, Elyon divided nations and assigned them to bene elohim (sons of God — DSS reading), keeping Israel as his own. The DSS (4QDeut<sup>j</sup>) and LXX independently confirm "sons of God" as original. MT's "sons of Israel" is a scribal alteration.</p>
  <p><strong>THE SHEMA</strong> (6:4) <span class="badge badge-critical">CRITICAL</span> — "Hear O Israel: YHWH our God, YHWH echad." echad = "one" or "alone"? In covenant context with other elohim, "YHWH alone" captures the loyalty oath. This is monolatry, not monotheism.</p>
  <p><strong>PROPHET LIKE MOSES</strong> (18:15-19) <span class="badge badge-major">MAJOR</span> — "A prophet like me from among your brothers — to him you shall listen." Fulfilled in Christ. At the Transfiguration (Matt 17:5) the voice echoes: "Listen to him."</p>
  <p><strong>HEART CIRCUMCISION</strong> (30:6) <span class="badge badge-major">MAJOR</span> — The new covenant in seed form. 10:16 commands Israel to circumcise their hearts. 29:4 admits they can't. 30:6: God will do it FOR them. &rarr; Jer 31:31-34, Ezek 36:26-27, Rom 2:28-29.</p>

  <h4>Key Contested Words</h4>
  <table class="ref-table">
    <tr><th>Hebrew</th><th>Issue</th><th>Severity</th></tr>
    <tr><td><strong>bene elohim</strong> (32:8)</td><td>MT: "sons of Israel" vs. DSS/LXX: "sons of God." Most consequential textual variant in the OT.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>echad</strong> (6:4)</td><td>"One" (ontological) vs. "alone" (covenantal). yachid (strict unity) was available but not used.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>Torah</strong></td><td>"Law" (wrong — Western juridical import) vs. "instruction/direction" from yarah (to direct).</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>cherem</strong> (7:2)</td><td>"Utterly destroy" — but means "consecrated to God." Religious category, not ethnic genocide.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>shedim</strong> (32:17)</td><td>"Demons" — only here and Ps 106:37. Distinct from allotted elohim. Disembodied Nephilim (1 En 15:8-10).</td><td><span class="badge badge-major">MAJOR</span></td></tr>
  </table>

  <h4>Outlier Flags</h4>
  <p><span class="badge badge-outlier">O-COUNCIL</span> <span class="badge badge-outlier">O-TREATY</span> <span class="badge badge-outlier">O-QUOTATION</span> <span class="badge badge-outlier">O-TEXTUAL</span></p>
  <p>Most quoted OT book in the NT (~200 times). Jesus uses it to defeat Satan (all three temptation responses from Deut 6-8). Contains the most critical textual variant in the OT (32:8).</p>
</div>
</div>

<!-- This is Part 1 — Pentateuch complete. More books follow. -->
<!-- Remaining books are loaded below -->''',
        "key_claim": "Deuteronomy 32:8-9 is the single most important verse for understanding the spiritual architecture of the nations — after Babel, Elyon divided humanity among bene elohim (sons of God), keeping only Israel as YHWH's own portion.",
        "contested_words": [
            {"word": "bene elohim", "hebrew": "בְּנֵי אֱלֹהִים", "issue": "MT: 'sons of Israel' vs. DSS/LXX: 'sons of God.' Most consequential textual variant in the OT.", "severity": "CRITICAL"},
            {"word": "echad", "hebrew": "אֶחָד", "issue": "'One' (ontological) vs. 'alone' (covenantal). yachid (strict unity) was available but not used.", "severity": "CRITICAL"},
            {"word": "cherem", "hebrew": "חֵרֶם", "issue": "'Utterly destroy' — but means 'consecrated to God.' Religious category, not ethnic genocide.", "severity": "MAJOR"},
            {"word": "Torah", "hebrew": "תּוֹרָה", "issue": "'Law' (wrong — Western juridical import) vs. 'instruction/direction' from yarah (to direct).", "severity": "MAJOR"},
            {"word": "shedim", "hebrew": "שֵׁדִים", "issue": "'Demons' — only here and Ps 106:37. Distinct from allotted elohim. Disembodied Nephilim (1 En 15:8-10).", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "genesis", "why": "Babel scattering (Gen 11) is the event Deut 32:8 interprets — the nations were allotted to bene elohim as consequence"},
            {"target": "psalms", "why": "Psalm 82 depicts YHWH judging the corrupt elohim given nations in Deut 32:8 — 'you shall die like men'"},
            {"target": "daniel", "why": "Daniel 10 reveals the territorial princes (Prince of Persia, Prince of Greece) assigned at the Deut 32:8 allotment"},
            {"target": "matthew", "why": "Jesus quotes Deuteronomy three times to defeat Satan (Matt 4:4, 7, 10 — all from Deut 6-8)"},
            {"target": "acts", "why": "Pentecost (Acts 2) reverses Babel/Deut 32:8 — tongues unite what was divided, nations reclaimed for YHWH"},
            {"target": "romans", "why": "Heart circumcision (Deut 30:6) becomes Paul's argument in Rom 2:28-29; new covenant in seed form"},
        ],
        "what_it_doesnt_say": [
            "Who altered 'sons of God' to 'sons of Israel' in the MT — the most consequential scribal change in the OT has no explanation",
            "How the allotted elohim became corrupt — Deut 32:8 assigns them but Ps 82 condemns them, with no narrative bridge",
            "Moses' burial location — God buries him personally and 'no one knows his burial place to this day' (34:6)",
            "Why God chose Israel specifically — Deut 7:7 says 'not because you were more numerous' but never gives the positive reason",
        ],
        "unusual_characters": [
            {"name": "The Prophet Like Moses", "ref": "18:15", "detail": "A future prophet from among the brothers — fulfilled in Christ. Transfiguration echoes: 'Listen to him' (Matt 17:5).", "connections": ["matthew", "john", "acts"]},
            {"name": "The shedim", "ref": "32:17", "detail": "Demons Israel sacrificed to — distinct from the allotted elohim. Disembodied Nephilim spirits (1 En 15:8-10).", "connections": ["psalms", "1enoch"]},
        ],
        "patterns": [
            "Suzerainty treaty structure: preamble (1:1-5), historical prologue (1:6-4:43), stipulations (4:44-26:19), blessings/curses (27-28), witnesses (30:19, 31:28)",
            "Deut 32 (Song of Moses) is a self-contained prophetic history: creation → election → rebellion → exile → restoration",
            "Most quoted OT book in the NT (~200 times) — Jesus uses it to defeat Satan with all three temptation responses from Deut 6-8",
            "Heart circumcision progression: 10:16 commands it, 29:4 admits Israel can't do it, 30:6 promises God will do it FOR them — new covenant in embryo",
        ],
        "mistranslations": [
            {"english": "sons of Israel", "original": "bene elohim", "issue": "MT scribal alteration hides the divine council allotment — DSS and LXX independently preserve 'sons of God'"},
            {"english": "the LORD is one", "original": "YHWH echad", "issue": "Implies ontological monotheism when the Hebrew context (among other elohim) means 'YHWH alone' — covenantal loyalty oath"},
            {"english": "Law", "original": "Torah", "issue": "Western juridical import obscures 'instruction/direction' from yarah — makes Torah sound punitive rather than formative"},
            {"english": "demons", "original": "shedim", "issue": "Generic English term hides the specific category — disembodied Nephilim spirits, distinct from the territorial elohim"},
        ],
    },
    {
        "id": 'joshua',
        "section": 'historical-books',
        "title": 'Book 6: Joshua (Yehoshua)',
        "themes": 'LAND COV HOLY KING SPIRIT',
        "era_count": 4,
        "chapters": 24,
        "grade": 'A',
        "meta_text": '4 era files &middot; 24 chapters &middot; Grade: A',
        "body_html": '''<p><strong>CONQUEST AS COSMIC RECLAMATION</strong> — Joshua (= Yeshua = Jesus) leads Israel into the land. The conquest targets Nephilim-remnant populations (Anakim in Hebron). Jericho falls by divine intervention, not military strategy. Rahab (Canaanite prostitute) is saved — in Jesus' genealogy (Matt 1:5). The Commander of YHWH's army (5:13-15) = Angel of YHWH / preincarnate Christ.</p><p><strong>Key terms</strong>: cherem (devoted to destruction), nachalah (inheritance), Yehoshua (YHWH saves — same name as Jesus)</p>''',
        "key_claim": "The conquest of Canaan is not ethnic warfare but cosmic reclamation — Joshua targets Nephilim-remnant populations (Anakim) occupying the land YHWH allotted to Israel, and the Commander of YHWH's army (5:13-15) reveals this is a divine council military operation.",
        "contested_words": [
            {"word": "cherem", "hebrew": "חֵרֶם", "issue": "'Devoted to destruction' — consecrated to God, not genocide. A religious category removing Nephilim-contaminated populations from the land.", "severity": "CRITICAL"},
            {"word": "Yehoshua", "hebrew": "יְהוֹשֻׁעַ", "issue": "'YHWH saves' — identical name to Jesus (Yeshua). The conquest leader prefigures the ultimate deliverer.", "severity": "CRITICAL"},
            {"word": "nachalah", "hebrew": "נַחֲלָה", "issue": "'Inheritance' — the land is YHWH's nachalah allotted to Israel, not mere real estate. Theological territory.", "severity": "MAJOR"},
            {"word": "sar tseva YHWH", "hebrew": "שַׂר צְבָא יהוה", "issue": "'Commander of YHWH's army' (5:14) — a divine being Joshua worships. Angel of YHWH / preincarnate Christ.", "severity": "CRITICAL"},
        ],
        "hidden_connections": [
            {"target": "numbers", "why": "The Nephilim/Anakim the spies feared (Num 13:33) are the specific targets of Joshua's conquest campaigns"},
            {"target": "deuteronomy", "why": "The cherem warfare commanded in Deut 7:2 and 20:16-17 is executed in Joshua — destroying Nephilim-contaminated populations"},
            {"target": "matthew", "why": "Rahab the Canaanite prostitute enters Jesus' genealogy (Matt 1:5) — a pagan woman saved by faith in YHWH"},
            {"target": "hebrews", "why": "Rahab commended for faith (Heb 11:31); Joshua's rest as type of the greater rest (Heb 4:8-9)"},
            {"target": "ephesians", "why": "The territorial spiritual warfare in Joshua prefigures Eph 6:12 — struggle against cosmic powers over territory"},
            {"target": "revelation", "why": "Jericho's walls fall by divine intervention, not military strategy — the pattern of supernatural conquest repeated in Revelation's final battles"},
        ],
        "what_it_doesnt_say": [
            "The Commander of YHWH's army (5:13-15) never identifies himself — Joshua worships him but the text leaves his identity unstated",
            "How Rahab heard about YHWH — she knows about the Red Sea crossing (2:10) but the information channel is never explained",
            "Why Ai's initial defeat was permitted — Achan's sin is revealed after, but God didn't warn Joshua beforehand",
            "What happened to the Nephilim/Anakim who were NOT in the targeted cities — the text says they remained in Gaza, Gath, Ashdod (11:22)",
        ],
        "unusual_characters": [
            {"name": "Commander of YHWH's army", "ref": "5:13-15", "detail": "A divine being with drawn sword who accepts Joshua's worship — holy ground, like the burning bush. Angel of YHWH / preincarnate Christ.", "connections": ["exodus", "revelation"]},
            {"name": "Rahab", "ref": "2:1", "detail": "Canaanite prostitute who hides the spies. Saved by faith. Enters the seed line — great-great-grandmother of David, in Jesus' genealogy.", "connections": ["matthew", "hebrews", "james"]},
            {"name": "Achan", "ref": "7:1", "detail": "Takes cherem-devoted items from Jericho. His sin causes Israel's defeat at Ai. The entire household is destroyed — corporate solidarity.", "connections": []},
            {"name": "Caleb", "ref": "14:6-15", "detail": "At 85 years old, demands the hardest territory — Hebron, where the Anakim giants live. 'Give me this hill country.'", "connections": ["numbers"]},
        ],
        "patterns": [
            "The conquest follows a three-campaign structure: central (Jericho-Ai), southern coalition, northern coalition — divide and conquer",
            "Yehoshua/Yeshua typology: Joshua leads Israel through the Jordan into the Promised Land as Jesus leads believers through death into resurrection life",
            "The spies-and-Rahab narrative in ch. 2 mirrors and reverses the failed spy mission of Numbers 13 — this time faith prevails",
            "Holy ground appears twice in the Torah-era narrative: burning bush (Ex 3:5) and Commander of YHWH's army (Josh 5:15) — bookends for the wilderness period",
        ],
        "mistranslations": [
            {"english": "utterly destroyed", "original": "cherem", "issue": "Hides the religious-consecration meaning — makes it sound like ethnic cleansing rather than removal of Nephilim-contaminated populations"},
            {"english": "captain of the host", "original": "sar tseva YHWH", "issue": "Diminishes a divine being to a military rank — this is a theophany Joshua worships on holy ground"},
            {"english": "inheritance", "original": "nachalah", "issue": "Sounds like mere property transfer — misses the theological weight of YHWH's allotted territory for his people"},
        ],
    },
    {
        "id": 'judges',
        "section": 'historical-books',
        "title": 'Book 7: Judges (Shofetim)',
        "themes": 'REBEL KING SPIRIT WOMEN REVERSAL',
        "era_count": 3,
        "chapters": 21,
        "grade": 'A-',
        "meta_text": '3 era files &middot; 21 chapters &middot; Grade: A-',
        "body_html": '''<p><strong>THE DOWNWARD SPIRAL</strong> — Apostasy &rarr; oppression &rarr; cry &rarr; deliverance &rarr; apostasy. Each cycle worse. Refrain: "In those days there was no king in Israel. Everyone did what was right in his own eyes." Deborah (female judge), Gideon (300 vs. 135,000), Samson (Nazirite who breaks every vow). Ends in civil war and near-extinction of Benjamin.</p><p><strong>Divine council</strong>: Judges 5:19-20 — "From heaven the STARS fought" against Sisera. Host of heaven as divine warriors.</p>''',
        "key_claim": "Judges is a controlled demolition of human self-rule — each cycle of apostasy spirals deeper, proving that without YHWH's direct kingship, Israel degrades from compromise to civil war to near-tribal extinction.",
        "contested_words": [
            {"word": "shofet", "hebrew": "שׁוֹפֵט", "issue": "'Judge' is misleading — these are military deliverers and charismatic leaders, not courtroom officials.", "severity": "MAJOR"},
            {"word": "kokhavim", "hebrew": "כּוֹכָבִים", "issue": "'Stars' in Judges 5:20 — 'from heaven the stars fought against Sisera.' Stars = divine council members acting as cosmic warriors.", "severity": "CRITICAL"},
            {"word": "ruach YHWH", "hebrew": "רוּחַ יהוה", "issue": "'Spirit of YHWH' rushes upon judges (Othniel, Gideon, Jephthah, Samson) — empowerment is temporary and external, not indwelling.", "severity": "MAJOR"},
            {"word": "nazirite", "hebrew": "נָזִיר", "issue": "'Separated one' — Samson's nazirite vow (no wine, no razor, no corpses) and his systematic violation of every condition.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "deuteronomy", "why": "The cycle of apostasy fulfills Moses' warnings in Deut 28-32 — the blessings/curses covenant playing out in real time"},
            {"target": "1samuel", "why": "The refrain 'no king in Israel' sets up the kingship demand in 1 Sam 8 — Judges creates the crisis Samuel must resolve"},
            {"target": "ruth", "why": "Ruth is set 'in the days when the judges ruled' (Ruth 1:1) — a seed-line story hidden inside the darkest period"},
            {"target": "hebrews", "why": "Gideon, Barak, Samson, Jephthah listed in the hall of faith (Heb 11:32) — flawed deliverers still counted as faithful"},
            {"target": "revelation", "why": "Stars as divine warriors (Judg 5:20) reappears in Revelation's cosmic warfare imagery"},
        ],
        "what_it_doesnt_say": [
            "Why God keeps raising deliverers for a people who keep betraying him — the mercy is never explained, only demonstrated",
            "What happened to the Levitical priesthood during this period — the priests are almost entirely absent from the narrative",
            "How Jephthah's vow actually played out — did he sacrifice his daughter or dedicate her to perpetual virginity? The text is deliberately ambiguous",
            "Why the tribe of Dan migrates north and adopts idolatry — Dan disappears from Revelation's tribal list (Rev 7:5-8)",
        ],
        "unusual_characters": [
            {"name": "Deborah", "ref": "4:4", "detail": "Female judge, prophet, and military strategist. Commands Barak to battle. The Song of Deborah (ch. 5) is among the oldest Hebrew poetry.", "connections": []},
            {"name": "Gideon", "ref": "6:11", "detail": "Defeats 135,000 Midianites with 300 men — God strips the army to prove the victory is divine, not human.", "connections": ["hebrews"]},
            {"name": "Samson", "ref": "13:24", "detail": "Nazirite who breaks every vow. Superhuman strength from the Spirit, but no moral compass. A cautionary anti-hero.", "connections": ["hebrews"]},
            {"name": "Jael", "ref": "4:17", "detail": "Kills Sisera with a tent peg through his temple. A non-Israelite woman delivers the decisive blow in Israel's war.", "connections": []},
        ],
        "patterns": [
            "Six-cycle downward spiral: each judge-cycle is worse than the last — from Othniel (ideal) to Samson (anti-hero) to civil war (no judge at all)",
            "The refrain 'no king in Israel, everyone did what was right in his own eyes' appears 4 times (17:6, 18:1, 19:1, 21:25) — framing the final collapse",
            "Spirit empowerment follows a degradation pattern: Othniel (clean victory) → Gideon (needs signs) → Jephthah (rash vow) → Samson (personal vendettas)",
            "Stars fighting from heaven (5:20) uses cosmic warfare language — the divine council participates in Israel's battles",
        ],
        "mistranslations": [
            {"english": "judges", "original": "shofetim", "issue": "Implies legal officials — these are charismatic military deliverers raised up by YHWH's Spirit"},
            {"english": "the stars fought", "original": "kokhavim nilchamu", "issue": "Sounds like poetic metaphor — the Hebrew identifies cosmic beings (divine council members) fighting from heaven"},
            {"english": "Spirit of the LORD came upon", "original": "ruach YHWH tsalachah", "issue": "Various English renderings obscure the specific Hebrew verb tsalachah (rushed upon) — violent, sudden empowerment"},
        ],
    },
    {
        "id": 'ruth',
        "section": 'historical-books',
        "title": 'Book 8: Ruth',
        "themes": 'SEED COV WOMEN REVERSAL NATIONS',
        "era_count": 1,
        "chapters": 4,
        "grade": 'A',
        "meta_text": '1 era file &middot; 4 chapters &middot; Grade: A',
        "body_html": '''<p><strong>MOABITESS IN THE SEED LINE</strong> — Deut 23:3 excludes Moabites from the assembly. Yet Ruth the Moabitess becomes David's great-grandmother and appears in Jesus' genealogy (Matt 1:5). The go'el (kinsman-redeemer) theology: Boaz redeems Ruth's inheritance &rarr; Christ redeems humanity's inheritance. "Your people shall be my people, and your God my God" (1:16) — the most profound conversion statement in the OT.</p><p><strong>Key term</strong>: go'el (kinsman-redeemer) — same title applied to YHWH (Isa 41:14) and to Christ.</p>''',
        "key_claim": "Ruth shatters the ethnic boundary of the seed line — a Moabitess excluded by Deuteronomy 23:3 becomes David's great-grandmother and enters the genealogy of Christ, proving the seed promise was always intended to draw in the nations.",
        "contested_words": [
            {"word": "go'el", "hebrew": "גֹּאֵל", "issue": "'Kinsman-redeemer' — the one with legal right and duty to buy back family land and marry the widow. Same title applied to YHWH (Isa 41:14) and to Christ.", "severity": "CRITICAL"},
            {"word": "hesed", "hebrew": "חֶסֶד", "issue": "'Kindness/loyalty' — Ruth's hesed to Naomi (1:8, 3:10) mirrors YHWH's covenant faithfulness. No single English word captures it.", "severity": "MAJOR"},
            {"word": "kanap", "hebrew": "כָּנָף", "issue": "'Wing/corner of garment' — Ruth asks Boaz to spread his kanap over her (3:9). Same word used for YHWH's protective wings (Ps 91:4). Marital and divine imagery merged.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "deuteronomy", "why": "Deut 23:3 excludes Moabites from the assembly — Ruth's inclusion directly challenges this prohibition through hesed and faith"},
            {"target": "matthew", "why": "Ruth appears in Jesus' genealogy (Matt 1:5) alongside Tamar, Rahab, and Bathsheba — four outsider women in the seed line"},
            {"target": "genesis", "why": "The seed line (Gen 3:15) runs through Ruth: Perez → Boaz → Obed → Jesse → David → Christ"},
            {"target": "1samuel", "why": "Ruth 4:22 ends with David — the entire book exists to explain how a Moabitess entered the royal seed line"},
            {"target": "isaiah", "why": "YHWH as go'el (Isa 41:14, 43:14) uses the same kinsman-redeemer concept embodied by Boaz"},
            {"target": "judges", "why": "Set 'in the days when the judges ruled' (1:1) — a story of hesed hidden inside Israel's darkest period"},
        ],
        "what_it_doesnt_say": [
            "How Ruth's Moabite identity was accepted in Bethlehem — the Deut 23:3 exclusion is never addressed in the narrative",
            "Why the unnamed closer kinsman refused to redeem — he says it would 'impair my own inheritance' (4:6) but never explains how",
            "Whether Naomi's bitterness toward God (1:20-21) was ever resolved — she renames herself Mara ('bitter') and the text never revisits it",
            "The political implications of David's Moabite ancestry — his enemies could have used this against his legitimacy",
        ],
        "unusual_characters": [
            {"name": "Ruth", "ref": "1:16", "detail": "Moabitess who makes the most profound conversion statement in the OT: 'Your people shall be my people, and your God my God.' Enters the seed line.", "connections": ["matthew", "1samuel"]},
            {"name": "Boaz", "ref": "2:1", "detail": "The go'el (kinsman-redeemer) who buys back Naomi's land and marries Ruth. A type of Christ redeeming his bride.", "connections": ["isaiah", "revelation"]},
            {"name": "Naomi", "ref": "1:2", "detail": "Renames herself Mara ('bitter'). Orchestrates the threshing floor encounter. Her emptiness becomes fullness through the seed line.", "connections": []},
            {"name": "The unnamed kinsman", "ref": "4:1", "detail": "The closer redeemer who refuses to act. Called peloni almoni ('so-and-so') — deliberately unnamed, erased from memory for refusing his duty.", "connections": []},
        ],
        "patterns": [
            "Emptiness-to-fullness arc: Naomi loses husband and sons (ch. 1), gains a grandson in the seed line (ch. 4) — famine to harvest, death to life",
            "Four outsider women in Matthew's genealogy: Tamar (Canaanite), Rahab (Canaanite), Ruth (Moabite), Bathsheba (Hittite connection) — the seed line deliberately includes the nations",
            "The threshing floor scene (ch. 3) echoes and reverses the sexual exploitation patterns of Judges — here, vulnerability is met with honor",
            "Go'el theology structures the entire book: the right of redemption, the willing redeemer, the legal transaction at the gate — all fulfilled in Christ",
        ],
        "mistranslations": [
            {"english": "kinsman-redeemer", "original": "go'el", "issue": "English compound obscures the concrete Hebrew: the one who buys back, avenges blood, restores what was lost — applied to YHWH himself"},
            {"english": "kindness", "original": "hesed", "issue": "Reduces covenantal faithfulness to mere niceness — hesed is loyalty that persists when every reason to quit exists"},
            {"english": "wings/skirt", "original": "kanap", "issue": "Different translations choose different meanings — but the deliberate double entendre (divine protection + marital covering) is the point"},
        ],
    },
    {
        "id": '1samuel',
        "section": 'historical-books',
        "title": 'Books 9-10: 1-2 Samuel',
        "themes": 'KING DC SPIRIT SEED REBEL',
        "era_count": 5,
        "chapters": 55,
        "grade": 'A',
        "meta_text": '5 era files &middot; 55 chapters &middot; Grade: A',
        "body_html": '''<p><strong>THE KINGSHIP CRISIS</strong> — Israel demands a king "like the nations" (8:5) — rejecting YHWH's direct rule. Saul chosen by height, fails by disobedience. David chosen by heart, anointed by Samuel. The Davidic covenant (2 Sam 7) = eternal throne &rarr; Christ. David vs. Goliath: the last named Nephilim-descendant warrior (1 Sam 17:4; 2 Sam 21:15-22 lists four more).</p><p><strong>Divine council</strong>: 1 Sam 28:13 — the medium at Endor sees Samuel rising, calls him "elohim" — the word for divine beings.</p><p><strong>Key term</strong>: mashiach (anointed one) — from which "Messiah" derives. Both Saul and David are "YHWH's anointed."</p>''',
        "key_claim": "Israel's demand for a king 'like the nations' (1 Sam 8:5) is the third rebellion pattern — rejecting YHWH's direct rule in favor of human authority — and the Davidic covenant (2 Sam 7) is God's answer: an eternal throne that only Christ can occupy.",
        "contested_words": [
            {"word": "mashiach", "hebrew": "מָשִׁיחַ", "issue": "'Anointed one' — from which 'Messiah' derives. Applied to Saul and David equally. The concept of divine anointing predates the eschatological Messiah.", "severity": "CRITICAL"},
            {"word": "elohim", "hebrew": "אֱלֹהִים", "issue": "The medium at Endor sees Samuel rising and calls him 'elohim' (28:13) — the same word for God, gods, and divine beings.", "severity": "CRITICAL"},
            {"word": "ruach ra'ah", "hebrew": "רוּחַ רָעָה", "issue": "'Evil spirit from YHWH' tormenting Saul (16:14) — a divine council agent dispatched by God, not a random demon.", "severity": "CRITICAL"},
            {"word": "Rephaim", "hebrew": "רְפָאִים", "issue": "Goliath and his brothers are Rephaim — Nephilim-descendant giant clans. The seed war's physical front.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "judges", "why": "'No king in Israel' (Judg 21:25) creates the crisis that drives the kingship demand in 1 Sam 8"},
            {"target": "ruth", "why": "Ruth's genealogy (Ruth 4:22) ends with David — Samuel-Kings shows what that seed line was building toward"},
            {"target": "psalms", "why": "David's psalms are the internal soundtrack to the external narrative — many psalm superscriptions reference specific Samuel events"},
            {"target": "matthew", "why": "The Davidic covenant (2 Sam 7:12-16) is THE foundation of NT messianic expectation — 'Son of David' is Jesus' most common title"},
            {"target": "acts", "why": "Peter cites the Davidic covenant at Pentecost (Acts 2:30-31) — David's throne fulfilled in Christ's resurrection"},
            {"target": "1kings", "why": "Solomon inherits David's throne and the covenant promise — but immediately begins the trajectory toward division"},
        ],
        "what_it_doesnt_say": [
            "How the 'evil spirit from YHWH' (16:14) relates to God's goodness — a divine council agent tormenting the king is stated without theological explanation",
            "Whether Samuel actually appeared at Endor or whether it was a demonic deception — the text presents it as genuinely Samuel (28:15-19)",
            "Why David was spared for his sins when Saul was rejected for lesser offenses — the 'man after God's own heart' distinction is never fully explained",
            "The identity of Goliath's four Rephaim brothers (2 Sam 21:15-22) — they are listed but their origin is unexplained",
        ],
        "unusual_characters": [
            {"name": "Samuel's ghost", "ref": "28:13-19", "detail": "The medium calls the risen Samuel 'elohim' — a divine being. He delivers accurate prophecy from beyond death.", "connections": ["deuteronomy"]},
            {"name": "Goliath", "ref": "17:4", "detail": "Champion of Gath, over 9 feet tall. A Rephaim — Nephilim-descendant giant. David defeats him with a sling and the name of YHWH.", "connections": ["numbers", "joshua"]},
            {"name": "David", "ref": "16:12", "detail": "Chosen by heart, not height. Shepherd, warrior, poet, king. The covenant recipient whose throne is eternal.", "connections": ["psalms", "matthew", "acts"]},
            {"name": "The evil spirit from YHWH", "ref": "16:14", "detail": "A divine council agent sent to torment Saul after the Spirit of YHWH departs — spiritual authority transferred from Saul to David.", "connections": ["1kings", "job"]},
        ],
        "patterns": [
            "Two-king contrast structure: Saul (chosen by height, fails by disobedience) vs. David (chosen by heart, succeeds through faith) — external vs. internal qualification",
            "The ruach YHWH transfers: departs from Saul (16:14) and comes upon David (16:13) — anointing and Spirit are portable, not permanent under the old covenant",
            "David vs. Goliath is a seed-war microcosm: the seed of the woman (shepherd boy) vs. the seed of the Nephilim (Rephaim giant)",
            "Samuel bridges two eras: last judge, first prophet of the monarchy, and kingmaker — the hinge figure between theocracy and monarchy",
        ],
        "mistranslations": [
            {"english": "evil spirit from the LORD", "original": "ruach ra'ah me'et YHWH", "issue": "Makes God sound malevolent — this is a divine council agent dispatched with a specific mission, like the lying spirit in 1 Kings 22"},
            {"english": "a god coming up", "original": "elohim olim", "issue": "The medium sees Samuel and calls him 'elohim' — most translations avoid the divine-being implication"},
            {"english": "giant", "original": "Rephaim", "issue": "Reduces a specific Nephilim-descendant clan category to a mere physical description"},
        ],
    },
    {
        "id": '2samuel',
        "section": 'historical-books',
        "title": 'Book 10: 2 Samuel',
        "themes": 'KING COV SEED DC WOMEN REBEL',
        "era_count": 3,
        "chapters": 24,
        "grade": 'A',
        "meta_text": '3 era files &middot; 24 chapters &middot; Grade: A',
        "body_html": '''<h4>Major Themes</h4>
  <div class="theme-grid">
    <span class="badge badge-theme">DAVIDIC COVENANT</span><span class="badge badge-theme">KINGSHIP &amp; FAILURE</span><span class="badge badge-theme">DIVINE COUNCIL</span><span class="badge badge-theme">SEED LINE</span><span class="badge badge-theme">CONSEQUENCES</span><span class="badge badge-theme">WOMEN</span>
  </div>
  <p><strong>DAVIDIC COVENANT (2 Sam 7)</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; The theological heart of the entire book: YHWH promises David an eternal throne, an eternal house, and an eternal kingdom. "I will be to him a father, and he shall be to me a son" (7:14). This is THE covenant that generates all messianic expectation &mdash; "Son of David" as Christ's title flows from here.</p>
  <p><strong>KINGSHIP &amp; FAILURE</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; David&rsquo;s adultery with Bathsheba and murder of Uriah (chs. 11-12) triggers a cascade: the child dies, Amnon rapes Tamar, Absalom murders Amnon, Absalom rebels. The sword "never departs" (12:10). The "man after God's heart" proves the point &mdash; no human king can sit the eternal throne.</p>
  <p><strong>DIVINE COUNCIL</strong> <span class="badge badge-major">MAJOR</span> &mdash; The destroying angel (mal&rsquo;ak) stands over Jerusalem with drawn sword (24:16). David SEES the angel. YHWH "relents" (nacham) from the destruction. The threshing floor of Araunah becomes the Temple site &mdash; divine council judgment determines sacred geography.</p>

  <h4>Contested Words</h4>
  <table class="ref-table">
    <tr><th>Hebrew</th><th>Issue</th><th>Severity</th></tr>
    <tr><td><strong>bayit</strong> (7:11)</td><td>"House" &mdash; triple meaning in the Davidic covenant: dynasty, temple, family. YHWH will build David a house (dynasty), not the other way around.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>hesed</strong> (7:15)</td><td>"Steadfast love" &mdash; YHWH&rsquo;s hesed will NOT be removed from David's line, even when the son sins. Unconditional covenantal commitment.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>mal'ak YHWH</strong> (24:16)</td><td>"Angel of YHWH" with drawn sword over Jerusalem &mdash; a divine council agent executing judgment. David sees him at Araunah's threshing floor.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>nacham</strong> (24:16)</td><td>"Relented" &mdash; YHWH relents from destroying Jerusalem. Same word as Ex 32:14. Does God change his mind, or is this anthropomorphic language for responsive sovereignty?</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>Rephaim</strong> (21:16-22)</td><td>Four Rephaim warriors killed by David's men &mdash; Nephilim-descendant giant clans still active in the seed war.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
  </table>

  <h4>Unusual Characters</h4>
  <ul>
    <li><strong>Bathsheba</strong> (11:3) &mdash; Victim of royal power, yet becomes mother of Solomon and appears in Jesus' genealogy (Matt 1:6). The seed line runs through scandal.</li>
    <li><strong>Nathan the prophet</strong> (12:1-14) &mdash; Covenant prosecutor who brings YHWH's riv against David with the parable of the ewe lamb. "You are the man."</li>
    <li><strong>Absalom</strong> (chs. 13-18) &mdash; David's son who rebels, takes the throne, and is killed. His rebellion is the direct consequence of David's sin &mdash; the sword that never departs.</li>
    <li><strong>The destroying angel</strong> (24:16) &mdash; Divine council agent with drawn sword over Jerusalem. The threshing floor where he stands becomes the Temple site.</li>
  </ul>

  <h4>Conspicuous Silences</h4>
  <ul>
    <li>David's internal response to Absalom's death beyond "O my son" (18:33) &mdash; the deepest grief in the OT given minimal narration</li>
    <li>Bathsheba's perspective on the affair is never given &mdash; she speaks only when spoken to until 1 Kings 1</li>
    <li>How David's "man after God's heart" status survives adultery and murder &mdash; the theology is assumed, never explained</li>
    <li>Why the census (ch. 24) provoked divine wrath &mdash; the sin of numbering the people is stated but never clarified</li>
  </ul>

  <h4>Cross-References</h4>
  <p class="xref">2 Samuel <span class="arrow">&rarr;</span> <span class="badge badge-ot">1 Samuel</span> <span class="badge badge-ot">1 Chronicles</span> <span class="badge badge-ot">Psalms</span> <span class="badge badge-nt">Matthew</span> <span class="badge badge-nt">Acts</span> <span class="badge badge-nt">Romans</span> <span class="badge badge-nt">Hebrews</span> <span class="badge badge-nt">Luke</span></p>''',
        "key_claim": "The Davidic covenant (2 Sam 7) is the theological engine of messianic expectation — YHWH promises an eternal throne, house, and kingdom, and David's catastrophic failure with Bathsheba proves no human king can occupy it, pointing forward to Christ as the only one who can.",
        "contested_words": [
            {"word": "bayit", "hebrew": "בַּיִת", "issue": "'House' — triple meaning in the Davidic covenant: dynasty, temple, family. YHWH will build David a house (dynasty), not the other way around.", "severity": "CRITICAL"},
            {"word": "hesed", "hebrew": "חֶסֶד", "issue": "YHWH's 'steadfast love' will NOT be removed from David's line, even when the son sins. Unconditional covenantal commitment.", "severity": "CRITICAL"},
            {"word": "mal'ak YHWH", "hebrew": "מַלְאַךְ יהוה", "issue": "'Angel of YHWH' with drawn sword over Jerusalem (24:16) — a divine council agent executing judgment. David sees him at Araunah's threshing floor.", "severity": "CRITICAL"},
            {"word": "nacham", "hebrew": "נָחַם", "issue": "'Relented' (24:16) — YHWH relents from destroying Jerusalem. Does God change his mind, or is this anthropomorphic language for responsive sovereignty?", "severity": "MAJOR"},
            {"word": "Rephaim", "hebrew": "רְפָאִים", "issue": "Four Rephaim warriors killed by David's men (21:16-22) — Nephilim-descendant giant clans still active in the seed war.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "1samuel", "why": "David's anointing (1 Sam 16) reaches its throne in 2 Sam 2-5 — the covenant promise (2 Sam 7) answers the kingship crisis of 1 Sam 8"},
            {"target": "1chronicles", "why": "Chronicles retells the same events but OMITS Bathsheba and Absalom — the priestly lens sanitizes what Samuel records raw"},
            {"target": "psalms", "why": "Many psalm superscriptions reference 2 Samuel events: Ps 51 (Bathsheba), Ps 3 (Absalom's rebellion), Ps 18 (deliverance) — the internal soundtrack"},
            {"target": "matthew", "why": "'Son of David' as Jesus' title (Matt 1:1) flows directly from the Davidic covenant (2 Sam 7:12-16)"},
            {"target": "acts", "why": "Peter at Pentecost (Acts 2:30-31) cites the Davidic covenant — David knew God swore to seat one of his descendants on his throne"},
            {"target": "romans", "why": "Paul opens Romans declaring Jesus 'descended from David according to the flesh' (Rom 1:3) — the seed line runs through 2 Samuel"},
            {"target": "hebrews", "why": "'I will be to him a father, and he shall be to me a son' (7:14) — adopted by Hebrews 1:5 for the Son's divine sonship"},
            {"target": "luke", "why": "Gabriel announces to Mary: 'The Lord God will give him the throne of his father David' (Luke 1:32) — the Davidic covenant fulfilled"},
        ],
        "what_it_doesnt_say": [
            "David's internal response to Absalom's death beyond 'O my son' (18:33) — the deepest grief in the OT given minimal narration",
            "Bathsheba's perspective on the affair is never given — she speaks only when spoken to until 1 Kings 1",
            "How David's 'man after God's own heart' status survives adultery and murder — the theology is assumed, never explained",
            "Why the census (ch. 24) provoked divine wrath — the sin of numbering the people is stated but never clarified",
        ],
        "unusual_characters": [
            {"name": "Bathsheba", "ref": "11:3", "detail": "Victim of royal power, yet becomes mother of Solomon and appears in Jesus' genealogy (Matt 1:6). The seed line runs through scandal.", "connections": ["matthew", "1kings"]},
            {"name": "Nathan the prophet", "ref": "12:1", "detail": "Covenant prosecutor who brings YHWH's riv against David with the parable of the ewe lamb. 'You are the man.'", "connections": ["1kings"]},
            {"name": "Absalom", "ref": "13:1", "detail": "David's son who rebels, takes the throne, and is killed. His rebellion is the direct consequence of David's sin — the sword that never departs.", "connections": []},
            {"name": "The destroying angel", "ref": "24:16", "detail": "Divine council agent with drawn sword over Jerusalem. The threshing floor where he stands becomes the Temple site.", "connections": ["1chronicles", "exodus", "revelation"]},
        ],
        "patterns": [
            "Sin-consequence cascade: adultery (ch. 11) triggers child's death (ch. 12), Amnon's rape of Tamar (ch. 13), Absalom's murder and rebellion (chs. 13-18), Sheba's revolt (ch. 20) — 'the sword shall never depart' (12:10)",
            "Covenant despite failure: the Davidic covenant (ch. 7) is given BEFORE the fall (chs. 11-12), and YHWH's hesed is explicitly not withdrawn even when the son sins (7:15) — grace precedes and survives catastrophe",
            "Women as seed-line agents: Bathsheba, Tamar (Absalom's sister), the wise woman of Tekoa, the wise woman of Abel — women drive the narrative at critical junctures",
            "Sacred geography: the threshing floor of Araunah (24:18-25), purchased after divine judgment, becomes the Temple mount — judgment site becomes worship site",
        ],
        "mistranslations": [
            {"english": "house", "original": "bayit", "issue": "English collapses the triple meaning: dynasty/lineage, physical temple, and family — the entire Davidic covenant turns on this wordplay"},
            {"english": "angel of the LORD", "original": "mal'ak YHWH", "issue": "Reduces a terrifying divine council agent standing between heaven and earth with a drawn sword to a generic 'angel'"},
            {"english": "steadfast love", "original": "hesed", "issue": "No English word captures it — covenantal faithfulness that persists through the worst betrayal. YHWH's hesed survives David's adultery and murder"},
        ],
    },
    {
        "id": '1kings',
        "section": 'historical-books',
        "title": 'Books 11-12: 1-2 Kings',
        "themes": 'KING DC REBEL HOLY RIV',
        "era_count": 6,
        "chapters": 47,
        "grade": 'A',
        "meta_text": '6 era files &middot; 47 chapters &middot; Grade: A',
        "body_html": '''<p><strong>SOLOMON TO EXILE</strong> — Solomon builds the Temple but violates all three kingship prohibitions (Deut 17:16-17): horses, wives, gold. Kingdom splits. Northern kings: 100% bad. Southern kings: mixed. Elijah vs. Baal on Carmel. Exile of north (722 BC, Assyria) then south (586 BC, Babylon).</p><p><strong>Divine council</strong>: 1 Kings 22:19-23 — Micaiah sees YHWH on his throne, the host of heaven standing beside him. A "lying spirit" is dispatched to deceive Ahab. THE most explicit divine council deliberation scene in the OT (alongside Job 1-2).</p>''',
        "key_claim": "1 Kings 22:19-23 is the most explicit divine council deliberation scene in the OT — YHWH on his throne, the host of heaven around him, a lying spirit volunteering and being dispatched — proving the council is a functioning administration, not a metaphor.",
        "contested_words": [
            {"word": "ruach sheqer", "hebrew": "רוּחַ שֶׁקֶר", "issue": "'Lying spirit' dispatched by YHWH to deceive Ahab (22:22-23) — a divine council agent given a mission, not a rogue demon.", "severity": "CRITICAL"},
            {"word": "tseva hashamayim", "hebrew": "צְבָא הַשָּׁמַיִם", "issue": "'Host of heaven' standing beside YHWH's throne (22:19) — the divine council in session, not decorative angels.", "severity": "CRITICAL"},
            {"word": "Baal", "hebrew": "בַּעַל", "issue": "'Lord/master' — not just an idol but one of the territorial elohim assigned at Deut 32:8 who became corrupt.", "severity": "MAJOR"},
            {"word": "riv", "hebrew": "רִיב", "issue": "Covenant lawsuit — the prophets (Elijah, Elisha) function as covenant prosecutors bringing YHWH's riv against Israel's kings.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "deuteronomy", "why": "Solomon violates all three kingship prohibitions of Deut 17:16-17 (horses, wives, gold) — the text practically checks them off"},
            {"target": "job", "why": "1 Kings 22:19-23 and Job 1-2 are the two explicit divine council deliberation scenes — same structure of YHWH on throne with spirits presenting themselves"},
            {"target": "1samuel", "why": "The evil spirit from YHWH tormenting Saul (1 Sam 16:14) is the same pattern as the lying spirit sent to Ahab — divine council agents on mission"},
            {"target": "isaiah", "why": "Elijah's confrontation with Baal-worship prefigures Isaiah's covenant prosecution of Judah — both are riv lawsuits"},
            {"target": "james", "why": "Elijah's prayer shutting heaven (1 Kings 17:1) is cited in James 5:17 as the model for effective prayer"},
            {"target": "revelation", "why": "Jezebel becomes an archetype of false teaching in Rev 2:20 — the same spirit of idolatrous compromise"},
        ],
        "what_it_doesnt_say": [
            "Why God sends a lying spirit — the moral implications of divine deception through a council agent are never addressed",
            "What happened to the 10 northern tribes after Assyrian exile (722 BC) — they vanish from the biblical narrative",
            "Why Elijah despairs after his greatest victory on Carmel (19:4) — the psychology of prophetic burnout is presented without analysis",
            "How Solomon's wisdom and his catastrophic apostasy coexist — the wisest man makes the most obvious errors",
        ],
        "unusual_characters": [
            {"name": "The lying spirit", "ref": "22:21-22", "detail": "Volunteers in the divine council to deceive Ahab. YHWH approves and dispatches it. A council agent, not a rogue demon.", "connections": ["job", "1samuel"]},
            {"name": "Elijah", "ref": "17:1", "detail": "Covenant prosecutor who shuts heaven, defeats 450 Baal prophets on Carmel, and is taken to heaven without dying.", "connections": ["malachi", "matthew", "james"]},
            {"name": "Jezebel", "ref": "16:31", "detail": "Phoenician princess who imports Baal worship into Israel. Kills YHWH's prophets. Becomes an archetype of religious corruption.", "connections": ["revelation"]},
            {"name": "Elisha", "ref": "19:19", "detail": "Elijah's successor who receives a double portion. Performs twice as many miracles. His bones raise a dead man (2 Kings 13:21).", "connections": ["luke"]},
        ],
        "patterns": [
            "Three kingship prohibitions violated: Deut 17:16-17 forbids horses (1 Kings 10:26), wives (11:3), and gold (10:14-22) — Solomon checks every box",
            "Prophet vs. king structure: every major king is confronted by a prophet — Nathan/David, Ahijah/Jeroboam, Elijah/Ahab, Micaiah/Ahab — the riv framework in action",
            "Northern kingdom: 100% bad kings across 19 rulers and 9 dynasties. Southern kingdom: mixed, with periodic reforms (Asa, Jehoshaphat, Hezekiah, Josiah)",
            "The divine council scene in 22:19-23 mirrors Job 1-2: throne room, assembled spirits, a volunteer agent, a mission approved by YHWH",
        ],
        "mistranslations": [
            {"english": "a lying spirit", "original": "ruach sheqer", "issue": "Makes it sound random — this is a specific divine council member who volunteers for a mission YHWH approves"},
            {"english": "host of heaven", "original": "tseva hashamayim", "issue": "Sounds like a vague crowd — this is the divine council assembled for deliberation around YHWH's throne"},
            {"english": "LORD", "original": "YHWH", "issue": "Throughout Kings, the divine name is hidden behind a title — readers never see that the personal God of Israel has a name"},
        ],
    },
    {
        "id": '2kings',
        "section": 'historical-books',
        "title": 'Book 12: 2 Kings',
        "themes": 'KING REBEL EXILE RIV DC NATIONS',
        "era_count": 3,
        "chapters": 25,
        "grade": 'A',
        "meta_text": '3 era files &middot; 25 chapters &middot; Grade: A',
        "body_html": '''<h4>Major Themes</h4>
  <div class="theme-grid">
    <span class="badge badge-theme">ELISHA</span><span class="badge badge-theme">FALL OF ISRAEL</span><span class="badge badge-theme">FALL OF JUDAH</span><span class="badge badge-theme">EXILE</span><span class="badge badge-theme">DIVINE COUNCIL</span><span class="badge badge-theme">COVENANT LAWSUIT</span>
  </div>
  <p><strong>ELISHA&rsquo;S DOUBLE PORTION</strong> <span class="badge badge-major">MAJOR</span> &mdash; Elisha receives a "double portion" of Elijah&rsquo;s spirit (2:9) and performs twice as many miracles. His ministry proves the Spirit is transferable and multiplicative. His bones raise a dead man (13:21) &mdash; power persists beyond death.</p>
  <p><strong>FALL OF ISRAEL (722 BC)</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; The northern kingdom falls to Assyria. "This occurred because the people of Israel had sinned against YHWH their God" (17:7). The Deuteronomic verdict: Israel served "other gods" &mdash; the territorial elohim of Deut 32:8 who seduced the nation allotted to YHWH.</p>
  <p><strong>FALL OF JUDAH (586 BC)</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; Nebuchadnezzar destroys the Temple, burns Jerusalem, exiles Judah. "YHWH removed Israel out of his sight, as he had spoken by all his servants the prophets" (17:23). The covenant curses of Deut 28 executed in full.</p>
  <p><strong>DIVINE COUNCIL</strong> <span class="badge badge-major">MAJOR</span> &mdash; Elisha prays and the servant&rsquo;s eyes are opened: "The mountain was full of horses and chariots of fire" (6:17). The divine council&rsquo;s army surrounds the prophets &mdash; invisible warfare made visible.</p>

  <h4>Contested Words</h4>
  <table class="ref-table">
    <tr><th>Hebrew</th><th>Issue</th><th>Severity</th></tr>
    <tr><td><strong>pi shenayim</strong> (2:9)</td><td>"Double portion" &mdash; NOT twice as much power, but the firstborn&rsquo;s inheritance share (Deut 21:17). Elisha claims Elijah&rsquo;s spiritual inheritance.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>elohim acherim</strong> (17:7)</td><td>"Other gods" &mdash; the Deuteronomic verdict on Israel&rsquo;s fall. These are real beings &mdash; the territorial elohim of Deut 32:8 &mdash; not mere statues.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>sus va'rekev esh</strong> (6:17)</td><td>"Horses and chariots of fire" &mdash; the divine council&rsquo;s army surrounding Elisha. The same fiery chariots that took Elijah (2:11).</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>mal'ak YHWH</strong> (19:35)</td><td>"Angel of YHWH" strikes 185,000 Assyrians in one night. A single divine council agent annihilates an entire army.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
  </table>

  <h4>Unusual Characters</h4>
  <ul>
    <li><strong>Elisha</strong> (2:9-14) &mdash; Firstborn heir of Elijah&rsquo;s prophetic ministry. Twice the miracles. His bones resurrect a dead man (13:21) &mdash; the Spirit persists beyond death.</li>
    <li><strong>Naaman</strong> (5:1-19) &mdash; Aramean general healed of leprosy by washing in the Jordan. A Gentile brought to faith: "There is no God in all the earth but in Israel" (5:15).</li>
    <li><strong>Josiah</strong> (22:1-23:30) &mdash; The last great reformer. Finds the lost Torah scroll, tears his robes, purges the land of idolatry. But too late &mdash; exile is already decreed.</li>
    <li><strong>Hezekiah</strong> (18:1-20:21) &mdash; Prays and YHWH sends one angel to destroy 185,000 Assyrians. Then shows Babylonian envoys all his treasure &mdash; planting the seed of the Babylonian exile.</li>
  </ul>

  <h4>Conspicuous Silences</h4>
  <ul>
    <li>What happened to the ten northern tribes after 722 BC &mdash; they vanish from biblical history entirely</li>
    <li>HOW one angel killed 185,000 Assyrians overnight (19:35) &mdash; the mechanism is never described</li>
    <li>Why Josiah&rsquo;s sweeping reforms could not avert exile &mdash; the decree was already final (23:26-27) but no explanation of why repentance failed</li>
    <li>The Ark of the Covenant disappears before the exile and is never mentioned again &mdash; the most important object in Israel simply vanishes</li>
  </ul>

  <h4>Cross-References</h4>
  <p class="xref">2 Kings <span class="arrow">&rarr;</span> <span class="badge badge-ot">Deuteronomy</span> <span class="badge badge-ot">Isaiah</span> <span class="badge badge-ot">Jeremiah</span> <span class="badge badge-nt">Luke</span> <span class="badge badge-ot">2 Chronicles</span> <span class="badge badge-ot">Daniel</span> <span class="badge badge-ot">1 Kings</span></p>''',
        "key_claim": "2 Kings records the execution of the Deuteronomic covenant curses — Israel falls to Assyria (722 BC) and Judah to Babylon (586 BC) because they served 'other gods,' the real territorial elohim of Deut 32:8, proving that the spiritual rebellion behind idolatry has geopolitical consequences.",
        "contested_words": [
            {"word": "pi shenayim", "hebrew": "פִּי שְׁנַיִם", "issue": "'Double portion' — NOT twice as much power, but the firstborn's inheritance share (Deut 21:17). Elisha claims Elijah's spiritual inheritance.", "severity": "CRITICAL"},
            {"word": "elohim acherim", "hebrew": "אֱלֹהִים אֲחֵרִים", "issue": "'Other gods' — the Deuteronomic verdict on Israel's fall. These are real beings — the territorial elohim of Deut 32:8 — not mere statues.", "severity": "CRITICAL"},
            {"word": "sus va'rekev esh", "hebrew": "סוּס וְרֶכֶב אֵשׁ", "issue": "'Horses and chariots of fire' — the divine council's army surrounding Elisha. The same fiery chariots that took Elijah (2:11).", "severity": "MAJOR"},
            {"word": "mal'ak YHWH", "hebrew": "מַלְאַךְ יהוה", "issue": "'Angel of YHWH' strikes 185,000 Assyrians in one night (19:35). A single divine council agent annihilates an entire army.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "deuteronomy", "why": "The entire Deuteronomic verdict (2 Kings 17:7-23) is the covenant curses of Deut 28 executed in history — exile was prophesied before the conquest"},
            {"target": "isaiah", "why": "Hezekiah's crisis with Assyria (2 Kings 18-19) is paralleled in Isaiah 36-37 — the prophet and the king face the same threat from the same divine council perspective"},
            {"target": "jeremiah", "why": "Jeremiah prophesies during Judah's final kings and witnesses the fall — the events of 2 Kings 24-25 are Jeremiah's lived experience"},
            {"target": "daniel", "why": "Nebuchadnezzar's conquest of Jerusalem (2 Kings 24) creates the exile setting for Daniel — the seed line survives in Babylon"},
            {"target": "luke", "why": "Jesus references Naaman the Syrian (Luke 4:27) and Elijah/Elisha — Gentile faith in 2 Kings prefigures the gospel going to the nations"},
            {"target": "2chronicles", "why": "Chronicles retells the same kings from a priestly/worship perspective — same events, different theological emphasis"},
        ],
        "what_it_doesnt_say": [
            "What happened to the ten northern tribes after 722 BC — they vanish from biblical history entirely",
            "HOW one angel killed 185,000 Assyrians overnight (19:35) — the mechanism is never described",
            "Why Josiah's sweeping reforms could not avert exile — the decree was already final (23:26-27) but no explanation of why repentance failed",
            "The Ark of the Covenant disappears before the exile and is never mentioned again — the most important object in Israel simply vanishes",
        ],
        "unusual_characters": [
            {"name": "Elisha", "ref": "2:9", "detail": "Firstborn heir of Elijah's prophetic ministry. Twice the miracles. His bones resurrect a dead man (13:21) — the Spirit persists beyond death.", "connections": ["1kings", "luke"]},
            {"name": "Naaman", "ref": "5:1", "detail": "Aramean general healed of leprosy by washing in the Jordan. A Gentile confesses: 'There is no God in all the earth but in Israel.'", "connections": ["luke"]},
            {"name": "Josiah", "ref": "22:1", "detail": "The last great reformer. Finds the lost Torah scroll, tears his robes, purges idolatry. But too late — exile is already decreed.", "connections": ["jeremiah", "2chronicles"]},
            {"name": "The angel of YHWH", "ref": "19:35", "detail": "A single divine council agent destroys 185,000 Assyrians overnight — the invisible army made manifest.", "connections": ["isaiah", "exodus"]},
        ],
        "patterns": [
            "Deuteronomic verdict: every king evaluated by one criterion — did he do right 'in the eyes of YHWH'? The formula repeats for every king, no exceptions",
            "Prophet vs. king intensifies: Elisha confronts kings of Israel and Aram, Isaiah confronts Hezekiah, Huldah pronounces judgment on Josiah's generation — the riv framework never stops",
            "Exile as covenant curse fulfillment: Deut 28:36 ('YHWH will bring you and your king to a nation you have not known') is precisely what happens in 2 Kings 24-25",
            "Gentile faith foreshadowing: Naaman the Syrian (ch. 5) and the Shunammite woman's faith (ch. 4) — the nations respond while Israel rejects",
        ],
        "mistranslations": [
            {"english": "double portion", "original": "pi shenayim", "issue": "Sounds like twice the power — but it is the firstborn's inheritance share (two-thirds). Elisha is Elijah's spiritual heir, not his superior"},
            {"english": "other gods", "original": "elohim acherim", "issue": "English readers assume these are imaginary — but they are the real territorial elohim of Deut 32:8, spiritual beings who received the nations and became corrupt"},
            {"english": "angel of the LORD", "original": "mal'ak YHWH", "issue": "Domesticates a terrifying divine council warrior — a single agent who annihilates 185,000 soldiers is not a greeting-card angel"},
        ],
    },
    {
        "id": '1chronicles',
        "section": 'historical-books',
        "title": 'Books 13-14: 1-2 Chronicles',
        "themes": 'KING PRIEST HOLY SEED',
        "era_count": 4,
        "chapters": 65,
        "grade": 'B+',
        "meta_text": '4 era files &middot; 65 chapters &middot; Grade: B+',
        "body_html": '''<p><strong>THE PRIESTLY RETELLING</strong> — Same history as Samuel-Kings but from a priestly/worship perspective. Focuses on David's preparations for the Temple and the Levitical worship system. 1 Chr 21:1 introduces "Satan" (ha-satan) as the instigator of David's census — 2 Sam 24:1 attributes this to YHWH's anger. Same event, two perspectives: divine council sovereignty vs. adversarial agency.</p>''',
        "key_claim": "1 Chronicles 21:1 attributes David's census to 'Satan' (ha-satan) while 2 Samuel 24:1 attributes the same event to YHWH's anger — revealing that divine council agency and divine sovereignty are not contradictions but two lenses on the same reality.",
        "contested_words": [
            {"word": "satan", "hebrew": "שָׂטָן", "issue": "1 Chr 21:1 uses 'satan' without the article — proper name or title? 2 Sam 24:1 attributes the same event to YHWH. The divine council resolves the tension.", "severity": "CRITICAL"},
            {"word": "mal'ak YHWH", "hebrew": "מַלְאַךְ יהוה", "issue": "'Angel of YHWH' appears with drawn sword over Jerusalem (21:16) — David sees the divine council agent executing judgment.", "severity": "CRITICAL"},
            {"word": "Leviyyim", "hebrew": "לְוִיִּם", "issue": "'Levites' — Chronicles foregrounds Levitical worship roles that Samuel-Kings barely mentions. The priestly lens reshapes the narrative.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "1samuel", "why": "Chronicles retells Samuel-Kings from a priestly perspective — same events, different theological emphasis on worship and temple"},
            {"target": "job", "why": "The satan figure in 1 Chr 21:1 functions like ha-Satan in Job 1-2 — a divine council adversary operating within YHWH's sovereignty"},
            {"target": "psalms", "why": "Chronicles credits David with organizing Levitical worship (1 Chr 25) — the liturgical context for many psalms"},
            {"target": "ezra", "why": "2 Chronicles ends with Cyrus's decree (36:22-23) — the same decree that opens Ezra. Chronicles-Ezra may be one continuous work"},
            {"target": "hebrews", "why": "The Levitical worship system organized in Chronicles is the 'shadow' that Hebrews argues Christ fulfills and surpasses"},
        ],
        "what_it_doesnt_say": [
            "Why Chronicles omits David's adultery with Bathsheba and the murder of Uriah — the priestly retelling sanitizes the king's darkest moments",
            "How 'Satan' and 'YHWH's anger' can both cause the same event — the divine council mechanism is assumed, not explained",
            "Why the northern kingdom is virtually ignored — Chronicles focuses almost exclusively on Judah and the Davidic line",
            "Whether the Chronicler had access to Samuel-Kings or used independent sources — the 'book of the kings' cited repeatedly is unidentified",
        ],
        "unusual_characters": [
            {"name": "Satan (ha-satan)", "ref": "21:1", "detail": "Incites David to take a census — but 2 Sam 24:1 says YHWH's anger did it. Both are true: the adversary operates within divine council sovereignty.", "connections": ["job", "zechariah"]},
            {"name": "The Angel of YHWH", "ref": "21:16", "detail": "Stands between earth and heaven with drawn sword over Jerusalem. David sees the divine council agent executing judgment.", "connections": ["exodus", "joshua", "revelation"]},
            {"name": "Heman, Asaph, Jeduthun", "ref": "25:1", "detail": "The three chief Levitical musicians appointed by David. 'They prophesied with lyres, harps, and cymbals' — worship as prophetic act.", "connections": ["psalms"]},
        ],
        "patterns": [
            "Dual causation: Satan incites (1 Chr 21:1) and YHWH's anger incites (2 Sam 24:1) the same event — divine council agency within divine sovereignty",
            "Chronicles omits negative material about David (Bathsheba, Absalom's rebellion) — the priestly lens focuses on worship preparation, not moral failure",
            "The genealogies (1 Chr 1-9) trace the seed line from Adam to the post-exilic community — the longest continuous genealogy in Scripture",
            "Temple preparation dominates: David cannot build the temple (a man of blood) but organizes everything — the pattern of one generation preparing for the next",
        ],
        "mistranslations": [
            {"english": "Satan", "original": "satan", "issue": "English capitalizes it as a proper name, but the Hebrew may be a title ('an adversary') — the lack of article in 1 Chr 21:1 is debated"},
            {"english": "angel of the LORD", "original": "mal'ak YHWH", "issue": "Reduces a theophanic figure (standing between heaven and earth with a sword) to a generic messenger"},
            {"english": "prophesied with instruments", "original": "nib'u b'kinnorot", "issue": "English separates prophecy from music — the Hebrew shows worship IS prophetic activity, not accompaniment to it"},
        ],
    },
    {
        "id": '2chronicles',
        "section": 'historical-books',
        "title": 'Book 14: 2 Chronicles',
        "themes": 'KING PRIEST HOLY EXILE COV REMNANT',
        "era_count": 3,
        "chapters": 36,
        "grade": 'B+',
        "meta_text": '3 era files &middot; 36 chapters &middot; Grade: B+',
        "body_html": '''<h4>Major Themes</h4>
  <div class="theme-grid">
    <span class="badge badge-theme">SOLOMON&rsquo;S TEMPLE</span><span class="badge badge-theme">DIVIDED KINGDOM</span><span class="badge badge-theme">PRIESTLY WORSHIP</span><span class="badge badge-theme">REFORM &amp; REVIVAL</span><span class="badge badge-theme">EXILE &amp; RETURN</span><span class="badge badge-theme">REMNANT</span>
  </div>
  <p><strong>SOLOMON&rsquo;S TEMPLE</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; 2 Chronicles opens with Solomon&rsquo;s glory and the Temple construction (chs. 1-9). The glory cloud fills the Temple so that "the priests could not stand to minister" (5:14). This is the LAST time the divine presence visibly inhabits a structure &mdash; it will not happen in the Second Temple.</p>
  <p><strong>JUDAH&rsquo;S PERSPECTIVE</strong> <span class="badge badge-major">MAJOR</span> &mdash; Chronicles almost completely ignores the northern kingdom. The focus is on Judah&rsquo;s kings, the Davidic line, and the Levitical worship system. Same events as 2 Kings but through a priestly lens &mdash; worship, Temple, and the seed line are what matter.</p>
  <p><strong>REFORM CYCLES</strong> <span class="badge badge-major">MAJOR</span> &mdash; Periodic revivals: Asa (ch. 14-16), Jehoshaphat (chs. 17-20), Hezekiah (chs. 29-32), Josiah (chs. 34-35). Each reforms worship, restores the Temple, and renews the covenant. Each is followed by decline &mdash; proving human reform cannot fix the heart problem.</p>
  <p><strong>EXILE &amp; CYRUS DECREE</strong> <span class="badge badge-major">MAJOR</span> &mdash; "Until the land had enjoyed its Sabbaths" (36:21) &mdash; 70 years of exile to repay 490 years of violated sabbath years. The book ends with Cyrus&rsquo;s decree: "YHWH has charged me to build him a house" (36:23).</p>

  <h4>Contested Words</h4>
  <table class="ref-table">
    <tr><th>Hebrew</th><th>Issue</th><th>Severity</th></tr>
    <tr><td><strong>kavod YHWH</strong> (5:14)</td><td>"Glory of YHWH" fills the Temple &mdash; a physical manifestation of divine presence so intense the priests cannot function. This never happens in the Second Temple.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>shabbat</strong> (36:21)</td><td>"Sabbath" &mdash; the land must rest. 70 years of exile = repayment for 490 years of violated sabbath-year cycles (Lev 25-26). The exile has mathematical precision.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>teshuvah</strong> (30:9)</td><td>"Return/repentance" &mdash; Hezekiah calls the remnant to return to YHWH. The same root (shuv) structures the entire prophetic message: turn back.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>Koresh</strong> (36:22)</td><td>"Cyrus" &mdash; a pagan king whose spirit YHWH "stirred up." The last word of Chronicles looks forward to restoration through a Gentile instrument.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
  </table>

  <h4>Unusual Characters</h4>
  <ul>
    <li><strong>Solomon</strong> (chs. 1-9) &mdash; Builder of the Temple, recipient of divine wisdom. Chronicles emphasizes his glory and worship organization, minimizing the apostasy that 1 Kings highlights.</li>
    <li><strong>Jehoshaphat</strong> (chs. 17-20) &mdash; Sends Levites to teach Torah throughout Judah. Faces a vast army and is told: "The battle is not yours but God&rsquo;s" (20:15). Worship precedes victory.</li>
    <li><strong>Hezekiah</strong> (chs. 29-32) &mdash; Reopens and cleanses the Temple on day one of his reign. Celebrates the greatest Passover since Solomon. Worship restoration as the first act of governance.</li>
    <li><strong>Josiah</strong> (chs. 34-35) &mdash; Finds the lost Torah scroll at age 26. The prophetess Huldah (not a male prophet) delivers YHWH&rsquo;s verdict: judgment is irreversible, but Josiah will die in peace.</li>
  </ul>

  <h4>Conspicuous Silences</h4>
  <ul>
    <li>The northern kingdom is virtually ignored &mdash; Chronicles treats the ten tribes as if they barely exist after the split</li>
    <li>David&rsquo;s sin with Bathsheba and Absalom&rsquo;s rebellion are completely omitted &mdash; the priestly retelling sanitizes the king</li>
    <li>The glory cloud fills Solomon&rsquo;s Temple but will never fill the Second Temple &mdash; the text never addresses why the divine presence does not return</li>
    <li>How Manasseh&rsquo;s repentance in exile (33:12-13) relates to YHWH&rsquo;s irreversible judgment on Judah &mdash; personal repentance cannot undo national decree</li>
  </ul>

  <h4>Cross-References</h4>
  <p class="xref">2 Chronicles <span class="arrow">&rarr;</span> <span class="badge badge-ot">1 Kings</span> <span class="badge badge-ot">2 Kings</span> <span class="badge badge-ot">Ezra</span> <span class="badge badge-ot">Leviticus</span> <span class="badge badge-ot">Isaiah</span> <span class="badge badge-ot">Jeremiah</span> <span class="badge badge-nt">Hebrews</span></p>''',
        "key_claim": "2 Chronicles records the glory cloud filling Solomon's Temple so intensely the priests cannot stand (5:14) — and this is the LAST time divine presence visibly inhabits a structure, making the Second Temple's conspicuous absence of glory the Old Testament's greatest unanswered question.",
        "contested_words": [
            {"word": "kavod YHWH", "hebrew": "כְּבוֹד יהוה", "issue": "'Glory of YHWH' fills the Temple — a physical manifestation so intense the priests cannot function (5:14). This never happens in the Second Temple.", "severity": "CRITICAL"},
            {"word": "shabbat", "hebrew": "שַׁבָּת", "issue": "'Sabbath' — the land must rest. 70 years of exile = repayment for 490 years of violated sabbath-year cycles (Lev 25-26). The exile has mathematical precision.", "severity": "CRITICAL"},
            {"word": "teshuvah", "hebrew": "תְּשׁוּבָה", "issue": "'Return/repentance' — Hezekiah calls the remnant to return to YHWH. The root shuv structures the entire prophetic message: turn back.", "severity": "MAJOR"},
            {"word": "Koresh", "hebrew": "כֹּרֶשׁ", "issue": "'Cyrus' — a pagan king whose spirit YHWH 'stirred up.' The last word of Chronicles looks forward to restoration through a Gentile instrument.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "1kings", "why": "Same events but different lens — 1 Kings records Solomon's apostasy and the political disaster; 2 Chronicles foregrounds his Temple and worship legacy"},
            {"target": "2kings", "why": "The fall of Judah in 2 Kings 25 is retold in 2 Chr 36 — same event, but Chronicles adds the sabbath-year calculation (36:21) and Cyrus's decree"},
            {"target": "ezra", "why": "2 Chronicles ends with Cyrus's decree (36:22-23) using nearly identical wording to Ezra 1:1-3 — the narrative continues seamlessly"},
            {"target": "leviticus", "why": "The sabbath-year exile calculation (36:21) directly fulfills Lev 26:34-35 — the land finally enjoys its sabbaths"},
            {"target": "isaiah", "why": "Cyrus named as YHWH's instrument (Isa 44:28-45:1) is the same Cyrus who closes 2 Chronicles — prophecy fulfilled in the closing verse"},
            {"target": "hebrews", "why": "The Levitical worship system organized by Solomon in Chronicles is the 'shadow' that Hebrews argues Christ fulfills and surpasses"},
        ],
        "what_it_doesnt_say": [
            "The northern kingdom is virtually ignored — Chronicles treats the ten tribes as if they barely exist after the split",
            "David's sin with Bathsheba and Absalom's rebellion are completely omitted — the priestly retelling sanitizes the king",
            "The glory cloud fills Solomon's Temple but will never fill the Second Temple — the text never addresses why the divine presence does not return",
            "How Manasseh's repentance in exile (33:12-13) relates to YHWH's irreversible judgment on Judah — personal repentance cannot undo national decree",
        ],
        "unusual_characters": [
            {"name": "Solomon", "ref": "1:1", "detail": "Builder of the Temple, recipient of divine wisdom. Chronicles emphasizes his glory and worship, minimizing the apostasy 1 Kings highlights.", "connections": ["1kings", "proverbs"]},
            {"name": "Jehoshaphat", "ref": "17:1", "detail": "Sends Levites to teach Torah throughout Judah. Faces a vast army: 'The battle is not yours but God's' (20:15). Worship precedes victory.", "connections": []},
            {"name": "Hezekiah", "ref": "29:1", "detail": "Reopens and cleanses the Temple on day one. Celebrates the greatest Passover since Solomon. Worship restoration as first act of governance.", "connections": ["isaiah", "2kings"]},
            {"name": "Huldah", "ref": "34:22", "detail": "The prophetess — not a male prophet — delivers YHWH's verdict on Josiah's generation. A woman speaks the definitive word of judgment.", "connections": ["2kings"]},
        ],
        "patterns": [
            "Reform-decline cycle: every reforming king (Asa, Jehoshaphat, Hezekiah, Josiah) is followed by decline — human reform cannot permanently fix the covenant breach",
            "Worship as warfare: Jehoshaphat sends singers ahead of the army (20:21-22) and YHWH sets ambushes — the priestly lens shows worship as the weapon, not swords",
            "Sabbath-year mathematics: 70 years of exile repays 490 years of violated sabbath cycles — YHWH keeps precise accounts even when Israel ignores them",
            "The glory cloud appears at dedication (5:14) and never returns — the trajectory from filled Temple to empty Second Temple is the OT's silent tragedy",
        ],
        "mistranslations": [
            {"english": "the glory of the LORD", "original": "kavod YHWH", "issue": "'Glory' sounds abstract — kavod means heavy, weighty, substantial. The divine presence was a physical, overwhelming force that incapacitated the priests"},
            {"english": "Sabbath rest", "original": "shabbat", "issue": "Reduces a cosmic principle to a day off — the land itself requires sabbath, and violating it for 490 years triggers mathematical exile"},
            {"english": "the LORD stirred up the spirit of Cyrus", "original": "he'ir YHWH et ruach Koresh", "issue": "Makes it sound like gentle inspiration — YHWH commandeered a pagan emperor's decision-making to fulfill covenant purposes"},
        ],
    },
    {
        "id": 'ezra',
        "section": 'historical-books',
        "title": 'Books 15-16: Ezra-Nehemiah',
        "themes": 'COV EXILE HOLY PRIEST',
        "era_count": 3,
        "chapters": 23,
        "grade": 'B+',
        "meta_text": '3 era files &middot; 23 chapters &middot; Grade: B+',
        "body_html": '''<p><strong>RETURN FROM EXILE</strong> — Cyrus decree (538 BC), Temple rebuilt, walls rebuilt. The intermarriage crisis (Ezra 9-10). Nehemiah rebuilds Jerusalem's walls in 52 days against opposition. Ezra reads Torah publicly — covenant renewal. The exile-return pattern reaches its historical resolution, though the spiritual exile continues (no glory fills the Second Temple).</p>''',
        "key_claim": "The exile-return pattern reaches its historical resolution but NOT its spiritual one — the Second Temple is rebuilt, yet no glory cloud fills it, no ark is present, and the people remain under foreign rule, proving the true restoration awaits a greater return.",
        "contested_words": [
            {"word": "Koresh", "hebrew": "כֹּרֶשׁ", "issue": "Cyrus — called YHWH's 'anointed' (mashiach) in Isa 45:1. A pagan king fulfilling divine council purposes, named by Isaiah 150 years before his birth.", "severity": "CRITICAL"},
            {"word": "golah", "hebrew": "גּוֹלָה", "issue": "'Exile/exilic community' — the returnees define themselves by exile, not by return. Identity shaped by displacement.", "severity": "MAJOR"},
            {"word": "mamlaket kohanim", "hebrew": "מַמְלֶכֶת כֹּהֲנִים", "issue": "'Kingdom of priests' — Ezra's Torah reading (Neh 8) restores the Sinai identity (Ex 19:6), but now under Persian authority, not divine theocracy.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "isaiah", "why": "Cyrus is named as YHWH's instrument (Isa 44:28-45:1) — the exile-return fulfills Isaiah's prophecy with a pagan 'messiah'"},
            {"target": "jeremiah", "why": "Jeremiah's 70-year prophecy (Jer 25:11-12, 29:10) is fulfilled by the Cyrus decree — Daniel reads Jeremiah to understand the timeline (Dan 9:2)"},
            {"target": "daniel", "why": "Daniel 9:2 reads Jeremiah's 70 years and prays — the return from exile is triggered by prophetic reading and intercessory prayer"},
            {"target": "1chronicles", "why": "2 Chronicles ends with Cyrus's decree (36:22-23) using nearly identical wording to Ezra 1:1-3 — continuous narrative"},
            {"target": "haggai", "why": "Haggai rebukes the returnees for building their own houses while the Temple lies in ruins (Hag 1:4) — the Second Temple is completed under his prophetic pressure"},
            {"target": "malachi", "why": "Malachi addresses the same post-exilic community — intermarriage, corrupt priests, tithing failures — the return didn't fix the heart problem"},
        ],
        "what_it_doesnt_say": [
            "No glory cloud fills the Second Temple — unlike Solomon's Temple (1 Kings 8:10-11), the divine presence is conspicuously absent",
            "The Ark of the Covenant is never mentioned — it vanished before or during the exile and the text never explains where it went",
            "What happened to the majority who stayed in Babylon — only a small remnant returned; most preferred exile",
            "Why Ezra's forced divorce decree (Ezra 10) was necessary when Ruth the Moabitess was accepted — the contradiction is never reconciled",
        ],
        "unusual_characters": [
            {"name": "Cyrus", "ref": "1:1", "detail": "Persian king who decrees Israel's return. Called YHWH's 'anointed' (Isa 45:1) — a pagan king serving divine council purposes.", "connections": ["isaiah", "daniel"]},
            {"name": "Ezra", "ref": "7:6", "detail": "Priest and scribe who reads Torah publicly (Neh 8), triggering weeping and covenant renewal. Restores the word to the center.", "connections": []},
            {"name": "Nehemiah", "ref": "1:1", "detail": "Cupbearer to the Persian king who rebuilds Jerusalem's walls in 52 days against fierce opposition. Governance as spiritual act.", "connections": []},
            {"name": "Sanballat and Tobiah", "ref": "2:10", "detail": "Opposition leaders who mock, threaten, and conspire against the wall project — the seed war's political front in the post-exilic period.", "connections": []},
        ],
        "patterns": [
            "The exile-return pattern: Egypt (Gen-Ex) → Assyria (2 Kings 17) → Babylon (2 Kings 25) → return (Ezra-Neh) — each exile deeper, each return more diminished",
            "Walls before worship: Nehemiah rebuilds physical walls (chs. 1-7), then Ezra restores Torah (chs. 8-10) — security enables spiritual renewal",
            "The Second Temple is conspicuously inferior: no ark, no glory cloud, no Urim and Thummim — the return is physical but the spiritual exile continues",
            "Intermarriage crisis bookends: Ezra 9-10 (forced divorces) and Neh 13 (Nehemiah's rebuke) — the same problem persists despite repeated intervention",
        ],
        "mistranslations": [
            {"english": "the decree of Cyrus", "original": "ta'am Koresh", "issue": "Presents a bureaucratic edict — misses that YHWH 'stirred up the spirit' (he'ir et ruach) of a pagan king, divine council orchestration through foreign power"},
            {"english": "the house of God", "original": "beit ha'elohim", "issue": "Generic 'house of God' obscures that this is a diminished replacement — no glory, no ark, no divine presence manifest"},
            {"english": "the law of Moses", "original": "torat Moshe", "issue": "'Law' import again — Ezra reads 'instruction of Moses,' and the people weep because they understand it, not because they fear punishment"},
        ],
    },
    {
        "id": 'nehemiah',
        "section": 'historical-books',
        "title": 'Book 16: Nehemiah',
        "themes": 'COV EXILE HOLY REMNANT',
        "era_count": 2,
        "chapters": 13,
        "grade": 'B+',
        "meta_text": '2 era files &middot; 13 chapters &middot; Grade: B+',
        "body_html": '''<h4>Major Themes</h4>
  <div class="theme-grid">
    <span class="badge badge-theme">WALL REBUILDING</span><span class="badge badge-theme">COVENANT RENEWAL</span><span class="badge badge-theme">OPPOSITION</span><span class="badge badge-theme">REMNANT</span><span class="badge badge-theme">REFORM</span><span class="badge badge-theme">TORAH READING</span>
  </div>
  <p><strong>WALL REBUILDING</strong> <span class="badge badge-major">MAJOR</span> &mdash; Nehemiah rebuilds Jerusalem&rsquo;s walls in 52 days against fierce opposition (6:15). Workers build with one hand and hold a weapon in the other (4:17). Physical restoration as spiritual warfare &mdash; the seed-line city must be defended.</p>
  <p><strong>COVENANT RENEWAL</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; Ezra reads the Torah publicly for hours (ch. 8). The people weep when they hear it. Then they celebrate: "The joy of YHWH is your strength" (8:10). The covenant is renewed (ch. 9-10) with a comprehensive confession of national history from Abraham to exile.</p>
  <p><strong>OPPOSITION AS SEED WAR</strong> <span class="badge badge-major">MAJOR</span> &mdash; Sanballat, Tobiah, and Geshem mock, threaten, and conspire. They attempt psychological warfare, false prophecy (6:10-14), and infiltration. The opposition to rebuilding Jerusalem is the seed war&rsquo;s political front in the post-exilic period.</p>
  <p><strong>REFORM</strong> <span class="badge badge-major">MAJOR</span> &mdash; Nehemiah&rsquo;s second term (ch. 13): Sabbath enforcement, intermarriage confrontation, tithing restoration. The same problems persist despite the wall, the Torah, and the covenant &mdash; proving external reform cannot change the heart.</p>

  <h4>Contested Words</h4>
  <table class="ref-table">
    <tr><th>Hebrew</th><th>Issue</th><th>Severity</th></tr>
    <tr><td><strong>chedvat YHWH</strong> (8:10)</td><td>"The joy of YHWH is your strength" &mdash; not human happiness but divine joy as the source of communal power. The word chedvah appears only here in the OT.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>mevin</strong> (8:8)</td><td>"Gave the sense" / "made it understood" &mdash; the Levites translated or interpreted the Torah for the people. Possibly the origin of Targum (Aramaic paraphrase) tradition.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>aravim</strong> (10:31)</td><td>"Pledges/guarantors" &mdash; the people seal a written covenant with specific obligations: sabbath commerce, sabbath year, temple tax, tithes. A legal contract with YHWH.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>mamzer</strong> (13:23-24)</td><td>Children of mixed marriages who "could not speak the language of Judah" &mdash; linguistic assimilation as covenant erosion. Identity maintained through language.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
  </table>

  <h4>Unusual Characters</h4>
  <ul>
    <li><strong>Nehemiah</strong> (1:1) &mdash; Cupbearer to the Persian king who becomes governor of Judah. Weeps, prays, plans, then acts. Governance as spiritual calling &mdash; he rebuilds with a sword and a trowel.</li>
    <li><strong>Sanballat and Tobiah</strong> (2:10, 4:1-3) &mdash; Opposition leaders who use mockery, military threats, false prophecy, and political infiltration. The seed war fought through bureaucracy and intimidation.</li>
    <li><strong>Noadiah</strong> (6:14) &mdash; A false prophetess hired to intimidate Nehemiah. "Remember Noadiah and the rest of the prophets who wanted to make me afraid." Prophetic corruption in the post-exilic community.</li>
    <li><strong>Ezra</strong> (8:1-8) &mdash; Reads the Torah from a wooden platform from dawn to midday. The people stand, listen, weep, then feast &mdash; the word of God as the center of communal life.</li>
  </ul>

  <h4>Conspicuous Silences</h4>
  <ul>
    <li>No prophetic voice accompanies Nehemiah &mdash; unlike Moses, Joshua, or David, he operates without a named prophet beside him (Ezra fills a priestly role, not prophetic)</li>
    <li>The Second Temple has no glory cloud, no ark, no Urim and Thummim &mdash; the physical return does not restore the divine presence</li>
    <li>Nehemiah&rsquo;s reforms in chapter 13 repeat the same problems already addressed &mdash; the text offers no solution to the cycle of failure</li>
    <li>The book ends abruptly with "Remember me, O my God, for good" (13:31) &mdash; no resolution, no divine response, no closure</li>
  </ul>

  <h4>Cross-References</h4>
  <p class="xref">Nehemiah <span class="arrow">&rarr;</span> <span class="badge badge-ot">Ezra</span> <span class="badge badge-ot">Deuteronomy</span> <span class="badge badge-ot">Leviticus</span> <span class="badge badge-ot">Haggai</span> <span class="badge badge-ot">Malachi</span> <span class="badge badge-nt">Acts</span></p>''',
        "key_claim": "Nehemiah proves that walls, Torah, and covenant renewal cannot fix the human heart — the same sins (Sabbath-breaking, intermarriage, tithing failures) resurface in chapter 13 despite everything, demonstrating that the true restoration requires something beyond external reform.",
        "contested_words": [
            {"word": "chedvat YHWH", "hebrew": "חֶדְוַת יהוה", "issue": "'The joy of YHWH is your strength' — not human happiness but divine joy as the source of communal power. The word chedvah appears only here in the OT.", "severity": "CRITICAL"},
            {"word": "mevin", "hebrew": "מֵבִין", "issue": "'Gave the sense/made it understood' — the Levites translated or interpreted the Torah for the people. Possibly the origin of Targum tradition.", "severity": "MAJOR"},
            {"word": "aravim", "hebrew": "עֲרָבִים", "issue": "The people seal a written covenant with specific obligations: sabbath commerce, sabbath year, temple tax, tithes. A legal contract with YHWH.", "severity": "MAJOR"},
            {"word": "mamzer", "hebrew": "מַמְזֵר", "issue": "Children of mixed marriages who 'could not speak the language of Judah' — linguistic assimilation as covenant erosion. Identity maintained through language.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "ezra", "why": "Ezra-Nehemiah may have been one scroll — Ezra's Torah reading (Neh 8) and Nehemiah's wall-building are two halves of the same restoration"},
            {"target": "deuteronomy", "why": "The covenant renewal (Neh 9-10) recounts history from creation to exile using Deuteronomic categories — the same riv/covenant lawsuit framework"},
            {"target": "leviticus", "why": "Sabbath-year enforcement (10:31, 13:15-22) and tithing restoration (10:37-39, 13:10-13) enforce the Levitical code in the post-exilic community"},
            {"target": "haggai", "why": "Haggai rebuked the returnees for neglecting the Temple (Hag 1:4); Nehemiah continues the same confrontation with communal neglect"},
            {"target": "malachi", "why": "Malachi addresses the SAME post-exilic sins: intermarriage, corrupt priests, tithing failures — the problems Nehemiah confronts are still unresolved"},
            {"target": "acts", "why": "Pentecost (Acts 2) reverses the linguistic fragmentation — where Nehemiah's community lost its language, the Spirit restores communication across all nations"},
        ],
        "what_it_doesnt_say": [
            "No prophetic voice accompanies Nehemiah — unlike Moses, Joshua, or David, he operates without a named prophet beside him",
            "The Second Temple has no glory cloud, no ark, no Urim and Thummim — the physical return does not restore the divine presence",
            "Nehemiah's reforms in chapter 13 repeat problems already addressed — the text offers no solution to the cycle of failure",
            "The book ends abruptly with 'Remember me, O my God, for good' (13:31) — no resolution, no divine response, no closure",
        ],
        "unusual_characters": [
            {"name": "Nehemiah", "ref": "1:1", "detail": "Cupbearer to the Persian king who becomes governor. Weeps, prays, plans, then acts. Rebuilds with a sword and a trowel.", "connections": ["ezra"]},
            {"name": "Sanballat and Tobiah", "ref": "2:10", "detail": "Opposition leaders using mockery, military threats, false prophecy, and political infiltration — the seed war through bureaucracy.", "connections": []},
            {"name": "Noadiah", "ref": "6:14", "detail": "A false prophetess hired to intimidate Nehemiah. Prophetic corruption in the post-exilic community.", "connections": []},
            {"name": "Ezra", "ref": "8:1", "detail": "Reads Torah from dawn to midday on a wooden platform. The people stand, listen, weep, then feast — the word as the center of communal life.", "connections": ["ezra"]},
        ],
        "patterns": [
            "Build-then-renew sequence: walls first (chs. 1-7), then Torah (ch. 8), then covenant (chs. 9-10), then community reform (chs. 11-13) — physical security enables spiritual restoration",
            "Opposition escalation: mockery (4:1-3) to military threat (4:7-8) to false prophecy (6:10-14) to infiltration (13:4-9) — the enemy adapts tactics when each fails",
            "The confession prayer (ch. 9) recounts covenant history from Abraham to exile — the community locates itself within the larger story of failure and faithfulness",
            "Nehemiah's 'remember me' refrain (5:19, 13:14, 13:22, 13:31) — the governor appeals directly to God's memory, bypassing all human systems of recognition",
        ],
        "mistranslations": [
            {"english": "the joy of the LORD is your strength", "original": "chedvat YHWH hi ma'uzkem", "issue": "Often sentimentalized — this is not a happy feeling but divine joy as a defensive fortress (ma'oz = stronghold). Joy IS the fortification"},
            {"english": "gave the sense", "original": "meforash/mevin", "issue": "Sounds like simple explanation — this may be the earliest evidence of Targum, translating Hebrew Torah into Aramaic for a community that lost its language in exile"},
            {"english": "governor", "original": "tirshata/pechah", "issue": "English bureaucratic title hides that Nehemiah held Persian imperial authority — he was a political appointee of Artaxerxes with military backing"},
        ],
    },
    {
        "id": 'esther',
        "section": 'historical-books',
        "title": 'Book 17: Esther',
        "themes": 'PROV WOMEN REVERSAL',
        "era_count": 2,
        "chapters": 10,
        "grade": 'A-',
        "meta_text": '2 era files &middot; 10 chapters &middot; Grade: A-',
        "body_html": '''<p><strong>GOD NEVER MENTIONED</strong> — Not once. No prayer, no covenant, no temple, no sacrifice, no prophet, no miracle. Set entirely in Persia. Yet it's canonical. Providence without naming Providence. The seed war continues: Haman (Agagite = descendant of Agag the Amalekite king Saul spared) attempts genocide of the Jews. The ancient enmity of Amalek (Exod 17, Deut 25:17-19) plays out in the Persian court. Reversal: the gallows Haman builds for Mordecai become his own execution site.</p></div></div>

<!-- WISDOM -->''',
        "key_claim": "Esther is the seed war operating through pure providence — God is never named, yet the ancient enmity of Amalek (Gen 36, Ex 17, 1 Sam 15) plays out in a Persian court, and the genocide meant to end the seed line becomes the gallows for its perpetrator.",
        "contested_words": [
            {"word": "Agagi", "hebrew": "אֲגָגִי", "issue": "'Agagite' — Haman's lineage traces to Agag, king of the Amalekites whom Saul spared (1 Sam 15). The ancient enmity of Amalek continues.", "severity": "CRITICAL"},
            {"word": "pur", "hebrew": "פּוּר", "issue": "'Lot' (Persian loanword) — Haman casts lots to determine the date of genocide. The festival Purim is named for the lots meant to destroy them.", "severity": "MAJOR"},
            {"word": "dat", "hebrew": "דָּת", "issue": "'Decree/law' (Persian loanword) — the irrevocable law of the Medes and Persians becomes both the weapon and the instrument of reversal.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "exodus", "why": "Amalek first attacks Israel at Rephidim (Ex 17:8-16) — YHWH declares perpetual war against Amalek. Haman is the continuation of that war."},
            {"target": "deuteronomy", "why": "Deut 25:17-19 commands Israel to 'blot out the memory of Amalek' — Esther's story is the near-reversal where Amalek almost blots out Israel instead"},
            {"target": "1samuel", "why": "Saul spares Agag the Amalekite king (1 Sam 15) against YHWH's command — Haman the Agagite is the consequence of Saul's disobedience"},
            {"target": "genesis", "why": "The seed war (Gen 3:15) operates even when God is unnamed — providence preserves the line through which Christ will come"},
            {"target": "revelation", "why": "The reversal pattern (the weapon meant for the righteous destroys the wicked) reappears in Revelation's final judgments"},
        ],
        "what_it_doesnt_say": [
            "God is never mentioned — no prayer, no covenant, no temple, no sacrifice, no prophet, no miracle in the entire book",
            "Why Mordecai refuses to bow to Haman — the text never explains whether this is ethnic, religious, or personal",
            "How Esther maintained her Jewish identity secretly in a pagan harem — the logistics are never addressed",
            "Whether the Jews' counter-violence (ch. 9) was proportional — 75,000 enemies killed, and the text does not evaluate it morally",
        ],
        "unusual_characters": [
            {"name": "Esther (Hadassah)", "ref": "2:7", "detail": "Jewish orphan who becomes Persian queen. Her Hebrew name (Hadassah, 'myrtle') is hidden behind a Persian name — identity concealed in exile.", "connections": []},
            {"name": "Mordecai", "ref": "2:5", "detail": "Described as a Benjaminite descendant of Kish — the same clan as King Saul. The Saul-Agag conflict literally replays through their descendants.", "connections": ["1samuel"]},
            {"name": "Haman", "ref": "3:1", "detail": "The Agagite — descendant of the Amalekite royal line. The ancient enemy of Israel operating in the Persian court. Hanged on his own gallows.", "connections": ["exodus", "1samuel"]},
            {"name": "Vashti", "ref": "1:9", "detail": "The queen who refuses to be displayed. Her defiance creates the vacancy Esther fills — providence working through a pagan queen's dignity.", "connections": []},
        ],
        "patterns": [
            "Complete reversal structure: every weapon aimed at the Jews is turned back — the decree, the gallows, the date of destruction all become instruments of Jewish victory",
            "The Saul-Agag parallel: Mordecai (Benjaminite, clan of Kish = Saul's father) vs. Haman (Agagite = Agag's descendant) — the same conflict replaying centuries later",
            "Providence without theophany: God is never named but every 'coincidence' is precisely timed — the king's insomnia (6:1), the timing of Esther's banquets, the gallows' height",
            "Hiddenness motif: Esther hides her identity, God hides his name, and the seed war hides behind Persian court politics",
        ],
        "mistranslations": [
            {"english": "Agagite", "original": "Agagi", "issue": "English readers miss the Amalekite connection entirely — this single word links Haman to the ancient enemy YHWH swore to destroy (Ex 17:16)"},
            {"english": "gallows", "original": "ets", "issue": "'Tree/pole' — not a modern gallows but an impalement stake. The execution method is more brutal than English suggests"},
            {"english": "lots", "original": "purim", "issue": "The festival name comes from the Persian word for lots — the instrument of fate-manipulation becomes a celebration of divine counter-manipulation"},
        ],
    },
    {
        "id": 'job',
        "section": 'wisdom-books',
        "title": 'Book 18: Job (Iyyov)',
        "themes": 'DC SPIRIT TYPE',
        "era_count": 3,
        "chapters": 42,
        "grade": 'A+',
        "meta_text": '3 era files &middot; 42 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>THE DIVINE COUNCIL IN SESSION</strong> — Job 1-2 opens in YHWH's throne room. The bene ha'elohim (sons of God) present themselves. ha-Satan ("the adversary") is among them — a divine council member with a prosecutorial role. He challenges Job's loyalty. YHWH sets boundaries ("only do not touch his life"). This is THE divine council framework: spiritual beings influencing earthly events within divine permission.</p><p><strong>THEODICY WITHOUT RESOLUTION</strong> — God answers from the whirlwind (38-41) but NEVER explains Job's suffering. Instead he reveals his cosmic sovereignty: "Where were you when I laid the foundation of the earth... when the morning stars sang together and all the sons of God (bene elohim) shouted for joy?" (38:4-7). The answer to suffering is not explanation but ENCOUNTER.</p><p><strong>Key terms</strong>: ha-Satan (the accuser/adversary — with the article, a TITLE not a name), Leviathan/Behemoth (chaos creatures — divine council cosmology), bene elohim (sons of God — council members celebrating creation)</p>''',
        "key_claim": "Job 1-2 is the clearest divine council scene in the OT — ha-Satan operates as a prosecutorial member of the council, not an independent adversary, and YHWH's answer to suffering is not explanation but encounter with cosmic sovereignty.",
        "contested_words": [{'word': 'ha-Satan', 'hebrew': 'הַשָּׂטָן', 'issue': "The article (ha-) makes this a TITLE ('the adversary'), not a proper name. A divine council role, not yet the personal devil of later theology.", 'severity': 'CRITICAL'}, {'word': 'bene elohim', 'hebrew': 'בְּנֵי אֱלֹהִים', 'issue': 'Sons of God — divine council members presenting themselves before YHWH. Same phrase as Gen 6:2.', 'severity': 'CRITICAL'}, {'word': 'Leviathan', 'hebrew': 'לִוְיָתָן', 'issue': 'Chaos creature in 41:1-34 — literal monster or symbol of cosmic evil? Ugaritic Litanu parallels. YHWH alone controls it.', 'severity': 'CRITICAL'}, {'word': 'Behemoth', 'hebrew': 'בְּהֵמוֹת', 'issue': "Plural of 'beast' used as singular (40:15-24). Primal chaos creature, not a hippo. Paired with Leviathan as cosmic forces.", 'severity': 'MAJOR'}, {'word': "go'el", 'hebrew': 'גֹּאֵל', 'issue': "'I know that my Redeemer (go'el) lives' (19:25) — kinsman-redeemer. Who is Job's go'el? God himself? A divine mediator?", 'severity': 'CRITICAL'}],
        "hidden_connections": [{'target': 'genesis', 'why': "bene ha'elohim (Job 1:6, 2:1) is the same phrase as Gen 6:2 — divine council members in both passages"}, {'target': '1enoch', 'why': 'The Watcher framework explains the council hierarchy Job depicts — beings with access to the throne room and delegated authority'}, {'target': 'psalms', 'why': "Ps 82 depicts the same divine council Job sees; Ps 104:26 references Leviathan as God's plaything"}, {'target': 'isaiah', 'why': 'Isaiah 6 throne room scene parallels Job 1-2 — both show the divine council in session with YHWH presiding'}, {'target': 'revelation', 'why': 'Satan as accuser (Rev 12:10) fulfills the ha-Satan prosecutorial role established in Job; the throne room scenes echo Job 1-2'}, {'target': 'romans', 'why': "Rom 8:28 ('all things work together for good') is the theological answer to Job's unanswered question"}],
        "what_it_doesnt_say": ["Why God accepted the wager — YHWH never explains why he permits ha-Satan's challenge", "What happened to Job's first children — they are never mourned or mentioned again after the restoration", "Elihu's origin — he appears without introduction (ch. 32) and God neither commends nor condemns him", 'Whether Leviathan and Behemoth are literal or symbolic — God describes them in detail but never classifies them', 'Why the friends are condemned for saying God punishes sin — which is technically true, just misapplied'],
        "unusual_characters": [{'name': 'ha-Satan', 'ref': '1:6', 'detail': "Divine council member with prosecutorial role. Challenges Job's loyalty within YHWH's permission boundaries. A title, not yet a proper name.", 'connections': ['zechariah', '1chronicles', 'revelation']}, {'name': 'Elihu', 'ref': '32:2', 'detail': 'Appears from nowhere after the three friends fail. God neither endorses nor rebukes him. The most enigmatic figure in wisdom literature.', 'connections': []}, {'name': 'Leviathan', 'ref': '41:1', 'detail': 'Chaos creature only YHWH can control. Fire-breathing, armored, untamable. Cosmic evil personified.', 'connections': ['psalms', 'isaiah', 'revelation']}],
        "patterns": ['Chiastic structure: prose prologue (1-2) -> dialogue cycles (3-31) -> Elihu (32-37) -> God speaks (38-41) -> prose epilogue (42)', "Three cycles of dialogue deteriorate: friends become harsher, arguments more circular, third cycle breaks down (Bildad's speech is only 6 verses, Zophar disappears)", "God's answer (38-41) asks 70+ unanswered questions — the divine response to human questioning is MORE questions, revealing the asymmetry between Creator and creature", 'Double restoration (42:10) — Job receives twice what he lost, EXCEPT children (same number) because the first children still exist in Sheol'],
        "mistranslations": [{'english': 'Satan', 'original': 'ha-Satan', 'issue': "Dropping the article turns a divine council title ('the adversary/accuser') into a proper name, importing later theology"}, {'english': 'monster/hippo/crocodile', 'original': 'Behemoth/Leviathan', 'issue': "Naturalizing cosmic chaos creatures into ordinary animals strips the divine council cosmology from God's speech"}, {'english': 'Redeemer', 'original': "go'el", 'issue': "English loses the kinsman-redeemer legal framework — go'el is a specific role with obligations, not a generic title"}],
    },
    {
        "id": 'psalms',
        "section": 'wisdom-books',
        "title": 'Book 19: Psalms (Tehillim)',
        "themes": 'DC KING PRIEST SEED COV HOLY SPIRIT RIV',
        "era_count": 7,
        "grade": 'A+',
        "meta_text": '7 era files &middot; 150 psalms in 5 books &middot; Grade: A+',
        "body_html": '''<p><strong>THE DIVINE COUNCIL HYMNBOOK</strong> — Ps 82: "God (Elohim) stands in the divine assembly (adat-el); in the midst of the gods (elohim) he holds judgment." YHWH judges the allotted gods for failing their nations. "You are gods (elohim), sons of the Most High (bene elyon), all of you; nevertheless, like men you shall die." Jesus quotes this (John 10:34).</p><p><strong>Ps 110</strong> — Most quoted OT verse in NT. "The LORD (YHWH) said to my Lord (Adoni): Sit at my right hand... You are a priest forever after the order of Melchizedek." Two figures, both divine. Christ's priesthood is Melchizedekian, not Levitical.</p><p><strong>Ps 2</strong> — "You are my Son; today I have begotten you." The divine decree of sonship. Applied to Jesus at baptism (Mark 1:11), resurrection (Acts 13:33), and in Hebrews 1:5.</p><p><strong>Ps 22</strong> — "My God, my God, why have you forsaken me?" Jesus quotes from the cross. Describes crucifixion 800+ years before the practice existed: "They have pierced my hands and feet" (22:16), "They divide my garments" (22:18).</p><p><strong>Ps 68</strong> — Divine warrior marching from Sinai with "tens of thousands of holy ones." Paul quotes 68:18 in Eph 4:8 for Christ's ascension gifts.</p>''',
        "key_claim": 'Psalm 82 is the Rosetta Stone of the divine council — YHWH stands in the assembly of El, judges the corrupt elohim assigned to nations under Deut 32:8, and sentences them to die like men, while Psalm 110 establishes the Melchizedekian priesthood that bypasses the entire Levitical system.',
        "contested_words": [{'word': 'elohim', 'hebrew': 'אֱלֹהִים', 'issue': "Ps 82:1, 6 — 'God stands in the assembly of God; among the gods he judges.' Same word for YHWH and the council members. Most translations obscure this.", 'severity': 'CRITICAL'}, {'word': 'adat-el', 'hebrew': 'עֲדַת אֵל', 'issue': "'Assembly of God/El' (82:1) — the divine council itself. Not a metaphor for human judges but the actual heavenly assembly.", 'severity': 'CRITICAL'}, {'word': 'bene elyon', 'hebrew': 'בְּנֵי עֶלְיוֹן', 'issue': "'Sons of the Most High' (82:6) — the allotted elohim of Deut 32:8. Jesus quotes this in John 10:34.", 'severity': 'CRITICAL'}, {'word': 'Adoni', 'hebrew': 'אֲדֹנִי', 'issue': "'My Lord' (110:1) — YHWH speaks to David's Lord. Two distinct divine figures in one verse. Messianic crux.", 'severity': 'CRITICAL'}, {'word': "ka'ari", 'hebrew': 'כָּאֲרִי', 'issue': "'Like a lion' vs. 'they pierced' (22:16) — MT reads ka'ari ('like a lion'), LXX/DSS support 'pierced' (ka'aru). Crucifixion detail.", 'severity': 'CRITICAL'}, {'word': 'hesed', 'hebrew': 'חֶסֶד', 'issue': 'Covenant faithfulness/loyal love — appears 127 times in Psalms. No single English word captures it.', 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'deuteronomy', 'why': 'Ps 82 is the judicial sequel to Deut 32:8 — the gods given nations are now condemned for their corruption'}, {'target': 'john', 'why': "Jesus quotes Ps 82:6 in John 10:34 to defend his divine claim — 'Is it not written in your Law, I said you are gods?'"}, {'target': 'hebrews', 'why': 'Ps 110:4 (Melchizedek priesthood) is the foundation of Hebrews 5-7; Ps 2:7 quoted in Heb 1:5'}, {'target': 'genesis', 'why': 'Melchizedek first appears in Gen 14:18; Ps 110 picks up the thread and makes it eternal and messianic'}, {'target': 'daniel', 'why': 'The territorial princes of Dan 10 are the same corrupt elohim being judged in Ps 82'}, {'target': 'revelation', 'why': "The throne room worship of Rev 4-5 echoes the Psalms' vision of cosmic praise; Ps 2 fulfilled in Rev 19"}, {'target': 'acts', 'why': "Ps 2:7 applied to the resurrection (Acts 13:33); Ps 16:10 ('you will not let your holy one see corruption') quoted by Peter at Pentecost"}, {'target': 'ephesians', 'why': "Ps 68:18 ('he ascended on high, leading captives') quoted in Eph 4:8 for Christ's ascension gifts"}],
        "what_it_doesnt_say": ["Who the 'gods' of Psalm 82 are specifically — the text assumes the audience knows the Deut 32:8 framework", "How the elohim will 'die like men' — divine beings sentenced to mortality with no mechanism explained", 'Why the Psalter is arranged in five books — the structure mirrors the Torah but no editorial note explains why', 'The identity of many psalm authors — 50 psalms have no attributed author'],
        "unusual_characters": [{'name': 'Melchizedek', 'ref': '110:4', 'detail': 'Eternal priest-king order that supersedes Levi. Only two OT mentions (Gen 14, Ps 110) but becomes central to NT Christology.', 'connections': ['genesis', 'hebrews']}, {'name': 'The corrupt elohim', 'ref': '82:1-7', 'detail': 'Divine council members judged for failing to protect the vulnerable. Sentenced to die like mortals.', 'connections': ['deuteronomy', 'daniel', '1enoch']}, {'name': 'The suffering righteous one', 'ref': '22:1', 'detail': 'Describes crucifixion details 800+ years before the practice existed. Jesus quotes the opening line from the cross.', 'connections': ['matthew', 'mark', 'john']}],
        "patterns": ['Five-book structure mirrors the Torah: Book I (1-41), II (42-72), III (73-89), IV (90-106), V (107-150) — each ending with a doxology', 'Royal psalms (2, 18, 20, 21, 45, 72, 89, 101, 110, 132, 144) trace the Davidic covenant from promise to apparent failure (Ps 89) to eschatological fulfillment', 'Hallel collections: Egyptian Hallel (113-118, Passover), Great Hallel (120-136), Final Hallel (146-150) — the Psalter builds toward unending praise', 'Lament-to-praise arc: most lament psalms turn to trust/praise before ending, modeling the faith journey from suffering to hope'],
        "mistranslations": [{'english': 'God/judges', 'original': 'elohim', 'issue': "Ps 82 — translating elohim as 'judges' or 'rulers' hides the divine council entirely. These are divine beings, not humans."}, {'english': 'like a lion they pierced', 'original': "ka'ari/ka'aru", 'issue': "Ps 22:16 — MT reads 'like a lion' but DSS/LXX support 'pierced.' The difference between an animal metaphor and a crucifixion prophecy."}, {'english': 'my Lord', 'original': 'Adoni', 'issue': "Ps 110:1 — English 'Lord' hides the two-Yahweh theology. YHWH speaks to David's Adoni, a second divine figure."}],
    },
    {
        "id": 'proverbs',
        "section": 'wisdom-books',
        "title": 'Book 20: Proverbs (Mishlei)',
        "themes": 'TYPE HOLY',
        "era_count": 3,
        "chapters": 31,
        "grade": 'A',
        "meta_text": '3 era files &middot; 31 chapters &middot; Grade: A',
        "body_html": '''<p><strong>LADY WISDOM — PRE-CREATION FIGURE</strong> <span class="badge badge-critical">CRITICAL</span> — Prov 8:22-31: Wisdom personified, present at creation. "YHWH possessed me (qanani) at the beginning." NT identifies her with Christ: John 1:1-3 (Logos at creation), Col 1:15-17, 1 Cor 1:24 (Christ IS the wisdom of God).</p><p><strong>Contested word</strong>: qanani (8:22) — "possessed me" or "created me"? The Arian controversy hinged on this. <span class="badge badge-critical">CRITICAL</span></p><p><strong>TWO WAYS</strong> — Lady Wisdom (life) vs. Woman Folly (death). Connects to Deut 30 ("choose life"), Didache, Matt 7:13-14.</p><p><strong>ESHET CHAYIL</strong> (31:10-31) — "Woman of Valor." Acrostic poem (22 Hebrew letters). Not domestic drudgery but strength, business acumen, wisdom. Many read her as incarnate Lady Wisdom.</p>''',
        "key_claim": "Lady Wisdom in Proverbs 8:22-31 is a pre-creation figure present when YHWH laid the foundations of the earth — the NT identifies her with Christ (John 1:1-3, Col 1:15-17, 1 Cor 1:24), making this the OT's clearest portrait of the pre-incarnate Son.",
        "contested_words": [{'word': 'qanani', 'hebrew': 'קָנָנִי', 'issue': "'Possessed me' or 'created me' (8:22)? The Arian controversy hinged on this. If 'created,' Wisdom/Christ is a creature; if 'possessed,' eternally with God.", 'severity': 'CRITICAL'}, {'word': 'chokmah', 'hebrew': 'חָכְמָה', 'issue': "Wisdom — feminine noun personified as a woman. Pre-creation figure who 'delights in the sons of men' (8:31). Christological implications.", 'severity': 'CRITICAL'}, {'word': 'eshet chayil', 'hebrew': 'אֵשֶׁת חַיִל', 'issue': "'Woman of valor' (31:10) — chayil means military strength/wealth/capability. Not domestic virtue but warrior-strength. Many read her as incarnate Lady Wisdom.", 'severity': 'MAJOR'}, {'word': 'musar', 'hebrew': 'מוּסָר', 'issue': "'Discipline/instruction' (1:2) — includes correction, training, chastening. Not punishment but formation. Shapes the book's entire pedagogy.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'john', 'why': 'John 1:1-3 (Logos at creation) echoes Prov 8:22-31 (Wisdom at creation) — the same pre-creation figure in both'}, {'target': 'colossians', 'why': "Col 1:15-17 ('by him all things were created') maps directly onto Wisdom's role in Prov 8:27-30"}, {'target': '1corinthians', 'why': "'Christ the power of God and the WISDOM of God' (1 Cor 1:24) — Paul explicitly identifies Christ with chokmah"}, {'target': 'deuteronomy', 'why': "The Two Ways (Lady Wisdom vs. Woman Folly) echoes Deut 30:15-19 ('I set before you life and death — choose life')"}, {'target': 'ecclesiastes', 'why': "Ecclesiastes tests Proverbs' wisdom framework 'under the sun' and finds it insufficient without the fear of God"}, {'target': 'james', 'why': "James 3:17 describes wisdom 'from above' — picking up Proverbs' Lady Wisdom as heavenly origin"}],
        "what_it_doesnt_say": ['Whether Lady Wisdom is a person, a hypostasis, or a literary device — the text personifies but never explains the ontology', "How the 'Two Ways' relate to the tree of life and tree of knowledge — the Eden parallel is never made explicit", "Who collected and arranged the proverbs — editorial hands are acknowledged (25:1 'men of Hezekiah') but the process is obscure", "Why Agur (ch. 30) and Lemuel's mother (ch. 31) are included — non-Solomonic material with no explanation"],
        "unusual_characters": [{'name': 'Lady Wisdom', 'ref': '8:1', 'detail': "Pre-creation figure present when YHWH founded the earth. 'Rejoicing before him always, delighting in the sons of men.' NT identifies her with Christ.", 'connections': ['john', 'colossians', '1corinthians']}, {'name': 'Woman Folly', 'ref': '9:13', 'detail': "Anti-Wisdom. Loud, seductive, leading to Sheol. The counterfeit that mimics Wisdom's invitation.", 'connections': ['revelation']}, {'name': 'Eshet Chayil', 'ref': '31:10', 'detail': 'Woman of valor — 22-verse acrostic. Strength, business acumen, wisdom. Many scholars read her as Lady Wisdom incarnate in daily life.', 'connections': ['ruth']}, {'name': 'Agur son of Jakeh', 'ref': '30:1', 'detail': "Non-Israelite sage. Asks: 'Who has ascended to heaven and come down?' (30:4) — echoed in John 3:13.", 'connections': ['john']}],
        "patterns": ['Acrostic structure: Eshet Chayil (31:10-31) uses all 22 Hebrew letters — the alphabet of wisdom completing the book', "Two invitations: Lady Wisdom (9:1-6) and Woman Folly (9:13-18) both say 'Come eat my food' — identical form, opposite destinations (life vs. Sheol)", "Numerical sayings (30:15-31): 'Three things... four things...' — a counting pattern unique in biblical literature", "Solomon-to-Solomon frame: begins with Solomon's proverbs (1:1), ends with a non-Solomonic woman who embodies everything Solomon taught but failed to live"],
        "mistranslations": [{'english': 'created me', 'original': 'qanani', 'issue': "Prov 8:22 — 'created' imports Arian theology. Hebrew qanah more commonly means 'possessed/acquired,' preserving Wisdom's eternal nature."}, {'english': 'virtuous woman', 'original': 'eshet chayil', 'issue': 'Domesticates a word (chayil) that means military valor, wealth, and capability — reducing a warrior-sage to a housewife.'}, {'english': 'fear', 'original': "yir'ah", 'issue': "'Fear of the LORD' — English implies terror. Hebrew yir'ah includes awe, reverence, and covenant loyalty. It is relational, not cowering."}],
    },
    {
        "id": 'ecclesiastes',
        "section": 'wisdom-books',
        "title": 'Book 21: Ecclesiastes (Qoheleth)',
        "themes": '',
        "era_count": 2,
        "chapters": 12,
        "grade": 'A',
        "meta_text": '2 era files &middot; 12 chapters &middot; Grade: A',
        "body_html": '''<p><strong>HEBEL — VAPOR, NOT VANITY</strong> <span class="badge badge-critical">CRITICAL</span> — "Vanity of vanities (havel havalim)" — hebel literally = breath/vapor. Transient, fleeting, incomprehensible. 38 occurrences. NOT nihilism but honest observation: everything "under the sun" is fleeting. Rom 8:20: creation "subjected to futility (mataiotes)" = same concept.</p><p><strong>"UNDER THE SUN"</strong> — tachath hashamesh (29 times). This frames the investigation as earthly observation. The divine council operates "above the sun." Ecclesiastes is theology from the ground floor.</p><p><strong>THE VERDICT</strong> — "Fear God and keep his commandments" (12:13). The "under the sun" perspective is NOT the final word.</p>''',
        "key_claim": "Hebel does not mean 'vanity' but 'vapor/breath' — Ecclesiastes is not nihilism but an honest investigation of life 'under the sun' (the earthly plane) that concludes the only stable reality is the fear of God, pointing beyond human wisdom to divine encounter.",
        "contested_words": [{'word': 'hebel', 'hebrew': 'הֶבֶל', 'issue': "'Vanity' is wrong — hebel literally means breath/vapor. Transient, fleeting, incomprehensible. 38 occurrences. Same word as Abel's name.", 'severity': 'CRITICAL'}, {'word': 'tachath hashamesh', 'hebrew': 'תַּחַת הַשָּׁמֶשׁ', 'issue': "'Under the sun' (29 times) — frames the entire investigation as earthly, ground-level observation. The divine council operates ABOVE the sun.", 'severity': 'CRITICAL'}, {'word': 'Qoheleth', 'hebrew': 'קֹהֶלֶת', 'issue': "'Preacher' or 'Assembler' — from qahal (assembly). One who gathers and addresses the assembly. Not a name but a title.", 'severity': 'MAJOR'}, {'word': 'yitron', 'hebrew': 'יִתְרוֹן', 'issue': "'Profit/gain' (1:3) — commercial term. 'What yitron does a person have for all their toil under the sun?' The question is economic.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'romans', 'why': "Rom 8:20 ('creation subjected to futility/mataiotes') is the Greek equivalent of hebel — Paul reads the cosmos through Ecclesiastes' lens"}, {'target': 'proverbs', 'why': "Ecclesiastes stress-tests Proverbs' wisdom framework and finds it insufficient without the 'fear of God' conclusion"}, {'target': 'genesis', 'why': "hebel = Abel's name (Gen 4:2). The first human death is named 'vapor' — Ecclesiastes' theme embedded in Genesis from the start"}, {'target': 'job', 'why': 'Both wrestle with the same question: does righteous living guarantee good outcomes? Both answer no — but from different angles'}, {'target': 'james', 'why': "James 4:14 ('What is your life? A mist/vapor') echoes Ecclesiastes' hebel theology directly"}],
        "what_it_doesnt_say": ['Who Qoheleth actually is — the text implies Solomon but never names him after 1:1', "Whether the 'under the sun' limitation is deliberate literary framing or genuine philosophical boundary", 'Why this book is canonical — the rabbis debated whether to exclude it; no explanation for its inclusion is given', "What happens after death — 3:21 asks 'who knows?' and 12:7 says the spirit returns to God, but no details"],
        "unusual_characters": [{'name': 'Qoheleth', 'ref': '1:1', 'detail': "The Assembler — implied to be Solomon but never named after the superscription. Speaks from experience of having 'everything' and finding it hebel.", 'connections': ['1kings']}],
        "patterns": ['Hebel refrain: 38 occurrences of hebel create a drumbeat of transience that structures the entire book', "'Under the sun' frame (29 times): every observation is explicitly bounded to the earthly plane, implying there IS something above the sun", "Enjoy-life refrains (2:24, 3:12-13, 3:22, 5:18-20, 8:15, 9:7-10): punctuate the investigation with permission to receive life as God's gift", "Envelope structure: 1:2 ('hebel of hebels') and 12:8 ('hebel of hebels') frame the entire investigation, with the editorial verdict (12:13-14) standing outside"],
        "mistranslations": [{'english': 'vanity', 'original': 'hebel', 'issue': "KJV's 'vanity' imports moral emptiness. Hebrew hebel means vapor/breath — something real but transient and ungraspable. Not worthless, but fleeting."}, {'english': 'meaningless', 'original': 'hebel', 'issue': "NIV's 'meaningless' is worse than 'vanity' — implies nihilism that the text explicitly rejects in 12:13"}, {'english': 'Preacher', 'original': 'Qoheleth', 'issue': "Neither preacher nor teacher — Qoheleth means 'one who assembles/gathers,' from the root qahal (assembly). A convener, not a sermonizer."}],
    },
    {
        "id": 'song',
        "section": 'wisdom-books',
        "title": 'Book 22: Song of Solomon (Shir HaShirim)',
        "themes": 'COV',
        "era_count": 2,
        "chapters": 8,
        "grade": 'A+',
        "meta_text": '2 era files &middot; 8 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>LOVE AS DIVINE FIRE</strong> <span class="badge badge-critical">CRITICAL</span> — 8:6: "Love is strong as death... its flashes are flashes of fire, the very flame of YAH (shalhevet-yah)." The ONLY possible divine name in the book. Love's source is God himself. "Many waters cannot quench love."</p><p><strong>GARDEN AS EDEN RESTORED</strong> — The lovers are in the garden. Nakedness without shame. What was lost in Genesis 3 is glimpsed here. Allegorically: YHWH's love for Israel / Christ's love for the church (Eph 5:25-32).</p><p>Rabbi Akiva: "All the ages are not worth the day Song of Songs was given to Israel. All Writings are holy; Song of Songs is the Holy of Holies."</p></div></div>

<!-- MAJOR PROPHETS -->''',
        "key_claim": "Song of Solomon 8:6 contains the only possible divine name in the book — shalhevet-yah ('flame of YAH') — revealing that the source of love's invincible power is God himself, and the garden imagery throughout restores what was lost in Eden's fall.",
        "contested_words": [{'word': 'shalhevet-yah', 'hebrew': 'שַׁלְהֶבֶתְיָה', 'issue': "'Flame of YAH' (8:6) — is -yah a divine name suffix or just an intensifier ('mighty flame')? If divine, this is the book's only God-reference.", 'severity': 'CRITICAL'}, {'word': 'dodim', 'hebrew': 'דֹּדִים', 'issue': "'Lovemaking/caresses' — explicit erotic language throughout. The same root (dod) as David's name. Love as both physical and covenantal.", 'severity': 'MAJOR'}, {'word': 'Shulammite', 'hebrew': 'שׁוּלַמִּית', 'issue': "'The Shulammite' (6:13) — feminine of Solomon (Shelomoh)? From Shunem? The female counterpart to the king.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'genesis', 'why': 'Garden imagery (4:12-5:1) restores Eden — lovers in the garden, nakedness without shame, what Gen 3 destroyed'}, {'target': 'ephesians', 'why': 'Eph 5:25-32 reads marriage as Christ/church allegory — Song of Solomon provides the OT foundation'}, {'target': 'revelation', 'why': 'The marriage supper of the Lamb (Rev 19:7-9) is the eschatological fulfillment of the love Song celebrates'}, {'target': 'hosea', 'why': 'Both use marriage as covenant metaphor — Hosea shows the broken version, Song shows the ideal'}, {'target': 'psalms', 'why': "Ps 45 is a royal wedding psalm with similar imagery — the king desires the bride's beauty"}],
        "what_it_doesnt_say": ['God is never explicitly named — if shalhevet-yah is just an intensifier, there is zero divine reference in the entire book', 'Whether the relationship is pre-marital or marital — the timeline is ambiguous and the boundaries unclear', 'Why this book is canonical — no prophetic formula, no covenant language, no Torah', 'Whether the allegory (YHWH-Israel / Christ-Church) was original intent or later interpretation'],
        "unusual_characters": [{'name': 'The Shulammite', 'ref': '6:13', 'detail': "Feminine counterpart to Solomon. Dark-skinned ('black and beautiful,' 1:5). The only woman in Scripture who pursues her beloved with equal agency.", 'connections': ['ruth', 'proverbs']}, {'name': 'The Daughters of Jerusalem', 'ref': '1:5', 'detail': 'Chorus figure — the audience within the poem. They witness and respond to the love story.', 'connections': []}],
        "patterns": ["Adjuration refrain: 'Do not stir up or awaken love until it pleases' (2:7, 3:5, 8:4) — love has its own timing and cannot be forced", 'Seeking-and-finding: the beloved is lost and found repeatedly (3:1-4, 5:6-8) — love involves absence, longing, and reunion', "Garden-to-garden arc: the enclosed garden (4:12) opens to 'let my beloved come to his garden' (4:16) — from protection to invitation", "Military imagery for love: 'terrible as an army with banners' (6:4, 10) — love is not gentle but fierce, a force that conquers"],
        "mistranslations": [{'english': 'a mighty flame', 'original': 'shalhevet-yah', 'issue': 'Translating -yah as merely an intensifier rather than the divine name hides the only possible God-reference in the book.'}, {'english': 'dark', 'original': 'shechorah', 'issue': "'I am black/dark and beautiful' (1:5) — many translations add 'but' (dark BUT beautiful), importing a contrast the Hebrew does not make."}],
    },
    {
        "id": 'isaiah',
        "section": 'major-prophets',
        "title": 'Book 23: Isaiah (Yeshayahu)',
        "themes": 'SEED DC KING REMNANT EXILE NATIONS HOLY RIV SPIRIT',
        "era_count": 6,
        "chapters": 66,
        "grade": 'A+',
        "meta_text": '6 era files &middot; 66 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>THE SUFFERING SERVANT</strong> (52:13-53:12) <span class="badge badge-critical">CRITICAL</span> — "He was pierced for our transgressions, crushed for our iniquities." The most detailed messianic prophecy in the OT. DSS Great Isaiah Scroll (1QIsa<sup>a</sup>) confirms the text.</p><p><strong>DIVINE COUNCIL THRONE ROOM</strong> (ch. 6) — "I saw the Lord seated on a throne, high and exalted... seraphim above him." Isaiah sees the divine council in session. "Holy, holy, holy is YHWH of hosts." John 12:41 says Isaiah saw JESUS' glory.</p><p><strong>HELEL BEN SHACHAR</strong> (14:12-14) <span class="badge badge-critical">CRITICAL</span> — "How you are fallen from heaven, O Day Star (Helel), son of Dawn (ben Shachar)!" Behind the king of Babylon: a divine council rebel who said "I will make myself like the Most High." Combined with Ezek 28: the nachash/Satan backstory.</p><p><strong>VIRGIN BIRTH</strong> (7:14) — almah (young woman) vs. parthenos (LXX: virgin). Matthew 1:23 quotes this for Jesus' birth. <span class="badge badge-critical">CRITICAL</span></p><p><strong>NEW EXODUS</strong> (chs. 40-55) — "In the wilderness prepare the way of YHWH." Return from Babylon as a new exodus. John the Baptist fulfills this (Mark 1:3).</p>''',
        "key_claim": "Isaiah contains both the most detailed messianic prophecy (the Suffering Servant of 52:13-53:12) and the divine council rebel backstory (Helel ben Shachar in 14:12-14) — the entire cosmic drama from Satan's fall to the Messiah's atoning death in one book.",
        "contested_words": [{'word': 'almah', 'hebrew': 'עַלְמָה', 'issue': "'Young woman' (7:14) vs. LXX parthenos ('virgin'). Matthew 1:23 follows the LXX. The virgin birth hinges on this word.", 'severity': 'CRITICAL'}, {'word': 'Helel ben Shachar', 'hebrew': 'הֵילֵל בֶּן שָׁחַר', 'issue': "'Day Star, son of Dawn' (14:12) — behind the king of Babylon: a divine council rebel. Combined with Ezek 28: the nachash/Satan backstory.", 'severity': 'CRITICAL'}, {'word': 'ebed YHWH', 'hebrew': 'עֶבֶד יהוה', 'issue': "'Servant of YHWH' — four Servant Songs (42:1-9, 49:1-7, 50:4-9, 52:13-53:12). Individual messiah or collective Israel? Both?", 'severity': 'CRITICAL'}, {'word': 'mashiach', 'hebrew': 'מָשִׁיחַ', 'issue': "Cyrus called YHWH's 'anointed' (mashiach, 45:1) — a PAGAN king given the messianic title. Shatters ethnic exclusivism.", 'severity': 'CRITICAL'}, {'word': 'seraphim', 'hebrew': 'שְׂרָפִים', 'issue': "'Burning ones' (6:2) — divine council beings with six wings. From saraph (to burn). Same root as the nachash seraph serpents (Num 21:6).", 'severity': 'MAJOR'}, {'word': "go'el", 'hebrew': 'גֹּאֵל', 'issue': "YHWH as kinsman-redeemer of Israel (41:14, 43:14, 44:6). The go'el concept applied to God himself.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'ezekiel', 'why': 'Isa 14:12-14 (Helel) + Ezek 28:11-19 (Prince of Tyre) together reconstruct the full nachash/Satan origin story'}, {'target': 'matthew', 'why': 'Virgin birth (Matt 1:23/Isa 7:14), Galilee prophecy (Matt 4:15-16/Isa 9:1-2), Servant Songs throughout the passion narrative'}, {'target': 'mark', 'why': "Mark 1:3 ('voice crying in the wilderness') directly quotes Isa 40:3 — the New Exodus begins with John the Baptist"}, {'target': 'acts', 'why': "Ethiopian eunuch reads Isa 53 (Acts 8:32-35); Paul's commission echoes the Servant calling (Acts 13:47/Isa 49:6)"}, {'target': 'romans', 'why': 'Rom 10:16 quotes Isa 53:1; Rom 9:27-29 quotes the remnant theology of Isa 10:22-23'}, {'target': 'revelation', 'why': "Isa 6 throne room -> Rev 4; new heavens and new earth (Isa 65:17) -> Rev 21:1; Babylon's fall (Isa 13-14) -> Rev 17-18"}, {'target': '1peter', 'why': "1 Pet 2:22-25 applies the Suffering Servant (Isa 53) directly to Christ's atoning work"}],
        "what_it_doesnt_say": ["Whether chapters 40-66 are by the same author as 1-39 — the so-called 'Two Isaiahs' debate; the text presents a unified voice", 'How the Suffering Servant can be both Israel (49:3) AND someone who restores Israel (49:5-6) — the paradox is never resolved within Isaiah', 'What the seraphim look like beyond their wings — six wings but the face and body are never described', "How Cyrus would know YHWH's name — 45:4 says 'I name you, though you do not know me'"],
        "unusual_characters": [{'name': 'Helel ben Shachar', 'ref': '14:12', 'detail': "Day Star, son of Dawn — a divine being who fell from heaven after claiming 'I will make myself like the Most High.' Behind the king of Babylon: the nachash backstory.", 'connections': ['ezekiel', 'revelation', 'luke']}, {'name': 'The Suffering Servant', 'ref': '52:13', 'detail': 'Pierced for transgressions, crushed for iniquities. Bore the sin of many. The most detailed messianic prophecy in the OT.', 'connections': ['matthew', 'mark', 'acts', '1peter']}, {'name': 'Cyrus', 'ref': '45:1', 'detail': "A pagan Persian king called YHWH's 'anointed' (mashiach) by name — 150 years before his birth.", 'connections': ['ezra', 'daniel', '2chronicles']}, {'name': 'Seraphim', 'ref': '6:2', 'detail': "Burning ones with six wings — divine council beings who cry 'Holy, holy, holy.' Same root as the fiery serpents (nachash seraph) of Numbers 21.", 'connections': ['numbers', 'revelation']}],
        "patterns": ['Three-part structure mirrors the exile-return-restoration arc: judgment (1-39), comfort (40-55), future glory (56-66) — 66 chapters parallel the 66 books of the Bible', 'Four Servant Songs (42:1-9, 49:1-7, 50:4-9, 52:13-53:12) trace a progressive revelation: calling -> mission -> suffering -> atoning death and vindication', 'Remnant theology: the stump of Jesse (11:1), the holy seed in the stump (6:13), a remnant shall return (shear-jashub, 7:3 — Isaiah names his son this)', "New Exodus motif (chs. 40-55): 'In the wilderness prepare the way of YHWH' — return from Babylon as a second exodus that surpasses the first"],
        "mistranslations": [{'english': 'Lucifer', 'original': 'Helel ben Shachar', 'issue': "Latin Vulgate's 'Lucifer' became a proper name for Satan. Hebrew means 'Shining One, son of Dawn' — a divine council title, not a personal name."}, {'english': 'virgin/young woman', 'original': 'almah', 'issue': "Isa 7:14 — almah means 'young woman of marriageable age.' LXX chose parthenos (virgin). The translation choice carries enormous theological weight."}, {'english': 'the LORD', 'original': 'YHWH', 'issue': "Isaiah uses YHWH over 400 times. English 'LORD' hides the personal name behind a title, especially critical in passages about YHWH's unique identity."}],
    },
    {
        "id": 'jeremiah',
        "section": 'major-prophets',
        "title": 'Book 24: Jeremiah (Yirmeyahu)',
        "themes": 'COV RIV EXILE REBEL SEED',
        "era_count": 5,
        "chapters": 52,
        "grade": 'A',
        "meta_text": '5 era files &middot; 52 chapters &middot; Grade: A',
        "body_html": '''<p><strong>THE NEW COVENANT</strong> (31:31-34) <span class="badge badge-critical">CRITICAL</span> — "I will make a new covenant... I will put my Torah within them, and I will write it on their hearts." The Deut 30:6 promise developed. Quoted in full in Hebrews 8:8-12 — the longest OT quotation in the NT.</p><p><strong>THE WEEPING PROPHET</strong> — Called before birth (1:5). Told not to marry (16:2). Beaten, imprisoned, thrown in a cistern. Witnesses Jerusalem's destruction. The costliest prophetic calling in the OT.</p><p><strong>DIVINE COUNCIL ACCESS</strong> (23:18, 22) — "Who has stood in the council (sod) of YHWH?" False prophets have NOT stood in the sod. True prophets HAVE. Sod = the divine council's deliberation room.</p>''',
        "key_claim": 'Jeremiah 31:31-34 announces the new covenant — Torah written on hearts instead of stone — which Hebrews 8:8-12 quotes in full as the longest OT citation in the NT, establishing that the old covenant was always designed to be replaced by internal transformation.',
        "contested_words": [{'word': 'berit chadashah', 'hebrew': 'בְּרִית חֲדָשָׁה', 'issue': "'New covenant' (31:31) — the ONLY place in the OT that uses this exact phrase. Foundation of NT covenant theology.", 'severity': 'CRITICAL'}, {'word': 'sod', 'hebrew': 'סוֹד', 'issue': "'Council' (23:18, 22) — 'Who has stood in the sod of YHWH?' The divine council's deliberation room. False prophets lack sod access.", 'severity': 'CRITICAL'}, {'word': 'shub', 'hebrew': 'שׁוּב', 'issue': "'Return/repent' — Jeremiah's key verb. 111 occurrences. Both physical return from exile and spiritual turning. The book's central imperative.", 'severity': 'MAJOR'}, {'word': 'riv', 'hebrew': 'רִיב', 'issue': "Covenant lawsuit — Jeremiah as covenant prosecutor bringing YHWH's case against a faithless nation.", 'severity': 'MAJOR'}, {'word': 'topheth', 'hebrew': 'תֹּפֶת', 'issue': "'Topheth' (7:31-32) — the Valley of Hinnom where children were burned for Molech. Becomes ge-hinnom = Gehenna.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'hebrews', 'why': 'Heb 8:8-12 quotes Jer 31:31-34 in full — the longest OT quotation in the NT. The new covenant supersedes the old.'}, {'target': 'deuteronomy', 'why': "Jer 31:33 ('write it on their hearts') fulfills the Deut 30:6 promise of heart circumcision — what Moses foresaw, Jeremiah names"}, {'target': 'ezekiel', 'why': "Ezek 36:26-27 ('new heart, new spirit') parallels Jer 31:31-34 — both prophets independently announce the same internal transformation"}, {'target': 'luke', 'why': "Jesus at the Last Supper: 'This cup is the new covenant in my blood' (Luke 22:20) — directly invoking Jer 31:31"}, {'target': 'lamentations', 'why': 'Lamentations is the aftermath of what Jeremiah prophesied — the covenant curses of Deut 28 realized in real time'}, {'target': 'daniel', 'why': "Daniel reads Jeremiah's 70-year prophecy (Dan 9:2, cf. Jer 25:11-12) and receives the 70-weeks revelation in response"}],
        "what_it_doesnt_say": ["How the new covenant differs mechanically from the old — 'write it on their hearts' is metaphorical with no procedural explanation", 'Why God chose Jeremiah before birth (1:5) — pre-natal calling with no rationale given', "Who the 'Righteous Branch' (23:5-6) is — messianic title with no identification in the text", 'Why Jeremiah was forbidden to marry (16:2) — the command is given but the symbolic logic is only implied'],
        "unusual_characters": [{'name': 'Baruch', 'ref': '36:4', 'detail': "Jeremiah's scribe who wrote the scroll that the king burned. Preserved the prophet's words against royal destruction.", 'connections': []}, {'name': 'Ebed-melech', 'ref': '38:7', 'detail': "Ethiopian eunuch who rescues Jeremiah from the cistern. A foreigner saves the prophet when Israel won't.", 'connections': ['acts']}, {'name': 'Hananiah', 'ref': '28:1', 'detail': "False prophet who breaks Jeremiah's yoke and says exile will end in two years. Dies within the year as Jeremiah predicted.", 'connections': []}],
        "patterns": ["Confessions of Jeremiah (11:18-12:6, 15:10-21, 17:14-18, 18:18-23, 20:7-18): raw prophetic anguish unmatched in Scripture — 'You deceived me, YHWH'", "Scroll destruction and rewriting (ch. 36): the king burns the scroll, God commands a second with 'many similar words added' — the Word cannot be destroyed", 'Covenant lawsuit (riv) structure: accusation (chs. 2-6), warning (7-20), judgment (21-29), hope (30-33), narrative of fall (34-45), oracles against nations (46-51)', 'Potter and clay (18:1-12): God reshapes nations — sovereignty and conditionality held in tension'],
        "mistranslations": [{'english': 'the LORD', 'original': 'YHWH', 'issue': "Jeremiah uses YHWH's personal name in intimate dialogue — 'LORD' flattens the covenant relationship into a generic title"}, {'english': 'repent', 'original': 'shub', 'issue': "English 'repent' carries guilt/penance overtones. Hebrew shub means 'turn/return' — directional, not emotional. Come home."}, {'english': 'hell', 'original': 'ge-hinnom/Topheth', 'issue': "The Valley of Hinnom where children were burned (7:31-32) became 'Gehenna.' Understanding the literal horror is essential to Jesus' later use of the term."}],
    },
    {
        "id": 'lamentations',
        "section": 'major-prophets',
        "title": 'Book 25: Lamentations (Eikhah)',
        "themes": 'COV EXILE',
        "era_count": 1,
        "chapters": 5,
        "grade": 'A',
        "meta_text": '1 era file &middot; 5 chapters &middot; Grade: A',
        "body_html": '''<p><strong>COVENANT AFTERMATH</strong> — What Deuteronomy 28 looks like in real time. Five acrostic poems. YHWH described as Israel's ENEMY (2:4-5). Yet at the exact center of the triple acrostic (3:22-23): "The steadfast love (hesed) of YHWH never ceases; they are new every morning; great is your faithfulness (emunah)."</p>''',
        "key_claim": "Lamentations is Deuteronomy 28 in real time — the covenant curses playing out in Jerusalem's destruction — yet at the mathematical center of the triple acrostic (3:22-23) stands the declaration that YHWH's hesed never ceases, making faithfulness the structural heart of devastation.",
        "contested_words": [{'word': 'hesed', 'hebrew': 'חֶסֶד', 'issue': "'Steadfast love' (3:22) — at the center of the book's center. Covenant faithfulness persists even when the covenant has been broken.", 'severity': 'CRITICAL'}, {'word': 'emunah', 'hebrew': 'אֱמוּנָה', 'issue': "'Faithfulness' (3:23) — 'Great is your emunah.' God's reliability even amid his own judgment.", 'severity': 'MAJOR'}, {'word': 'eikhah', 'hebrew': 'אֵיכָה', 'issue': "'How!' (1:1) — the opening cry. Same word God uses in Eden: 'Where are you?' (Gen 3:9, ayyekah). Exile echoes the first exile.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'deuteronomy', 'why': 'Every curse in Lamentations corresponds to Deut 28 covenant curses — siege, famine, cannibalism, exile. The treaty has been enforced.'}, {'target': 'jeremiah', 'why': 'Lamentations is the aftermath of everything Jeremiah warned about — traditionally attributed to Jeremiah himself'}, {'target': 'genesis', 'why': "Eikhah (1:1) echoes ayyekah (Gen 3:9) — Jerusalem's exile mirrors Adam's exile from Eden. Same root word, same devastation."}, {'target': 'psalms', 'why': 'The lament genre in Psalms (22, 44, 74, 79, 137) provides the liturgical framework Lamentations extends into an entire book'}, {'target': 'revelation', 'why': 'The fall of Babylon in Rev 18 uses language and structure echoing Lamentations — cosmic city destruction'}],
        "what_it_doesnt_say": ['Who wrote it — traditionally Jeremiah, but the text is anonymous', "Whether restoration will come — the book ends with 'unless you have utterly rejected us' (5:22), leaving the question open", 'How long the suffering will last — no timeline, no promise of return within the text itself'],
        "unusual_characters": [{'name': 'Daughter Zion', 'ref': '1:6', 'detail': 'Jerusalem personified as a weeping woman — stripped, shamed, abandoned by her lovers (the false allies/gods she trusted).', 'connections': ['hosea', 'ezekiel']}],
        "patterns": ['Acrostic architecture: chapters 1, 2, 4 are 22-verse acrostics (Hebrew alphabet); chapter 3 is a TRIPLE acrostic (66 verses, 3 per letter); chapter 5 has 22 verses but breaks the acrostic — order dissolving', 'hesed at the center: 3:22-23 sits at the mathematical midpoint of the central triple acrostic — faithfulness is structurally embedded at the heart of devastation', "YHWH as enemy: 2:4-5 describes God as Israel's adversary — the most shocking theological reversal in the OT. The protector became the destroyer.", 'Descending hope: each chapter is more despairing until the acrostic itself breaks in ch. 5 — literary form mirrors theological collapse'],
        "mistranslations": [{'english': 'steadfast love', 'original': 'hesed', 'issue': 'No single English word captures hesed — covenant loyalty, faithful love, mercy, kindness all rolled into one. Every translation loses something.'}, {'english': 'How!', 'original': 'eikhah', 'issue': "A mere exclamation in English. In Hebrew it echoes ayyekah (Gen 3:9, 'where are you?') — linking Jerusalem's fall to Eden's fall."}],
    },
    {
        "id": 'ezekiel',
        "section": 'major-prophets',
        "title": 'Book 26: Ezekiel (Yechezkel)',
        "themes": 'DC HOLY PRIEST EXILE KING SPIRIT',
        "era_count": 4,
        "chapters": 48,
        "grade": 'A+',
        "meta_text": '4 era files &middot; 48 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>THE MERKABAH — THRONE CHARIOT</strong> (ch. 1, 10) <span class="badge badge-critical">CRITICAL</span> — Most elaborate divine council throne scene: four living creatures (chayyot) with 4 faces each, wheels within wheels (ophannim) full of eyes, throne of sapphire, "the appearance of the likeness of the glory of YHWH" — triple buffer. They're identified as cherubim in ch. 10. YHWH's throne is MOBILE — not imprisoned in the Temple.</p><p><strong>GLORY DEPARTS AND RETURNS</strong> (10-11, 43) <span class="badge badge-critical">CRITICAL</span> — Kavod (glory) leaves the Temple in stages: cherubim &rarr; threshold &rarr; east gate &rarr; Mount of Olives &rarr; gone. In the new Temple vision (43:1-5), glory returns from the east. Jesus enters Jerusalem from the east.</p><p><strong>PRINCE OF TYRE = NACHASH BACKSTORY</strong> (28:11-19) <span class="badge badge-critical">CRITICAL</span> — "You were in Eden, the garden of God... You were an anointed guardian cherub... blameless until unrighteousness was found in you." Combined with Isaiah 14: the full picture of the first rebellion.</p><p><strong>VALLEY OF DRY BONES</strong> (ch. 37) — National resurrection from exile. Establishes the principle of bodily resurrection &rarr; Daniel 12, NT.</p><p><strong>GOG AND MAGOG</strong> (chs. 38-39) — Eschatological enemy. &rarr; Rev 20:8.</p>''',
        "key_claim": "Ezekiel contains the most elaborate divine council throne scene in Scripture (the Merkabah, ch. 1/10), the nachash origin story (28:11-19), and the glory departure-and-return motif that structures Israel's entire exile-restoration theology — YHWH's throne is MOBILE, not imprisoned in the Temple.",
        "contested_words": [{'word': 'Merkabah', 'hebrew': 'מֶרְכָּבָה', 'issue': "Throne chariot (ch. 1, 10) — wheels within wheels, four living creatures, sapphire throne. Foundation of Jewish mysticism. YHWH's throne is mobile.", 'severity': 'CRITICAL'}, {'word': 'kavod', 'hebrew': 'כָּבוֹד', 'issue': "'Glory' — the visible manifestation of YHWH's presence. Departs the Temple in stages (10-11), returns from the east (43:1-5). The weight of God.", 'severity': 'CRITICAL'}, {'word': 'kerub', 'hebrew': 'כְּרוּב', 'issue': "'Cherub/cherubim' (28:14) — anointed guardian cherub in Eden. NOT the chubby babies of Renaissance art. Throne guardians with terrifying form.", 'severity': 'CRITICAL'}, {'word': 'ophannim', 'hebrew': 'אוֹפַנִּים', 'issue': "'Wheels' (1:15-21) — wheels within wheels, full of eyes. A class of divine council beings, not mere mechanical objects.", 'severity': 'MAJOR'}, {'word': 'chayyot', 'hebrew': 'חַיּוֹת', 'issue': "'Living creatures' (1:5) — four faces (human, lion, ox, eagle), four wings. Identified as cherubim in ch. 10. Throne bearers.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'isaiah', 'why': 'Isa 14:12-14 (Helel/Satan) + Ezek 28:11-19 (guardian cherub in Eden) together reconstruct the full first rebellion narrative'}, {'target': 'genesis', 'why': 'Ezek 28:13-15 places the guardian cherub IN Eden — filling the gap Genesis 3 leaves about who the nachash was before the fall'}, {'target': 'revelation', 'why': "The four living creatures of Rev 4:6-8 directly parallel Ezekiel's chayyot; Gog and Magog (Ezek 38-39) reappear in Rev 20:8"}, {'target': 'daniel', 'why': "Daniel's throne scene (Dan 7:9-14) shares the same divine council throne room Ezekiel describes — thrones, fire, the Ancient of Days"}, {'target': 'matthew', 'why': "Jesus enters Jerusalem from the east (Matt 21:1) — the same direction from which Ezekiel's kavod returns to the Temple (43:1-4)"}, {'target': 'john', 'why': "John 12:41 says Isaiah saw Jesus' glory — Ezekiel's kavod theology provides the framework for the incarnation of divine glory"}],
        "what_it_doesnt_say": ["What the cherub did wrong in Eden (28:15) — 'unrighteousness was found in you' with no specifics given", 'Whether the new Temple vision (chs. 40-48) is literal, symbolic, or eschatological — the most debated section of Ezekiel', "How dry bones can live (37:3) — Ezekiel's answer is 'O Lord GOD, you know,' refusing to speculate on resurrection mechanics", 'Why the glory departed in stages rather than all at once — the lingering departure suggests reluctance but the text never says so'],
        "unusual_characters": [{'name': 'The guardian cherub', 'ref': '28:14', 'detail': 'Anointed cherub in Eden, adorned with precious stones, blameless until unrighteousness was found. The nachash/Satan before the fall.', 'connections': ['genesis', 'isaiah', 'revelation']}, {'name': 'The chayyot', 'ref': '1:5', 'detail': 'Four living creatures with four faces each — human, lion, ox, eagle. Throne bearers identified as cherubim in ch. 10.', 'connections': ['revelation', 'isaiah']}, {'name': 'Gog of Magog', 'ref': '38:2', 'detail': 'Eschatological enemy from the north. An anti-divine-council figure who attacks restored Israel. Reappears in Rev 20:8.', 'connections': ['revelation']}, {'name': 'The son of man (ben adam)', 'ref': '2:1', 'detail': "God's address to Ezekiel — 'son of man' (ben adam) used 93 times. Emphasizes human frailty before divine majesty.", 'connections': ['daniel', 'matthew']}],
        "patterns": ['Glory departure in stages: cherubim -> threshold -> east gate -> Mount of Olives -> gone (10:4, 10:18-19, 11:22-23). Glory returns by the same route in 43:1-5.', 'Sign-acts: Ezekiel performs more enacted prophecies than any other prophet — lying on his side 430 days (4:4-8), eating a scroll (3:1-3), shaving his head (5:1-4)', 'The three-part structure mirrors exile theology: judgment on Israel (1-24), judgment on nations (25-32), restoration (33-48)', "Shepherds and sheep (ch. 34): bad shepherds condemned, YHWH himself becomes shepherd, then appoints 'my servant David' — messianic promise through pastoral imagery"],
        "mistranslations": [{'english': 'cherub', 'original': 'kerub', 'issue': 'English domesticates a terrifying divine being into Renaissance baby art. Biblical cherubim are multi-faced throne guardians with lethal holiness.'}, {'english': 'prince of Tyre', 'original': 'melek Tsor', 'issue': "Ezek 28:12 says 'king' (melek) not 'prince' — the shift from nagid (28:2) to melek (28:12) signals the move from human ruler to divine being behind the throne."}, {'english': 'glory', 'original': 'kavod', 'issue': "English 'glory' is vague and ethereal. Hebrew kavod means 'weight, heaviness, substance' — the tangible, dangerous presence of God."}],
    },
    {
        "id": 'daniel',
        "section": 'major-prophets',
        "title": 'Book 27: Daniel (Daniyyel)',
        "themes": 'DC KING SEED NATIONS SPIRIT',
        "era_count": 3,
        "chapters": 12,
        "grade": 'A+',
        "meta_text": '3 era files &middot; 12 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>THE ANCIENT OF DAYS AND THE SON OF MAN</strong> (ch. 7) <span class="badge badge-critical">CRITICAL</span> — "Thrones were placed, and the Ancient of Days took his seat... with the clouds of heaven there came one like a son of man." The cloud-rider = exclusively divine prerogative. Jesus' self-designation "Son of Man" claims THIS figure. At Mark 14:62, Jesus combines Dan 7:13 + Ps 110:1. The high priest tears his robes — he understands the DIVINE claim.</p><p><strong>TERRITORIAL PRINCES</strong> (ch. 10) <span class="badge badge-critical">CRITICAL</span> — "The prince (sar) of Persia withstood me twenty-one days, but Michael came to help me." Deut 32:8 in action: nations allotted to divine council members who now oppose YHWH's purposes. The invisible war behind visible geopolitics.</p><p><strong>70 WEEKS</strong> (9:24-27) <span class="badge badge-critical">CRITICAL</span> — Messianic timeline. "An anointed one (mashiach) will be cut off (yikkaret)." Most detailed messianic timeline in the OT.</p><p><strong>RESURRECTION</strong> (12:2) — "Many who sleep in the dust shall awake, some to everlasting life." Clearest OT statement of bodily resurrection.</p></div></div>

<!-- MINOR PROPHETS -->''',
        "key_claim": "Daniel 7:13-14 is the christological linchpin — the 'one like a son of man' rides the clouds (exclusively divine prerogative) and receives universal dominion from the Ancient of Days, and when Jesus claims THIS title at his trial (Mark 14:62), the high priest tears his robes because he understands the DIVINE claim.",
        "contested_words": [{'word': 'bar enash', 'hebrew': 'בַּר אֱנָשׁ', 'issue': "'Son of man' (7:13, Aramaic) — a divine figure riding clouds, not just a human title. Jesus' self-designation claims THIS figure.", 'severity': 'CRITICAL'}, {'word': 'Attiq Yomin', 'hebrew': 'עַתִּיק יוֹמִין', 'issue': "'Ancient of Days' (7:9, Aramaic) — YHWH as eternal judge. White hair, throne of fire, books opened. Two distinct divine figures in one vision.", 'severity': 'CRITICAL'}, {'word': 'sar', 'hebrew': 'שַׂר', 'issue': "'Prince' (10:13, 20) — territorial divine beings (Prince of Persia, Prince of Greece). Deut 32:8 allotment in action. Not human rulers but council members.", 'severity': 'CRITICAL'}, {'word': 'mashiach', 'hebrew': 'מָשִׁיחַ', 'issue': "'Anointed one' (9:25-26) — 'cut off' (yikkaret). Most detailed messianic timeline in the OT. The 70-weeks prophecy.", 'severity': 'CRITICAL'}, {'word': 'qaddishin', 'hebrew': 'קַדִּישִׁין', 'issue': "'Holy ones' (7:18, Aramaic) — the 'saints of the Most High' who receive the kingdom. Divine council members? God's people? Both?", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'mark', 'why': 'Mark 14:62 — Jesus combines Dan 7:13 + Ps 110:1 at his trial. The high priest tears his robes because he understands the divine cloud-rider claim.'}, {'target': 'deuteronomy', 'why': 'The territorial princes of Dan 10 are the bene elohim of Deut 32:8 — the same allotted divine beings governing nations'}, {'target': 'revelation', 'why': 'Dan 7 throne room -> Rev 4-5; the four beasts of Dan 7 -> the beast of Rev 13; the Son of Man receives the kingdom in both'}, {'target': 'ezekiel', 'why': 'Dan 7:9-14 shares the divine council throne room with Ezek 1/10 — fire, thrones, the presence of God. Same cosmic courtroom.'}, {'target': 'jeremiah', 'why': "Daniel reads Jeremiah's 70-year prophecy (Dan 9:2, cf. Jer 25:11-12) and receives the 70-weeks revelation in response"}, {'target': 'matthew', 'why': "'Son of Man' is Jesus' most common self-designation in Matthew — every use points back to Dan 7:13-14"}],
        "what_it_doesnt_say": ['Whether the 70 weeks are literal or symbolic — the calculation has generated more interpretive schemes than almost any other prophecy', "How the 'prince of Persia' detained Gabriel for 21 days — a divine council conflict with no military details", "Who the fourth figure in the furnace is (3:25) — 'like a son of the gods' but never identified", "Whether Daniel knew the full implications of his visions — he says 'I was appalled and did not understand' (8:27)"],
        "unusual_characters": [{'name': 'The Son of Man', 'ref': '7:13', 'detail': 'Cloud-rider who receives universal dominion from the Ancient of Days. Cloud-riding is exclusively divine prerogative. Jesus claims this title.', 'connections': ['mark', 'matthew', 'revelation']}, {'name': 'Michael', 'ref': '10:13', 'detail': "Israel's guardian prince (sar) who fights the territorial prince of Persia. The only named archangel in the Protestant canon.", 'connections': ['jude', 'revelation']}, {'name': 'The Prince of Persia', 'ref': '10:13', 'detail': 'Territorial divine being who resists Gabriel for 21 days. Deut 32:8 allotment in visible action — the invisible war behind geopolitics.', 'connections': ['deuteronomy', 'ephesians']}, {'name': 'The fourth in the furnace', 'ref': '3:25', 'detail': "'Like a son of the gods' — divine council member present in the fire. Nebuchadnezzar sees what the three Hebrews trusted.", 'connections': []}],
        "patterns": ['Bilingual structure: chs. 2-7 in Aramaic (the imperial language), chs. 1, 8-12 in Hebrew (the covenant language) — the book itself embodies the tension between empire and faith', "Chiasm in chs. 2-7: dream of statue (2) / fiery furnace (3) / tree dream (4) || writing on wall (5) / lion's den (6) / four beasts vision (7)", 'Four-kingdom progression (2:31-45, 7:1-27): Babylon -> Medo-Persia -> Greece -> Rome — empires rise and fall but the kingdom of God endures', 'Prayer-and-revelation pattern: Daniel prays (2:17-18, 9:3-19), and heaven responds with visions — the divine council responds to covenant faithfulness'],
        "mistranslations": [{'english': 'Son of Man', 'original': 'bar enash', 'issue': "English makes it sound humble ('mere human'). In Dan 7 context, this figure rides clouds (divine prerogative), receives worship, and rules forever — it is a divine title."}, {'english': 'saints', 'original': 'qaddishin', 'issue': "'Saints of the Most High' may include divine council members, not just human believers. The Aramaic qaddishin is used for holy ones/angels elsewhere in Daniel."}, {'english': 'prince', 'original': 'sar', 'issue': "English 'prince' implies human royalty. These are divine territorial beings — the same class as the bene elohim of Deut 32:8, ruling nations."}],
    },
    {
        "id": 'hosea',
        "section": 'minor-prophets-section',
        "title": 'Book 28: Hosea',
        "themes": 'COV RIV SEED NATIONS',
        "era_count": 2,
        "chapters": 14,
        "grade": 'A+',
        "meta_text": '2 era files &middot; 14 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>DIVINE HEARTBREAK</strong> — Hosea's marriage to unfaithful Gomer IS the message. YHWH as heartbroken husband. Hos 11:8: "My heart is overturned within me." Most sustained emotional metaphor in OT.</p><p><strong>Key terms</strong>: hesed (covenant love), zanah (spiritual adultery), da'at Elohim (covenant knowledge — same verb as intimacy), shub (return)</p><p><strong>NT</strong>: Matt 2:15 (Hos 11:1), Matt 9:13 (Hos 6:6 "mercy not sacrifice"), Rom 9:25-26 (Gentile inclusion via Lo-Ammi reversal)</p>''',
        "key_claim": "Hosea's marriage to unfaithful Gomer IS the prophetic message — YHWH as heartbroken husband, Israel as adulterous wife — making this the most sustained and emotionally raw covenant-love metaphor in the OT.",
        "contested_words": [{'word': 'hesed', 'hebrew': 'חֶסֶד', 'issue': "Covenant love/loyalty — the word YHWH demands Israel return to. 'I desire hesed, not sacrifice' (6:6, quoted by Jesus in Matt 9:13).", 'severity': 'CRITICAL'}, {'word': 'zanah', 'hebrew': 'זָנָה', 'issue': "'Play the harlot/commit adultery' — spiritual unfaithfulness described in explicitly sexual terms. Covenant breaking = marital betrayal.", 'severity': 'CRITICAL'}, {'word': "da'at Elohim", 'hebrew': 'דַּעַת אֱלֹהִים', 'issue': "'Knowledge of God' (4:1, 6:6) — da'at is the same verb as sexual intimacy (Gen 4:1). Covenant knowledge is not intellectual but relational.", 'severity': 'MAJOR'}, {'word': 'shub', 'hebrew': 'שׁוּב', 'issue': "'Return' — Hosea's central imperative. Both physical return from exile and spiritual turning back to YHWH.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'matthew', 'why': "Matt 2:15 ('Out of Egypt I called my son') quotes Hos 11:1; Matt 9:13 quotes Hos 6:6 ('I desire mercy, not sacrifice')"}, {'target': 'romans', 'why': "Rom 9:25-26 quotes Hos 2:23 and 1:10 — Lo-Ammi ('not my people') reversed for Gentile inclusion"}, {'target': 'jeremiah', 'why': "Jeremiah extends Hosea's marriage metaphor — the unfaithful wife who will receive a new covenant (Jer 31:31-34)"}, {'target': 'song', 'why': 'Song of Solomon shows the ideal marriage; Hosea shows the broken version. Both use covenant-marriage theology.'}, {'target': 'revelation', 'why': "The Bride of Christ (Rev 19:7-9, 21:2) is the restored marriage Hosea's broken relationship points toward"}],
        "what_it_doesnt_say": ["Whether Gomer was a prostitute before marriage or became one after — 'wife of whoredom' (1:2) is ambiguous", 'How Hosea felt — the emotional toll of the commanded marriage is never described from his perspective', 'Who Lo-Ammi and Lo-Ruhamah grew up to be — the children named as prophetic signs disappear from the narrative'],
        "unusual_characters": [{'name': 'Gomer', 'ref': '1:3', 'detail': "Hosea's unfaithful wife — the living parable of Israel's covenant betrayal. Bought back from slavery (3:2) as YHWH redeems Israel.", 'connections': []}, {'name': 'Lo-Ammi', 'ref': '1:9', 'detail': "'Not my people' — prophetic child whose name declares covenant severance. Reversed in 2:23: 'I will say to Lo-Ammi, You are my people.'", 'connections': ['romans', '1peter']}],
        "patterns": ['Marriage metaphor structures the entire book: marriage (ch. 1), divorce (ch. 2), redemption/remarriage (ch. 3), then the theological unpacking (chs. 4-14)', "Name reversals: Lo-Ruhamah ('not pitied') becomes Ruhamah ('pitied'); Lo-Ammi ('not my people') becomes Ammi ('my people') — judgment reversed", "Hos 11:8 ('My heart is overturned within me') — YHWH experiences internal conflict over judgment. The most emotionally vulnerable divine speech in the OT."],
        "mistranslations": [{'english': 'mercy', 'original': 'hesed', 'issue': "'I desire hesed, not sacrifice' (6:6) — 'mercy' is too thin. Hesed is covenant faithfulness, loyal love, steadfast commitment."}, {'english': 'know', 'original': "da'at", 'issue': "'Knowledge of God' reduces relational intimacy to intellectual content. Hebrew da'at is the word for sexual knowing (Gen 4:1)."}],
    },
    {
        "id": 'joel',
        "section": 'minor-prophets-section',
        "title": 'Book 29: Joel',
        "themes": 'DC SPIRIT NATIONS',
        "era_count": 2,
        "chapters": 3,
        "grade": 'A',
        "meta_text": '2 era files &middot; 3 chapters &middot; Grade: A',
        "body_html": '''<p><strong>PENTECOST FOUNDATION</strong> — Joel 2:28-32: Spirit on "ALL flesh" — sons, daughters, servants, slaves. Peter quotes this at Pentecost (Acts 2:16-21). Spirit outpouring = divine council democratization (previously reserved for prophets/kings).</p>''',
        "key_claim": 'Joel 2:28-32 democratizes the Spirit — previously reserved for prophets, kings, and select individuals, the Spirit will be poured on ALL flesh (sons, daughters, servants, slaves), which Peter declares fulfilled at Pentecost (Acts 2:16-21).',
        "contested_words": [{'word': 'ruach', 'hebrew': 'רוּחַ', 'issue': "'Spirit' — poured out on ALL flesh (2:28). Previously restricted to prophets and kings. Pentecost fulfillment democratizes divine council access.", 'severity': 'CRITICAL'}, {'word': 'yom YHWH', 'hebrew': 'יוֹם יהוה', 'issue': "'Day of YHWH' (1:15, 2:1, 2:11, 2:31, 3:14) — five occurrences in three chapters. Both near (locust plague) and far (eschatological) fulfillment.", 'severity': 'CRITICAL'}],
        "hidden_connections": [{'target': 'acts', 'why': "Peter quotes Joel 2:28-32 at Pentecost (Acts 2:16-21) — the Spirit outpouring IS Joel's prophecy fulfilled"}, {'target': 'deuteronomy', 'why': "Joel reverses the Deut 32:8 allotment — Spirit on ALL flesh, not just Israel's prophets, reclaims the nations"}, {'target': 'numbers', 'why': "Moses wished 'that all YHWH's people were prophets' (Num 11:29) — Joel says it will happen"}, {'target': 'revelation', 'why': 'The Day of YHWH imagery (sun dark, moon to blood) reappears in Rev 6:12-17'}],
        "what_it_doesnt_say": ['When Joel was written — no king named, no specific historical event identified. The most undatable book in the OT.', 'Whether the locust plague is literal, metaphorical for an army, or both — the imagery shifts between natural and military'],
        "unusual_characters": [{'name': 'The locusts', 'ref': '1:4', 'detail': 'Four types of locusts in succession — devastation as divine judgment. Whether literal insects or metaphorical army is debated.', 'connections': ['revelation']}],
        "patterns": ['Crisis-to-cosmic escalation: locust plague (local) -> Day of YHWH (cosmic). The near event opens a window to the ultimate event.', "Before/after structure: devastation (1:1-2:17) then restoration (2:18-3:21) — the pivot is YHWH's pity (2:18)"],
        "mistranslations": [{'english': 'afterward', 'original': 'acharei-khen', 'issue': "'Afterward I will pour out my Spirit' (2:28) — English timeline word hides the Hebrew emphasis: AFTER the devastation, restoration. Sequence matters."}],
    },
    {
        "id": 'amos',
        "section": 'minor-prophets-section',
        "title": 'Book 30: Amos',
        "themes": 'DC RIV NATIONS REMNANT',
        "era_count": 2,
        "chapters": 9,
        "grade": 'A+',
        "meta_text": '2 era files &middot; 9 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>DIVINE COUNCIL ACCESS</strong> — Amos 3:7: "Surely the Lord does nothing without revealing his sod (council/secret) to his servants the prophets." FOUNDATIONAL text. Amos 5:24: "Let justice roll down like waters." Election = heightened accountability (3:2). Acts 15:16-17 quotes Amos 9:11-12 for Gentile inclusion.</p>''',
        "key_claim": 'Amos 3:7 is the foundational text for prophetic access — YHWH does NOTHING without first revealing his sod (council/secret) to his servants the prophets — making prophecy not prediction but divine council intelligence disclosed to human agents.',
        "contested_words": [{'word': 'sod', 'hebrew': 'סוֹד', 'issue': "'Secret/council' (3:7) — the divine council's deliberation. YHWH reveals his sod to prophets. Both the council itself and its decisions.", 'severity': 'CRITICAL'}, {'word': 'mishpat', 'hebrew': 'מִשְׁפָּט', 'issue': "'Justice' (5:24) — 'Let justice roll down like waters.' Not abstract fairness but concrete covenant faithfulness enacted for the vulnerable.", 'severity': 'CRITICAL'}, {'word': 'yada', 'hebrew': 'יָדַע', 'issue': "'Known' (3:2) — 'You only have I KNOWN of all the families of the earth.' Covenant intimacy, not mere awareness. Election = heightened accountability.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'acts', 'why': "Acts 15:16-17 quotes Amos 9:11-12 — James uses it to justify Gentile inclusion without circumcision. The 'fallen booth of David' restored."}, {'target': 'deuteronomy', 'why': "Amos' social justice demands are grounded in Deuteronomic covenant law — the poor, the widow, the alien"}, {'target': 'micah', 'why': 'Amos and Micah are contemporary prophets with overlapping social justice themes — Mic 6:8 distills what Amos 5:24 demands'}, {'target': 'revelation', 'why': "Amos' Day of YHWH imagery feeds into Revelation's judgment sequences"}],
        "what_it_doesnt_say": ["Why a shepherd from Tekoa was chosen over a professional prophet — Amos insists 'I am no prophet' (7:14) but never explains the divine logic", "How the 'fallen booth of David' (9:11) will be rebuilt — the messianic promise is given without mechanism"],
        "unusual_characters": [{'name': 'Amos', 'ref': '1:1', 'detail': "Shepherd and fig-tree dresser from Tekoa — not a professional prophet. 'I am no prophet, nor a prophet's son' (7:14). God drafts from outside the system.", 'connections': []}, {'name': 'Amaziah', 'ref': '7:10', 'detail': 'Priest of Bethel who opposes Amos and reports him to the king — institutional religion silencing prophetic truth.', 'connections': []}],
        "patterns": ["Oracles against nations (1:3-2:16): seven nations judged with 'for three transgressions and for four' formula, then the surprise — Israel is the eighth, judged harshest", 'Five visions (7:1-9:10): locusts, fire, plumb line, summer fruit, temple destruction — escalating from averting judgment to its inevitability', "Election-accountability paradox: 'You only have I known... THEREFORE I will punish you' (3:2) — chosen status increases judgment, not immunity"],
        "mistranslations": [{'english': 'secret', 'original': 'sod', 'issue': "Amos 3:7 — 'secret' hides the divine council meaning. sod is both the council assembly and its deliberations. Prophets attend the council."}, {'english': 'justice', 'original': 'mishpat', 'issue': 'English abstraction. Hebrew mishpat is concrete: the legal rights of the poor, the verdict for the oppressed, the covenant enacted in courts.'}],
    },
    {
        "id": 'obadiah',
        "section": 'minor-prophets-section',
        "title": 'Book 31: Obadiah',
        "themes": 'NATIONS',
        "era_count": 1,
        "meta_text": '1 era file &middot; 21 verses &middot; O-BREVITY',
        "body_html": '''<p>Esau-Jacob conflict cosmicized. Edom's betrayal during Jerusalem's fall judged. Climax: "The kingdom shall be YHWH's" (v. 21).</p>''',
        "key_claim": "Obadiah cosmicizes the Esau-Jacob conflict — Edom's betrayal during Jerusalem's fall is not merely political but the latest chapter in a rivalry that began in the womb (Gen 25:23), and the climax declares 'the kingdom shall be YHWH's' (v. 21).",
        "contested_words": [{'word': 'malkhut', 'hebrew': 'מַלְכוּת', 'issue': "'The kingdom shall be YHWH's' (v. 21) — the final word. Cosmic sovereignty declared through the lens of one small nation's betrayal.", 'severity': 'CRITICAL'}],
        "hidden_connections": [{'target': 'genesis', 'why': "The Esau-Jacob rivalry begins in Gen 25:23 ('the older shall serve the younger') — Obadiah is the latest chapter of that cosmic conflict"}, {'target': 'jeremiah', 'why': 'Jer 49:7-22 contains parallel oracles against Edom — shared source material or prophetic tradition'}, {'target': 'malachi', 'why': "Mal 1:2-5 ('Jacob I loved, Esau I hated') interprets the same Edom theology Obadiah pronounces judgment on"}, {'target': 'revelation', 'why': "'The kingdom shall be YHWH's' (v. 21) anticipates 'The kingdom of the world has become the kingdom of our Lord' (Rev 11:15)"}],
        "what_it_doesnt_say": ['When Obadiah prophesied — the shortest book in the OT with no dating formula', 'Which specific betrayal is in view — multiple occasions when Edom betrayed Judah'],
        "unusual_characters": [],
        "patterns": ['Shortest book in the OT (21 verses) — the entire Esau-Jacob conflict compressed into one oracle. Brevity as prophetic intensity.', "Reversal structure: Edom's height (v. 3-4) -> brought low (v. 5-9) -> reason: betrayal of brother (v. 10-14) -> YHWH's kingdom (v. 15-21)"],
        "mistranslations": [{'english': 'pride', 'original': 'zadon', 'issue': "Edom's 'pride' (v. 3) — zadon is presumption, arrogant overreach. Not mere self-esteem but active defiance of divine order."}],
    },
    {
        "id": 'jonah',
        "section": 'minor-prophets-section',
        "title": 'Book 32: Jonah',
        "themes": 'NATIONS TYPE REVERSAL',
        "era_count": 2,
        "chapters": 4,
        "meta_text": '2 era files &middot; 4 chapters &middot; O-NARRATIVE',
        "body_html": '''<p><strong>TYPE OF RESURRECTION</strong> — Three days in fish = three days in tomb (Matt 12:39-41). Pagan sailors convert. Nineveh repents at 5 words. Jonah is FURIOUS — quotes Ex 34:6-7 AS A COMPLAINT. Book ends with an unanswered question: "Should I not pity Nineveh?" The reader must answer.</p>''',
        "key_claim": "Jonah is furious that God shows mercy to Nineveh and quotes Exodus 34:6-7 AS A COMPLAINT — the only prophet who runs from his calling and succeeds in his mission but considers the success a disaster, exposing Israel's exclusivism against YHWH's universal compassion.",
        "contested_words": [{'word': "da'ag", 'hebrew': 'דָּאַג', 'issue': "Fish/sea creature — 'great fish' (dag gadol, 1:17). Not a whale. The species is irrelevant; the divine sovereignty over creation is the point.", 'severity': 'MAJOR'}, {'word': 'nacham', 'hebrew': 'נָחַם', 'issue': "'Relented' (3:10) — God 'repented/changed his mind' about the judgment. Same word as Ex 32:14. Does God change his mind?", 'severity': 'CRITICAL'}, {'word': "ra'ah", 'hebrew': 'רָעָה', 'issue': "'Evil/calamity/wickedness' — used for BOTH Nineveh's wickedness (1:2) and Jonah's displeasure (4:1). Same word, different moral valence.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'matthew', 'why': "Matt 12:39-41 — three days in fish = three days in tomb. 'Something greater than Jonah is here.' Resurrection typology."}, {'target': 'exodus', 'why': "Jonah 4:2 quotes Ex 34:6-7 (YHWH's self-revelation) as a COMPLAINT — he knows God's character and resents it"}, {'target': 'nahum', 'why': 'Nahum is the sequel — mercy was offered to Nineveh (Jonah), Nineveh returned to violence, now judgment comes (Nahum)'}, {'target': 'luke', 'why': "Luke 11:29-32 parallels Matt 12 — Nineveh repented at Jonah's preaching; this generation will not repent at something greater"}],
        "what_it_doesnt_say": ["Why Jonah ran — the text assumes the audience understands Israelite resentment toward Assyria (Nineveh's empire)", "What happened to Jonah after the book ends — the final question ('Should I not pity Nineveh?') is unanswered; the reader must answer", 'How the entire city repented — from king to cattle (3:7-8), with no explanation of how the message spread so fast'],
        "unusual_characters": [{'name': 'The pagan sailors', 'ref': '1:16', 'detail': 'Fear YHWH and offer sacrifices after the sea calms — pagans convert while the prophet runs. Reversal of expectations.', 'connections': []}, {'name': 'The Ninevites', 'ref': '3:5', 'detail': 'Repent at five Hebrew words from a reluctant prophet — the fastest mass conversion in Scripture. Even the cattle fast.', 'connections': ['nahum', 'matthew']}],
        "patterns": ['Reversal upon reversal: the prophet runs, pagans convert, the enemy repents, the prophet rages — every expectation is inverted', "The book ends with an unanswered question (4:11) — the reader is the jury. 'Should I not pity Nineveh?' demands a response.", 'Three-day pattern: three days in the fish (1:17), three days walking Nineveh (3:3) — prefigures three days in the tomb (Matt 12:40)'],
        "mistranslations": [{'english': 'whale', 'original': 'dag gadol', 'issue': "'Great fish' — not a whale. The species is irrelevant to the text's point about divine sovereignty over creation."}, {'english': 'repented/relented', 'original': 'nacham', 'issue': "'God relented' (3:10) — does God change his mind? nacham encompasses grief, comfort, and change of course. The English binary (did he / didn't he change his mind) misses Hebrew nuance."}],
    },
    {
        "id": 'micah',
        "section": 'minor-prophets-section',
        "title": 'Book 33: Micah',
        "themes": 'DC RIV SEED NATIONS',
        "era_count": 4,
        "chapters": 7,
        "grade": 'A+',
        "meta_text": '4 era files &middot; 7 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>BETHLEHEM</strong> (5:2) — "From you shall come forth one whose coming forth is from of old, from days of eternity (yemei olam)." Pre-existent Messiah from the smallest village. Matt 2:4-6.</p><p><strong>MICAH 6:8</strong> — "What does YHWH require? Do justice, love mercy, walk humbly." Most concise prophetic ethics in the OT.</p>''',
        "key_claim": "Micah 5:2 declares the Messiah's origin is 'from of old, from days of eternity' (yemei olam) — a pre-existent ruler from Bethlehem, the smallest village, collapsing the distance between humility and cosmic antiquity in one verse.",
        "contested_words": [{'word': 'yemei olam', 'hebrew': 'יְמֵי עוֹלָם', 'issue': "'Days of eternity/antiquity' (5:2) — the Messiah's goings forth are from eternity. Pre-existence or ancient lineage?", 'severity': 'CRITICAL'}, {'word': 'mishpat', 'hebrew': 'מִשְׁפָּט', 'issue': "'Justice' (6:8) — 'Do justice, love mercy, walk humbly.' The most concise prophetic ethics summary. Concrete covenant faithfulness.", 'severity': 'CRITICAL'}, {'word': 'riv', 'hebrew': 'רִיב', 'issue': "Covenant lawsuit (6:1-2) — 'Hear, you mountains, YHWH's riv.' The mountains are witnesses, as in Deut 30:19.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'matthew', 'why': "Matt 2:4-6 quotes Mic 5:2 — the chief priests identify Bethlehem as the Messiah's birthplace from this text"}, {'target': 'amos', 'why': 'Contemporary prophets with overlapping social justice themes — Mic 6:8 distills what Amos 5:24 demands'}, {'target': 'isaiah', 'why': "Mic 4:1-3 parallels Isa 2:2-4 almost verbatim — 'swords into plowshares.' Shared prophetic tradition."}, {'target': 'deuteronomy', 'why': 'The riv (covenant lawsuit) of Mic 6 uses the Deuteronomic treaty framework — mountains as witnesses per Deut 30:19'}],
        "what_it_doesnt_say": ['How the Messiah can be from both Bethlehem (tiny village) and eternity — the paradox is stated but not explained', "When 'swords into plowshares' (4:3) will happen — eschatological promise with no timeline"],
        "unusual_characters": [{'name': 'The ruler from Bethlehem', 'ref': '5:2', 'detail': "Pre-existent Messiah from the smallest, most insignificant village. Origin 'from of old, from days of eternity.'", 'connections': ['matthew', 'john']}],
        "patterns": ['Three cycles of judgment and hope: doom (1-2) / hope (2:12-13), doom (3) / hope (4-5), doom (6:1-7:7) / hope (7:8-20)', "Mic 6:8 as prophetic summary: 'Do justice (mishpat), love mercy (hesed), walk humbly (hatznea lekhet)' — the entire prophetic ethic in one verse", 'Cosmic courtroom (6:1-2): mountains and hills as jury — the covenant lawsuit uses creation as witnesses, echoing Deut 30:19'],
        "mistranslations": [{'english': 'justice', 'original': 'mishpat', 'issue': "Abstract English. Micah's mishpat means concrete covenant action — defend the poor, correct the powerful, enact Torah in the courts."}, {'english': 'from ancient times', 'original': 'yemei olam', 'issue': "Weakens 'days of eternity' to mere antiquity. The Hebrew allows — and the NT confirms — genuine pre-existence."}],
    },
    {
        "id": 'nahum',
        "section": 'minor-prophets-section',
        "title": 'Book 34: Nahum',
        "themes": 'DC SPIRIT',
        "era_count": 2,
        "chapters": 3,
        "meta_text": '2 era files &middot; 3 chapters &middot; O-VENGEANCE',
        "body_html": '''<p>Continuation of Jonah — mercy was offered, Nineveh returned to violence, now judgment. Pestilence and Plague as personified divine agents. Confirmed by Babylon Chronicle (612 BC).</p>''',
        "key_claim": "Nahum is Jonah's sequel — mercy was offered to Nineveh and received, but Nineveh returned to violence, and now divine judgment falls with the certainty of a cosmic warrior's advance, confirmed by the Babylon Chronicle's record of Nineveh's fall in 612 BC.",
        "contested_words": [{'word': 'noqem', 'hebrew': 'נֹקֵם', 'issue': "'Avenging' (1:2) — YHWH as avenger, used three times in one verse. Not vindictiveness but covenant enforcement against oppression.", 'severity': 'MAJOR'}, {'word': 'Deber and Resheph', 'hebrew': 'דֶּבֶר / רֶשֶׁף', 'issue': "'Pestilence and Plague' (Hab 3:5, applied to Nahum's theology) — personified divine agents, not mere diseases. Council executioners.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'jonah', 'why': 'Nahum completes the Jonah arc — mercy offered (Jonah), mercy squandered, judgment executed (Nahum). Together they teach: grace has a shelf life when rejected.'}, {'target': 'revelation', 'why': "Nahum's language of divine warrior judgment feeds into Revelation's portrayal of Christ's return (Rev 19:11-16)"}, {'target': 'exodus', 'why': "Nah 1:3 quotes Ex 34:6-7 — the same divine self-revelation Jonah complained about. Nahum applies the 'will not leave guilty unpunished' clause."}],
        "what_it_doesnt_say": ['Whether any Ninevites repented a second time — no opportunity is mentioned, only judgment', "How Nahum received his oracle — no call narrative, no divine council vision, just 'the oracle concerning Nineveh'"],
        "unusual_characters": [],
        "patterns": ['Acrostic poem (1:2-8): partial alphabetic acrostic describing YHWH as divine warrior — form dissolves as chaos overtakes Nineveh', "Jonah-Nahum theological pair: mercy (Jonah) then judgment (Nahum) — together they form a complete picture of YHWH's character from Ex 34:6-7"],
        "mistranslations": [{'english': 'jealous/vengeful', 'original': 'qanno/noqem', 'issue': 'English makes YHWH sound petty. Hebrew qanno is zealous covenant passion; noqem is righteous enforcement against oppression, not personal revenge.'}],
    },
    {
        "id": 'habakkuk',
        "section": 'minor-prophets-section',
        "title": 'Book 35: Habakkuk',
        "themes": 'DC SPIRIT COV',
        "era_count": 3,
        "chapters": 3,
        "grade": 'A+',
        "meta_text": '3 era files &middot; 3 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>JUSTIFICATION BY FAITH</strong> — Hab 2:4: "The righteous shall live by his emunah (faith/faithfulness)." Quoted 3x in NT (Rom 1:17, Gal 3:11, Heb 10:38). Ignited the Reformation. The only prophetic book structured as a DIALOGUE with God. Theodicy without resolution — "Trust" IS the answer.</p>''',
        "key_claim": "Habakkuk 2:4 — 'the righteous shall live by his emunah (faith/faithfulness)' — quoted three times in the NT (Rom 1:17, Gal 3:11, Heb 10:38) and the spark that ignited the Reformation, making this the only prophetic book structured as a dialogue with God where 'trust' is the answer to theodicy.",
        "contested_words": [{'word': 'emunah', 'hebrew': 'אֱמוּנָה', 'issue': "'Faith/faithfulness' (2:4) — is it human faith IN God or human faithFULNESS? The Hebrew holds both. Quoted 3x in NT. Ignited the Reformation.", 'severity': 'CRITICAL'}, {'word': 'chazon', 'hebrew': 'חָזוֹן', 'issue': "'Vision' (2:2) — 'Write the vision; make it plain on tablets.' The divine council revelation committed to writing. Prophetic disclosure.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'romans', 'why': "Rom 1:17 quotes Hab 2:4 — 'the righteous shall live by faith.' Paul makes it the thesis of Romans."}, {'target': 'galatians', 'why': 'Gal 3:11 quotes Hab 2:4 — justification by faith, not by works of the law'}, {'target': 'hebrews', 'why': 'Heb 10:38 quotes Hab 2:4 — perseverance through suffering grounded in faith'}, {'target': 'job', 'why': "Both wrestle with theodicy — righteous suffering under divine sovereignty. Both receive 'trust' rather than explanation as the answer."}],
        "what_it_doesnt_say": ['Why God would use a MORE wicked nation (Babylon) to punish a LESS wicked one (Judah) — Habakkuk asks but the mechanism is never explained', "When the 'vision' (2:2-3) will be fulfilled — 'it awaits its appointed time; it will not lie'"],
        "unusual_characters": [{'name': 'Habakkuk', 'ref': '1:1', 'detail': 'The only prophet who argues with God and receives a direct answer. The book is structured as a lawsuit (riv) with YHWH as both defendant and judge.', 'connections': []}],
        "patterns": ["Dialogue structure: complaint (1:2-4) -> God's answer (1:5-11) -> second complaint (1:12-2:1) -> God's answer (2:2-20) -> psalm of trust (ch. 3)", 'Five woes (2:6-20): against the Babylonian oppressor. Even the instrument of judgment will itself be judged.', 'Theophany hymn (ch. 3): YHWH as divine warrior striding across creation — the most vivid theophany outside the Pentateuch'],
        "mistranslations": [{'english': 'faith', 'original': 'emunah', 'issue': "English splits 'faith' and 'faithfulness' into two concepts. Hebrew emunah holds both — trust in God expressed through covenant loyalty. The Reformation read it as 'faith alone' but the Hebrew includes faithful living."}],
    },
    {
        "id": 'zephaniah',
        "section": 'minor-prophets-section',
        "title": 'Book 36: Zephaniah',
        "themes": 'DC REMNANT NATIONS',
        "era_count": 2,
        "chapters": 3,
        "meta_text": '2 era files &middot; 3 chapters',
        "body_html": '''<p><strong>UN-CREATION</strong> — Most comprehensive Day of YHWH: reverses Genesis 1 itself. Yet 3:17: "YHWH your God will quiet you by his love; he will exult over you with loud singing." The divine warrior who unmakes creation SINGS over the remnant.</p>''',
        "key_claim": 'Zephaniah describes the most comprehensive Day of YHWH — a cosmic un-creation that reverses Genesis 1 itself — yet at the center places YHWH singing over the remnant with joy (3:17), the divine warrior who unmakes creation also SINGS over those he saves.',
        "contested_words": [{'word': 'yom YHWH', 'hebrew': 'יוֹם יהוה', 'issue': "'Day of YHWH' (1:7, 14) — Zephaniah's version is the most comprehensive: sweeps away humans, animals, birds, fish. Genesis 1 in reverse.", 'severity': 'CRITICAL'}, {'word': 'yagil', 'hebrew': 'יָגִיל', 'issue': "'He will rejoice/exult' (3:17) — YHWH rejoicing over his people with singing. The divine warrior sings. Most tender divine image in the prophets.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'genesis', 'why': 'Zeph 1:2-3 reverses the Genesis 1 creation order — fish, birds, animals, humans swept away. Un-creation as judgment.'}, {'target': 'joel', 'why': "Both focus on the Day of YHWH — Joel's locust plague and Zephaniah's cosmic sweep are parallel visions of the same event"}, {'target': 'revelation', 'why': "The comprehensive destruction of Zeph 1 anticipates Revelation's bowl judgments — total cosmic upheaval"}],
        "what_it_doesnt_say": ['How the remnant survives the un-creation — total destruction is described but a remnant emerges without explanation', "Why YHWH sings — 3:17 is stunning but no context is given for the divine warrior's joy in the middle of judgment"],
        "unusual_characters": [],
        "patterns": ['Un-creation structure (1:2-3): sweeps away humans, animals, birds, fish — reverse order of Genesis 1 creation. YHWH undoes his own work.', 'Judgment-to-joy pivot: the book moves from total cosmic destruction (ch. 1) to YHWH singing over the remnant (3:17) — the most dramatic emotional reversal in the Twelve'],
        "mistranslations": [{'english': 'quiet you', 'original': 'yacharish', 'issue': "'He will quiet you by his love' (3:17) — some render 'be silent' (with awe). The divine warrior is speechless with love, then breaks into song. Translation choice shapes whether God is calming Israel or overwhelmed himself."}],
    },
    {
        "id": 'haggai',
        "section": 'minor-prophets-section',
        "title": 'Book 37: Haggai',
        "themes": 'HOLY',
        "era_count": 1,
        "chapters": 2,
        "meta_text": '1 era file &middot; 2 chapters',
        "body_html": '''<p>Temple rebuilding. "The latter glory of this house shall be greater than the former" (2:9) — unfulfilled until Christ enters.</p>''',
        "key_claim": "Haggai's prophecy that 'the latter glory of this house shall be greater than the former' (2:9) remained unfulfilled for 500 years — until Christ himself entered the Second Temple, making the promise christological rather than architectural.",
        "contested_words": [{'word': 'kavod', 'hebrew': 'כָּבוֹד', 'issue': "'Glory' (2:9) — 'The latter glory of this house shall be greater than the former.' No glory-cloud filled the Second Temple. Fulfilled only in Christ's presence.", 'severity': 'CRITICAL'}],
        "hidden_connections": [{'target': 'ezekiel', 'why': "Ezekiel's kavod departed the First Temple (Ezek 10-11); Haggai promises greater glory for the Second — the return Ezekiel foresaw"}, {'target': 'malachi', 'why': "Mal 3:1 ('the Lord whom you seek will suddenly come to his temple') fulfills Haggai's promise of greater glory"}, {'target': 'john', 'why': "Jesus in the Temple (John 2:13-22) — the glory greater than Solomon's is the incarnate Son"}, {'target': 'ezra', 'why': 'Haggai is the historical context for Ezra 5-6 — the prophetic push behind the Temple rebuilding'}],
        "what_it_doesnt_say": ["How the Second Temple's glory would exceed the First — no Shekinah cloud, no ark, no Urim and Thummim. The promise seemed impossible.", "Why the people prioritized their own houses over God's (1:4) — the motivation for neglect is assumed, not explained"],
        "unusual_characters": [{'name': 'Zerubbabel', 'ref': '2:23', 'detail': "Called YHWH's 'signet ring' — the Davidic heir through whom the messianic line continues after exile. Royal authority compressed into a seal.", 'connections': ['matthew', 'luke']}],
        "patterns": ['Four dated oracles (1:1, 2:1, 2:10, 2:20): precisely dated to the month and day — the most chronologically specific book in the prophets', "Priorities rebuked: 'Is it time for you to dwell in paneled houses while this house lies in ruins?' (1:4) — the Temple-first principle"],
        "mistranslations": [{'english': 'glory', 'original': 'kavod', 'issue': "Haggai's kavod is not abstract splendor but the tangible divine presence — weight, substance, the Shekinah. The Second Temple lacked it until Christ entered."}],
    },
    {
        "id": 'zechariah',
        "section": 'minor-prophets-section',
        "title": 'Book 38: Zechariah',
        "themes": 'DC SEED KING PRIEST SPIRIT',
        "era_count": 4,
        "chapters": 14,
        "grade": 'A+',
        "meta_text": '4 era files &middot; 14 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>MOST CHRISTOLOGICALLY DENSE MINOR PROPHET</strong> — 40+ NT quotations. Passion narratives SATURATED with Zechariah:</p><ul><li>9:9 — Triumphal entry on donkey (Matt 21:5)</li><li>11:12-13 — Thirty pieces of silver (Matt 27:9)</li><li>12:10 — "They will look on ME whom they have PIERCED" (John 19:37)</li><li>13:7 — "Strike the shepherd" (Matt 26:31)</li></ul><p><strong>DIVINE COUNCIL COURTROOM</strong> (3:1-10) — Satan accuses Joshua the high priest. YHWH acquits. Most explicit council courtroom in the Twelve.</p>''',
        "key_claim": "Zechariah is the most christologically dense minor prophet — with 40+ NT quotations saturating the passion narratives: triumphal entry on a donkey (9:9), thirty pieces of silver (11:12-13), 'they will look on ME whom they have PIERCED' (12:10), and 'strike the shepherd' (13:7).",
        "contested_words": [{'word': 'daqaru', 'hebrew': 'דָּקָרוּ', 'issue': "'Pierced' (12:10) — 'they will look on ME whom they have pierced.' YHWH is the speaker — YHWH himself is pierced? Quoted in John 19:37.", 'severity': 'CRITICAL'}, {'word': 'tselach', 'hebrew': 'צֶלַח', 'issue': "'Branch' (tsemach, 3:8, 6:12) — messianic title. The Branch who builds the Temple and is BOTH priest AND king. Unique dual-office figure.", 'severity': 'CRITICAL'}, {'word': 'ha-Satan', 'hebrew': 'הַשָּׂטָן', 'issue': "'The adversary' (3:1) — ha-Satan accusing Joshua the high priest in the divine council courtroom. Same titled role as in Job.", 'severity': 'CRITICAL'}, {'word': 'shalosh', 'hebrew': 'שְׁלֹשִׁים', 'issue': "'Thirty pieces of silver' (11:12) — the 'lordly price' (ironic). Fulfilled in Judas's betrayal (Matt 27:9).", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'matthew', 'why': "Matt 21:5 (triumphal entry/Zech 9:9), Matt 26:31 ('strike the shepherd'/Zech 13:7), Matt 27:9 (thirty pieces of silver/Zech 11:12-13)"}, {'target': 'john', 'why': "John 19:37 quotes Zech 12:10 — 'they will look on him whom they have pierced.' Applied directly to the crucifixion."}, {'target': 'job', 'why': 'ha-Satan in Zech 3:1 plays the same prosecutorial role as in Job 1-2 — accusing the righteous before the divine council'}, {'target': 'revelation', 'why': "Rev 1:7 quotes Zech 12:10 ('every eye will see him, even those who pierced him'); the rider on a white horse echoes Zechariah's messianic warrior"}, {'target': 'hebrews', 'why': 'The priest-king Branch (Zech 6:12-13) who serves on his throne connects to the Melchizedekian priesthood of Hebrews'}],
        "what_it_doesnt_say": ["How YHWH can be both the speaker ('they will look on ME') and the one pierced — the divine identity of the pierced one is stated but not explained", "Who the 'worthless shepherd' (11:17) is — anti-messianic figure with no identification", 'How the Branch can be both priest AND king — the offices were always separated; Zechariah merges them without explanation'],
        "unusual_characters": [{'name': 'Joshua the high priest', 'ref': '3:1', 'detail': 'Accused by ha-Satan in the divine council courtroom. YHWH acquits him and gives him clean garments. The most explicit council courtroom scene in the Twelve.', 'connections': ['job', 'revelation']}, {'name': 'The Branch (Tsemach)', 'ref': '3:8', 'detail': 'Messianic figure who is both priest and king — builds the Temple and rules from his throne. Dual-office Messiah.', 'connections': ['hebrews', 'isaiah', 'jeremiah']}, {'name': 'The pierced one', 'ref': '12:10', 'detail': "YHWH says 'they will look on ME whom they have pierced' — the divine figure who is wounded. Applied to Christ in John 19:37.", 'connections': ['john', 'revelation']}],
        "patterns": ['Eight night visions (1:7-6:8): horsemen, horns, measuring line, Joshua accused, lampstand, flying scroll, woman in basket, chariots — a complete divine council intelligence briefing', 'Passion saturation: Zech 9-14 provides more raw material for the gospel passion narratives than any other OT section outside Isaiah 53', 'Two-part structure: visions and oracles (1-8, dated) + apocalyptic oracles (9-14, undated) — the book shifts from current restoration to eschatological fulfillment'],
        "mistranslations": [{'english': 'they will look on him', 'original': 've-hibitu elai', 'issue': "Zech 12:10 — the Hebrew says 'on ME' (elai), not 'on him.' YHWH is the speaker AND the pierced one. Most English translations soften this to avoid the christological implication."}, {'english': 'Branch', 'original': 'tsemach', 'issue': 'Generic English. Hebrew tsemach is a loaded messianic title appearing in Isaiah, Jeremiah, and Zechariah — each adding layers to the same figure.'}],
    },
    {
        "id": 'malachi',
        "section": 'minor-prophets-section',
        "title": 'Book 39: Malachi',
        "themes": 'COV PRIEST',
        "era_count": 2,
        "chapters": 4,
        "meta_text": '2 era files &middot; 4 chapters',
        "body_html": '''<p><strong>LAST WORD BEFORE SILENCE</strong> — "I will send my messenger to prepare the way" (3:1). "I will send Elijah before the great Day of YHWH" (4:5-6). Final OT word: "curse" (cherem). NT opens with "grace" (charis). Between them: 400 years of silence. John the Baptist breaks it.</p></div></div>

<!-- NEW TESTAMENT -->''',
        "key_claim": "Malachi is the last prophetic word before 400 years of silence — its final word is 'curse' (cherem), and the NT opens with 'grace' (charis), with John the Baptist breaking the silence as the 'Elijah' Malachi promised (4:5-6).",
        "contested_words": [{'word': "mal'akhi", 'hebrew': 'מַלְאָכִי', 'issue': "'My messenger' (1:1, 3:1) — is Malachi a proper name or a title? 'I will send my mal'akh (messenger) to prepare the way' (3:1). The book may be anonymous.", 'severity': 'MAJOR'}, {'word': 'cherem', 'hebrew': 'חֵרֶם', 'issue': "'Curse' (4:6) — the final word of the OT. Devoted destruction. The old covenant ends under the shadow of cherem; the new opens with charis (grace).", 'severity': 'CRITICAL'}, {'word': 'Eliyyahu', 'hebrew': 'אֵלִיָּהוּ', 'issue': "'Elijah' (4:5) — 'I will send Elijah before the great Day of YHWH.' Fulfilled in John the Baptist (Matt 11:14, 17:12-13).", 'severity': 'CRITICAL'}],
        "hidden_connections": [{'target': 'matthew', 'why': 'Matt 11:14 and 17:12-13 — Jesus identifies John the Baptist as the Elijah Malachi promised (Mal 4:5-6)'}, {'target': 'mark', 'why': "Mark 1:2 quotes Mal 3:1 ('I send my messenger before your face') combined with Isa 40:3 — the opening of the Gospel"}, {'target': 'luke', 'why': "Luke 1:17 — the angel tells Zechariah that John will go 'in the spirit and power of Elijah' to fulfill Malachi's prophecy"}, {'target': 'romans', 'why': "Rom 9:13 quotes Mal 1:2-3 ('Jacob I loved, Esau I hated') for the election argument"}, {'target': 'obadiah', 'why': "Both address the Esau/Edom theology — Obadiah judges Edom, Malachi opens with 'Jacob I loved, Esau I hated'"}],
        "what_it_doesnt_say": ['Why 400 years of prophetic silence follow — the last prophet speaks and then heaven goes silent with no explanation', "Whether Malachi is a name or a title — 'my messenger' could be the author's name or a description", 'How Elijah would return — literal return or spiritual successor? The ambiguity allows for John the Baptist as fulfillment'],
        "unusual_characters": [{'name': 'The messenger of the covenant', 'ref': '3:1', 'detail': "Two figures: 'my messenger' who prepares the way (John the Baptist) and 'the Lord whom you seek' who comes to the Temple (Christ). Two advents in one verse.", 'connections': ['matthew', 'mark', 'luke']}],
        "patterns": ["Disputation format: six dialogues where Israel challenges God and God responds — 'You say... But I say...' The people argue with YHWH.", "OT-to-NT bridge: last word 'curse' (cherem, 4:6) -> 400 years of silence -> first word of NT era: 'grace' (charis). The hinge of redemptive history.", "Tithing passage (3:10) — 'Test me in this' — the ONLY place YHWH invites being tested. Unique in all of Scripture."],
        "mistranslations": [{'english': 'Malachi', 'original': "mal'akhi", 'issue': "Treated as a proper name but means 'my messenger.' The book may be anonymous — the 'author' is a title, not an identity."}, {'english': 'curse', 'original': 'cherem', 'issue': "Generic 'curse' hides the specific meaning: devoted to destruction, total consecration to judgment. The weight of the OT's final word."}],
    },
    {
        "id": 'matthew',
        "section": 'new-testament',
        "title": 'Book 40: Matthew',
        "themes": 'SEED KING DC COV TYPE NATIONS',
        "era_count": 5,
        "chapters": 28,
        "grade": 'A+',
        "meta_text": '5 era files &middot; 28 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>GOSPEL OF THE KINGDOM</strong> — "Gates of Hades shall not prevail against my ekklesia" (16:18, governing assembly — not institutional church) — declared at Caesarea Philippi, base of Mount Hermon (Watcher descent site). "All authority in heaven and on earth has been given to me" (28:18) — Deut 32:8 allotment reversed.</p>''',
        "key_claim": "Matthew presents Jesus as the legitimate Davidic King whose Great Commission ('all authority in heaven and on earth') reverses the Deut 32:8 allotment — reclaiming the nations from the corrupt bene elohim.",
        "contested_words": [{'word': 'ekklesia', 'greek': 'ἐκκλησία', 'issue': "'Church' hides the political meaning — governing assembly with judicial authority, declared at Caesarea Philippi (base of Hermon, Watcher descent site).", 'severity': 'CRITICAL'}, {'word': 'basileia ton ouranon', 'greek': 'βασιλεία τῶν οὐρανῶν', 'issue': "'Kingdom of heaven' — uniquely Matthean circumlocution. Not 'going to heaven' but heaven's government invading earth.", 'severity': 'CRITICAL'}, {'word': 'pleroo', 'greek': 'πληρόω', 'issue': "'Fulfill' — appears 16 times. Does it mean predict-and-complete, or fill-up-the-meaning? Shapes how we read all OT quotations.", 'severity': 'MAJOR'}, {'word': 'proskyneo', 'greek': 'προσκυνέω', 'issue': "'Worship' — magi worship the infant Jesus (2:11). Same word used for God alone. Matthew presents Jesus receiving divine honors from birth.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'deuteronomy', 'why': 'Jesus quotes Deuteronomy three times to defeat Satan (4:4, 7, 10 from Deut 6-8); Great Commission reverses Deut 32:8 allotment'}, {'target': 'genesis', 'why': 'Genealogy (1:1-17) traces the seed line from Abraham through David to Christ — Gen 3:15 fulfilled'}, {'target': 'daniel', 'why': 'Son of Man coming on clouds (24:30, 26:64) draws directly from Dan 7:13 — divine cloud-rider claim'}, {'target': '1enoch', 'why': 'Caesarea Philippi declaration (16:13-20) is at the base of Mount Hermon — the Watcher descent site of 1 Enoch 6'}, {'target': 'revelation', 'why': "Great Commission's 'all authority' claim finds culmination in Rev 11:15 — 'The kingdom of the world has become the kingdom of our Lord'"}, {'target': 'psalms', 'why': "Ps 2:6-7 (the divine Son enthroned) and Ps 110:1 (sit at my right hand) underpin Matthew's royal Christology"}],
        "what_it_doesnt_say": ['Never explains WHY Jesus chose 12 apostles — the number parallels the 12 tribes but Matthew never makes the connection explicit', "The magi's identity and origin are never specified — tradition says three kings, but the text gives no number or rank", 'No account of Jesus between ages 12 and 30 — nearly two decades of silence', "Never names the 'star' the magi followed or explains its nature — astronomical, angelic, or supernatural?"],
        "unusual_characters": [{'name': 'The Magi', 'ref': '2:1', 'detail': "Pagan astrologers who recognize Israel's king before Israel does — Gentile worship before Jewish recognition.", 'connections': ['numbers', 'isaiah']}, {'name': "Pilate's wife", 'ref': '27:19', 'detail': 'Only in Matthew — receives a dream warning about Jesus. A pagan woman gets divine revelation while Jewish leaders reject it.', 'connections': []}, {'name': 'The centurion at the cross', 'ref': '27:54', 'detail': "'Truly this was the Son of God' — a Roman soldier makes the confession Israel's leaders refuse.", 'connections': ['mark']}],
        "patterns": ['Five major discourse blocks (chs. 5-7, 10, 13, 18, 23-25) mirror the five books of Torah — Jesus as the new Moses giving new Torah', "Fulfillment formula: 'This was to fulfill what was spoken by the prophet' appears 12+ times — Matthew reads the entire OT as pointing to Christ", 'Genealogy structure: 3 sets of 14 generations (1:17) — 14 = numerical value of David (dalet-vav-dalet = 4+6+4)', 'Mountain theology: Temptation mount, Sermon mount, Transfiguration mount, Olivet Discourse, Great Commission mount — Jesus acts on mountains like Moses'],
        "mistranslations": [{'english': 'church', 'original': 'ekklesia', 'issue': "Injects centuries of institutional religion into a term meaning 'governing assembly' with judicial and cosmic authority"}, {'english': 'kingdom of heaven', 'original': 'basileia ton ouranon', 'issue': "Sounds like a destination ('going to heaven') when it means heaven's reign breaking into earth"}, {'english': 'fulfilled', 'original': 'pleroo', 'issue': "Implies mere prediction-fulfillment when the Greek can mean 'filled up the meaning of' — a richer hermeneutic"}],
    },
    {
        "id": 'mark',
        "section": 'new-testament',
        "title": 'Book 41: Mark',
        "themes": 'SEED DC SPIRIT',
        "era_count": 3,
        "chapters": 16,
        "grade": 'A',
        "meta_text": '3 era files &middot; 16 chapters &middot; Grade: A',
        "body_html": '''<p><strong>Mark 14:62</strong> — THE christological climax: "You will see the Son of Man seated at the right hand of Power and coming with the clouds of heaven." Dan 7:13 + Ps 110:1. The high priest tears his robes — the DIVINE claim understood.</p>''',
        "key_claim": "Mark 14:62 is the christological climax of the Gospel — Jesus claims to be the divine cloud-rider of Daniel 7:13 seated at God's right hand (Ps 110:1), and the high priest tears his robes because he understands the DIVINE claim, not merely a messianic one.",
        "contested_words": [{'word': 'euangelion', 'greek': 'εὐαγγέλιον', 'issue': "'Gospel' — in Roman usage, an imperial proclamation of victory or a new emperor's accession. Mark co-opts Caesar's word for Jesus.", 'severity': 'CRITICAL'}, {'word': 'huios tou theou', 'greek': 'υἱὸς τοῦ θεοῦ', 'issue': "'Son of God' — Roman emperors claimed this title (divi filius). Mark's opening line is a direct counter-claim to Caesar.", 'severity': 'CRITICAL'}, {'word': 'euthys', 'greek': 'εὐθύς', 'issue': "'Immediately' — appears ~40 times. Mark's urgency is theological: the kingdom is breaking in NOW, not gradually.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'daniel', 'why': 'Mark 14:62 combines Dan 7:13 (cloud-rider) with Ps 110:1 (enthroned at right hand) — the two most explosive OT texts fused into one claim'}, {'target': 'isaiah', 'why': "Mark 1:2-3 opens with Isaiah's 'prepare the way of the LORD' — the way being prepared is for YHWH himself, and Jesus walks it"}, {'target': 'psalms', 'why': "Ps 110:1 quoted at 12:36 and alluded at 14:62 — the Lord who sits at YHWH's right hand is the interpretive key to Mark's Christology"}, {'target': '1peter', 'why': "Mark traditionally understood as Peter's memoir; 1 Peter's theology of suffering mirrors Mark's suffering-Messiah theme"}, {'target': 'exodus', 'why': "The feeding of 5,000 (6:30-44) and 4,000 (8:1-10) echo Moses' manna provision — Jesus as the new Moses in the wilderness"}],
        "what_it_doesnt_say": ['No birth narrative — Mark begins with Jesus as an adult at baptism, skipping 30 years entirely', 'The original ending (16:8) stops at the empty tomb with the women fleeing in fear — no resurrection appearances', 'No genealogy — unlike Matthew and Luke, Mark provides no family lineage for Jesus', 'Never records the Sermon on the Mount — Mark focuses on actions over extended teaching'],
        "unusual_characters": [{'name': 'The Gerasene demoniac', 'ref': '5:1-20', 'detail': "'My name is Legion, for we are many' — a Roman military term for 6,000 soldiers. The demons beg not to be sent 'out of the region' — territorial assignment.", 'connections': ['luke']}, {'name': 'The young man who fled naked', 'ref': '14:51-52', 'detail': "Only in Mark — flees naked at Jesus' arrest. Possibly Mark himself. Echoes Gen 39 (Joseph fleeing) and Amos 2:16.", 'connections': []}, {'name': 'Bartimaeus', 'ref': '10:46', 'detail': "The only healed blind man named — calls Jesus 'Son of David' publicly. Sees what the disciples cannot.", 'connections': []}],
        "patterns": ['Messianic Secret: Jesus repeatedly commands silence about his identity (1:34, 1:44, 3:12, 5:43, 8:30) — revelation must come through the cross, not miracles', 'Sandwich structure (intercalation): Mark inserts one story inside another to create interpretive tension (e.g., 5:21-43, 11:12-25, 14:1-11)', "Two-stage healing of the blind man (8:22-26) mirrors the disciples' two-stage understanding: partial sight at Caesarea Philippi, full sight after resurrection", 'Three passion predictions (8:31, 9:31, 10:33-34) followed by misunderstanding followed by teaching on discipleship — a repeating pedagogical cycle'],
        "mistranslations": [{'english': 'gospel', 'original': 'euangelion', 'issue': "Loses the imperial-proclamation context — this was Caesar's word for announcing military victories and enthronements"}, {'english': 'immediately', 'original': 'euthys', 'issue': "Often softened to 'then' or 'just then' in translations, hiding Mark's theological urgency about the inbreaking kingdom"}, {'english': 'Son of God', 'original': 'huios tou theou', 'issue': "Modern readers hear theological title; first-century readers heard a direct challenge to the emperor's claim to divine sonship"}],
    },
    {
        "id": 'luke',
        "section": 'new-testament',
        "title": 'Book 42: Luke',
        "themes": 'DC SPIRIT SEED NATIONS WOMEN',
        "era_count": 3,
        "chapters": 24,
        "grade": 'A',
        "meta_text": '3 era files &middot; 24 chapters &middot; Grade: A',
        "body_html": '''<p><strong>COSMIC WARFARE THROUGH THE SPIRIT</strong> — "I saw Satan fall like lightning from heaven" (10:18). "Satan has demanded to sift you like wheat" (22:31) — same divine council dynamic as Job 1-2.</p>''',
        "key_claim": "Luke presents the gospel as cosmic warfare through the Spirit — Jesus sees Satan fall like lightning (10:18) and Satan 'demands' to sift Peter (22:31), revealing the same divine council dynamic as Job 1-2 operating behind the scenes of Jesus' ministry.",
        "contested_words": [{'word': 'dynamis', 'greek': 'δύναμις', 'issue': "'Power' — used for the Holy Spirit's empowerment. Luke-Acts is the Spirit narrative: conceived by Spirit, anointed by Spirit, empowered by Spirit, filled with Spirit at Pentecost.", 'severity': 'CRITICAL'}, {'word': 'sozo', 'greek': 'σώζω', 'issue': "'Save/heal' — same Greek word. Luke uses it for physical healing AND spiritual salvation interchangeably, refusing to separate body and soul.", 'severity': 'MAJOR'}, {'word': 'exaiteomai', 'greek': 'ἐξαιτέομαι', 'issue': "Satan 'demanded' (22:31) — legal term for requesting custody. Same dynamic as Job 1-2: Satan petitions the divine council for permission.", 'severity': 'CRITICAL'}],
        "hidden_connections": [{'target': 'job', 'why': "Satan 'demands to sift you like wheat' (22:31) mirrors Job 1-2 — the adversary petitions the divine council for permission to test the righteous"}, {'target': 'leviticus', 'why': "Jesus' inaugural sermon (4:18-19) quotes Isa 61 declaring Jubilee fulfilled — Lev 25's economic reset realized in the kingdom"}, {'target': 'acts', 'why': "Luke-Acts is a unified two-volume work: Luke = Jesus' ministry by the Spirit, Acts = the ekklesia's ministry by the same Spirit"}, {'target': '1samuel', 'why': "Mary's Magnificat (1:46-55) directly echoes Hannah's prayer (1 Sam 2:1-10) — barren woman bearing the deliverer"}, {'target': 'genesis', 'why': "Luke's genealogy (3:23-38) goes back to 'Adam, son of God' — Jesus as the new Adam, reclaiming what the first Adam lost"}],
        "what_it_doesnt_say": ["Never explains how Satan 'fell like lightning from heaven' (10:18) — is this a past event or a present vision?", 'The 70/72 sent out parallel the 70 nations of Gen 10 but Luke never makes the connection explicit', 'Unique parables (Good Samaritan, Prodigal Son, Rich Man and Lazarus) have no parallels — why only Luke?', "Jesus' prayer life is emphasized (11 references to prayer) but what he prays is rarely disclosed"],
        "unusual_characters": [{'name': 'Zechariah', 'ref': '1:5-25', 'detail': "Struck mute for doubting Gabriel — a priest silenced in the temple. His speech returns when he writes 'His name is John.'", 'connections': ['malachi']}, {'name': 'Simeon', 'ref': '2:25-35', 'detail': "Told he would not die before seeing the Messiah. Calls Jesus 'a light for revelation to the Gentiles' — the nations theme from birth.", 'connections': ['isaiah']}, {'name': 'The thief on the cross', 'ref': '23:40-43', 'detail': "'Today you will be with me in Paradise' — only in Luke. Salvation at the last moment, no works, no baptism, just faith.", 'connections': []}],
        "patterns": ["Travel narrative (9:51-19:27): the entire central section is structured as a journey to Jerusalem — Jesus 'sets his face' toward the cross", 'Reversal theme: the rich sent away empty, the poor filled; the first last, the last first; outsiders in, insiders out', 'Prayer bookends: Jesus prays at every major transition — baptism, choosing apostles, transfiguration, Gethsemane, the cross', 'Spirit-power sequence: conceived by Spirit (1:35), anointed by Spirit (3:22), led by Spirit into wilderness (4:1), returns in power of Spirit (4:14) — programmatic for Acts'],
        "mistranslations": [{'english': 'saved', 'original': 'sozo', 'issue': "Splitting 'save' (spiritual) from 'heal' (physical) creates a false divide — Luke uses one word for both because wholeness is the point"}, {'english': 'demanded to have you', 'original': 'exaiteomai', 'issue': 'Often softened — the Greek is a legal demand, a petition before a court. Satan operates within a judicial framework, not chaos'}, {'english': 'power', 'original': 'dynamis', 'issue': 'Generic English hides the specific Spirit-empowerment theology that drives Luke-Acts'}],
    },
    {
        "id": 'john',
        "section": 'new-testament',
        "title": 'Book 43: John',
        "themes": 'DC SEED KING PRIEST HOLY',
        "era_count": 2,
        "chapters": 21,
        "grade": 'A+',
        "meta_text": '2 era files &middot; 21 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>THE DIVINE COUNCIL GOSPEL</strong> — "In the beginning was the Word, and the Word was with God, and the Word was God" (1:1). Two distinct persons, both divine. Jesus quotes Ps 82:6 (10:34-36) affirming the divine council. "Before Abraham was, I AM" (8:58). "Glorify me with the glory I had with you BEFORE the world existed" (17:5).</p>''',
        "key_claim": "John's Prologue ('In the beginning was the Word, and the Word was with God, and the Word was God') establishes Jesus as a pre-existent divine person present at creation — two persons, both called God, one distinct from the other.",
        "contested_words": [{'word': 'logos', 'greek': 'λόγος', 'issue': "'Word' — Greek philosophy (divine reason), Hebrew background (davar YHWH = God's active creative speech), Aramaic memra (divine intermediary). John bridges all three.", 'severity': 'CRITICAL'}, {'word': 'ego eimi', 'greek': 'ἐγώ εἰμι', 'issue': "'I AM' — Jesus' seven absolute 'I AM' statements echo God's self-revelation at the burning bush (Ex 3:14). The Jews try to stone him for it (8:58-59).", 'severity': 'CRITICAL'}, {'word': 'monogenes', 'greek': 'μονογενής', 'issue': "'Only begotten' or 'one and only/unique'? Mono-genes = unique-kind, not mono-gennao (only-born). Shapes whether the Son is 'begotten' or 'unique.'", 'severity': 'CRITICAL'}, {'word': 'parakletos', 'greek': 'παράκλητος', 'issue': "'Comforter/Helper/Advocate' — legal term for a defense attorney. The Spirit is a divine advocate continuing Jesus' work in the divine council's earthly court.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'genesis', 'why': "'In the beginning' (1:1) deliberately echoes Gen 1:1 — the Word who creates in Genesis is now identified as the incarnate Son"}, {'target': 'psalms', 'why': "Jesus quotes Ps 82:6 ('you are gods') in John 10:34 — directly affirming the divine council and using it to defend his own deity claim"}, {'target': 'exodus', 'why': "Seven 'I AM' statements echo Ex 3:14; Jesus replaces every Jewish institution: temple (2:19-21), manna (6:35), light (8:12), Passover lamb (1:29)"}, {'target': '1enoch', 'why': "The 'Son of Man' title in John draws from Dan 7:13 and the Parables of Enoch (1 En 37-71) where the Son of Man is pre-existent and enthroned"}, {'target': 'revelation', 'why': "John 1:1-3 (the Word creating all things) finds its culmination in Rev 19:13 — the returning warrior 'whose name is called The Word of God'"}, {'target': 'isaiah', 'why': "John 12:41 says Isaiah 'saw his glory and spoke of him' — identifying the figure on the throne in Isa 6 as the pre-incarnate Christ"}],
        "what_it_doesnt_say": ["No birth narrative — John goes further back than Bethlehem to 'before the world existed' (17:5)", "No Synoptic parables, no Sermon on the Mount, no exorcisms — John's Jesus teaches through signs and extended discourses", "No account of the institution of the Lord's Supper — replaced by the foot-washing (ch. 13)", "The 'beloved disciple' is never named — tradition says John, but the text deliberately withholds the identity"],
        "unusual_characters": [{'name': 'Nicodemus', 'ref': '3:1', 'detail': "Pharisee who comes at NIGHT — moves from darkness to light across the Gospel (3:1, 7:50, 19:39). A secret disciple's slow emergence.", 'connections': []}, {'name': 'The Samaritan woman', 'ref': '4:7', 'detail': 'Longest one-on-one conversation in the Gospels. Jesus crosses every boundary: gender, ethnic, religious, moral. She becomes an evangelist.', 'connections': []}, {'name': 'Lazarus', 'ref': '11:1', 'detail': 'Raised after four days — specifically to counter the Jewish belief that the soul lingered three days. This is unmistakable resurrection.', 'connections': []}, {'name': 'Thomas', 'ref': '20:24-29', 'detail': "'My Lord and my God' — the highest Christological confession in any Gospel, from the biggest doubter. John's theological climax.", 'connections': []}],
        "patterns": ["Seven signs (water to wine, healing official's son, pool of Bethesda, feeding 5000, walking on water, blind man healed, Lazarus raised) — each reveals a dimension of Jesus' divine identity", "Seven 'I AM' statements with predicates (bread, light, door, shepherd, resurrection, way, vine) plus the absolute 'I AM' (8:58) — eight total, echoing creation's eighth day (resurrection)", "Light vs. darkness motif runs from Prologue (1:5) through Nicodemus at night (3:2) to Judas going out 'and it was night' (13:30) to Easter morning dawn (20:1)", 'Replacement theology: Jesus replaces every Jewish institution — temple, manna, water ceremony, light ceremony, Passover — as the reality behind the shadows'],
        "mistranslations": [{'english': 'only begotten', 'original': 'monogenes', 'issue': "Implies biological generation; the Greek means 'one of a kind/unique' — not about origin but about uniqueness"}, {'english': 'Comforter', 'original': 'parakletos', 'issue': 'Sounds passive and emotional; the Greek is a legal advocate — a defense attorney in the divine court'}, {'english': 'Word', 'original': 'logos', 'issue': "English 'word' sounds like mere speech; logos carries the weight of divine reason, creative agency, and personal intermediary"}],
    },
    {
        "id": 'acts',
        "section": 'new-testament',
        "title": 'Book 44: Acts',
        "themes": 'DC SPIRIT NATIONS BABEL',
        "era_count": 5,
        "chapters": 28,
        "grade": 'A+',
        "meta_text": '5 era files &middot; 28 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>PENTECOST = BABEL REVERSED</strong> — Spirit falls, every nation hears in their own language. The Deut 32:8 allotment reversed. Nations reclaimed. Paul at Areopagus (17:26-27): God determined "allotted periods and boundaries" so nations would "seek God" — the PURPOSE revealed.</p>''',
        "key_claim": 'Pentecost is the reversal of Babel and the Deut 32:8 allotment — the Spirit falls, every nation hears in their own language, and the nations assigned to lesser elohim are reclaimed for YHWH through the ekklesia.',
        "contested_words": [{'word': 'glossa', 'greek': 'γλῶσσα', 'issue': "'Tongues' — at Pentecost, known languages (2:6-11). At Corinth, unknown speech needing interpretation (1 Cor 14). Same word, different phenomena.", 'severity': 'CRITICAL'}, {'word': 'ethnos', 'greek': 'ἔθνος', 'issue': "'Nations/Gentiles' — Paul's mission is to reclaim the ethne allotted to corrupt elohim at Deut 32:8. Every conversion is cosmic territory recaptured.", 'severity': 'CRITICAL'}, {'word': 'horothesia', 'greek': 'ὁροθεσία', 'issue': "'Boundaries' (17:26) — God 'determined allotted periods and boundaries of their dwelling.' Paul at the Areopagus reveals the PURPOSE behind the Deut 32:8 allotment.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'deuteronomy', 'why': 'Pentecost reverses Deut 32:8 — the nations divided among lesser elohim are reunited under YHWH through the Spirit'}, {'target': 'genesis', 'why': 'Babel scattered languages (Gen 11); Pentecost reunites them. The table of nations (Gen 10) becomes the mission field of Acts'}, {'target': 'luke', 'why': 'Acts is volume 2 of Luke-Acts — the Spirit who empowered Jesus in Luke now empowers the ekklesia in Acts'}, {'target': 'joel', 'why': "Peter's Pentecost sermon quotes Joel 2:28-32 — 'I will pour out my Spirit on ALL flesh.' The Spirit is no longer restricted to prophets, priests, and kings"}, {'target': 'daniel', 'why': 'The territorial prince concept (Dan 10) explains why Paul encounters spiritual resistance in specific regions — each territory has a ruling power'}],
        "what_it_doesnt_say": ['Never records the deaths of Paul or Peter — Acts ends abruptly with Paul under house arrest in Rome', 'No mention of what happened to most of the Twelve after Pentecost — only Peter and John get narrative attention', 'Never explains why the Spirit falls differently each time — sometimes with tongues, sometimes without, sometimes with laying on of hands', 'The Jerusalem Council (ch. 15) never addresses the divine council theology behind the Gentile mission — the cosmic framework is assumed, not stated'],
        "unusual_characters": [{'name': 'Stephen', 'ref': '7:55-56', 'detail': "Sees 'the Son of Man STANDING at the right hand of God' — the only time Jesus is described standing, not sitting. Rising to receive the first martyr.", 'connections': ['daniel']}, {'name': 'The Ethiopian eunuch', 'ref': '8:27', 'detail': 'A Gentile, a eunuch (excluded from the assembly in Deut 23:1), reading Isaiah 53 — every barrier broken by the gospel.', 'connections': ['isaiah']}, {'name': 'Cornelius', 'ref': '10:1', 'detail': 'Roman centurion — the Gentile Pentecost. The Spirit falls on uncircumcised pagans before baptism, shattering every category.', 'connections': ['romans']}],
        "patterns": ['Geographical expansion fulfills 1:8 exactly: Jerusalem (chs. 1-7), Judea and Samaria (chs. 8-12), ends of the earth (chs. 13-28)', 'Three conversion accounts of Paul (chs. 9, 22, 26) — each retelling emphasizes different theological aspects for different audiences', 'The Spirit drives every major advance: Pentecost, Samaritan mission, Cornelius, Antioch sending, Macedonian call — human planning follows divine initiative', "Trial scenes parallel Jesus' trials: Stephen before the Sanhedrin, Paul before Jewish courts, Roman governors, and kings — the pattern of witness through suffering"],
        "mistranslations": [{'english': 'church', 'original': 'ekklesia', 'issue': "Every occurrence in Acts should read 'assembly' or 'governing body' — the early movement was a counter-imperial governing structure, not a religious institution"}, {'english': 'Gentiles', 'original': 'ethne', 'issue': "Hides the cosmic dimension — these are the 'nations' allotted to corrupt elohim at Babel, now being reclaimed"}, {'english': 'tongues', 'original': 'glossa', 'issue': 'Makes Pentecost sound like ecstatic gibberish when Acts 2 specifies known languages — every nation hearing in their own tongue'}],
    },
    {
        "id": 'romans',
        "section": 'new-testament',
        "title": 'Book 45: Romans',
        "themes": 'SEED COV DC NATIONS SPIRIT',
        "era_count": 4,
        "chapters": 16,
        "grade": 'A+',
        "meta_text": '4 era files &middot; 16 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>THE COSMIC GOSPEL</strong> — God "gave them over" (1:24, 26, 28) = Deut 32:8 allotment. Creation "subjected to futility" (8:20) = the cosmic consequences. "Neither angels nor rulers nor powers" can separate (8:38-39). "The God of peace will crush Satan under YOUR feet" (16:20) = Gen 3:15 fulfilled through ekklesia.</p>''',
        "key_claim": "Romans reveals the cosmic scope of the gospel: God 'gave them over' (1:24, 26, 28) echoes the Deut 32:8 allotment, creation itself groans under bondage (8:20-22), and the ekklesia will crush Satan underfoot (16:20) — fulfilling Gen 3:15 through Christ's body.",
        "contested_words": [{'word': 'hilasterion', 'greek': 'ἱλαστήριον', 'issue': "'Propitiation/mercy seat' (3:25) — the kapporet, the lid of the Ark where blood was sprinkled on Yom Kippur. Christ IS the mercy seat. Connects to Lev 16 and kaphar.", 'severity': 'CRITICAL'}, {'word': 'paredoken', 'greek': 'παρέδωκεν', 'issue': "'Gave over' (1:24, 26, 28) — three-fold giving over of the nations. This IS the Deut 32:8 allotment described from Paul's perspective.", 'severity': 'CRITICAL'}, {'word': 'stoicheia', 'greek': 'στοιχεῖα', 'issue': "'Elementary principles' or 'elemental spirits'? These are the spiritual powers behind the cosmos — the allotted rulers of the Deut 32 framework.", 'severity': 'MAJOR'}, {'word': 'hyper', 'greek': 'ὑπέρ', 'issue': "Rom 8:31 'God is FOR us' — hyper means more than support; it means 'on behalf of' in a legal/covenantal sense. Divine council advocacy.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'genesis', 'why': "Adam-Christ typology (5:12-21) is the most systematic treatment of Gen 3:15 — one man's trespass, one man's obedience. Rom 16:20 ('crush Satan under your feet') directly echoes Gen 3:15"}, {'target': 'deuteronomy', 'why': "The three-fold 'gave them over' (1:24, 26, 28) echoes the Deut 32:8 allotment — God handed the nations to corrupt spiritual powers"}, {'target': 'leviticus', 'why': 'hilasterion (3:25) = the mercy seat of Lev 16 — Christ IS the kapporet where atonement blood is sprinkled'}, {'target': 'psalms', 'why': 'Rom 3:10-18 strings together Ps 14, 5, 140, 10, 36, Isa 59 — a divine prosecution case using Scripture as evidence'}, {'target': 'habakkuk', 'why': "'The righteous shall live by faith' (1:17) quotes Hab 2:4 — the thesis statement of the entire letter"}, {'target': 'galatians', 'why': "Abraham's faith-righteousness (Rom 4, Gen 15:6) parallels Galatians 3 — justification by faith precedes the Law by 430 years"}],
        "what_it_doesnt_say": ["Never uses the word 'Trinity' — yet Rom 8 has Father, Son, and Spirit all working distinctly in the same passage", "The 'powers and principalities' of 8:38 are listed without explanation — Paul assumes his audience knows the spiritual hierarchy", "Chapters 9-11 (Israel's future) never resolve cleanly — 'all Israel will be saved' (11:26) remains one of the most debated verses in Scripture", "Rom 16:20 ('crush Satan under YOUR feet') transfers Gen 3:15 to the ekklesia without explaining the mechanism"],
        "unusual_characters": [{'name': 'Phoebe', 'ref': '16:1', 'detail': 'Called diakonos (deacon/minister — same word used for Paul) and prostatis (patron/benefactor). She likely carried and read the letter to the Roman assemblies.', 'connections': []}, {'name': 'Junia', 'ref': '16:7', 'detail': "'Outstanding among the apostles' — a woman apostle. Later manuscripts changed the name to masculine 'Junias' but no male name 'Junias' exists in ancient sources.", 'connections': []}, {'name': 'Adam', 'ref': '5:14', 'detail': "Called 'a type of the one to come' — the first explicit typological framework. Adam's failure is the template Christ reverses.", 'connections': ['genesis', '1corinthians']}],
        "patterns": ["Courtroom structure: indictment (1:18-3:20), verdict of grace (3:21-5:21), new life (6-8), Israel's case (9-11), life in the Spirit (12-16)", "Three-fold 'gave them over' (1:24, 26, 28) — escalating divine judgment that mirrors the Deut 32:8 allotment", "The 'therefore' chain: 3:20, 5:1, 8:1, 12:1 — each 'therefore' introduces the next phase of the argument. 'Therefore' in 12:1 pivots from theology to practice", 'Rom 8 forms an inclusio with Gen 3: creation subjected to futility (8:20) will be liberated (8:21) — the cosmic curse reversed'],
        "mistranslations": [{'english': 'propitiation', 'original': 'hilasterion', 'issue': 'Abstract theological term hides the concrete image — the mercy seat where blood was sprinkled. Christ IS the furniture of the Holy of Holies'}, {'english': 'gave them up', 'original': 'paredoken', 'issue': 'Sounds like abandonment; the Greek is a judicial handing-over — a divine council act of consigning nations to their chosen gods'}, {'english': 'elementary principles', 'original': 'stoicheia', 'issue': 'Makes it sound like ABCs when Paul may mean the spiritual powers governing the cosmos — personal beings, not abstract concepts'}],
    },
    {
        "id": '1corinthians',
        "section": 'new-testament',
        "title": 'Book 46: 1 Corinthians',
        "themes": 'DC SPIRIT TYPE',
        "era_count": 3,
        "chapters": 16,
        "meta_text": '3 era files &middot; 16 chapters',
        "body_html": '''<p>"None of the rulers (archontes) of this age understood, for if they had, they would not have crucified the Lord of glory" (2:8). "Do you not know we are to judge ANGELS?" (6:3). "The last enemy to be destroyed is death" (15:26).</p>''',
        "key_claim": "The 'rulers of this age' who crucified Christ (2:8) are spiritual powers — archontes — who failed to understand the hidden wisdom of God, and the ekklesia is destined to judge angels (6:3), exercising authority over the very beings that rule the nations.",
        "contested_words": [{'word': 'archontes', 'greek': 'ἄρχοντες', 'issue': "'Rulers of this age' (2:8) — human rulers or spiritual powers? The context ('none of them understood' the hidden wisdom) points to cosmic powers who orchestrated the cross without grasping its meaning.", 'severity': 'CRITICAL'}, {'word': 'teleios', 'greek': 'τέλειος', 'issue': "'Perfect/complete' (13:10) — 'when the perfect comes.' Cessationists say = completed canon. But teleios means 'mature/complete' and 1 Cor 13:12 explains it as seeing 'face to face' = Christ's return.", 'severity': 'CRITICAL'}, {'word': 'soma', 'greek': 'σῶμα', 'issue': "'Body' — Paul's body metaphor for the ekklesia (ch. 12) is not a mere illustration but an ontological claim about corporate identity in Christ.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'exodus', 'why': "'Christ our Passover lamb has been sacrificed' (5:7) — direct identification of Jesus with the Exodus 12 lamb. Passover typology fulfilled"}, {'target': 'genesis', 'why': "Adam-Christ contrast continues: 'the first Adam became a living being; the last Adam became a life-giving spirit' (15:45) — Gen 2:7 reinterpreted"}, {'target': 'daniel', 'why': "The resurrection body discussion (ch. 15) connects to Dan 12:2-3 — those raised 'shall shine like the stars,' a divine council image"}, {'target': 'psalms', 'why': "'He must reign until he has put all enemies under his feet' (15:25) quotes Ps 110:1 — the enthroned Son subduing all powers"}, {'target': 'numbers', 'why': "Israel's wilderness failures are 'examples for us' (10:6, 11) — Paul reads Numbers typologically"}],
        "what_it_doesnt_say": ["Never defines who the 'rulers of this age' are — spiritual or political? Paul leaves the ambiguity as a test of worldview", "'We shall judge angels' (6:3) is stated without any explanation of how, when, or which angels", "The nature of 'tongues of angels' (13:1) is never explained — are these actual angelic languages?", "No timeline given for 'when the perfect comes' (13:10) — the debate between Christ's return and the completed canon remains unresolved in the text itself"],
        "unusual_characters": [{'name': 'The man delivered to Satan', 'ref': '5:5', 'detail': "'Deliver this man to Satan for the destruction of the flesh, that his spirit may be saved.' Paul uses divine council authority to hand someone to the adversary — same framework as Job 1-2.", 'connections': ['job', '1timothy']}, {'name': "Chloe's people", 'ref': '1:11', 'detail': "A woman's household reports the church divisions — a woman is Paul's intelligence network in Corinth.", 'connections': []}],
        "patterns": ["Already/not yet tension: 'you were washed, sanctified, justified' (6:11) past tense, yet 'we shall be changed' (15:52) future — inaugurated eschatology", 'Wisdom reversal: God chose the foolish to shame the wise (1:27) — the cross inverts every human power hierarchy', 'Body metaphor: individual body (ch. 6, sexual ethics), corporate body (ch. 12, spiritual gifts), resurrection body (ch. 15) — three dimensions of soma', "Each problem Paul addresses traces back to a worldview failure — Corinth's issues are theological, not merely behavioral"],
        "mistranslations": [{'english': 'rulers', 'original': 'archontes', 'issue': "Could mean human rulers or spiritual powers — most translations default to 'rulers' without flagging the spiritual dimension"}, {'english': 'perfect', 'original': 'teleios', 'issue': "'Perfect' in English implies flawless; the Greek means 'mature/complete/arrived at telos' — the cessationism debate hangs on this one word"}, {'english': 'charity', 'original': 'agape', 'issue': "KJV's 'charity' reduces divine self-giving love to human generosity — agape is covenant faithfulness in action"}],
    },
    {
        "id": '2corinthians',
        "section": 'new-testament',
        "title": 'Book 47: 2 Corinthians',
        "themes": 'DC SPIRIT',
        "era_count": 3,
        "chapters": 13,
        "meta_text": '3 era files &middot; 13 chapters',
        "body_html": '''<p>"The god of this age (ho theos tou aionos) has blinded minds" (4:4). Satan called "god" — a Deut 32:8 territorial deity. Paul caught up to "the third heaven" (12:2-4) — divine council access.</p>''',
        "key_claim": "Paul identifies Satan as 'the god of this age' (4:4) who blinds minds — a direct reference to the Deut 32:8 territorial deity framework — and Paul himself has been caught up to 'the third heaven' (12:2), gaining divine council access.",
        "contested_words": [{'word': 'ho theos tou aionos', 'greek': 'ὁ θεὸς τοῦ αἰῶνος', 'issue': "'The god of this age' (4:4) — Satan called 'god' (theos). This is Deut 32:8 language: a spiritual being ruling over territory with divine authority.", 'severity': 'CRITICAL'}, {'word': 'tritos ouranos', 'greek': 'τρίτος οὐρανός', 'issue': "'Third heaven' (12:2) — cosmological layers: atmosphere, stars, God's throne. Paul claims divine council access — he has been to the throne room.", 'severity': 'CRITICAL'}, {'word': 'metamorphoo', 'greek': 'μεταμορφόω', 'issue': "'Transformed' (3:18) — same word used for the Transfiguration. Believers are being metamorphosed into the image of Christ progressively.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'deuteronomy', 'why': "'The god of this age' (4:4) is a Deut 32:8 territorial deity — Satan as one of the allotted elohim who corrupted his assignment"}, {'target': 'job', 'why': "Paul's 'thorn in the flesh, a messenger of Satan' (12:7) mirrors Job's framework — satanic affliction permitted by God for divine purposes"}, {'target': 'exodus', 'why': "Moses' veiled face (3:13-16) reinterpreted — the veil hides the fading glory of the old covenant. Christ removes it"}, {'target': 'genesis', 'why': "'God who said let light shine out of darkness' (4:6) — new creation language echoing Gen 1:3. The gospel is re-creation"}, {'target': 'isaiah', 'why': "'Behold, now is the day of salvation' (6:2) quotes Isa 49:8 — the servant's mission becomes the present reality"}],
        "what_it_doesnt_say": ["The 'third heaven' experience (12:2-4) — Paul heard 'things that cannot be told, which man may not utter.' What did he hear?", "The 'thorn in the flesh' (12:7) is never identified — physical ailment, spiritual opposition, or something else?", "Paul mentions 'super-apostles' (11:5) but never names them — who were his opponents in Corinth?", "The nature of the 'treasure in jars of clay' (4:7) is cosmic power in human weakness, but the mechanism is never explained"],
        "unusual_characters": [{'name': 'The god of this age', 'ref': '4:4', 'detail': "Satan given the title theos (god) — a divine being ruling a territorial domain, not merely a tempter. Deut 32:8 framework in Paul's own words.", 'connections': ['deuteronomy', 'ephesians']}, {'name': "Paul's thorn messenger", 'ref': '12:7', 'detail': "A 'messenger of Satan' (angelos satana) — a spirit being dispatched by the adversary, permitted by God to keep Paul humble.", 'connections': ['job']}],
        "patterns": ["Weakness-power paradox: 'when I am weak, then I am strong' (12:10) — divine power operates through human vulnerability, not despite it", "New creation language: 'if anyone is in Christ, new creation' (5:17) — the gospel is not reformation but RE-creation, echoing Genesis 1", 'Ministry of the Spirit vs. ministry of death (ch. 3): old covenant → glory that fades; new covenant → glory that increases. Progressive transformation', "Fool's speech (chs. 11-12): Paul inverts boasting — instead of achievements, he boasts of sufferings, weaknesses, and divine encounters"],
        "mistranslations": [{'english': 'god of this world', 'original': 'ho theos tou aionos', 'issue': "'World' obscures 'age' (aion) — Satan rules a temporal domain, not just a geographical one. His authority has an expiration date"}, {'english': 'caught up', 'original': 'harpazo', 'issue': 'Sounds passive; the Greek implies violent seizure — Paul was snatched up to heaven, not gently transported'}, {'english': 'transformed', 'original': 'metamorphoo', 'issue': "English 'transformed' is too vague — this is metamorphosis, the same word for Christ's transfiguration"}],
    },
    {
        "id": 'galatians',
        "section": 'new-testament',
        "title": 'Book 48: Galatians',
        "themes": 'SEED COV NATIONS',
        "era_count": 2,
        "chapters": 6,
        "meta_text": '2 era files &middot; 6 chapters',
        "body_html": '''<p>"It does not say 'seeds' but 'seed,' referring to ONE, who is Christ" (3:16). Gen 3:15 is SINGULAR. Law "ordained through angels" (3:19). Before Christ, enslaved to stoicheia tou kosmou (4:3, 9) — the allotted elemental powers.</p>''',
        "key_claim": "Paul argues that the 'seed' (sperma) promised to Abraham is SINGULAR — 'referring to one, who is Christ' (3:16) — proving Gen 3:15's zera is fulfilled in one person, and before Christ humanity was enslaved to the stoicheia tou kosmou, the elemental spiritual powers governing the nations.",
        "contested_words": [{'word': 'sperma', 'greek': 'σπέρμα', 'issue': "'Seed' (3:16) — Paul makes the singular-vs-plural argument central. Gen 3:15's zera and Gen 12:7's seed are SINGULAR = Christ. The entire Bible narrows to one person.", 'severity': 'CRITICAL'}, {'word': 'stoicheia tou kosmou', 'greek': 'στοιχεῖα τοῦ κόσμου', 'issue': "'Elementary principles of the world' or 'elemental spirits of the cosmos'? (4:3, 9). Before Christ, humanity was enslaved to spiritual powers — the allotted elohim.", 'severity': 'CRITICAL'}, {'word': 'diatageis di angelon', 'greek': 'διαταγεὶς δι’ ἀγγέλων', 'issue': "Law 'ordained through angels' (3:19) — the Torah was mediated by divine council beings. Confirmed by Acts 7:53 and Heb 2:2.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'genesis', 'why': "The seed promise (Gen 3:15, 12:7) is Paul's central argument — sperma is singular, pointing to Christ alone"}, {'target': 'deuteronomy', 'why': 'The stoicheia enslavement parallels the Deut 32:8 allotment — before Christ, nations were under the authority of allotted spiritual powers'}, {'target': 'romans', 'why': "Abraham's faith-righteousness (Gal 3:6, Gen 15:6) parallels Rom 4 — justification by faith precedes the Law by 430 years"}, {'target': 'colossians', 'why': "stoicheia tou kosmou appears in both Gal 4:3 and Col 2:8, 20 — Paul's consistent framework of spiritual powers behind earthly systems"}, {'target': 'acts', 'why': "Gal 2 records the Jerusalem Council from Paul's perspective — the Gentile mission's theological foundation"}],
        "what_it_doesnt_say": ["Never explains WHO the stoicheia are — personal beings or impersonal forces? Paul's other letters suggest personal powers", "How angels 'ordained' the Law (3:19) is never detailed — what role did divine council beings play at Sinai?", "'Neither male nor female in Christ' (3:28) — Paul never works out the social implications in this letter", "The 'Jerusalem above is our mother' (4:26) is introduced without explanation of the heavenly Jerusalem concept"],
        "unusual_characters": [{'name': 'Abraham', 'ref': '3:6-9', 'detail': "Paul's primary example: justified by faith 430 years BEFORE the Law existed. If Abraham was righteous without Torah, Torah cannot be the path to righteousness.", 'connections': ['genesis', 'romans', 'hebrews']}, {'name': 'Hagar and Sarah', 'ref': '4:21-31', 'detail': 'Allegorized as two covenants: Sinai (slavery) vs. promise (freedom). Bold reinterpretation of Gen 16-21.', 'connections': ['genesis']}],
        "patterns": ["Before/after Christ structure: enslaved to stoicheia (4:3) → 'when the fullness of time came' (4:4) → adopted as sons (4:5). The turning point is incarnation", 'Freedom-slavery binary: the entire letter oscillates between freedom in Christ and slavery to law/flesh/powers', "Autobiography as theology: Paul's conversion (chs. 1-2) is not memoir but evidence that the gospel comes from revelation, not human tradition", "Fruit vs. works contrast (5:19-23): 'works of the flesh' (human striving) vs. 'fruit of the Spirit' (divine production) — singular 'fruit,' one organic reality"],
        "mistranslations": [{'english': 'elementary principles', 'original': 'stoicheia tou kosmou', 'issue': 'Makes enslaving cosmic powers sound like ABCs — hides the spiritual warfare dimension of pre-Christian existence'}, {'english': 'seed', 'original': 'sperma', 'issue': "Modern readers miss Paul's singular-plural argument — the English 'seed' can be either, but Paul's whole argument rests on the singular"}, {'english': 'ordained by angels', 'original': 'diatageis di angelon', 'issue': 'Often footnoted rather than translated — the angelic mediation of Torah is theologically explosive and usually suppressed'}],
    },
    {
        "id": 'ephesians',
        "section": 'new-testament',
        "title": 'Book 49: Ephesians',
        "themes": 'DC SPIRIT NATIONS',
        "era_count": 2,
        "chapters": 6,
        "grade": 'A+',
        "meta_text": '2 era files &middot; 6 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>THE SPIRITUAL WARFARE EPISTLE</strong> — "Through the ekklesia the wisdom of God is made known to the rulers and authorities in heavenly places" (3:10). The ekklesia — God's governing assembly — teaches the COUNCIL. Eph 6:12: "We wrestle not against flesh and blood but against rulers, authorities, cosmic powers, spiritual forces of evil in heavenly places." Most explicit spiritual warfare passage in NT.</p>''',
        "key_claim": 'Through the ekklesia, the manifold wisdom of God is made known to the rulers and authorities in heavenly places (3:10) — the governing assembly of believers TEACHES the divine council, and the battle is not against flesh and blood but against cosmic powers in the heavenlies (6:12).',
        "contested_words": [{'word': 'ta epourania', 'greek': 'τὰ ἐπουράνια', 'issue': "'Heavenly places' — appears 5 times in Ephesians (1:3, 20; 2:6; 3:10; 6:12). The spiritual realm where Christ is enthroned AND where hostile powers operate. Same space, contested territory.", 'severity': 'CRITICAL'}, {'word': 'kosmokratores', 'greek': 'κοσμοκράτορες', 'issue': "'Cosmic powers/world rulers' (6:12) — a term used in astrology for planetary deities ruling earthly affairs. Paul co-opts pagan language to describe real spiritual enemies.", 'severity': 'CRITICAL'}, {'word': 'mysterion', 'greek': 'μυστήριον', 'issue': "'Mystery' (3:3-6) — not a puzzle to solve but a hidden plan now revealed: Gentiles are co-heirs. The Deut 32:8 allotment is being reversed.", 'severity': 'MAJOR'}, {'word': 'panoplia', 'greek': 'πανοπλία', 'issue': "'Full armor' (6:11) — complete Roman military kit. Each piece maps to a spiritual reality. The battle is real and requires real equipment.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'deuteronomy', 'why': 'The Gentile inclusion (2:11-22) reverses the Deut 32:8 allotment — the dividing wall between Jew and Gentile is demolished because the cosmic partition is abolished'}, {'target': 'daniel', 'why': "The 'rulers and authorities in heavenly places' (3:10, 6:12) are the territorial princes of Dan 10 — the ekklesia now confronts them with God's wisdom"}, {'target': 'genesis', 'why': "'Predestined before the foundation of the world' (1:4) — God's plan precedes creation, precedes the Fall, precedes the allotment"}, {'target': 'colossians', 'why': 'Ephesians and Colossians are sister letters — Col 2:15 (disarming powers at the cross) is the victory; Eph 6:12 is the ongoing enforcement'}, {'target': 'isaiah', 'why': "The armor of God (6:14-17) draws from Isa 59:17 where YHWH himself puts on armor — believers wear GOD's own battle gear"}],
        "what_it_doesnt_say": ["HOW the ekklesia makes known God's wisdom to cosmic powers (3:10) is never explained — by its existence? Its worship? Its proclamation?", "The 'mystery of Christ' (3:4) was 'not made known to sons of men in other generations' — who ARE the 'sons of men' here? Humans or divine beings?", "'He descended into the lower regions of the earth' (4:9) — Sheol, the grave, or earth itself? The descent is never clarified", 'The armor passage (6:10-20) assumes the battle is already happening but never says who initiates the attacks or how they manifest'],
        "unusual_characters": [{'name': 'The kosmokratores', 'ref': '6:12', 'detail': "'World rulers of this darkness' — astral powers governing earthly territories. The most explicit naming of the spiritual hierarchy in Paul's letters.", 'connections': ['daniel', 'deuteronomy', 'colossians']}, {'name': "The 'one new man'", 'ref': '2:15', 'detail': 'Jew and Gentile fused into a single new humanity in Christ — not Gentiles becoming Jewish or Jews becoming Gentile, but a third category entirely.', 'connections': ['galatians']}],
        "patterns": ['Heavenly places (ta epourania) as contested space: believers seated there (2:6), Christ enthroned there (1:20), hostile powers there (3:10, 6:12) — one realm, multiple occupants', "Prayer → power → cosmic purpose: the prayer of 1:17-23 leads to resurrection power leads to cosmic authority. Paul's prayers are not personal comfort but cosmic commission", "The body metaphor matures: from individual gifts (1 Cor 12) to cosmic entity making God's wisdom known to spiritual powers (3:10) — the ekklesia has a supernatural audience", "Walk language: 'walk worthy' (4:1), 'no longer walk as Gentiles' (4:17), 'walk in love' (5:2), 'walk as children of light' (5:8), 'walk carefully' (5:15) — progressive transformation"],
        "mistranslations": [{'english': 'heavenly realms', 'original': 'ta epourania', 'issue': 'Sounds like a distant afterlife destination; Paul means the present spiritual dimension where cosmic powers operate and believers are already seated with Christ'}, {'english': 'rulers of darkness', 'original': 'kosmokratores tou skotous', 'issue': "'World rulers' is too tame — kosmokratores implies governing authority over the entire cosmos, not just 'dark rulers'"}, {'english': 'struggle', 'original': 'pale', 'issue': "'Struggle' softens what is literally hand-to-hand wrestling — the spiritual battle is close combat, not distant warfare"}],
    },
    {
        "id": 'philippians',
        "section": 'new-testament',
        "title": 'Book 50: Philippians',
        "themes": 'DC SEED',
        "era_count": 2,
        "chapters": 4,
        "meta_text": '2 era files &middot; 4 chapters',
        "body_html": '''<p><strong>THE CHRIST HYMN</strong> (2:5-11) — "In the form of God (morphe theou)... emptied himself... the NAME above every name... every knee shall bow, in heaven and on earth and under the earth." Three realms bow: heaven (council), earth (humanity), under earth (imprisoned).</p>''',
        "key_claim": "The Christ Hymn (2:5-11) declares that Jesus existed 'in the form of God' (morphe theou), emptied himself, and is now exalted so that every knee bows in three realms — heaven (the divine council), earth (humanity), and under the earth (imprisoned spirits).",
        "contested_words": [{'word': 'morphe theou', 'greek': 'μορφὴ θεοῦ', 'issue': "'Form of God' (2:6) — morphe = essential nature, not mere appearance. Christ possessed the divine nature before incarnation. NOT a lesser being promoted.", 'severity': 'CRITICAL'}, {'word': 'kenoo', 'greek': 'κενόω', 'issue': "'Emptied himself' (2:7) — kenosis. What did he empty? Not divinity itself but the privileges and prerogatives of divine status. He did not cease to be God but ceased to live as God.", 'severity': 'CRITICAL'}, {'word': 'harpagmos', 'greek': 'ἁρπαγμός', 'issue': "'Something to be grasped' (2:6) — did not consider equality with God something to exploit/cling to. Contrasts with Adam who DID grasp at being 'like God' (Gen 3:5).", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'genesis', 'why': "The Christ Hymn reverses Adam's grasping: Adam reached for equality with God (Gen 3:5); Christ, already possessing it, emptied himself — the anti-Adam"}, {'target': 'isaiah', 'why': "'Every knee shall bow' (2:10) quotes Isa 45:23 — a passage about YHWH alone. Paul applies YHWH's exclusive prerogative to Jesus"}, {'target': '1peter', 'why': "Three realms bow: heaven, earth, under the earth — the imprisoned spirits of 1 Pet 3:19 are forced to acknowledge Christ's lordship"}, {'target': 'revelation', 'why': "The universal acclamation 'Jesus Christ is Lord' (2:11) prefigures Rev 5:13 — every creature in every realm confessing"}, {'target': 'colossians', 'why': 'Col 1:15-20 (Christ hymn) parallels Phil 2:5-11 — both pre-existence, both cosmic scope, both exaltation after humiliation'}],
        "what_it_doesnt_say": ['WHAT Jesus emptied himself of is never specified — divinity? Glory? Power? The text says morphe doulou (form of a servant) but not what was relinquished', "The three-realm acclamation (heaven, earth, under earth) never explains who 'under the earth' includes — imprisoned Watchers? Dead humans? Both?", 'Why Philippi specifically receives this christological hymn — was there a specific heresy or situation prompting it?'],
        "unusual_characters": [{'name': 'Epaphroditus', 'ref': '2:25-30', 'detail': "Nearly died serving Paul. Called 'fellow soldier' (systratiotes) — military language for the spiritual battle.", 'connections': []}, {'name': 'Euodia and Syntyche', 'ref': '4:2-3', 'detail': "Two women leaders 'who have labored side by side with me in the gospel' — Paul names women as co-workers in the cosmic mission.", 'connections': []}],
        "patterns": ["Kenosis pattern: divine status → voluntary humiliation → exaltation above all. The same pattern shapes Christian ethics: 'have this mind among yourselves' (2:5)", "Joy in suffering: Paul writes from prison yet 'joy/rejoice' appears 16 times — suffering and joy are not opposites but companions in the cosmic mission", 'Three-realm cosmology: heaven, earth, under earth (2:10) — the entire created order, visible and invisible, acknowledges Christ. No territory exempt'],
        "mistranslations": [{'english': 'being in the form of God', 'original': 'en morphe theou hyparchon', 'issue': "'Being' sounds static; the Greek participle hyparchon means 'existing as/continuously being' — Christ's divinity is ontological and ongoing, not a phase"}, {'english': 'made himself nothing', 'original': 'heauton ekenosen', 'issue': "NIV's 'made himself nothing' goes too far — 'emptied himself' preserves the mystery of what was and wasn't relinquished"}, {'english': 'every knee should bow', 'original': 'pan gony kampse', 'issue': "'Should' implies optional; the Greek is future indicative — every knee WILL bow, without exception"}],
    },
    {
        "id": 'colossians',
        "section": 'new-testament',
        "title": 'Book 51: Colossians',
        "themes": 'DC SEED',
        "era_count": 2,
        "chapters": 4,
        "meta_text": '2 era files &middot; 4 chapters',
        "body_html": '''<p>"By him all things were created — thrones, dominions, rulers, authorities — all through him and for him" (1:16). The council was CREATED BY Christ. "He disarmed the rulers and authorities, triumphing over them in the cross" (2:15). The Cross is VICTORY.</p>''',
        "key_claim": "Christ created the entire spiritual hierarchy — thrones, dominions, rulers, authorities (1:16) — and then disarmed them at the cross, making a public spectacle of them in triumphal procession (2:15). The Creator defeated his own creation's rebellion.",
        "contested_words": [{'word': 'thronoi, kyriotetes, archai, exousiai', 'greek': 'θρόνοι, κυριότητες, ἀρχαί, ἐξουσίαι', 'issue': 'Four ranks of spiritual powers (1:16) — the most detailed hierarchy in Paul. Created BY Christ, created FOR Christ. Their rebellion does not cancel their origin.', 'severity': 'CRITICAL'}, {'word': 'apekdysamenos', 'greek': 'ἀπεκδυσάμενος', 'issue': "'Disarmed/stripped' (2:15) — middle voice: Christ himself stripped the powers. Like a victorious general stripping armor from defeated enemies in a Roman triumph.", 'severity': 'CRITICAL'}, {'word': 'stoicheia tou kosmou', 'greek': 'στοιχεῖα τοῦ κόσμου', 'issue': "'Elemental spirits of the world' (2:8, 20) — same as Gal 4:3. The spiritual powers behind human religion and philosophy. You died WITH Christ to their authority.", 'severity': 'CRITICAL'}],
        "hidden_connections": [{'target': 'ephesians', 'why': 'Sister letter: Col 2:15 (disarming powers at the cross) provides the VICTORY; Eph 6:12 describes the ongoing ENFORCEMENT of that victory'}, {'target': 'genesis', 'why': "'Firstborn of all creation' (1:15) echoes Gen 1 — Christ is not the first creature but the one who holds primacy over all creation, as creator"}, {'target': 'philippians', 'why': 'Col 1:15-20 and Phil 2:5-11 are parallel Christ hymns: pre-existence, creative agency, cosmic supremacy, exaltation'}, {'target': 'galatians', 'why': 'stoicheia tou kosmou appears in both — the enslaving powers are the same whether addressed to Galatia or Colossae'}, {'target': 'hebrews', 'why': "Christ as 'image of the invisible God' (1:15) connects to Heb 1:3 'exact imprint of his nature' — both establish divine Christology"}],
        "what_it_doesnt_say": ['The four-tier hierarchy (thrones, dominions, rulers, authorities) is listed without explaining the differences between the ranks', 'HOW Christ disarmed the powers at the cross is not explained — was it the act of dying? The resurrection? The descent?', "The 'Colossian heresy' Paul combats is never named — was it proto-Gnostic, Jewish mystical, or pagan? Scholars disagree", "'Worship of angels' (2:18) — were they worshipping angels or participating in angelic worship? The Greek is ambiguous"],
        "unusual_characters": [{'name': 'The cosmic Christ', 'ref': '1:15-20', 'detail': 'Not merely a teacher or prophet but the creator and sustainer of all things visible and invisible — including the powers that oppose him.', 'connections': ['john', 'hebrews']}, {'name': 'Onesimus', 'ref': '4:9', 'detail': "Called 'faithful and beloved brother, who is one of you' — the runaway slave of Philemon, now sent back as a brother in Christ.", 'connections': ['philemon']}],
        "patterns": ["Christ hymn structure (1:15-20): two stanzas — Christ's role in creation (15-17) and Christ's role in redemption (18-20). Cosmic scope in both", "Died with / raised with: 'you died with Christ to the stoicheia' (2:20), 'you have been raised with Christ' (3:1) — the believer's position change is cosmic, not merely personal", 'Put off / put on: old self (3:9) stripped off, new self (3:10) put on — the language of investiture, like a priest putting on garments for service'],
        "mistranslations": [{'english': 'powers and authorities', 'original': 'archai kai exousiai', 'issue': "Generic English obscures the specific spiritual hierarchy — these are ranked beings with defined jurisdictions, not vague 'forces'"}, {'english': 'made a public spectacle', 'original': 'edeigmatisen en parrhesia', 'issue': 'The image is a Roman triumphal procession — conquered enemies paraded in chains. The cross is not defeat but a victory parade'}, {'english': 'basic principles', 'original': 'stoicheia tou kosmou', 'issue': "Reduces enslaving cosmic spirits to 'elementary teachings' — hides the spiritual warfare dimension"}],
    },
    {
        "id": '1thessalonians',
        "section": 'new-testament',
        "title": 'Books 52-53: 1-2 Thessalonians',
        "themes": 'SPIRIT',
        "era_count": 4,
        "chapters": 8,
        "meta_text": '4 era files &middot; 8 chapters',
        "body_html": '''<p>"The Lord himself will descend with the voice of an archangel and the trumpet of God" (1 Thess 4:16). "The man of lawlessness exalts himself against every so-called god" (2 Thess 2:4) — anti-council figure.</p>''',
        "key_claim": "Christ's return involves the full apparatus of the divine council: 'the Lord himself will descend with a cry of command, with the voice of an archangel, and with the trumpet of God' (4:16) — and 'the man of lawlessness exalts himself against every so-called god' (2 Thess 2:4), an anti-council figure claiming supremacy over all spiritual powers.",
        "contested_words": [{'word': 'parousia', 'greek': 'παρουσία', 'issue': "'Coming' (4:15) — technical term for an emperor's official visit to a city. Citizens go OUT to meet him and escort him IN. Not 'rapture away' but 'welcoming the returning king.'", 'severity': 'CRITICAL'}, {'word': 'apantesis', 'greek': 'ἀπάντησις', 'issue': "'To meet' (4:17) — civic reception term: citizens going out to meet a dignitary and escorting him back to the city. Not departure but reception.", 'severity': 'CRITICAL'}, {'word': 'ho anomos', 'greek': 'ὁ ἄνομος', 'issue': "'The lawless one' (2 Thess 2:3) — exalts himself above every 'so-called god or object of worship.' An anti-council figure claiming authority over all spiritual hierarchies.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'daniel', 'why': "The 'man of lawlessness' exalting himself (2 Thess 2:4) echoes Dan 11:36 — the arrogant king who magnifies himself above every god"}, {'target': 'exodus', 'why': "'The trumpet of God' (4:16) echoes the Sinai theophany (Ex 19:16) — Christ's return is a new Sinai, a new divine encounter"}, {'target': 'revelation', 'why': 'The parousia imagery (4:16-17) parallels Rev 19:11-16 — the returning King with heavenly armies'}, {'target': 'isaiah', 'why': "'Peace and security, then sudden destruction' (5:3) echoes Isa 13:6-8 — the Day of the LORD as birth pains, sudden and inescapable"}],
        "what_it_doesnt_say": ["Never uses the word 'rapture' — the concept of being 'caught up' (harpazo) is about meeting the returning King, not escaping earth", "The identity of 'the restrainer' (2 Thess 2:6-7) is never revealed — one of the biggest mysteries in the NT", 'The timeline between the events of 4:16-17 is compressed — are these sequential moments or a single event?', 'Paul never addresses what happens to those alive DURING the tribulation — only the dead and the living at the parousia'],
        "unusual_characters": [{'name': 'The archangel', 'ref': '4:16', 'detail': "An unnamed archangel whose voice accompanies the Lord's descent — divine council herald announcing the King's return.", 'connections': ['daniel', 'jude', 'revelation']}, {'name': 'The restrainer', 'ref': '2 Thess 2:6-7', 'detail': "'You know what restrains him now' — Paul's audience knew but we don't. The Holy Spirit? Rome? An angelic being? The mystery persists.", 'connections': []}],
        "patterns": ['Parousia as civic reception (apantesis): the imagery is citizens going OUT of the city to meet the returning emperor and escorting him IN — not escape but welcome', "Already/not yet: 'you turned from idols to serve the living God' (1:9) — past event; 'to wait for his Son from heaven' (1:10) — future hope. Both equally real", "Day vs. night imagery (5:1-11): believers are 'children of light/day,' not caught off guard — spiritual wakefulness as the posture of waiting"],
        "mistranslations": [{'english': 'caught up', 'original': 'harpazo', 'issue': "Basis for 'rapture' theology — but the context is an apantesis (civic welcome), not an evacuation. Believers meet Christ to escort him to earth, not flee from it"}, {'english': 'coming', 'original': 'parousia', 'issue': "Generic 'coming' hides the imperial-visit context — this is a king arriving to take possession of his territory"}, {'english': 'man of sin', 'original': 'ho anthropos tes anomias', 'issue': "KJV 'man of sin' obscures 'man of lawlessness' — the figure is anti-Torah, anti-order, anti-council, not merely morally sinful"}],
    },
    {
        "id": '2thessalonians',
        "section": 'new-testament',
        "title": 'Book 53: 2 Thessalonians',
        "themes": 'SPIRIT DC REBEL',
        "era_count": 2,
        "chapters": 3,
        "grade": 'B+',
        "meta_text": '2 era files &middot; 3 chapters &middot; Grade: B+',
        "body_html": '''<h4>Major Themes</h4>
  <div class="theme-grid">
    <span class="badge badge-theme">MAN OF LAWLESSNESS</span><span class="badge badge-theme">THE RESTRAINER</span><span class="badge badge-theme">DAY OF THE LORD</span><span class="badge badge-theme">DIVINE COUNCIL</span><span class="badge badge-theme">DECEPTION</span>
  </div>
  <p><strong>MAN OF LAWLESSNESS</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; "The man of lawlessness is revealed, the son of destruction, who opposes and exalts himself against every so-called god (theos) or object of worship, so that he takes his seat in the temple of God, proclaiming himself to be God" (2:3-4). This is a divine council concept &mdash; the anti-messiah figure who usurps the position above all spiritual authorities.</p>
  <p><strong>THE RESTRAINER</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; "You know what is restraining him now" (2:6) and "he who now restrains" (2:7). Paul&rsquo;s audience knew the identity &mdash; we don&rsquo;t. The Holy Spirit? Michael the archangel? Rome? A divine council agent holding back chaos until the appointed time.</p>
  <p><strong>STRONG DELUSION</strong> <span class="badge badge-major">MAJOR</span> &mdash; "God sends them a strong delusion (energeian planes), so that they may believe what is false" (2:11). Like the lying spirit in 1 Kings 22, divine council agents can be dispatched to deceive those who refuse truth &mdash; judgment through deception.</p>

  <h4>Contested Words</h4>
  <table class="ref-table">
    <tr><th>Greek</th><th>Issue</th><th>Severity</th></tr>
    <tr><td><strong>ho anomos</strong> (&omicron; &alpha;&nu;&omicron;&mu;&omicron;&sigmaf;)</td><td>"The lawless one" (2:8) &mdash; not merely immoral but anti-Torah, anti-order, anti-council. He opposes every divine authority structure. Christ will destroy him "by the breath of his mouth."</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>to katechon / ho katechon</strong></td><td>"The restrainer" (2:6-7) &mdash; neuter (to katechon, "what restrains") and masculine (ho katechon, "he who restrains"). Both a thing and a person. One of the NT&rsquo;s greatest mysteries.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>energeian planes</strong> (&epsilon;&nu;&epsilon;&rho;&gamma;&epsilon;&iota;&alpha;&nu; &pi;&lambda;&alpha;&nu;&eta;&sigmaf;)</td><td>"Working of error/strong delusion" (2:11) &mdash; energeia = active supernatural power. This is not mere confusion but divinely empowered deception sent as judgment.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>apostasia</strong> (&alpha;&pi;&omicron;&sigma;&tau;&alpha;&sigma;&iota;&alpha;)</td><td>"Rebellion/apostasy" (2:3) &mdash; the day cannot come unless the apostasia comes first. Spiritual defection or political revolt? The word carries both senses.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
  </table>

  <h4>Unusual Characters</h4>
  <ul>
    <li><strong>The man of lawlessness</strong> (2:3-4) &mdash; Exalts himself above "every so-called god" &mdash; above the entire divine council. Takes God&rsquo;s seat in God&rsquo;s temple. The anti-messiah who claims supremacy over all spiritual hierarchy.</li>
    <li><strong>The restrainer</strong> (2:6-7) &mdash; Both neuter ("what restrains") and masculine ("he who restrains"). Paul&rsquo;s audience knew. We don&rsquo;t. Holds back cosmic chaos until the appointed revelation.</li>
    <li><strong>Christ as destroyer</strong> (2:8) &mdash; "The Lord Jesus will kill him with the breath of his mouth and bring to nothing by the appearance of his coming" &mdash; the parousia itself is a weapon.</li>
  </ul>

  <h4>Conspicuous Silences</h4>
  <ul>
    <li>The restrainer&rsquo;s identity &mdash; the biggest mystery in the letter. Paul says "you know" but never writes it down, leaving every generation guessing</li>
    <li>Whether the "temple of God" (2:4) is a literal rebuilt temple or a metaphor for the ekklesia &mdash; the ambiguity is never resolved</li>
    <li>The timeline between apostasia, restrainer removal, and lawless one&rsquo;s revelation &mdash; compressed into a few verses without chronological markers</li>
    <li>How "God sends strong delusion" (2:11) relates to God&rsquo;s truthfulness &mdash; divine deception as judgment parallels 1 Kings 22 but is never theologized</li>
  </ul>

  <h4>Cross-References</h4>
  <p class="xref">2 Thessalonians <span class="arrow">&rarr;</span> <span class="badge badge-ot">Daniel</span> <span class="badge badge-ot">Isaiah</span> <span class="badge badge-ot">1 Kings</span> <span class="badge badge-nt">Revelation</span> <span class="badge badge-nt">1 John</span> <span class="badge badge-nt">1 Thessalonians</span></p>''',
        "key_claim": "The man of lawlessness is a divine council concept — a figure who 'exalts himself against every so-called god' (2:4), claiming supremacy above the entire spiritual hierarchy, and God responds with 'strong delusion' (2:11), a supernatural judgment-through-deception that echoes the lying spirit of 1 Kings 22.",
        "contested_words": [
            {"word": "ho anomos", "greek": "ὁ ἄνομος", "issue": "'The lawless one' (2:8) — not merely immoral but anti-Torah, anti-order, anti-council. He opposes every divine authority structure. Christ destroys him 'by the breath of his mouth.'", "severity": "CRITICAL"},
            {"word": "to katechon / ho katechon", "greek": "τὸ κατέχον / ὁ κατέχων", "issue": "'The restrainer' (2:6-7) — neuter ('what restrains') and masculine ('he who restrains'). Both a thing and a person. One of the NT's greatest mysteries.", "severity": "CRITICAL"},
            {"word": "energeian planes", "greek": "ἐνέργειαν πλάνης", "issue": "'Strong delusion' (2:11) — energeia = active supernatural power. Not mere confusion but divinely empowered deception sent as judgment.", "severity": "CRITICAL"},
            {"word": "apostasia", "greek": "ἀποστασία", "issue": "'Rebellion/apostasy' (2:3) — the day cannot come unless the apostasia comes first. Spiritual defection or political revolt? Both senses present.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "daniel", "why": "The man of lawlessness exalting himself (2:4) echoes Dan 11:36 — the arrogant king who magnifies himself above every god"},
            {"target": "isaiah", "why": "'I will ascend above the heights of the clouds; I will make myself like the Most High' (Isa 14:13-14) — the same satanic aspiration embodied in the lawless one"},
            {"target": "1kings", "why": "God sending 'strong delusion' (2:11) parallels the lying spirit dispatched in 1 Kings 22:22 — divine council deception as judgment"},
            {"target": "revelation", "why": "The man of lawlessness prefigures the beast of Rev 13 — both claim divine status, both deceive through signs, both are destroyed at Christ's coming"},
            {"target": "1john", "why": "John's 'spirit of antichrist already at work' (1 John 4:3) confirms that the pattern Paul describes is not only future but present in every generation"},
        ],
        "what_it_doesnt_say": [
            "The restrainer's identity — Paul says 'you know' but never writes it down, leaving every generation guessing",
            "Whether the 'temple of God' (2:4) is a literal rebuilt temple or a metaphor for the ekklesia",
            "The timeline between apostasia, restrainer removal, and lawless one's revelation — compressed without chronological markers",
            "How 'God sends strong delusion' (2:11) relates to God's truthfulness — divine deception as judgment is stated without theological resolution",
        ],
        "unusual_characters": [
            {"name": "The man of lawlessness", "ref": "2:3-4", "detail": "Exalts himself above 'every so-called god' — above the entire divine council. Takes God's seat. The anti-messiah claiming supremacy over all spiritual hierarchy.", "connections": ["daniel", "revelation"]},
            {"name": "The restrainer", "ref": "2:6-7", "detail": "Both neuter and masculine. Paul's audience knew the identity. Holds back cosmic chaos until the appointed time.", "connections": []},
            {"name": "Christ as destroyer", "ref": "2:8", "detail": "'The Lord Jesus will kill him with the breath of his mouth and bring to nothing by the appearance of his coming' — the parousia itself is a weapon.", "connections": ["isaiah", "revelation"]},
        ],
        "patterns": [
            "Revelation sequence: apostasia first, then the restrainer removed, then the lawless one revealed, then Christ destroys him — a fixed eschatological order",
            "Signs and wonders of deception (2:9): the lawless one performs 'false signs and wonders' (pseudos) — miracles are not proof of divine origin; discernment is mandatory",
            "Judgment through deception: those who 'refused to love the truth' receive 'strong delusion' — the punishment fits the crime, echoing the lying spirit pattern of 1 Kings 22",
            "The parousia as weapon: Christ destroys the lawless one simply by appearing — no battle, no struggle, just the radiance of his presence (epiphaneia tes parousias)",
        ],
        "mistranslations": [
            {"english": "man of sin", "original": "ho anthropos tes anomias", "issue": "KJV 'man of sin' obscures 'man of lawlessness' — the figure is anti-Torah, anti-order, anti-council, not merely morally sinful"},
            {"english": "strong delusion", "original": "energeian planes", "issue": "'Delusion' sounds like a psychological condition; energeia means active supernatural power — this is divinely empowered deception"},
            {"english": "the falling away", "original": "he apostasia", "issue": "KJV 'falling away' is too gentle — apostasia is active rebellion, a deliberate defection from truth, not passive drifting"},
        ],
    },
    {
        "id": '1timothy',
        "section": 'new-testament',
        "title": 'Book 54: 1 Timothy',
        "themes": 'HOLY SPIRIT DC',
        "era_count": 2,
        "chapters": 6,
        "grade": 'B+',
        "meta_text": '2 era files &middot; 6 chapters &middot; Grade: B+',
        "body_html": '''<h4>Major Themes</h4>
  <div class="theme-grid">
    <span class="badge badge-theme">FALSE TEACHING</span><span class="badge badge-theme">EKKLESIA ORDER</span><span class="badge badge-theme">MYSTERY OF GODLINESS</span><span class="badge badge-theme">SPIRITUAL WARFARE</span><span class="badge badge-theme">DECEITFUL SPIRITS</span>
  </div>
  <p><strong>FALSE TEACHING</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; Paul charges Timothy to "wage the good warfare" against false teachers (1:18). The false teaching involves "myths and endless genealogies" (1:4), a proto-Gnostic fascination with speculative systems that distract from faith. This is spiritual warfare, not merely intellectual disagreement.</p>
  <p><strong>THE MYSTERY OF GODLINESS</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; "Great indeed, we confess, is the mystery of godliness: He was manifested in the flesh, vindicated by the Spirit, seen by angels, proclaimed among the nations, believed on in the world, taken up in glory" (3:16). An early christological hymn &mdash; note "seen by angels" &mdash; the divine council witnesses the incarnation.</p>
  <p><strong>DECEITFUL SPIRITS</strong> <span class="badge badge-major">MAJOR</span> &mdash; "The Spirit expressly says that in later times some will depart from the faith by devoting themselves to deceitful spirits (pneumasin planois) and teachings of demons (didaskaliais daimonion)" (4:1). Apostasy has a supernatural source &mdash; demonic doctrine, not just human error.</p>
  <p><strong>EKKLESIA ORDER</strong> <span class="badge badge-major">MAJOR</span> &mdash; Qualifications for overseers (3:1-7) and deacons (3:8-13). The ekklesia is a "pillar and buttress of the truth" (3:15) &mdash; a governing assembly with cosmic responsibility, not a religious social club.</p>

  <h4>Contested Words</h4>
  <table class="ref-table">
    <tr><th>Greek</th><th>Issue</th><th>Severity</th></tr>
    <tr><td><strong>mysterion tes eusebeias</strong></td><td>"Mystery of godliness" (3:16) &mdash; an early creedal hymn. "Seen by angels" (ophthe angelois) &mdash; the divine council witnesses the incarnation event.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>pneumasin planois</strong></td><td>"Deceitful spirits" (4:1) &mdash; real spiritual entities producing false teaching. Doctrine can have a demonic source, not just a human one.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>episkopos</strong> (&epsilon;&pi;&iota;&sigma;&kappa;&omicron;&pi;&omicron;&sigmaf;)</td><td>"Overseer" (3:1) &mdash; NOT "bishop" in the later hierarchical sense. A functional role in the ekklesia, not an ecclesiastical rank.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>stylos kai hedraioma</strong></td><td>"Pillar and buttress of the truth" (3:15) &mdash; the ekklesia as a governing assembly that UPHOLDS truth. Structural metaphor: without it, the truth collapses in the public sphere.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
  </table>

  <h4>Unusual Characters</h4>
  <ul>
    <li><strong>Timothy</strong> (1:2) &mdash; Paul&rsquo;s "true child in the faith" &mdash; young, possibly timid ("let no one despise your youth," 4:12), entrusted with the cosmic responsibility of guarding sound doctrine at Ephesus.</li>
    <li><strong>Hymenaeus and Alexander</strong> (1:20) &mdash; "Handed over to Satan" &mdash; Paul delivers false teachers to the adversary "that they may learn not to blaspheme." Discipline through divine council agency.</li>
    <li><strong>The deceitful spirits</strong> (4:1) &mdash; Supernatural entities behind false teaching &mdash; forbidding marriage and requiring abstinence from foods. The demonic agenda is ascetic distortion, not mere intellectual error.</li>
  </ul>

  <h4>Conspicuous Silences</h4>
  <ul>
    <li>The specific false teaching is never fully described &mdash; "myths and genealogies" are mentioned but never quoted or detailed</li>
    <li>What "handed over to Satan" (1:20) means in practice &mdash; excommunication? Physical affliction? The mechanism is unstated</li>
    <li>How "seen by angels" (3:16) fits the christological hymn &mdash; the divine council witness is inserted without explanation</li>
    <li>The relationship between "all Scripture is breathed out by God" (technically in 2 Timothy 3:16) and the oral traditions Paul also commands Timothy to guard</li>
  </ul>

  <h4>Cross-References</h4>
  <p class="xref">1 Timothy <span class="arrow">&rarr;</span> <span class="badge badge-nt">2 Timothy</span> <span class="badge badge-nt">Titus</span> <span class="badge badge-nt">Ephesians</span> <span class="badge badge-nt">1 Corinthians</span> <span class="badge badge-nt">Acts</span> <span class="badge badge-ot">Deuteronomy</span></p>''',
        "key_claim": "False teaching has a supernatural source — 'deceitful spirits and teachings of demons' (4:1) — making the ekklesia's role as 'pillar and buttress of the truth' (3:15) not a religious preference but a cosmic responsibility: the governing assembly holds the line against demonic doctrine.",
        "contested_words": [
            {"word": "mysterion tes eusebeias", "greek": "μυστήριον τῆς εὐσεβείας", "issue": "'Mystery of godliness' (3:16) — an early creedal hymn. 'Seen by angels' (ophthe angelois) — the divine council witnesses the incarnation.", "severity": "CRITICAL"},
            {"word": "pneumasin planois", "greek": "πνεύμασιν πλάνοις", "issue": "'Deceitful spirits' (4:1) — real spiritual entities producing false teaching. Doctrine can have a demonic source, not just a human one.", "severity": "CRITICAL"},
            {"word": "episkopos", "greek": "ἐπίσκοπος", "issue": "'Overseer' (3:1) — NOT 'bishop' in the later hierarchical sense. A functional role in the ekklesia, not an ecclesiastical rank.", "severity": "MAJOR"},
            {"word": "stylos kai hedraioma", "greek": "στῦλος καὶ ἑδραίωμα", "issue": "'Pillar and buttress of the truth' (3:15) — the ekklesia upholds truth. Structural metaphor: without it, truth collapses in the public sphere.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "ephesians", "why": "The ekklesia as 'pillar of truth' (1 Tim 3:15) complements Eph 3:10 — the governing assembly both upholds truth and makes it known to cosmic powers"},
            {"target": "2timothy", "why": "The same warfare against false teaching intensifies — 2 Tim warns of worse to come as 'evil people and impostors will go on from bad to worse' (2 Tim 3:13)"},
            {"target": "titus", "why": "Parallel pastoral instruction — Titus organizes Cretan churches while Timothy guards Ephesus. Same theology, different contexts"},
            {"target": "1corinthians", "why": "'Handing over to Satan' (1:20) parallels 1 Cor 5:5 — Paul uses the same divine council discipline in both communities"},
            {"target": "acts", "why": "Paul's warning to Ephesian elders (Acts 20:29-30) about 'fierce wolves' is fulfilled in the false teachers Timothy now confronts"},
            {"target": "deuteronomy", "why": "The false teaching involving 'the law' (1:7) is a distortion of Torah — 'desiring to be teachers of the law, without understanding' what they teach"},
        ],
        "what_it_doesnt_say": [
            "The specific false teaching is never fully described — 'myths and genealogies' are mentioned but never quoted or detailed",
            "What 'handed over to Satan' (1:20) means in practice — excommunication? Physical affliction? The mechanism is unstated",
            "How 'seen by angels' (3:16) fits the christological hymn — the divine council witness is inserted without explanation",
            "Whether women in the Ephesian context is a universal prohibition or a local correction to a specific false-teaching situation (2:11-15)",
        ],
        "unusual_characters": [
            {"name": "Timothy", "ref": "1:2", "detail": "Paul's 'true child in the faith' — young, possibly timid, entrusted with guarding sound doctrine at Ephesus against demonic false teaching.", "connections": ["2timothy", "acts"]},
            {"name": "Hymenaeus and Alexander", "ref": "1:20", "detail": "'Handed over to Satan' — Paul delivers false teachers to the adversary 'that they may learn not to blaspheme.' Divine council discipline.", "connections": ["2timothy", "1corinthians"]},
            {"name": "The deceitful spirits", "ref": "4:1", "detail": "Supernatural entities behind false teaching — forbidding marriage, requiring food abstinence. Demonic agenda expressed through ascetic distortion.", "connections": ["1john", "2peter"]},
        ],
        "patterns": [
            "Warfare language: 'wage the good warfare' (1:18), 'fight the good fight of faith' (6:12), spiritual armor assumed — pastoral ministry IS combat",
            "Sound doctrine vs. demonic doctrine: the contrast runs through the entire letter — healthy teaching (hygiainousa didaskalia) versus teachings of demons (didaskaliais daimonion)",
            "The ekklesia as governing assembly: overseer qualifications (3:1-7), deacon qualifications (3:8-13), 'pillar of truth' (3:15) — this is a structured administration, not a casual gathering",
            "Money as spiritual battleground: 'the love of money is a root of all kinds of evil' (6:10) — false teachers are motivated by financial gain (6:5), connecting material greed to spiritual corruption",
        ],
        "mistranslations": [
            {"english": "bishop", "original": "episkopos", "issue": "Later ecclesiastical hierarchy reads backward into a functional role — episkopos means 'overseer/supervisor,' not a ranked office with authority over multiple churches"},
            {"english": "church", "original": "ekklesia", "issue": "'Church' imports institutional religion; ekklesia = governing assembly with cosmic responsibility — the 'pillar of truth' is a council, not a congregation"},
            {"english": "godliness", "original": "eusebeia", "issue": "Sounds like personal piety; eusebeia means proper reverence and cosmic orientation — right relationship with God AND the divine order"},
        ],
    },
    {
        "id": '2timothy',
        "section": 'new-testament',
        "title": 'Book 55: 2 Timothy',
        "themes": 'HOLY SPIRIT',
        "era_count": 2,
        "chapters": 4,
        "grade": 'B+',
        "meta_text": '2 era files &middot; 4 chapters &middot; Grade: B+',
        "body_html": '''<h4>Major Themes</h4>
  <div class="theme-grid">
    <span class="badge badge-theme">SCRIPTURE INSPIRED</span><span class="badge badge-theme">ENDURANCE</span><span class="badge badge-theme">FINAL CHARGE</span><span class="badge badge-theme">APOSTASY</span><span class="badge badge-theme">CROWN</span>
  </div>
  <p><strong>ALL SCRIPTURE IS GOD-BREATHED</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; "All Scripture is breathed out by God (theopneustos) and profitable for teaching, for reproof, for correction, and for training in righteousness" (3:16). Theopneustos appears ONLY here in all of Greek literature &mdash; Paul may have coined it. Not "inspired" (breathing into humans) but "expired" (breathed out FROM God).</p>
  <p><strong>ENDURANCE UNDER SUFFERING</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; Paul writes from prison, expecting execution: "I am already being poured out as a drink offering" (4:6). He charges Timothy to "share in suffering as a good soldier" (2:3), "endure everything for the sake of the elect" (2:10). Ministry IS suffering.</p>
  <p><strong>THE CROWN OF RIGHTEOUSNESS</strong> <span class="badge badge-major">MAJOR</span> &mdash; "I have fought the good fight, I have finished the race, I have kept the faith. Henceforth there is laid up for me the crown of righteousness" (4:7-8). Athletic and military metaphors merge &mdash; the stephanos (victor&rsquo;s wreath) awaits all who love Christ&rsquo;s appearing (epiphaneia).</p>
  <p><strong>LAST-DAYS APOSTASY</strong> <span class="badge badge-major">MAJOR</span> &mdash; "In the last days there will come times of difficulty" (3:1). People will be "lovers of self, lovers of money... having the appearance of godliness but denying its power" (3:2-5). The description sounds contemporary because apostasy is a perpetual pattern, not only an end-time event.</p>

  <h4>Contested Words</h4>
  <table class="ref-table">
    <tr><th>Greek</th><th>Issue</th><th>Severity</th></tr>
    <tr><td><strong>theopneustos</strong> (&theta;&epsilon;&omicron;&pi;&nu;&epsilon;&upsilon;&sigma;&tau;&omicron;&sigmaf;)</td><td>"God-breathed" (3:16) &mdash; appears ONLY here in all Greek literature. Not "inspired" (God breathing into authors) but "expired" (breathed out from God). The direction of the breath matters.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>orthotomeo</strong> (&omicron;&rho;&theta;&omicron;&tau;&omicron;&mu;&epsilon;&omega;)</td><td>"Rightly handling" (2:15) &mdash; literally "cutting straight." A word from masonry or road-building: precision is required in handling truth, not approximate interpretation.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>stephanos dikaiosynes</strong></td><td>"Crown of righteousness" (4:8) &mdash; stephanos = victor&rsquo;s wreath (not diadema/royal crown). Awarded to all who have "loved his appearing" (epiphaneia).</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>sponde</strong> (&sigma;&pi;&omicron;&nu;&delta;&eta;)</td><td>"Drink offering" (4:6) &mdash; Paul describes his imminent execution using sacrificial language. His death is a liturgical act, not a tragedy.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
  </table>

  <h4>Unusual Characters</h4>
  <ul>
    <li><strong>Paul</strong> (1:1) &mdash; Writing his final letter from a Roman prison, expecting execution. "I am already being poured out." The apostle faces death as a drink offering &mdash; sacrificial, not defeated.</li>
    <li><strong>Hymenaeus and Philetus</strong> (2:17) &mdash; False teachers who say "the resurrection has already happened" &mdash; an over-realized eschatology that collapses future hope into past event, destroying faith.</li>
    <li><strong>Jannes and Jambres</strong> (3:8) &mdash; Named nowhere in the OT but identified here as the Egyptian magicians who opposed Moses. Paul draws from Jewish tradition (possibly Targum) to name unnamed enemies.</li>
    <li><strong>Lois and Eunice</strong> (1:5) &mdash; Timothy&rsquo;s grandmother and mother who transmitted "sincere faith" across three generations. Women as the primary agents of faith transmission in the seed line.</li>
  </ul>

  <h4>Conspicuous Silences</h4>
  <ul>
    <li>"All Scripture is God-breathed" (3:16) never defines which writings constitute "Scripture" &mdash; the canon was not yet closed when Paul wrote this</li>
    <li>Paul says "all deserted me" (4:16) at his first defense &mdash; the abandonment of the apostle by the community is stated without bitterness or explanation</li>
    <li>Demas "in love with this present world" (4:10) deserted Paul &mdash; no further detail, no resolution, no indication whether he ever returned</li>
    <li>How "the resurrection has already happened" (2:18) functioned as false teaching &mdash; the theological mechanism of this specific heresy is assumed, not explained</li>
  </ul>

  <h4>Cross-References</h4>
  <p class="xref">2 Timothy <span class="arrow">&rarr;</span> <span class="badge badge-nt">1 Timothy</span> <span class="badge badge-nt">Acts</span> <span class="badge badge-ot">Exodus</span> <span class="badge badge-nt">Philippians</span> <span class="badge badge-nt">Romans</span> <span class="badge badge-nt">1 Corinthians</span></p>''',
        "key_claim": "Theopneustos (3:16) appears ONLY here in all of Greek literature — Paul may have coined the word to express that Scripture is not 'inspired' (breathed into) but 'expired' (breathed out FROM God), making the direction of the divine breath the foundation of all biblical authority.",
        "contested_words": [
            {"word": "theopneustos", "greek": "θεόπνευστος", "issue": "'God-breathed' (3:16) — appears ONLY here in all Greek literature. Not 'inspired' (God breathing into authors) but 'expired' (breathed out from God). The direction matters.", "severity": "CRITICAL"},
            {"word": "orthotomeo", "greek": "ὀρθοτομέω", "issue": "'Rightly handling' (2:15) — literally 'cutting straight.' From masonry or road-building. Precision is required in handling truth.", "severity": "CRITICAL"},
            {"word": "stephanos dikaiosynes", "greek": "στέφανος δικαιοσύνης", "issue": "'Crown of righteousness' (4:8) — stephanos = victor's wreath. Awarded to all who have 'loved his appearing.'", "severity": "MAJOR"},
            {"word": "sponde", "greek": "σπονδή", "issue": "'Drink offering' (4:6) — Paul describes his execution using sacrificial language. His death is liturgical, not tragic.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "1timothy", "why": "The warfare continues — Hymenaeus appears in both letters (1 Tim 1:20, 2 Tim 2:17). The false teaching is spreading, not contained"},
            {"target": "acts", "why": "Paul's final imprisonment and trial (2 Tim 4) follows Acts 28 — this letter fills the gap Acts leaves open about Paul's end"},
            {"target": "exodus", "why": "Jannes and Jambres (3:8) are the Egyptian magicians of Ex 7:11 — Paul names them from Jewish tradition to identify the pattern of opposition to God's agents"},
            {"target": "philippians", "why": "'Being poured out as a drink offering' (4:6) echoes Phil 2:17 — Paul used the same sacrificial language earlier, but now it is imminent, not hypothetical"},
            {"target": "romans", "why": "'If we endure, we will also reign with him' (2:12) connects to Rom 8:17 — co-suffering leads to co-reigning in the cosmic administration"},
            {"target": "1corinthians", "why": "The resurrection false teaching (2:18) inverts Paul's resurrection argument in 1 Cor 15 — without future resurrection, faith is futile"},
        ],
        "what_it_doesnt_say": [
            "'All Scripture is God-breathed' never defines which writings constitute 'Scripture' — the canon was not yet closed when Paul wrote",
            "Paul says 'all deserted me' (4:16) — the abandonment by the community is stated without bitterness or explanation",
            "Demas 'in love with this present world' (4:10) deserted Paul — no further detail, no resolution, no return",
            "How 'the resurrection has already happened' (2:18) functioned as heresy — the mechanism is assumed, not explained",
        ],
        "unusual_characters": [
            {"name": "Paul (final letter)", "ref": "1:1", "detail": "Writing from prison, expecting execution. 'I am already being poured out.' Faces death as a drink offering — sacrificial, not defeated.", "connections": ["acts", "philippians"]},
            {"name": "Hymenaeus and Philetus", "ref": "2:17", "detail": "Say 'the resurrection has already happened' — over-realized eschatology that collapses future hope into past event, destroying faith.", "connections": ["1timothy"]},
            {"name": "Jannes and Jambres", "ref": "3:8", "detail": "Named nowhere in the OT but identified here as Egyptian magicians opposing Moses. Paul draws from Jewish tradition to name unnamed enemies.", "connections": ["exodus"]},
            {"name": "Lois and Eunice", "ref": "1:5", "detail": "Timothy's grandmother and mother who transmitted 'sincere faith' across generations. Women as primary agents of faith transmission.", "connections": []},
        ],
        "patterns": [
            "Soldier-athlete-farmer triad (2:3-6): three metaphors for ministry — the soldier endures, the athlete competes lawfully, the farmer works first and eats later. All require sacrifice before reward",
            "Faithful sayings: 'if we died with him, we will live; if we endure, we will reign; if we deny, he will deny; if we are faithless, he remains faithful' (2:11-13) — four conditions, four outcomes",
            "Last days as present reality: the characteristics of 'the last days' (3:1-5) describe not just a future period but an ongoing pattern of human corruption — 'having the appearance of godliness but denying its power'",
            "Three-generation faith transmission: Lois to Eunice to Timothy (1:5) — the 'sincere faith' passes through women's witness, not institutional structures",
        ],
        "mistranslations": [
            {"english": "inspired by God", "original": "theopneustos", "issue": "CRITICAL: 'inspired' reverses the direction — it means breathed INTO a person. Theopneustos means breathed OUT from God. Scripture originates from God, not from human inspiration"},
            {"english": "rightly dividing", "original": "orthotomeo", "issue": "KJV 'dividing' suggests cutting into pieces; the word means cutting straight like a mason — accurate handling, not dissection"},
            {"english": "fight the good fight", "original": "ton kalon agona agonizou", "issue": "'Fight' is too narrow — agon covers athletic contest, legal struggle, and military combat. Paul's entire ministry was the agon"},
        ],
    },
    {
        "id": 'titus',
        "section": 'new-testament',
        "title": 'Book 56: Titus',
        "themes": 'HOLY COV TYPE',
        "era_count": 2,
        "chapters": 3,
        "grade": 'B+',
        "meta_text": '2 era files &middot; 3 chapters &middot; Grade: B+',
        "body_html": '''<h4>Major Themes</h4>
  <div class="theme-grid">
    <span class="badge badge-theme">GRACE THAT TRAINS</span><span class="badge badge-theme">SOUND DOCTRINE</span><span class="badge badge-theme">GOOD WORKS</span><span class="badge badge-theme">JUSTIFIED BY GRACE</span><span class="badge badge-theme">BLESSED HOPE</span>
  </div>
  <p><strong>GRACE THAT TRAINS</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; "The grace of God has appeared, bringing salvation for all people, TRAINING us to renounce ungodliness" (2:11-12). The Greek paideuousa means disciplined instruction &mdash; grace is not permissive but pedagogical. It teaches, corrects, and shapes. Grace has content and demands transformation.</p>
  <p><strong>THE BLESSED HOPE</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; "Waiting for our blessed hope, the appearing (epiphaneia) of the glory of our great God and Savior Jesus Christ" (2:13). One of the most explicit deity-of-Christ statements in Paul &mdash; "our great God and Savior" applies both titles to one person, Jesus Christ.</p>
  <p><strong>JUSTIFIED BY GRACE</strong> <span class="badge badge-major">MAJOR</span> &mdash; "He saved us, not because of works done by us in righteousness, but according to his own mercy, by the washing of regeneration and renewal of the Holy Spirit... so that being justified by his grace we might become heirs according to the hope of eternal life" (3:5-7). The most concentrated salvation summary in Paul&rsquo;s letters.</p>
  <p><strong>SOUND DOCTRINE &amp; GOOD WORKS</strong> <span class="badge badge-major">MAJOR</span> &mdash; "Sound doctrine" (hygiainousa didaskalia) appears repeatedly &mdash; teaching that produces health. Good works (kala erga) are the RESULT of grace, not the means &mdash; mentioned six times in three chapters.</p>

  <h4>Contested Words</h4>
  <table class="ref-table">
    <tr><th>Greek</th><th>Issue</th><th>Severity</th></tr>
    <tr><td><strong>paideuousa</strong> (&pi;&alpha;&iota;&delta;&epsilon;&upsilon;&omicron;&upsilon;&sigma;&alpha;)</td><td>"Training" (2:12) &mdash; from paideia, the Greek concept of comprehensive education. Grace does not merely forgive; it TRAINS, disciplines, and transforms. Grace has teeth.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>tou megalou theou kai soteros</strong></td><td>"Our great God and Savior" (2:13) &mdash; Granville Sharp rule: one article governing two nouns joined by kai = one person. "God" and "Savior" are BOTH Jesus Christ.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>palingenesia</strong> (&pi;&alpha;&lambda;&iota;&gamma;&gamma;&epsilon;&nu;&epsilon;&sigma;&iota;&alpha;)</td><td>"Regeneration" (3:5) &mdash; used only here and Matt 19:28. In Matthew it refers to cosmic renewal; here to individual rebirth. "Washing of regeneration" &mdash; baptismal or spiritual?</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>hygiainousa didaskalia</strong></td><td>"Sound doctrine" (1:9, 2:1) &mdash; hygiainousa = healthy, producing health. Doctrine is not abstract theory but medicine. False teaching is disease; sound teaching heals.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
  </table>

  <h4>Unusual Characters</h4>
  <ul>
    <li><strong>Titus</strong> (1:4) &mdash; Paul&rsquo;s "true child in a common faith" &mdash; a Gentile entrusted with organizing churches on Crete. Never mentioned in Acts, yet Paul&rsquo;s most trusted troubleshooter.</li>
    <li><strong>The Cretans</strong> (1:12) &mdash; Paul quotes their own prophet (Epimenides): "Cretans are always liars, evil beasts, lazy gluttons." Then says: "This testimony is true" &mdash; the most politically incorrect verse in the NT.</li>
    <li><strong>Epimenides</strong> (1:12) &mdash; A pagan Cretan prophet whom Paul quotes approvingly. Paul engages pagan intellectual tradition when it speaks truth &mdash; just as he does at Athens (Acts 17:28).</li>
  </ul>

  <h4>Conspicuous Silences</h4>
  <ul>
    <li>Titus is never mentioned in Acts despite being one of Paul&rsquo;s most important colleagues &mdash; a significant gap in Luke&rsquo;s narrative</li>
    <li>The "factious person" (3:10) who should be warned twice then avoided is never named or described &mdash; the criterion for separation is minimal</li>
    <li>No mention of spiritual gifts, tongues, or charismatic manifestation on Crete &mdash; the entire focus is on character and sound teaching</li>
    <li>The relationship between "justified by grace" (3:7) and the repeated emphasis on "good works" is asserted but never systematically resolved</li>
  </ul>

  <h4>Cross-References</h4>
  <p class="xref">Titus <span class="arrow">&rarr;</span> <span class="badge badge-nt">1 Timothy</span> <span class="badge badge-nt">2 Timothy</span> <span class="badge badge-nt">Romans</span> <span class="badge badge-nt">Ephesians</span> <span class="badge badge-nt">Galatians</span> <span class="badge badge-nt">Acts</span></p>''',
        "key_claim": "Grace is not permissive but pedagogical — 'the grace of God has appeared, TRAINING us to renounce ungodliness' (2:11-12) — and Titus 2:13 is one of the most explicit deity-of-Christ statements in Paul: 'our great God and Savior Jesus Christ,' both titles applied to one person.",
        "contested_words": [
            {"word": "paideuousa", "greek": "παιδεύουσα", "issue": "'Training' (2:12) — from paideia, comprehensive education. Grace does not merely forgive; it TRAINS, disciplines, and transforms. Grace has teeth.", "severity": "CRITICAL"},
            {"word": "tou megalou theou kai soteros", "greek": "τοῦ μεγάλου θεοῦ καὶ σωτῆρος", "issue": "'Our great God and Savior' (2:13) — Granville Sharp rule: one article, two nouns, one person. God and Savior are BOTH Jesus.", "severity": "CRITICAL"},
            {"word": "palingenesia", "greek": "παλιγγενεσία", "issue": "'Regeneration' (3:5) — used only here and Matt 19:28. In Matthew: cosmic renewal. Here: individual rebirth. 'Washing of regeneration' — baptismal or spiritual?", "severity": "MAJOR"},
            {"word": "hygiainousa didaskalia", "greek": "ὑγιαίνουσα διδασκαλία", "issue": "'Sound doctrine' — hygiainousa = healthy, producing health. Doctrine is medicine. False teaching is disease; sound teaching heals.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "romans", "why": "'Justified by his grace' (3:7) is the condensed version of Romans 3-5 — the same theology in miniature, applied to pastoral context"},
            {"target": "ephesians", "why": "'Saved by grace through faith, not of works' (Eph 2:8-9) parallels Titus 3:5 — 'not because of works done by us in righteousness'"},
            {"target": "galatians", "why": "Titus himself was the test case: Paul refused to circumcise him (Gal 2:3) — a Gentile leader organizing churches proves the grace principle"},
            {"target": "1timothy", "why": "Parallel pastoral structure — elder qualifications (1:5-9) mirror 1 Tim 3:1-7. Same theology for different cultural contexts"},
            {"target": "acts", "why": "Paul quotes Epimenides (1:12) just as he quotes Aratus at Athens (Acts 17:28) — engaging pagan truth when it aligns with reality"},
        ],
        "what_it_doesnt_say": [
            "Titus is never mentioned in Acts — one of Paul's most important colleagues has no narrative presence in Luke's history",
            "The 'factious person' (3:10) to be warned then avoided is never named or described — the criterion for separation is minimal",
            "No mention of spiritual gifts or charismatic manifestation on Crete — the entire focus is character and sound teaching",
            "The relationship between 'justified by grace' (3:7) and repeated emphasis on 'good works' is asserted but never systematically resolved",
        ],
        "unusual_characters": [
            {"name": "Titus", "ref": "1:4", "detail": "Paul's 'true child in a common faith' — a Gentile organizing churches on Crete. Never in Acts, yet Paul's most trusted troubleshooter.", "connections": ["galatians", "2corinthians"]},
            {"name": "The Cretans", "ref": "1:12", "detail": "Paul quotes their own prophet: 'Cretans are always liars, evil beasts, lazy gluttons.' Then: 'This testimony is true.' The most culturally direct verse in the NT.", "connections": []},
            {"name": "Epimenides", "ref": "1:12", "detail": "A pagan Cretan prophet whom Paul quotes approvingly — Paul engages pagan intellectual tradition when it speaks truth.", "connections": ["acts"]},
        ],
        "patterns": [
            "Grace as pedagogy: grace 'appeared' (2:11), grace 'trains' (2:12), grace produces the 'blessed hope' (2:13) — a complete arc from revelation to transformation to consummation",
            "Good works as fruit: kala erga appears six times in three chapters — always as the RESULT of grace, never the means. The order is irreversible: salvation then works",
            "Sound/healthy language: hygiainousa (healthy) applied to doctrine, faith, speech — the medical metaphor runs throughout. The community's health depends on doctrinal health",
            "Elder qualifications as character profile (1:5-9): blameless, husband of one wife, not arrogant, not violent, hospitable, self-controlled — leadership is proven character, not gifting",
        ],
        "mistranslations": [
            {"english": "sound doctrine", "original": "hygiainousa didaskalia", "issue": "'Sound' as in 'solid' misses the medical metaphor — hygiainousa means 'healthy/health-producing.' Doctrine is either medicine or poison"},
            {"english": "the grace of God has appeared", "original": "epephane he charis tou theou", "issue": "'Appeared' is too bland — epiphaino is theophany language. Grace made a divine appearance, an epiphany. This is revelation, not a concept"},
            {"english": "washing of rebirth", "original": "loutrou palingenesias", "issue": "'Rebirth' domesticates palingenesia — the word means cosmic regeneration (Matt 19:28 uses it for the renewal of all things). Individual salvation is connected to cosmic restoration"},
        ],
    },
    {
        "id": 'philemon',
        "section": 'new-testament',
        "title": 'Book 57: Philemon',
        "themes": 'REVERSAL',
        "era_count": 1,
        "chapters": 1,
        "meta_text": '1 era file &middot; 1 chapter &middot; O-SILENCE',
        "body_html": '''<p>"No longer as a slave but as a beloved brother" (v. 16). Social distinctions abolished in Christ. Seed-line theme at its most personal.</p>''',
        "key_claim": "Philemon is the seed-line theme at its most personal — 'no longer as a slave but as a beloved brother' (v. 16) demonstrates that the gospel dismantles social hierarchies from the inside out, creating a new humanity where every distinction is abolished in Christ.",
        "contested_words": [{'word': 'adelphos agapetos', 'greek': 'ἀδελφὸς ἀγαπητός', 'issue': "'Beloved brother' (v. 16) — Paul redefines Onesimus's social status using family language. Not reform of slavery but a new ontological category that makes slavery absurd.", 'severity': 'CRITICAL'}, {'word': 'oninemi', 'greek': 'ὀνίνημι', 'issue': "'Benefit/refresh' (v. 20) — a wordplay on Onesimus's name (which means 'useful/beneficial'). Paul asks Philemon to live up to Onesimus's name by receiving him.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'galatians', 'why': "'Neither slave nor free' (Gal 3:28) is enacted in concrete reality — Onesimus returns not as property but as family"}, {'target': 'colossians', 'why': "Onesimus is mentioned in Col 4:9 as 'one of you' — sent with the Colossian letter. Philemon likely lived in Colossae"}, {'target': 'exodus', 'why': "Deut 23:15-16 forbids returning a runaway slave — Paul's letter navigates between Roman law and Torah principle"}],
        "what_it_doesnt_say": ['Never explicitly tells Philemon to free Onesimus — Paul hints, pressures, and shames, but never commands manumission', 'What Onesimus did is never clarified — did he steal? Simply run away? The offense is unnamed', "Paul's 'charge it to me' (v. 18) — did Philemon actually collect? The outcome is never recorded"],
        "unusual_characters": [{'name': 'Onesimus', 'ref': 'v. 10', 'detail': "A runaway slave whom Paul 'fathered' in prison. His name means 'useful' — Paul says he was formerly useless but now useful to both of them.", 'connections': ['colossians']}, {'name': 'Apphia', 'ref': 'v. 2', 'detail': "Called 'our sister' — likely Philemon's wife. Named as a recipient of the letter, making the household decision communal, not just Philemon's.", 'connections': []}],
        "patterns": ["Persuasion structure: Paul moves from praise (vv. 4-7) to appeal (vv. 8-16) to offer (vv. 17-21) to pressure (v. 21 'knowing you will do even more') — masterful rhetoric", "Name theology: Onesimus ('useful') was 'useless' as a slave but 'useful' as a brother — identity is transformed by relationship to Christ, not social status", 'The personal letter as theology: the shortest Pauline letter enacts the gospel in a single concrete situation — reconciliation, new identity, substitutionary payment'],
        "mistranslations": [{'english': 'slave', 'original': 'doulos', 'issue': "Modern 'slave' carries chattel slavery connotations; Roman slavery was a complex spectrum. But Paul's point transcends the institution — brother abolishes the category"}, {'english': 'partner', 'original': 'koinonos', 'issue': "Sounds like a business term; koinonos means 'one who shares in common' — Paul and Philemon share everything, including Onesimus's new identity"}],
    },
    {
        "id": 'hebrews',
        "section": 'new-testament',
        "title": 'Book 58: Hebrews',
        "themes": 'DC PRIEST SEED COV HOLY TYPE',
        "era_count": 3,
        "chapters": 13,
        "grade": 'A+',
        "meta_text": '3 era files &middot; 13 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>DIVINE COUNCIL CHRISTOLOGY</strong> — Systematic proof Christ is above every council member. Quotes Ps 2:7 (1:5), Deut 32:43 DSS/LXX (1:6 — "Let all God's angels worship him"), Ps 45:6 (1:8 — "Your throne, O GOD"), Ps 8 (2:5-8 — humanity's mandate restored). Melchizedek priesthood (chs. 5-7): Jesus' priesthood is NOT Levitical but Melchizedekian — older, superior, eternal. "You have come to Mount Zion, the heavenly Jerusalem, innumerable angels in festal gathering, the ekklesia of the firstborn" (12:22-24).</p>''',
        "key_claim": "Hebrews provides systematic proof that Christ is above every divine council member — quoting Ps 2:7, Deut 32:43 (DSS/LXX), Ps 45:6 ('Your throne, O God'), and Ps 8 — establishing a Melchizedekian priesthood older and superior to the Levitical order.",
        "contested_words": [{'word': 'charakter tes hypostaseos', 'greek': 'χαρακτὴρ τῆς ὑποστάσεως', 'issue': "'Exact imprint of his nature' (1:3) — charakter = stamp/die impression. The Son is not similar to God but the exact reproduction of the divine essence.", 'severity': 'CRITICAL'}, {'word': 'apaugasma', 'greek': 'ἀπαύγασμα', 'issue': "'Radiance' (1:3) — active radiance from a source, not reflected light. The Son actively shines forth God's glory, inseparable from the source.", 'severity': 'CRITICAL'}, {'word': 'kata ten taxin Melchisedek', 'greek': 'κατὰ τὴν τάξιν Μελχισεδέκ', 'issue': "'According to the order of Melchizedek' (5:6, 6:20, 7:17) — Jesus' priesthood is NOT Levitical. He is from Judah, not Levi (7:14). The Melchizedekian order is older, superior, eternal.", 'severity': 'CRITICAL'}, {'word': 'typos/skia', 'greek': 'τύπος/σκιά', 'issue': "'Copy and shadow' (8:5) — the earthly tabernacle is a replica of the heavenly original. Shadows are real but derivative. Christ ministers in the true tabernacle.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'genesis', 'why': "Melchizedek (Gen 14:18) is the anchor: no genealogy, no beginning or end (Heb 7:3) — priest-king of Salem who prefigures Christ's eternal priesthood"}, {'target': 'psalms', 'why': "Hebrews quotes Psalms more than any other OT book: Ps 2:7 (1:5), Ps 45:6 (1:8, 'Your throne, O God'), Ps 110:1, 4 (1:13, 5:6) — the divine council hymnbook as Christological proof"}, {'target': 'leviticus', 'why': 'The entire Day of Atonement (Lev 16) is reinterpreted: Christ enters the TRUE Holy of Holies with his own blood, once for all (9:11-12)'}, {'target': 'exodus', 'why': "The tabernacle was built according to the heavenly 'pattern' (tavnit, Ex 25:40) — Heb 8:5 confirms it was a shadow of the real thing"}, {'target': 'deuteronomy', 'why': "Heb 1:6 quotes Deut 32:43 (DSS/LXX): 'Let all God's angels worship him' — the divine council commanded to worship the Son"}, {'target': 'dss', 'why': '11Q13 (Melchizedek Scroll) presents Melchizedek as a divine figure executing Ps 82 judgment — the Qumran community saw the same connection Hebrews makes'}],
        "what_it_doesnt_say": ["The author is never named — Pauline authorship was debated even in antiquity. Origen: 'only God knows who wrote Hebrews'", "The audience is never explicitly identified — 'Hebrews' is a later title. Were they Jewish Christians tempted to revert to Judaism?", "HOW Melchizedek has 'no beginning of days or end of life' (7:3) — is this a literary argument from silence or an ontological claim?", "The 'great cloud of witnesses' (12:1) — are they observing us or simply testifying by their example? The text is ambiguous"],
        "unusual_characters": [{'name': 'Melchizedek', 'ref': '7:1-3', 'detail': "King of Salem, priest of God Most High. 'Without father, mother, genealogy, beginning of days, or end of life — resembling the Son of God.' The most mysterious figure in the Bible.", 'connections': ['genesis', 'psalms', 'dss']}, {'name': 'Moses', 'ref': '3:1-6', 'detail': "Faithful as a SERVANT in God's house; Christ faithful as a SON over God's house — both faithful, but vastly different rank.", 'connections': ['exodus', 'deuteronomy']}, {'name': 'The Son', 'ref': '1:1-4', 'detail': 'Named heir of all things, creator of the ages, radiance of glory, exact imprint of divine nature, sustainer of all things by his word — the highest Christology in the NT.', 'connections': ['john', 'colossians']}],
        "patterns": ['Better/superior comparisons: better covenant (7:22), better promises (8:6), better sacrifice (9:23), better country (11:16) — everything in the old order points to something superior in Christ', 'Warning passages (2:1-4, 3:7-4:13, 5:11-6:12, 10:26-31, 12:25-29) — five escalating warnings against apostasy, each more severe than the last', 'Shadow to reality: the entire old covenant system (tabernacle, priesthood, sacrifices) was the shadow; Christ is the substance that casts the shadow', "Faith hall of fame (ch. 11): Abel, Enoch, Noah, Abraham, Sarah, Moses — each exemplifies a different dimension of faith, building toward the 'pioneer and perfecter' (12:2)"],
        "mistranslations": [{'english': 'high priest', 'original': 'archiereus', 'issue': 'Familiar religious title obscures the radical claim — Jesus holds a priesthood that predates, outranks, and replaces the entire Levitical system'}, {'english': 'once for all', 'original': 'ephapax', 'issue': "Often read as 'once upon a time' when it means 'once and for all time, never to be repeated' — the finality is absolute"}, {'english': 'copy and shadow', 'original': 'hypodeigma kai skia', 'issue': 'Sounds dismissive of the OT system; the point is that shadows are cast by REAL objects — the earthly tabernacle proves the heavenly one exists'}],
    },
    {
        "id": 'james',
        "section": 'new-testament',
        "title": 'Book 59: James',
        "themes": 'HOLY',
        "era_count": 2,
        "chapters": 5,
        "meta_text": '2 era files &middot; 5 chapters',
        "body_html": '''<p>"The demons believe — and shudder" (2:19). "You have heard of the steadfastness of Job and seen the purpose (telos) of the Lord" (5:11).</p>''',
        "key_claim": "James reveals that the demons possess orthodox theology — 'the demons believe and shudder' (2:19) — meaning intellectual assent to truth is not faith. Real faith produces works, and James points back to Job's endurance to reveal 'the purpose of the Lord' (5:11).",
        "contested_words": [{'word': 'pistis', 'greek': 'πίστις', 'issue': "'Faith' (2:14-26) — James and Paul use the same word differently. Paul: faith vs. works of Torah. James: living faith vs. dead intellectual assent. No contradiction — different opponents.", 'severity': 'CRITICAL'}, {'word': 'phrissousin', 'greek': 'φρίσσουσιν', 'issue': "'Shudder' (2:19) — physical trembling from terror. The demons' response to God's existence is not worship but horror. Right doctrine with wrong relationship.", 'severity': 'MAJOR'}, {'word': 'telos kyriou', 'greek': 'τέλος κυρίου', 'issue': "'Purpose/outcome of the Lord' (5:11) — telos = end goal, purpose, completion. Job's suffering had a divine telos that was invisible during the trial.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'job', 'why': "'You have heard of the steadfastness of Job and seen the telos of the Lord' (5:11) — James reads Job as evidence that God's purposes are compassionate even when hidden"}, {'target': 'genesis', 'why': "Abraham 'offered up Isaac' (2:21) — faith completed by works. James reads Gen 22 as proof that Gen 15:6 faith produces Gen 22 obedience"}, {'target': 'matthew', 'why': "James's ethical teaching closely parallels the Sermon on the Mount — oaths (5:12, Matt 5:34), prayer (5:13-18, Matt 6:5-15), mercy (2:13, Matt 5:7)"}, {'target': 'proverbs', 'why': 'James is NT wisdom literature — practical, proverbial, focused on speech, wealth, and community. The Hebrew wisdom tradition continued'}],
        "what_it_doesnt_say": ["Never mentions the cross, resurrection, or atonement — the most 'Jewish' letter in the NT, focused on covenant faithfulness over theological system", "The 'faith vs. works' debate (2:14-26) never mentions Paul by name — is James responding to Paul or to a misunderstanding of Paul?", "The 'prayer of faith will save the sick' (5:15) is stated without qualification — what about unanswered prayers for healing?", "'The tongue is a fire, a world of unrighteousness' (3:6) — the most vivid speech ethics in the NT, but no system for controlling it is offered"],
        "unusual_characters": [{'name': 'James', 'ref': '1:1', 'detail': "Brother of Jesus who did not believe during Jesus' ministry (John 7:5) but became leader of the Jerusalem church. His conversion is one of the strongest resurrection evidences.", 'connections': ['acts', 'galatians']}, {'name': 'Rahab', 'ref': '2:25', 'detail': 'A Canaanite prostitute justified by works — paired with Abraham as proof that faith acts. Two extremes of society, same principle.', 'connections': ['joshua', 'hebrews']}],
        "patterns": ['Imperative density: James has more commands per verse than any NT book — practical, urgent, no room for passive religion', 'Speech/tongue theme runs through the entire letter: quick to hear, slow to speak (1:19), the tongue as fire (3:1-12), do not grumble (5:9) — words are the index of the heart', "Rich/poor reversal: the rich will 'fade away' (1:11), the poor are 'heirs of the kingdom' (2:5), the rich are condemned (5:1-6) — radical economic inversion"],
        "mistranslations": [{'english': 'faith without works is dead', 'original': 'he pistis choris ergon nekra estin', 'issue': "Often weaponized against Paul — but James defines 'works' as mercy and obedience, not Torah observance. Different word, different target"}, {'english': 'religion', 'original': 'threskeia', 'issue': "'Religion' (1:27) is too institutional — threskeia means 'worship practice/devotion.' Pure devotion is caring for orphans and widows, not ritual"}],
    },
    {
        "id": '1peter',
        "section": 'new-testament',
        "title": 'Book 60: 1 Peter',
        "themes": 'DC SPIRIT EXILE',
        "era_count": 2,
        "chapters": 5,
        "meta_text": '2 era files &middot; 5 chapters',
        "body_html": '''<p><strong>PROCLAMATION TO IMPRISONED SPIRITS</strong> (3:18-20) — Christ "proclaimed (ekerxen) to the spirits in prison, because they did not obey in the days of Noah." KERYSSO (proclaim victory), NOT euangelizo (preach gospel). Christ proclaimed victory to the imprisoned Watchers of Gen 6/1 Enoch. "Angels, authorities, and powers subjected to him" (3:22).</p>''',
        "key_claim": "Christ 'proclaimed (ekerxen) to the spirits in prison' (3:19) — the Greek is kerysso (proclaim victory), NOT euangelizo (preach gospel). Christ announced his triumph to the imprisoned Watchers of Gen 6/1 Enoch, and all 'angels, authorities, and powers' are now subject to him (3:22).",
        "contested_words": [{'word': 'ekerxen', 'greek': 'ἐκήρυξεν', 'issue': "'Proclaimed' (3:19) — kerysso = herald's announcement of victory, NOT euangelizo = preach the gospel. Christ did not offer salvation to imprisoned spirits; he announced their defeat.", 'severity': 'CRITICAL'}, {'word': 'pneumasin en phylake', 'greek': 'πνεύμασιν ἐν φυλακῇ', 'issue': "'Spirits in prison' (3:19) — these are the Watchers of Gen 6 / 1 Enoch 10 who 'did not obey in the days of Noah' (3:20). Not dead humans but imprisoned divine beings.", 'severity': 'CRITICAL'}, {'word': 'parepidemos', 'greek': 'παρεπίδημος', 'issue': "'Sojourner/exile' (1:1, 2:11) — believers are resident aliens in a world governed by hostile spiritual powers. Their true citizenship is in the heavenly Jerusalem.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': '1enoch', 'why': "The 'spirits in prison who did not obey in the days of Noah' (3:19-20) are the imprisoned Watchers of 1 Enoch 10 — Peter assumes the Enochic framework"}, {'target': 'genesis', 'why': "The disobedience 'in the days of Noah' (3:20) points to Gen 6:1-4 — the Watcher rebellion that provoked the Flood"}, {'target': '2peter', 'why': "2 Pet 2:4 expands: 'God did not spare angels when they sinned but cast them into Tartarus' — the same imprisoned spirits, named more explicitly"}, {'target': 'jude', 'why': "Jude 6 parallels exactly: 'angels who did not stay within their position' kept in 'eternal chains' — the same tradition Peter draws from"}, {'target': 'exodus', 'why': "'A royal priesthood, a holy nation' (2:9) quotes Ex 19:6 — Israel's vocation transferred to the ekklesia, including Gentiles"}],
        "what_it_doesnt_say": ['WHEN Christ proclaimed to the imprisoned spirits — between death and resurrection? At the ascension? The timing is debated', "What the 'spirits in prison' heard — did they respond? Was it pure announcement or did it include judgment?", "How 'baptism now saves you' (3:21) works — Peter immediately qualifies: 'not removal of dirt but an appeal to God for a good conscience.' The mechanism is unclear", "The 'fiery trial' (4:12) is never specified — Nero's persecution? General tribulation? Eschatological suffering?"],
        "unusual_characters": [{'name': 'The spirits in prison', 'ref': '3:19', 'detail': "Imprisoned Watchers who rebelled in Noah's day. Christ visits them not to save but to announce victory — kerysso, not euangelizo.", 'connections': ['1enoch', 'genesis', '2peter', 'jude']}, {'name': 'Sarah', 'ref': '3:6', 'detail': "Example of holy women who 'hoped in God' — called Abraham 'lord.' Peter uses her as a model of strength, not submission.", 'connections': ['genesis']}],
        "patterns": ['Suffering → glory pattern: Christ suffered then was glorified (1:11); believers suffer now and will be glorified later (4:13, 5:10). The sequence is fixed', 'Stone imagery: Christ as living stone rejected by men, chosen by God (2:4-8). Believers as living stones built into a spiritual house — Ps 118:22 + Isa 28:16', "Exile language: 'elect exiles of the Dispersion' (1:1), 'sojourners and exiles' (2:11) — the ekklesia lives as aliens in hostile territory governed by spiritual powers"],
        "mistranslations": [{'english': 'preached', 'original': 'ekerxen (kerysso)', 'issue': "CRITICAL: 'preached' implies gospel offer. The Greek is kerysso = announce/proclaim victory. Christ proclaimed triumph, not salvation, to the imprisoned Watchers"}, {'english': 'spirits in prison', 'original': 'pneumasin en phylake', 'issue': "Often interpreted as dead humans; the context ('did not obey in days of Noah') and parallel texts (2 Pet 2:4, Jude 6) identify them as fallen divine beings"}, {'english': 'aliens and strangers', 'original': 'paroikoi kai parepidēmoi', 'issue': 'Sounds like mere metaphor; Peter means it ontologically — believers belong to a different polity and their current world is enemy territory'}],
    },
    {
        "id": '2peter',
        "section": 'new-testament',
        "title": 'Book 61: 2 Peter',
        "themes": 'DC SPIRIT',
        "era_count": 2,
        "chapters": 3,
        "meta_text": '2 era files &middot; 3 chapters',
        "body_html": '''<p>"God did not spare angels when they sinned but cast them into TARTARUS (tartarosas)" (2:4). Greek term for prison of the Titans. Confirms the 1 Enoch/Watcher framework.</p>''',
        "key_claim": "2 Peter provides the most explicit Greek confirmation of the Watcher framework: 'God did not spare angels when they sinned but cast them into Tartarus' (2:4) — using the Greek term for the prison of the Titans, confirming that the 1 Enoch/Watcher imprisonment is historical reality.",
        "contested_words": [{'word': 'tartarosas', 'greek': 'ταρταρώσας', 'issue': "'Cast into Tartarus' (2:4) — NOT Gehenna or Hades. Tartarus is the Greek mythological prison of the Titans. Peter deliberately uses pagan cosmological language to describe a real spiritual prison.", 'severity': 'CRITICAL'}, {'word': 'seirais zophou', 'greek': 'σειραῖς ζόφου', 'issue': "'Chains of gloomy darkness' (2:4) — some manuscripts read 'pits' (seirois). Either way, imprisoned in darkness awaiting judgment — matching 1 Enoch 10:4-6 exactly.", 'severity': 'CRITICAL'}, {'word': 'theian physin', 'greek': 'θείαν φύσιν', 'issue': "'Divine nature' (1:4) — believers become 'partakers of the divine nature.' The only place in the NT that uses this phrase. Theosis/deification language.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': '1enoch', 'why': 'Tartarus = the prison described in 1 Enoch 10:4-6 and 18:11-19:3 — Peter confirms the Watcher imprisonment using Greek cosmological terms'}, {'target': 'jude', 'why': '2 Pet 2:4-17 closely parallels Jude 5-16 — both draw from the same Watcher tradition. The literary relationship is debated but the theology is identical'}, {'target': 'genesis', 'why': "The angels who sinned (2:4) are the bene ha'elohim of Gen 6:1-4 — Peter treats Genesis 6 as recording a real angelic rebellion"}, {'target': '1peter', 'why': "The 'spirits in prison' of 1 Pet 3:19 are the same 'angels cast into Tartarus' of 2 Pet 2:4 — Peter's consistent cosmology across both letters"}, {'target': 'numbers', 'why': "Balaam's 'way' (2:15) — the paradigm of the corrupt prophet who uses divine gifts for personal gain"}],
        "what_it_doesnt_say": ['Why Peter uses TARTARUS instead of Gehenna or Sheol — is he contextualizing for a Greek audience or making a theological point about the nature of the prison?', 'The relationship between 2 Peter and Jude is never addressed — did one copy the other? Did both use a common source?', "When 'the heavens will be set on fire and dissolved' (3:12) — is this literal cosmic destruction or transformation? The 'new heavens and new earth' (3:13) suggests renewal, not annihilation", "How believers 'become partakers of the divine nature' (1:4) — the mechanism of theosis is stated without explanation"],
        "unusual_characters": [{'name': 'The imprisoned angels', 'ref': '2:4', 'detail': 'Cast into Tartarus — the Greek prison of the Titans. Peter confirms the Watcher framework using the most explicit pagan-cosmological language in the NT.', 'connections': ['1enoch', 'genesis', 'jude']}, {'name': 'Balaam', 'ref': '2:15-16', 'detail': "'The way of Balaam' — using prophetic gifts for profit. His donkey had more spiritual discernment than the prophet.", 'connections': ['numbers', 'jude', 'revelation']}],
        "patterns": ['Three judgments in sequence (2:4-9): fallen angels → ancient world (Flood) → Sodom and Gomorrah. Each confirms God judges rebellious spiritual AND human agents', "Cosmic transformation: the present heavens and earth are 'stored up for fire' (3:7) but 'new heavens and new earth' will follow (3:13) — destruction is the prelude to renewal, not the end", "Eyewitness authority: 'we were eyewitnesses of his majesty' (1:16) at the Transfiguration — Peter grounds his teaching in direct divine encounter, not speculation"],
        "mistranslations": [{'english': 'hell', 'original': 'tartarosas', 'issue': "CRITICAL: most translations render this as 'hell,' hiding the specific cosmological claim. Tartarus is NOT Gehenna — it is the specific prison for fallen divine beings"}, {'english': 'cast them down', 'original': 'tartarosas', 'issue': "The verb form IS the name of the prison — 'tartarus-ed them.' The location is embedded in the action"}, {'english': 'partakers of the divine nature', 'original': 'theias koinonoi physeos', 'issue': "Sounds like abstract theology; this is the most radical deification language in the NT — human beings sharing in God's own nature"}],
    },
    {
        "id": '1john',
        "section": 'new-testament',
        "title": 'Books 62-64: 1-3 John',
        "themes": 'SPIRIT',
        "era_count": 4,
        "chapters": 7,
        "meta_text": '4 era files &middot; 7 chapters',
        "body_html": '''<p>"Test the spirits (pneumata) to see whether they are from God" (1 John 4:1). "The reason the Son of God appeared was to destroy the works of the devil" (3:8). "God is love" (4:8, 16).</p>''',
        "key_claim": "The purpose of the incarnation is cosmic warfare: 'the reason the Son of God appeared was to destroy the works of the devil' (3:8) — and believers must 'test the spirits' (4:1) because the spiritual realm produces both true and false revelation.",
        "contested_words": [{'word': 'lyse', 'greek': 'λύσῃ', 'issue': "'Destroy' (3:8) — lyo means to loose, untie, dissolve. Christ did not merely defeat the devil's works but DISSOLVED them — undoing the damage at a structural level.", 'severity': 'CRITICAL'}, {'word': 'dokimazete ta pneumata', 'greek': 'δοκιμάζετε τὰ πνεύματα', 'issue': "'Test the spirits' (4:1) — dokimazo = assay, examine like testing metal. The spiritual realm produces real entities, not just ideas. Discernment is mandatory.", 'severity': 'CRITICAL'}, {'word': 'hilasmos', 'greek': 'ἱλασμός', 'issue': "'Propitiation/atoning sacrifice' (2:2, 4:10) — same root as hilasterion (Rom 3:25). Christ IS the propitiation for our sins, 'and not for ours only but for the whole world.'", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'john', 'why': "'In the beginning was the Word' (John 1:1) echoes 'what was from the beginning' (1 John 1:1) — both establish pre-existence and personal encounter with the divine"}, {'target': 'genesis', 'why': "'Cain who was of the evil one and murdered his brother' (3:12) — the seed war of Gen 3:15 made personal. Cain = the serpent's seed, Abel = the righteous seed"}, {'target': 'revelation', 'why': 'The spirit of antichrist (2:18, 4:3) active now anticipates the final Antichrist of Revelation — the pattern is already at work'}, {'target': 'deuteronomy', 'why': 'Testing spirits (4:1) fulfills the Deut 13:1-5 mandate to test prophets — false revelation has been a threat since Sinai'}],
        "what_it_doesnt_say": ["How to test the spirits (4:1-3) — the only criterion given is christological: 'every spirit that confesses Jesus Christ has come in the flesh.' Is that sufficient?", "'God is love' (4:8, 16) — the most quoted verse from 1 John, but the letter equally insists God is light (1:5) and truth. Love without light and truth is sentimentality", "The 'sin that leads to death' (5:16) is never identified — apostasy? Blasphemy against the Spirit? An unforgivable threshold?", "'No one born of God makes a practice of sinning' (3:9) — the tension with 1:8 ('if we say we have no sin, we deceive ourselves') is never fully resolved"],
        "unusual_characters": [{'name': 'The antichrist(s)', 'ref': '2:18', 'detail': "'Many antichrists have come' — plural, present, already active. The eschatological Antichrist is preceded by a pattern of anti-Christ spirits in every generation.", 'connections': ['revelation', '2thessalonians']}, {'name': 'Cain', 'ref': '3:12', 'detail': "'Of the evil one' — John identifies Cain's line as belonging to Satan's seed. The Gen 3:15 war personified in the first murder.", 'connections': ['genesis']}],
        "patterns": ['Light/darkness dualism: God is light (1:5), walk in light (1:7), children of light vs. children of darkness — Qumran-like binary that is ultimately christological', "Love as theological test: 'whoever does not love does not know God' (4:8) — love is not sentiment but evidence of divine indwelling. The test is relational, not intellectual", 'Abide/remain (meno): appears 27 times — the central command. Not activity but positioning: stay connected to the vine (John 15 language continued)', "Three witnesses: 'the Spirit and the water and the blood' (5:8) — three dimensions of testimony to Christ's reality"],
        "mistranslations": [{'english': 'propitiation', 'original': 'hilasmos', 'issue': 'Abstract theological term hides the concrete: Christ himself IS the atonement, not merely its agent — the offering and the altar merged'}, {'english': 'test the spirits', 'original': 'dokimazete ta pneumata', 'issue': "'Test' sounds casual; dokimazo means metallurgical assay — rigorous, scientific examination of spiritual claims"}, {'english': 'destroy', 'original': 'lyse', 'issue': "English 'destroy' implies violence; the Greek means 'dissolve, untie, undo' — Christ unravels the devil's work at the structural level"}],
    },
    {
        "id": '2john',
        "section": 'new-testament',
        "title": 'Book 63: 2 John',
        "themes": 'SPIRIT',
        "era_count": 2,
        "chapters": 1,
        "grade": 'B+',
        "meta_text": '2 era files &middot; 1 chapter &middot; Grade: B+',
        "body_html": '''<h4>Major Themes</h4>
  <div class="theme-grid">
    <span class="badge badge-theme">TRUTH</span><span class="badge badge-theme">ANTICHRIST</span><span class="badge badge-theme">HOSPITALITY REFUSED</span><span class="badge badge-theme">INCARNATION TEST</span><span class="badge badge-theme">LOVE &amp; COMMAND</span>
  </div>
  <p><strong>WALKING IN TRUTH</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; "I rejoiced greatly to find some of your children walking in the truth" (v. 4). Truth (aletheia) appears five times in 13 verses. Walking in truth is not abstract belief but embodied practice &mdash; a lifestyle of alignment with the reality God has revealed.</p>
  <p><strong>THE ANTICHRIST TEST</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; "Many deceivers have gone out into the world, those who do not confess the coming of Jesus Christ in the flesh. Such a one is the deceiver and the antichrist" (v. 7). The incarnation &mdash; Christ truly taking on human flesh &mdash; is THE dividing line. Deny the flesh, and you serve the anti-Christ spirit.</p>
  <p><strong>REFUSE FALSE TEACHERS HOSPITALITY</strong> <span class="badge badge-major">MAJOR</span> &mdash; "If anyone comes to you and does not bring this teaching, do not receive him into your house or give him any greeting, for whoever greets him takes part in his wicked works" (vv. 10-11). Radical boundary-drawing: hospitality to false teachers makes you complicit in their deception.</p>

  <h4>Contested Words</h4>
  <table class="ref-table">
    <tr><th>Greek</th><th>Issue</th><th>Severity</th></tr>
    <tr><td><strong>ho planos kai ho antichristos</strong></td><td>"The deceiver and the antichrist" (v. 7) &mdash; the definite articles make this a category, not just a single figure. Everyone who denies Christ in the flesh IS "the antichrist" pattern.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>erchomenon en sarki</strong></td><td>"Coming in the flesh" (v. 7) &mdash; present participle, not past. Some argue this refers to Christ&rsquo;s future return in bodily form, not just the past incarnation. The incarnation is ongoing.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>eklekte kyria</strong> (&epsilon;&kappa;&lambda;&epsilon;&kappa;&tau;&eta; &kappa;&upsilon;&rho;&iota;&alpha;)</td><td>"Elect lady" (v. 1) &mdash; a specific woman? A personification of a local ekklesia? Her "children" could be members. The ambiguity is deliberate.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>proagon</strong> (&pi;&rho;&omicron;&alpha;&gamma;&omega;&nu;)</td><td>"Goes on ahead/runs ahead" (v. 9) &mdash; those who "go beyond" Christ&rsquo;s teaching. Progress beyond the apostolic foundation is regression, not advancement.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
  </table>

  <h4>Unusual Characters</h4>
  <ul>
    <li><strong>The elect lady</strong> (v. 1) &mdash; Either a specific woman leader or a personification of a local ekklesia. The letter is addressed to her and her "children" &mdash; a community under her care or influence.</li>
    <li><strong>The deceivers</strong> (v. 7) &mdash; "Many deceivers have gone out into the world" &mdash; not a future threat but a present reality. They are already embedded in the community&rsquo;s network.</li>
    <li><strong>The elder</strong> (v. 1) &mdash; John identifies himself only as "the elder" (ho presbyteros), not "the apostle." Authority through relationship and age, not title.</li>
  </ul>

  <h4>Conspicuous Silences</h4>
  <ul>
    <li>The identity of the "elect lady" is never clarified &mdash; woman or church? The ambiguity has never been resolved</li>
    <li>The specific false teaching beyond denying Christ "in the flesh" is not described &mdash; what exactly were the deceivers teaching?</li>
    <li>No mention of the Holy Spirit, prayer, or worship &mdash; the letter is entirely focused on truth-boundaries and hospitality ethics</li>
    <li>How to distinguish between legitimate traveling teachers and false ones &mdash; the only criterion is christological confession</li>
  </ul>

  <h4>Cross-References</h4>
  <p class="xref">2 John <span class="arrow">&rarr;</span> <span class="badge badge-nt">1 John</span> <span class="badge badge-nt">3 John</span> <span class="badge badge-nt">Jude</span> <span class="badge badge-nt">Revelation</span></p>''',
        "key_claim": "The incarnation is the non-negotiable dividing line — 'whoever does not confess the coming of Jesus Christ in the flesh' is 'the deceiver and the antichrist' (v. 7) — and extending hospitality to those who deny it makes you 'a participant in their wicked works' (v. 11).",
        "contested_words": [
            {"word": "ho planos kai ho antichristos", "greek": "ὁ πλάνος καὶ ὁ ἀντίχριστος", "issue": "'The deceiver and the antichrist' (v. 7) — definite articles make this a category. Everyone who denies Christ in the flesh IS the antichrist pattern.", "severity": "CRITICAL"},
            {"word": "erchomenon en sarki", "greek": "ἐρχόμενον ἐν σαρκί", "issue": "'Coming in the flesh' (v. 7) — present participle, not past. May refer to Christ's future return in bodily form, not just the past incarnation.", "severity": "CRITICAL"},
            {"word": "eklekte kyria", "greek": "ἐκλεκτὴ κυρία", "issue": "'Elect lady' (v. 1) — a specific woman? A personification of a local ekklesia? Her 'children' could be members. The ambiguity may be deliberate.", "severity": "MAJOR"},
            {"word": "proagon", "greek": "προάγων", "issue": "'Runs ahead' (v. 9) — those who 'go beyond' Christ's teaching. Progress beyond the apostolic foundation is regression, not advancement.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "1john", "why": "The antichrist warning (v. 7) continues 1 John 2:18-22 and 4:1-3 — the same christological test applied to concrete hospitality decisions"},
            {"target": "3john", "why": "2 John warns against receiving false teachers; 3 John rebukes Diotrephes for refusing to receive TRUE teachers — the two letters are complementary boundary-setting"},
            {"target": "jude", "why": "Jude warns of those who 'crept in unnoticed' (Jude 4) — the same infiltration problem that 2 John addresses with the hospitality ban"},
            {"target": "revelation", "why": "The spirit of antichrist (v. 7) active now anticipates the eschatological antichrist of Revelation — the pattern is already operational"},
            {"target": "colossians", "why": "Christ 'in the flesh' (v. 7) connects to Col 1:22 — reconciliation happened 'in his body of flesh by his death.' Deny the flesh, lose the reconciliation"},
        ],
        "what_it_doesnt_say": [
            "The identity of the 'elect lady' — woman or church? The ambiguity has never been resolved",
            "The specific false teaching beyond denying Christ 'in the flesh' — what exactly were the deceivers teaching?",
            "No mention of the Holy Spirit, prayer, or worship — entirely focused on truth-boundaries and hospitality ethics",
            "How to distinguish legitimate traveling teachers from false ones beyond christological confession",
        ],
        "unusual_characters": [
            {"name": "The elect lady", "ref": "v. 1", "detail": "Either a specific woman leader or a personification of a local ekklesia. The letter is addressed to her and her 'children.'", "connections": ["3john"]},
            {"name": "The deceivers", "ref": "v. 7", "detail": "'Many deceivers have gone out into the world' — not future but present. Already embedded in the community's network.", "connections": ["1john", "jude"]},
            {"name": "The elder (John)", "ref": "v. 1", "detail": "Identifies himself as 'the elder,' not 'the apostle.' Authority through relationship and age, not institutional title.", "connections": ["3john"]},
        ],
        "patterns": [
            "Truth as boundary: aletheia appears five times in 13 verses — truth defines who is in and who is out, who receives hospitality and who is turned away",
            "Incarnation as the test: the single theological criterion is christological — does the teacher confess Christ 'coming in the flesh'? Everything else is secondary",
            "Hospitality as theology: in the ancient world, hosting a teacher implied endorsing their message. Refusing hospitality is not rudeness but doctrinal faithfulness",
            "Love and command inseparable: 'this is love, that we walk according to his commandments' (v. 6) — love is not sentiment but obedience, echoing the Deuteronomic pattern",
        ],
        "mistranslations": [
            {"english": "the antichrist", "original": "ho antichristos", "issue": "The definite article makes readers think of one future figure — but John uses it as a CATEGORY. Anyone denying the incarnation embodies the antichrist pattern now"},
            {"english": "does not abide in the teaching", "original": "me menon en te didache", "issue": "'Abide' sounds passive; menon means to remain planted, to hold position. Departure from apostolic teaching is active desertion, not passive drift"},
            {"english": "greet", "original": "chairein", "issue": "'Greeting' sounds trivially social — in the ancient world, the greeting (chairein) was a formal acknowledgment of fellowship. Withholding it was a public declaration of separation"},
        ],
    },
    {
        "id": '3john',
        "section": 'new-testament',
        "title": 'Book 64: 3 John',
        "themes": 'HOLY',
        "era_count": 2,
        "chapters": 1,
        "grade": 'B+',
        "meta_text": '2 era files &middot; 1 chapter &middot; Grade: B+',
        "body_html": '''<h4>Major Themes</h4>
  <div class="theme-grid">
    <span class="badge badge-theme">HOSPITALITY</span><span class="badge badge-theme">TRUTH</span><span class="badge badge-theme">AUTHORITY ABUSE</span><span class="badge badge-theme">MISSIONARY SUPPORT</span><span class="badge badge-theme">IMITATION</span>
  </div>
  <p><strong>HOSPITALITY TO MISSIONARIES</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; Gaius is commended for receiving traveling teachers: "You will do well to send them on their journey in a manner worthy of God. For they have gone out for the sake of the name, accepting nothing from the Gentiles" (vv. 6-7). Material support for missionaries is "fellow workers for the truth" (v. 8) &mdash; hospitality IS partnership in the mission.</p>
  <p><strong>DIOTREPHES: AUTHORITY ABUSE</strong> <span class="badge badge-critical">CRITICAL</span> &mdash; "Diotrephes, who likes to put himself first (philoproteuo), does not acknowledge our authority" (v. 9). He refuses to receive traveling teachers, expels those who do, and slanders the elder with "wicked nonsense" (v. 10). The earliest portrait of authoritarian leadership corrupting the ekklesia.</p>
  <p><strong>IMITATION</strong> <span class="badge badge-major">MAJOR</span> &mdash; "Beloved, do not imitate evil but imitate good. Whoever does good is from God; whoever does evil has not seen God" (v. 11). The letter&rsquo;s ethical core: the choice between Gaius (good model) and Diotrephes (evil model). Character is revealed by imitation choices.</p>

  <h4>Contested Words</h4>
  <table class="ref-table">
    <tr><th>Greek</th><th>Issue</th><th>Severity</th></tr>
    <tr><td><strong>philoproteuo</strong> (&phi;&iota;&lambda;&omicron;&pi;&rho;&omega;&tau;&epsilon;&upsilon;&omega;)</td><td>"Loves to be first" (v. 9) &mdash; a rare word, only here in the NT. Diotrephes&rsquo; problem is not heresy but ambition. He loves preeminence more than truth.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>synergoi te aletheia</strong></td><td>"Fellow workers for the truth" (v. 8) &mdash; hosting missionaries makes you their co-laborer. Hospitality is not charity but partnership in the cosmic mission.</td><td><span class="badge badge-critical">CRITICAL</span></td></tr>
    <tr><td><strong>hyper tou onomatos</strong></td><td>"For the sake of the name" (v. 7) &mdash; THE Name, unspecified. So sacred that the name of Jesus does not need to be stated. The missionaries serve "the Name" itself.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
    <tr><td><strong>phlyaron</strong> (&phi;&lambda;&upsilon;&alpha;&rho;&omega;&nu;)</td><td>"Talking wicked nonsense" (v. 10) &mdash; phlyareo = babble, slander. Diotrephes attacks the elder&rsquo;s character with verbal ammunition. Authority abuse begins with speech.</td><td><span class="badge badge-major">MAJOR</span></td></tr>
  </table>

  <h4>Unusual Characters</h4>
  <ul>
    <li><strong>Gaius</strong> (v. 1) &mdash; Commended for walking in truth AND for showing hospitality to missionaries &mdash; doctrine and practice unified. He supports people he has never met because they serve "the Name."</li>
    <li><strong>Diotrephes</strong> (v. 9) &mdash; "Loves to be first" &mdash; refuses the elder&rsquo;s authority, bars missionaries, expels those who welcome them. The first authoritarian church leader in recorded Christian history.</li>
    <li><strong>Demetrius</strong> (v. 12) &mdash; "Testimony from everyone, and from the truth itself" &mdash; commended by universal witness and by truth as a personified judge. The positive model opposite Diotrephes.</li>
  </ul>

  <h4>Conspicuous Silences</h4>
  <ul>
    <li>What Diotrephes actually teaches is never stated &mdash; his problem is character (ambition), not doctrine, making him harder to identify than a heretic</li>
    <li>Why the elder cannot simply overrule Diotrephes &mdash; apostolic authority appears limited by local ekklesia autonomy</li>
    <li>The identity of Gaius &mdash; there are multiple men named Gaius in the NT (Acts 19:29, 20:4; Rom 16:23; 1 Cor 1:14). Which one, if any?</li>
    <li>The traveling teachers&rsquo; message is never described &mdash; the only criterion is that they go out "for the sake of the name"</li>
  </ul>

  <h4>Cross-References</h4>
  <p class="xref">3 John <span class="arrow">&rarr;</span> <span class="badge badge-nt">2 John</span> <span class="badge badge-nt">1 John</span> <span class="badge badge-nt">Acts</span> <span class="badge badge-nt">1 Corinthians</span></p>''',
        "key_claim": "Diotrephes is the NT's first portrait of authoritarian leadership — 'loves to be first' (philoproteuo, v. 9), refuses apostolic authority, bars missionaries, and expels dissenters — proving that the ekklesia's greatest threat is not always heresy but unchecked human ambition.",
        "contested_words": [
            {"word": "philoproteuo", "greek": "φιλοπρωτεύω", "issue": "'Loves to be first' (v. 9) — a rare word, only here in the NT. Diotrephes' problem is not heresy but ambition. He loves preeminence more than truth.", "severity": "CRITICAL"},
            {"word": "synergoi te aletheia", "greek": "συνεργοὶ τῇ ἀληθείᾳ", "issue": "'Fellow workers for the truth' (v. 8) — hosting missionaries makes you their co-laborer. Hospitality is partnership in the cosmic mission.", "severity": "CRITICAL"},
            {"word": "hyper tou onomatos", "greek": "ὑπὲρ τοῦ ὀνόματος", "issue": "'For the sake of the name' (v. 7) — THE Name, unspecified. So sacred it does not need stating.", "severity": "MAJOR"},
            {"word": "phlyaron", "greek": "φλυαρῶν", "issue": "'Talking wicked nonsense' (v. 10) — phlyareo = babble, slander. Authority abuse begins with speech attacks against legitimate leaders.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "2john", "why": "2 John warns against receiving false teachers; 3 John rebukes refusing TRUE teachers — the two letters are mirror-image boundary problems"},
            {"target": "1john", "why": "'Walking in truth' (v. 3) continues the theme of 1 John — truth is embodied practice, not abstract belief. Gaius is the living proof"},
            {"target": "acts", "why": "The traveling missionary model (vv. 5-8) reflects the apostolic pattern of Acts — itinerant teachers dependent on local ekklesia hospitality"},
            {"target": "1corinthians", "why": "Paul's 'I planted, Apollos watered' (1 Cor 3:6) shows the same missionary network — different roles, one mission, mutual dependency"},
            {"target": "matthew", "why": "'Whoever receives a prophet in the name of a prophet receives a prophet's reward' (Matt 10:41) — the principle behind Gaius's commendation"},
        ],
        "what_it_doesnt_say": [
            "What Diotrephes actually teaches — his problem is character (ambition), not doctrine, making him harder to identify than a heretic",
            "Why the elder cannot simply overrule Diotrephes — apostolic authority appears limited by local ekklesia autonomy",
            "The identity of Gaius — multiple men bear this name in the NT. Which one, if any?",
            "The traveling teachers' message is never described — the only criterion is 'for the sake of the name'",
        ],
        "unusual_characters": [
            {"name": "Gaius", "ref": "v. 1", "detail": "Commended for walking in truth AND hospitality to missionaries — doctrine and practice unified. Supports people he has never met.", "connections": ["romans", "1corinthians"]},
            {"name": "Diotrephes", "ref": "v. 9", "detail": "'Loves to be first' — refuses the elder, bars missionaries, expels dissenters. The first authoritarian ekklesia leader in recorded history.", "connections": []},
            {"name": "Demetrius", "ref": "v. 12", "detail": "'Testimony from everyone, and from the truth itself' — commended by universal witness and by truth personified. The positive model opposite Diotrephes.", "connections": []},
        ],
        "patterns": [
            "Three character portraits: Gaius (faithful host), Diotrephes (authoritarian abuser), Demetrius (commended by all) — the letter evaluates people by their relationship to truth and hospitality",
            "Hospitality as mission: supporting missionaries financially and materially makes you a 'fellow worker for the truth' (v. 8) — material provision is spiritual partnership",
            "Authority vs. ambition: the elder has legitimate authority but cannot enforce it against Diotrephes — local ekklesia autonomy creates both freedom and vulnerability",
            "Imitation ethics: 'do not imitate evil but imitate good' (v. 11) — the choice between models (Gaius vs. Diotrephes) is the choice between God and not-God",
        ],
        "mistranslations": [
            {"english": "who likes to put himself first", "original": "ho philoproteuo", "issue": "Sounds like mild vanity; philoproteuo is love of preeminence — an active, consuming desire to dominate that overrides truth, relationships, and apostolic authority"},
            {"english": "fellow workers", "original": "synergoi", "issue": "Sounds like colleagues; synergoi means co-laborers in the same cosmic enterprise. Hosting a missionary is not charity but front-line participation"},
            {"english": "church", "original": "ekklesia", "issue": "'Church' again obscures the governing-assembly meaning. Diotrephes is not a pastor gone bad — he is a council member who has seized unauthorized control of a governing body"},
        ],
    },
    {
        "id": 'jude',
        "section": 'new-testament',
        "title": 'Book 65: Jude',
        "themes": 'DC SPIRIT REBEL',
        "era_count": 1,
        "chapters": 1,
        "meta_text": '1 era file &middot; 1 chapter &middot; O-CANON',
        "body_html": '''<p><strong>MOST EXPLICIT NT ENGAGEMENT WITH 1 ENOCH</strong> — "Angels who did not stay within their position but left their proper dwelling — kept in eternal chains" (v. 6) = Watcher rebellion. "Michael the archangel disputed with the devil about the body of Moses" (v. 9) = divine council conflict. Jude 14-15 DIRECTLY QUOTES 1 Enoch 1:9 as prophecy: "Enoch, the seventh from Adam, prophesied." Treats 1 Enoch as authoritative.</p>''',
        "key_claim": "Jude is the most explicit NT engagement with 1 Enoch — directly quoting 1 Enoch 1:9 as prophecy ('Enoch, the seventh from Adam, prophesied,' vv. 14-15) and treating the Watcher rebellion as historical fact (v. 6), confirming the imprisoned-angel framework that 1 Peter and 2 Peter also assume.",
        "contested_words": [{'word': 'proephetyeusen', 'greek': 'προεφήτευσεν', 'issue': "'Prophesied' (v. 14) — Jude calls Enoch's words PROPHECY, not merely useful literature. This is the strongest canonical endorsement of 1 Enoch's authority.", 'severity': 'CRITICAL'}, {'word': 'oiketerion', 'greek': 'οἰκητήριον', 'issue': "'Proper dwelling' (v. 6) — the angels 'left their proper dwelling.' oiketerion is used only here and 2 Cor 5:2 (of the resurrection body). The Watchers abandoned their heavenly body/domain.", 'severity': 'CRITICAL'}, {'word': 'desmois aidiois', 'greek': 'δεσμοῖς ἀϊδίοις', 'issue': "'Eternal chains' (v. 6) — the imprisoned Watchers bound in everlasting bonds. Matches 1 Enoch 10:4-6 and 2 Pet 2:4 (Tartarus). Real prison, real chains, real judgment awaited.", 'severity': 'CRITICAL'}],
        "hidden_connections": [{'target': '1enoch', 'why': 'Jude 14-15 directly quotes 1 Enoch 1:9. Jude 6 parallels 1 Enoch 10:4-6 (imprisoned Watchers). The most explicit canonical use of 1 Enoch'}, {'target': 'genesis', 'why': "The angels 'who did not stay within their position' (v. 6) are the bene ha'elohim of Gen 6:1-4 who took human wives"}, {'target': '2peter', 'why': 'Jude and 2 Peter share extensive material — both cite fallen angels, Balaam, and similar false teachers. The literary relationship confirms a shared Watcher tradition'}, {'target': '1peter', 'why': "The 'spirits in prison' (1 Pet 3:19) are the same 'angels kept in eternal chains' (Jude 6) — Peter and Jude share the same cosmology"}, {'target': 'numbers', 'why': "Balaam (v. 11) and Korah's rebellion (v. 11) both from Numbers — Jude reads OT history as a pattern of spiritual rebellion"}, {'target': 'daniel', 'why': "'Michael the archangel disputed with the devil about the body of Moses' (v. 9) — divine council conflict at the highest levels"}],
        "what_it_doesnt_say": ["The source of the Michael-Satan dispute over Moses' body (v. 9) — Jude cites it as known but our source text (Assumption of Moses) is fragmentary", 'WHY Jude treats 1 Enoch as authoritative prophecy — does quotation equal canonization? The letter never addresses the canon question', "The identity of the false teachers (v. 4) — they 'crept in unnoticed' but their specific heresy is described in imagery, not doctrine", "How the Watchers 'left their proper dwelling' (v. 6) — the mechanics of angelic embodiment are assumed, not explained"],
        "unusual_characters": [{'name': 'Michael the archangel', 'ref': 'v. 9', 'detail': "Disputes with the devil over Moses' body — even the chief angel does not pronounce judgment independently but says 'The Lord rebuke you.' Divine council protocol.", 'connections': ['daniel', 'revelation']}, {'name': 'Enoch', 'ref': 'v. 14', 'detail': "'The seventh from Adam' — Jude specifies his genealogical position and calls his words PROPHECY. The strongest canonical endorsement of Enoch's authority.", 'connections': ['genesis', '1enoch', 'hebrews']}, {'name': 'Cain, Balaam, Korah', 'ref': 'v. 11', 'detail': 'Three OT rebels as a pattern: Cain (murder from envy), Balaam (prophecy for profit), Korah (rebellion against authority). Three types of apostasy.', 'connections': ['genesis', 'numbers']}],
        "patterns": ['Triad of judgment examples: angels who fell (v. 6), Sodom and Gomorrah (v. 7), and the wilderness generation (v. 5) — spiritual, sexual, and national rebellion all judged', "Triad of apostasy types: 'way of Cain' (murder/envy), 'error of Balaam' (greed/corruption), 'rebellion of Korah' (authority rejection) — the three patterns recur in every generation", "Doxology framework: the letter ends with one of the most powerful doxologies in Scripture (vv. 24-25) — 'to the only God our Savior... before all time and now and forever'"],
        "mistranslations": [{'english': 'contend for the faith', 'original': 'epagonizomai', 'issue': 'Sounds intellectual; the Greek is athletic/military — agonize, struggle, fight for the faith. This is combat language, not debate language'}, {'english': 'kept in eternal chains', 'original': 'desmois aidiois hypo zophon tetereken', 'issue': 'Often spiritualized; Jude means actual imprisonment of actual beings in actual darkness — the Watcher tradition taken at face value'}, {'english': 'wandering stars', 'original': 'asteres planetai', 'issue': 'Poetic in English; in Jewish cosmology, wandering stars are fallen angels — beings that left their ordained orbit/position. Direct 1 Enoch imagery'}],
    },
    {
        "id": 'revelation',
        "section": 'new-testament',
        "title": 'Book 66: Revelation (Apokalypsis)',
        "themes": 'DC KING SEED COV HOLY SPIRIT NATIONS REBEL EXILE',
        "era_count": 4,
        "chapters": 22,
        "grade": 'A+',
        "meta_text": '4 era files &middot; 22 chapters &middot; Grade: A+',
        "body_html": '''<p><strong>THE DIVINE COUNCIL'S FINAL SESSION</strong> — Every thread converges. The throne room (chs. 4-5): 24 elders, 4 living creatures (= Ezekiel's chayyot), myriads of angels. Only the slain Lamb can open the scroll. "You ransomed people from EVERY tribe and language and people and nation" (5:9) — Deut 32:8 FULLY reversed.</p><p><strong>THE NACHASH IDENTIFIED</strong> (12:9) — "That ancient serpent (ophis ho archaios), who is called the devil (diabolos) and Satan (satanas), the deceiver of the whole world." FOUR NAMES linking the entire story: serpent (Gen 3), devil (Job 1-2), Satan (1 Chr 21:1), deceiver of nations (Deut 32:8 corruption).</p><p><strong>EDEN RESTORED</strong> (21-22) — New heaven and new earth. River of life from the throne (Ezek 47). Tree of life on both sides (Gen 2:9). "They will see his face" (Num 6:25 Priestly Blessing fulfilled). "They will reign forever" (Gen 1:26 mandate restored). "Behold, I am making all things new" (21:5).</p></div></div>

<!-- NON-CANONICAL -->''',
        "key_claim": "Revelation is the divine council's final session — every thread converges as the Lamb opens the scroll, the nachash of Genesis 3 is identified by four names (serpent, devil, Satan, deceiver), and the Deut 32:8 allotment is FULLY reversed: 'You ransomed people from EVERY tribe and language and people and nation' (5:9).",
        "contested_words": [{'word': 'ophis ho archaios', 'greek': 'ὄφις ὁ ἀρχαῖος', 'issue': "'That ancient serpent' (12:9) — four names: serpent (Gen 3), devil (diabolos), Satan (ha-satan), deceiver of the whole world. The entire story unified in one identification.", 'severity': 'CRITICAL'}, {'word': 'arnion', 'greek': 'ἀρνίον', 'issue': "'Lamb' — appears 28 times in Revelation. NOT amnos (sacrificial lamb, John 1:29) but arnion (small lamb/lambkin). The most powerful being in the cosmos described by the weakest term.", 'severity': 'CRITICAL'}, {'word': 'nikao', 'greek': 'νικάω', 'issue': "'Conquer/overcome' — 17 times in Revelation. The seven letters each end with promises 'to the one who conquers.' Victory language permeates the entire book.", 'severity': 'MAJOR'}, {'word': 'martyria', 'greek': 'μαρτυρία', 'issue': "'Testimony/witness' — same root as 'martyr.' In Revelation, bearing witness and dying for it are the same word. Testimony IS the mechanism of conquest.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'genesis', 'why': 'Eden bookend: the nachash of Gen 3 identified (12:9), the tree of life restored (22:2), the curse removed (22:3) — Rev 21-22 is Genesis 1-3 restored and surpassed'}, {'target': 'deuteronomy', 'why': "'You ransomed people from every tribe, language, people, nation' (5:9) — the Deut 32:8 allotment FULLY reversed. Every nation reclaimed from the corrupt elohim"}, {'target': 'daniel', 'why': "Rev 13 draws from Dan 7 (beasts from the sea), Rev 20 from Dan 12 (resurrection and judgment). Daniel's visions find their consummation in Revelation"}, {'target': 'ezekiel', 'why': 'The new Jerusalem (Rev 21) draws from Ezek 40-48 (new temple), the river of life from Ezek 47, the throne vision from Ezek 1. Revelation is Ezekiel fulfilled'}, {'target': 'exodus', 'why': 'The plagues of Revelation (trumpets, bowls) recapitulate the Exodus plagues on a cosmic scale — liberation from a spiritual Egypt'}, {'target': '1enoch', 'why': 'The binding of Satan (20:1-3) parallels the binding of Azazel (1 Enoch 10:4-6) — both imprisoned in a pit, both released for a final period'}, {'target': 'psalms', 'why': "Ps 2 ('the nations rage') underlies Rev 11:18, 19:15 — the divine decree against rebellious nations and their spiritual rulers"}],
        "what_it_doesnt_say": ["The 'millennium' (20:1-6) — premillennial, postmillennial, or amillennial? The text describes 1,000 years without specifying whether the number is literal or symbolic", 'The identity of the 144,000 (7:4, 14:1) — literal Israel or symbolic of the complete people of God? Twelve tribes times twelve thousand — the number is clearly structured', "The new Jerusalem descending 'from heaven' (21:2) — is this a city, a people, or both? The bride/city fusion is never resolved", "How the 'nations will walk by its light' (21:24) — if all evil is destroyed, who are these nations? The relationship between the new earth's inhabitants and the New Jerusalem is unclear"],
        "unusual_characters": [{'name': 'The Lamb (arnion)', 'ref': '5:6', 'detail': "Standing 'as though slain' with seven horns and seven eyes — the sacrificial victim IS the most powerful being in the cosmos. Weakness IS power.", 'connections': ['john', 'exodus', 'isaiah']}, {'name': 'The four living creatures', 'ref': '4:6-8', 'detail': "Lion, ox, eagle, human — echoing Ezekiel's chayyot. They never stop saying 'Holy, holy, holy' — the throne room of God in perpetual worship.", 'connections': ['ezekiel', 'isaiah']}, {'name': 'The two witnesses', 'ref': '11:3-12', 'detail': 'Power to shut heaven (Elijah) and turn water to blood (Moses) — the Law and Prophets testifying together in the end.', 'connections': ['exodus', '1kings']}, {'name': 'Michael', 'ref': '12:7', 'detail': 'Leads the angelic army against the dragon — divine council warfare at its most explicit. Heaven itself becomes a battlefield.', 'connections': ['daniel', 'jude']}],
        "patterns": ['Sevenfold structure: 7 letters, 7 seals, 7 trumpets, 7 bowls — each cycle intensifies, but all cover the same period from different angles (recapitulation, not strict chronology)', 'Worship scenes punctuate every judgment cycle — the throne room doxologies (4:8-11, 5:9-14, 7:9-12, 11:15-18, 15:3-4, 19:1-8) frame all destruction in the context of worship', 'Babylon vs. New Jerusalem: the great prostitute (ch. 17) vs. the holy bride (ch. 21) — two cities, two systems, two destinies. Every human being lives in one or the other', 'The conqueror promises (chs. 2-3) are all fulfilled in chs. 21-22: tree of life (2:7→22:2), no second death (2:11→21:8), hidden manna (2:17→22:2), authority over nations (2:26→22:5)', "Eden-to-Eden arc: Gen 1-3 (garden, tree, river, presence of God, no curse) → Rev 21-22 (city-garden, tree, river, presence of God, no more curse) — the Bible's narrative envelope"],
        "mistranslations": [{'english': 'Lamb', 'original': 'arnion', 'issue': 'English cannot capture that Revelation uses a DIMINUTIVE (little lamb/lambkin) for the most powerful being in existence — deliberate paradox of power through weakness'}, {'english': 'beast', 'original': 'therion', 'issue': "English 'beast' sounds mythological; therion is a wild animal — the contrast is between the domesticated lamb and the wild, untamed power of empire"}, {'english': 'witness/testimony', 'original': 'martyria', 'issue': "Modern 'witness' has lost its teeth — the Greek became 'martyr' because testimony in Revelation costs your life. Witness = death sentence"}],
    },
    {
        "id": 'enoch',
        "section": 'non-canonical',
        "title": '1 Enoch (Ethiopic Enoch)',
        "themes": 'DC REBEL SPIRIT',
        "era_count": 5,
        "meta_text": '5 era files &middot; Highly authoritative — Jude quotes as prophecy',
        "body_html": '''<p><strong>WATCHER REBELLION</strong> (chs. 6-16) — Names the 200 Watchers. Azazel teaches warfare. Offspring (Nephilim) become demons when killed (15:8-10): disembodied spirits = demons. This explains why demons seek bodies (Matt 12:43-45).</p><p><strong>SON OF MAN</strong> (Parables, chs. 37-71) — Pre-existent figure on the throne of glory who judges. Daniel 7:13 expanded.</p>''',
        "key_claim": 'According to 1 Enoch, the 200 Watchers who descended on Mount Hermon taught forbidden knowledge to humanity, their offspring (the Nephilim) became demons when killed (15:8-10), and the pre-existent Son of Man sits on the throne of glory to judge all — a framework that the NT authors (Jude, Peter, Jesus himself) treat as authoritative.',
        "contested_words": [{'word': 'Watchers (Irin)', 'hebrew': 'עִירִין', 'issue': "'Watchers' — divine beings who 'watch' over humanity. The term appears in Dan 4:13, 17, 23 (Aramaic). 1 Enoch expands their story: 200 descend on Hermon, take human wives, teach forbidden arts.", 'severity': 'CRITICAL'}, {'word': 'Azazel', 'hebrew': 'עֲזָאזֵל', 'issue': 'Leader of the Watchers who taught humanity warfare and cosmetics (1 En 8:1-2). The same being addressed in Lev 16 (Day of Atonement scapegoat) — sins sent BACK to their originator.', 'severity': 'CRITICAL'}, {'word': 'Nephilim', 'hebrew': 'נְפִילִים', 'issue': 'Offspring of Watchers and human women. 1 Enoch 15:8-10 explains that when they die, their disembodied spirits become DEMONS — the missing origin story for evil spirits.', 'severity': 'CRITICAL'}, {'word': 'Son of Man', 'greek': 'υἱὸς τοῦ ἀνθρώπου', 'issue': "The Parables of Enoch (chs. 37-71) describe a pre-existent, enthroned Son of Man who judges. Jesus' self-designation draws from both Dan 7:13 AND the Enochic tradition.", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'genesis', 'why': '1 Enoch 6-16 is the expanded narrative of Gen 6:1-4 — what Genesis compresses into four verses, 1 Enoch unfolds into eleven chapters'}, {'target': 'jude', 'why': 'Jude 14-15 directly quotes 1 Enoch 1:9 as prophecy and treats the Watcher rebellion (Jude 6) as historical fact'}, {'target': 'leviticus', 'why': 'Azazel in Lev 16 is the same being named in 1 Enoch 10:4-6 — the Day of Atonement scapegoat ritual sends sins back to the Watcher leader'}, {'target': 'daniel', 'why': "The 'Watchers' appear in Dan 4:13, 17, 23. The 'Son of Man' in Dan 7:13 is expanded in 1 Enoch's Parables (chs. 37-71)"}, {'target': '2peter', 'why': "'God did not spare angels when they sinned but cast them into Tartarus' (2 Pet 2:4) — Peter confirms the 1 Enoch imprisonment narrative"}, {'target': 'matthew', 'why': "Jesus' demons seeking bodies (Matt 12:43-45) is explained by 1 Enoch 15:8-10 — disembodied Nephilim spirits seeking re-embodiment"}],
        "what_it_doesnt_say": ["According to 1 Enoch, the Watchers' motivation beyond lust is never fully explored — why did 200 divine beings coordinate a rebellion?", 'The relationship between the Parables (chs. 37-71) and the Book of Giants (found at Qumran instead) — why did different communities preserve different traditions?', 'How Enoch traveled through the heavens — the cosmological journeys describe locations but not the mechanism of ascent', "According to 1 Enoch, the ultimate fate of the Watchers after final judgment is described but the duration of 'forever' is ambiguous in the original language"],
        "unusual_characters": [{'name': 'Semjaza (Shemihazah)', 'ref': '6:3', 'detail': 'Leader of the 200 Watchers who organized the oath on Mount Hermon. According to 1 Enoch, he feared acting alone and required a mutual pact.', 'connections': ['genesis']}, {'name': 'Azazel', 'ref': '8:1, 10:4-6', 'detail': 'According to 1 Enoch, the Watcher who taught warfare, metalwork, and cosmetics. Bound hand and foot, cast into darkness — the same being addressed in Lev 16.', 'connections': ['leviticus']}, {'name': 'The Son of Man (Parables)', 'ref': '46:1-4', 'detail': "According to 1 Enoch, a pre-existent figure with 'a head white as wool' who sits on the throne of glory. The imagery Jesus drew from for his self-designation.", 'connections': ['daniel', 'matthew', 'revelation']}],
        "patterns": ['According to 1 Enoch, the Watcher narrative follows a rebellion-judgment-imprisonment arc that parallels the Eden rebellion and the Babel rebellion — three cosmic failures, three divine responses', 'The heavenly journeys (chs. 17-36, 72-82) establish a cosmological framework: Sheol compartments, celestial mechanics, boundary geography — systematic supernatural cartography', 'The demon-origin theory (15:8-10): Nephilim die → spirits have no body → seek embodiment → become demons. This explains the entire NT exorcism tradition', "The Son of Man in the Parables (37-71) grows from hidden to revealed to enthroned — the same revelation pattern as Jesus' ministry in the Gospels"],
        "mistranslations": [{'english': 'angels', 'original': 'Watchers (Irin)', 'issue': "Calling them 'angels' conflates different categories — Watchers are a specific class of divine beings with a specific function and a specific rebellion"}, {'english': 'giants', 'original': 'Nephilim', 'issue': 'Reduces the theological category to physical size — the Nephilim are divine-human hybrids whose spiritual status (disembodied = demons) matters more than their height'}, {'english': 'Son of Man', 'original': 'Son of Man', 'issue': "The Enochic Son of Man is pre-existent and enthroned — 'Son of Man' sounds humble in English but in this context it is the highest possible title"}],
    },
    {
        "id": 'jubilees',
        "section": 'non-canonical',
        "title": 'Jubilees',
        "themes": 'COV DC',
        "era_count": 5,
        "meta_text": '5 era files &middot; Calendar theology',
        "body_html": '''<p>Retells Genesis-Exodus. Angel of the Presence mediates Torah (confirmed Acts 7:53, Gal 3:19). Mastema (chief demon) retains 1/10 of demons after the Flood. 364-day solar calendar divided Second Temple Judaism.</p>''',
        "key_claim": 'According to Jubilees, the Angel of the Presence mediated Torah to Moses directly — a tradition confirmed by Acts 7:53 and Gal 3:19 — and the chief demon Mastema retained one-tenth of the demons after the Flood to test humanity, explaining why evil persists in a post-Flood world.',
        "contested_words": [{'word': 'Angel of the Presence', 'hebrew': 'מַלְאַךְ הַפָּנִים', 'issue': 'According to Jubilees, Torah was dictated by the Angel of the Presence (malak ha-panim) — a specific divine being who stands before God. This is the mediating angel confirmed by Stephen (Acts 7:53) and Paul (Gal 3:19).', 'severity': 'CRITICAL'}, {'word': 'Mastema', 'hebrew': 'מַשְׂטֵמָה', 'issue': 'According to Jubilees, the chief of demons — derived from satan/accuse. After the Flood, God agrees to let Mastema retain 1/10 of the demons to test humanity. A negotiated arrangement, not uncontrolled evil.', 'severity': 'CRITICAL'}, {'word': '364-day calendar', 'hebrew': '', 'issue': 'According to Jubilees, the solar calendar of 364 days (52 weeks exactly) is the true calendar ordained at creation. This calendar controversy divided Second Temple Judaism and is central to the Dead Sea Scrolls community.', 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'acts', 'why': "Stephen's speech: 'you who received the law as delivered by angels' (Acts 7:53) confirms Jubilees' tradition of angelic mediation of Torah"}, {'target': 'galatians', 'why': "Paul: the law was 'ordained through angels' (Gal 3:19) — same tradition as Jubilees. The angelic mediation is canonical even if Jubilees is not"}, {'target': 'genesis', 'why': 'Jubilees retells Genesis with expanded detail — filling gaps, providing dates, and adding the angelic perspective on patriarchal history'}, {'target': 'exodus', 'why': 'Jubilees retells the Exodus with emphasis on the calendar and Passover dating — the liturgical framework behind the narrative'}, {'target': '1enoch', 'why': 'Jubilees shares the Watcher tradition with 1 Enoch but adds the Mastema negotiation — a different emphasis on the demon problem'}, {'target': 'dss', 'why': "Jubilees was one of the most popular texts at Qumran — the 364-day calendar was the community's liturgical backbone"}],
        "what_it_doesnt_say": ['According to Jubilees, WHY God agreed to let Mastema keep 1/10 of the demons is never explained — a divine concession with enormous consequences', 'The 364-day calendar creates a perpetual conflict with the 354-day lunar calendar — Jubilees never acknowledges the astronomical problem', 'How the Angel of the Presence could mediate Torah when Exodus describes YHWH speaking directly to Moses — the mediation framework is added, not reconciled', 'According to Jubilees, the relationship between Mastema and Satan/ha-satan is unclear — are they the same being or different?'],
        "unusual_characters": [{'name': 'Mastema', 'ref': '10:8-11', 'detail': 'According to Jubilees, the prince of demons who petitioned God to retain 1/10 of the spirits. Same role as ha-satan in Job but with a different name and backstory.', 'connections': ['job', '1enoch']}, {'name': 'The Angel of the Presence', 'ref': '1:27', 'detail': 'According to Jubilees, the specific angel who dictates the entire book to Moses. A divine being with face-to-face access to God — the mediator of Torah.', 'connections': ['exodus', 'acts', 'galatians']}],
        "patterns": ['According to Jubilees, all history is organized into jubilee periods (49-year cycles) — time itself has a theological structure rooted in Lev 25', 'The Mastema negotiation (10:8-11): Flood → spirits released → Mastema asks to retain some → God allows 1/10. Evil is permitted, bounded, and purposeful', 'According to Jubilees, calendar polemics run throughout: the 364-day solar calendar ensures festivals always fall on the same weekday — liturgical order reflecting cosmic order'],
        "mistranslations": [{'english': 'Book of Jubilees', 'original': 'Sefer ha-Yovelim', 'issue': 'The title refers to jubilee-year dating system — the text organizes ALL of history into jubilee periods, making the calendar itself the theological framework'}, {'english': 'Mastema', 'original': 'Mastema', 'issue': "Often left untranslated; the root means 'hostility/accusation' — functionally equivalent to ha-satan (the accuser) but with a specific post-Flood origin story"}],
    },
    {
        "id": 'jasher',
        "section": 'non-canonical',
        "title": 'Jasher (Sefer HaYashar)',
        "themes": 'SEED',
        "era_count": 6,
        "meta_text": '6 era files &middot; Referenced in Josh 10:13, 2 Sam 1:18',
        "body_html": '''<p>Expands patriarchal narratives. Abraham's childhood, Nimrod, tower of Babel details. NOT the original Book of Jashar (that text is lost).</p>''',
        "key_claim": "Jasher expands the patriarchal narratives with vivid detail — Abraham's childhood, Nimrod's tyranny, the tower of Babel — but this medieval compilation is NOT the original Book of Jashar referenced in Joshua 10:13 and 2 Samuel 1:18, which is lost.",
        "contested_words": [{'word': 'Sefer HaYashar', 'hebrew': 'סֵפֶר הַיָּשָׁר', 'issue': "'Book of the Upright/Righteous' — the original Jashar is cited in Josh 10:13 and 2 Sam 1:18 as a source the biblical authors used. This medieval text claims that title but cannot be verified as the original.", 'severity': 'CRITICAL'}, {'word': 'Nimrod', 'hebrew': 'נִמְרוֹד', 'issue': 'Genesis mentions Nimrod briefly (Gen 10:8-12); Jasher expands him into a major figure — tyrant, tower builder, hunter. The expansion is vivid but cannot be verified against the lost original.', 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'genesis', 'why': "Jasher fills narrative gaps in Genesis: Abraham's childhood, the tower of Babel details, Jacob and Esau's conflicts — whether historical or legendary, it shows how ancient readers imagined the missing stories"}, {'target': 'joshua', 'why': 'Josh 10:13 cites the ORIGINAL Book of Jashar for the sun standing still — this text claims that name but predates the original by over a millennium'}, {'target': '2samuel', 'why': "2 Sam 1:18 cites the original Book of Jashar for David's lament — another canonical reference to the lost source"}, {'target': '1enoch', 'why': 'Jasher shares some patriarchal expansion traditions with 1 Enoch — particularly the pre-Flood period and the giants'}],
        "what_it_doesnt_say": ['No claim to divine inspiration — unlike biblical texts, Jasher presents itself as historical narrative without prophetic authority', 'The connection to the ORIGINAL Book of Jashar is never proven — the medieval text appeared in the 16th-18th century with no manuscript chain to antiquity', 'The expanded Nimrod narrative has no parallel in other ancient sources — it may preserve genuine tradition or may be medieval invention', 'How to distinguish historical memory from legendary expansion — Jasher mixes plausible detail with fantastic elements without differentiation'],
        "unusual_characters": [{'name': 'Nimrod', 'ref': 'ch. 7-12', 'detail': "Expanded from Genesis's brief mention into a full-scale tyrant — receives the garments of Adam, becomes a mighty hunter, builds the tower. Historically unverifiable.", 'connections': ['genesis']}, {'name': 'Abraham (childhood)', 'ref': 'ch. 8-12', 'detail': "Jasher provides a detailed childhood narrative — hiding in a cave, confronting idolatry, conflict with Nimrod. Fills Genesis's total silence about Abraham before age 75.", 'connections': ['genesis']}],
        "patterns": ["Gap-filling pattern: wherever Genesis is silent (Abraham's childhood, Nimrod's story, the tower of Babel), Jasher provides detailed narrative — ancient midrashic tradition in action", "The patriarchal narratives follow Genesis's sequence but with expanded dialogue, motivation, and secondary characters — interpretive expansion, not contradiction", 'The text preserves the seed-line emphasis: patriarchal genealogies and conflicts are always framed in terms of the righteous line vs. the rebellious'],
        "mistranslations": [{'english': 'Book of Jasher', 'original': 'Sefer HaYashar', 'issue': 'The title creates confusion with the biblical reference — readers must understand this is NOT the text Joshua and Samuel cite. That text is lost'}, {'english': 'Jasher', 'original': 'Yashar', 'issue': "'Jasher' sounds like a person's name; yashar means 'upright/straight/righteous' — it is a TITLE ('Book of the Upright'), not an author's name"}],
    },
    {
        "id": 'dss',
        "section": 'non-canonical',
        "title": 'Dead Sea Scrolls',
        "themes": 'DC SPIRIT',
        "era_count": 5,
        "meta_text": '5 era files &middot; ~250 BC - 68 AD',
        "body_html": '''<p><strong>4QDeut<sup>j</sup></strong> — Preserves "sons of God" at Deut 32:8. THE most important textual witness for this app.</p><p><strong>11Q13 (Melchizedek Scroll)</strong> — Melchizedek as divine figure executing judgment on fallen gods of Psalm 82. Connects Gen 14 &rarr; Ps 82 &rarr; Ps 110 &rarr; Hebrews 7.</p><p><strong>War Scroll (1QM)</strong> — Cosmic warfare: Sons of Light vs. Sons of Darkness. Divine council military theology.</p>''',
        "key_claim": "The Dead Sea Scrolls preserve the original reading of Deut 32:8 ('sons of God' instead of 'sons of Israel') — the most important textual witness for the divine council framework — and 11Q13 presents Melchizedek as a divine figure executing the judgment of Psalm 82.",
        "contested_words": [{'word': 'bene elohim (4QDeut-j)', 'hebrew': 'בְּנֵי אֱלֹהִים', 'issue': "4QDeut-j preserves 'sons of God' at Deut 32:8 where the MT has 'sons of Israel' — the most consequential textual variant in the OT. The DSS reading is independently confirmed by the LXX.", 'severity': 'CRITICAL'}, {'word': 'Melchizedek (11Q13)', 'hebrew': 'מַלְכִּי־צֶדֶק', 'issue': '11Q13 presents Melchizedek as an ELOHIM — a divine being who executes the judgment of Ps 82 against fallen gods. Not merely a human priest-king but a divine figure.', 'severity': 'CRITICAL'}, {'word': 'Sons of Light / Sons of Darkness', 'hebrew': 'בְּנֵי אוֹר / בְּנֵי חוֹשֶׁךְ', 'issue': "The War Scroll (1QM) divides all reality into Sons of Light and Sons of Darkness — cosmic warfare between YHWH's camp and Belial's. The binary shapes NT language (John, Paul, 1 John).", 'severity': 'MAJOR'}, {'word': 'Belial', 'hebrew': 'בְּלִיַּעַל', 'issue': "The DSS name for the chief adversary — distinct from ha-satan. Belial rules the Sons of Darkness. Paul uses the name once: 'What accord has Christ with Belial?' (2 Cor 6:15).", 'severity': 'MAJOR'}],
        "hidden_connections": [{'target': 'deuteronomy', 'why': "4QDeut-j is THE textual witness: 'sons of God' at Deut 32:8 proves the MT 'sons of Israel' is a scribal alteration — the divine council allotment is original"}, {'target': 'psalms', 'why': '11Q13 reads Ps 82 as Melchizedek judging the corrupt elohim — connecting Gen 14 → Ps 82 → Ps 110 into a continuous divine-figure narrative'}, {'target': 'hebrews', 'why': "11Q13's divine Melchizedek illuminates Heb 7 — the Qumran community saw the same Melchizedek-as-divine-being connection that Hebrews develops christologically"}, {'target': 'genesis', 'why': 'The Genesis Apocryphon (1QapGen) retells patriarchal stories with expanded detail — parallel to Jubilees and Jasher in the gap-filling tradition'}, {'target': '1enoch', 'why': 'Multiple copies of 1 Enoch found at Qumran (except the Parables) — the community treated it as authoritative. The Watcher tradition was mainstream, not fringe'}, {'target': 'isaiah', 'why': 'The Great Isaiah Scroll (1QIsa-a) is the oldest nearly complete OT manuscript — confirming the textual stability of Isaiah across 1,000 years'}],
        "what_it_doesnt_say": ["The identity of the 'Teacher of Righteousness' — the community's founder is never named in any scroll", 'Why the Qumran community separated from Jerusalem — the calendar dispute is clear but the triggering event is debated', 'The scrolls never mention Jesus or early Christianity — the temporal overlap exists but direct connection is unproven', 'How the community understood the relationship between Melchizedek (11Q13) and the Messiah(s) they expected — one figure or two?'],
        "unusual_characters": [{'name': 'Melchizedek (11Q13)', 'ref': '11Q13', 'detail': 'Presented as a divine figure (elohim) who executes Ps 82 judgment, proclaims liberty in the final Jubilee, and atones for the Sons of Light. The Qumran community read Gen 14 as about a divine being.', 'connections': ['genesis', 'psalms', 'hebrews']}, {'name': 'Belial', 'ref': '1QM, 1QS', 'detail': "Prince of Darkness, ruler of the Sons of Darkness. The DSS chief adversary — distinct from ha-satan in the OT. Paul's only use: 'What accord has Christ with Belial?' (2 Cor 6:15).", 'connections': ['2corinthians']}, {'name': 'The Teacher of Righteousness', 'ref': 'CD, 1QpHab', 'detail': "Unnamed founder of the community. Opposed by the 'Wicked Priest.' His identity is the biggest unsolved mystery of Dead Sea Scrolls scholarship.", 'connections': []}],
        "patterns": ['Cosmic dualism: every scroll assumes a warfare binary — Sons of Light vs. Sons of Darkness, Angel of Truth vs. Angel of Darkness, Michael vs. Belial. No neutrality exists', 'Pesher interpretation: the scrolls read OT prophets as speaking about THEIR community and THEIR time — every prophecy has a present application. The NT does the same thing', 'Calendar as theology: the 364-day solar calendar is not just practical but theological — the right calendar determines the right worship, which determines covenant faithfulness', "Textual preservation: the scrolls confirm both the stability of the biblical text (Isaiah scroll matches MT closely) and its variability (Deut 32:8 'sons of God' vs. MT 'sons of Israel')"],
        "mistranslations": [{'english': 'Dead Sea Scrolls', 'original': 'Various', 'issue': "The collective label obscures the diversity — these are hundreds of distinct texts from multiple authors spanning 200+ years, not a single 'book'"}, {'english': 'sons of Israel', 'original': 'bene elohim', 'issue': "The MT reading at Deut 32:8 is a scribal alteration — the DSS preserve the original 'sons of God' that the scribes changed to avoid divine council theology"}],
    },
]

BIBLE_ANALYSIS = {
    "filters": THEME_FILTERS,
    "sections": BOOK_SECTIONS,
    "books": BOOK_ENTRIES,
}
