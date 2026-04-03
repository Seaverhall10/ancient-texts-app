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
    },
    {
        "id": '2samuel',
        "section": 'historical-books',
        "title": '2samuel',
        "themes": 'KING COV SEED DC',
        "meta_text": '',
        "body_html": '''''',
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
    },
    {
        "id": '2kings',
        "section": 'historical-books',
        "title": '2kings',
        "themes": 'KING REBEL EXILE RIV',
        "meta_text": '',
        "body_html": '''''',
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
    },
    {
        "id": '2chronicles',
        "section": 'historical-books',
        "title": '2chronicles',
        "themes": 'KING PRIEST HOLY EXILE',
        "meta_text": '',
        "body_html": '''''',
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
    },
    {
        "id": 'nehemiah',
        "section": 'historical-books',
        "title": 'nehemiah',
        "themes": 'COV EXILE HOLY',
        "meta_text": '',
        "body_html": '''''',
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
    },
    {
        "id": 'obadiah',
        "section": 'minor-prophets-section',
        "title": 'Book 31: Obadiah',
        "themes": 'NATIONS',
        "era_count": 1,
        "meta_text": '1 era file &middot; 21 verses &middot; O-BREVITY',
        "body_html": '''<p>Esau-Jacob conflict cosmicized. Edom's betrayal during Jerusalem's fall judged. Climax: "The kingdom shall be YHWH's" (v. 21).</p>''',
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
    },
    {
        "id": '2thessalonians',
        "section": 'new-testament',
        "title": '2thessalonians',
        "themes": 'SPIRIT DC',
        "meta_text": '',
        "body_html": '''''',
    },
    {
        "id": '1timothy',
        "section": 'new-testament',
        "title": '1timothy',
        "themes": 'HOLY',
        "meta_text": '',
        "body_html": '''''',
    },
    {
        "id": '2timothy',
        "section": 'new-testament',
        "title": '2timothy',
        "themes": 'HOLY',
        "meta_text": '',
        "body_html": '''''',
    },
    {
        "id": 'titus',
        "section": 'new-testament',
        "title": 'titus',
        "themes": 'HOLY',
        "meta_text": '',
        "body_html": '''''',
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
    },
    {
        "id": '2john',
        "section": 'new-testament',
        "title": '2john',
        "themes": '',
        "meta_text": '',
        "body_html": '''''',
    },
    {
        "id": '3john',
        "section": 'new-testament',
        "title": '3john',
        "themes": '',
        "meta_text": '',
        "body_html": '''''',
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
    },
    {
        "id": 'enoch',
        "section": 'non-canonical',
        "title": '1 Enoch (Ethiopic Enoch)',
        "themes": 'DC REBEL SPIRIT',
        "era_count": 5,
        "meta_text": '5 era files &middot; Highly authoritative — Jude quotes as prophecy',
        "body_html": '''<p><strong>WATCHER REBELLION</strong> (chs. 6-16) — Names the 200 Watchers. Azazel teaches warfare. Offspring (Nephilim) become demons when killed (15:8-10): disembodied spirits = demons. This explains why demons seek bodies (Matt 12:43-45).</p><p><strong>SON OF MAN</strong> (Parables, chs. 37-71) — Pre-existent figure on the throne of glory who judges. Daniel 7:13 expanded.</p>''',
    },
    {
        "id": 'jubilees',
        "section": 'non-canonical',
        "title": 'Jubilees',
        "themes": 'COV DC',
        "era_count": 5,
        "meta_text": '5 era files &middot; Calendar theology',
        "body_html": '''<p>Retells Genesis-Exodus. Angel of the Presence mediates Torah (confirmed Acts 7:53, Gal 3:19). Mastema (chief demon) retains 1/10 of demons after the Flood. 364-day solar calendar divided Second Temple Judaism.</p>''',
    },
    {
        "id": 'jasher',
        "section": 'non-canonical',
        "title": 'Jasher (Sefer HaYashar)',
        "themes": 'SEED',
        "era_count": 6,
        "meta_text": '6 era files &middot; Referenced in Josh 10:13, 2 Sam 1:18',
        "body_html": '''<p>Expands patriarchal narratives. Abraham's childhood, Nimrod, tower of Babel details. NOT the original Book of Jashar (that text is lost).</p>''',
    },
    {
        "id": 'dss',
        "section": 'non-canonical',
        "title": 'Dead Sea Scrolls',
        "themes": 'DC SPIRIT',
        "era_count": 5,
        "meta_text": '5 era files &middot; ~250 BC - 68 AD',
        "body_html": '''<p><strong>4QDeut<sup>j</sup></strong> — Preserves "sons of God" at Deut 32:8. THE most important textual witness for this app.</p><p><strong>11Q13 (Melchizedek Scroll)</strong> — Melchizedek as divine figure executing judgment on fallen gods of Psalm 82. Connects Gen 14 &rarr; Ps 82 &rarr; Ps 110 &rarr; Hebrews 7.</p><p><strong>War Scroll (1QM)</strong> — Cosmic warfare: Sons of Light vs. Sons of Darkness. Divine council military theology.</p>''',
    },
]

BIBLE_ANALYSIS = {
    "filters": THEME_FILTERS,
    "sections": BOOK_SECTIONS,
    "books": BOOK_ENTRIES,
}
