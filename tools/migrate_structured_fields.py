"""
One-time migration: Add structured fields to Wisdom, Major Prophets, and Minor Prophets
entries in bible_analysis.py. Keeps body_html intact. Adds 7 new fields per entry.
"""
import re

FILE = "C:/Users/User/Desktop/ANCIENT_TEXTS Study App/data/bible_analysis.py"

# ── Structured data to inject ──────────────────────────────────────────────

FIELDS = {
    # ═══════════════ WISDOM & POETRY ═══════════════
    "job": {
        "key_claim": "Job 1-2 is the clearest divine council scene in the OT — ha-Satan operates as a prosecutorial member of the council, not an independent adversary, and YHWH's answer to suffering is not explanation but encounter with cosmic sovereignty.",
        "contested_words": [
            {"word": "ha-Satan", "hebrew": "הַשָּׂטָן", "issue": "The article (ha-) makes this a TITLE ('the adversary'), not a proper name. A divine council role, not yet the personal devil of later theology.", "severity": "CRITICAL"},
            {"word": "bene elohim", "hebrew": "בְּנֵי אֱלֹהִים", "issue": "Sons of God — divine council members presenting themselves before YHWH. Same phrase as Gen 6:2.", "severity": "CRITICAL"},
            {"word": "Leviathan", "hebrew": "לִוְיָתָן", "issue": "Chaos creature in 41:1-34 — literal monster or symbol of cosmic evil? Ugaritic Litanu parallels. YHWH alone controls it.", "severity": "CRITICAL"},
            {"word": "Behemoth", "hebrew": "בְּהֵמוֹת", "issue": "Plural of 'beast' used as singular (40:15-24). Primal chaos creature, not a hippo. Paired with Leviathan as cosmic forces.", "severity": "MAJOR"},
            {"word": "go'el", "hebrew": "גֹּאֵל", "issue": "'I know that my Redeemer (go'el) lives' (19:25) — kinsman-redeemer. Who is Job's go'el? God himself? A divine mediator?", "severity": "CRITICAL"},
        ],
        "hidden_connections": [
            {"target": "genesis", "why": "bene ha'elohim (Job 1:6, 2:1) is the same phrase as Gen 6:2 — divine council members in both passages"},
            {"target": "1enoch", "why": "The Watcher framework explains the council hierarchy Job depicts — beings with access to the throne room and delegated authority"},
            {"target": "psalms", "why": "Ps 82 depicts the same divine council Job sees; Ps 104:26 references Leviathan as God's plaything"},
            {"target": "isaiah", "why": "Isaiah 6 throne room scene parallels Job 1-2 — both show the divine council in session with YHWH presiding"},
            {"target": "revelation", "why": "Satan as accuser (Rev 12:10) fulfills the ha-Satan prosecutorial role established in Job; the throne room scenes echo Job 1-2"},
            {"target": "romans", "why": "Rom 8:28 ('all things work together for good') is the theological answer to Job's unanswered question"},
        ],
        "what_it_doesnt_say": [
            "Why God accepted the wager — YHWH never explains why he permits ha-Satan's challenge",
            "What happened to Job's first children — they are never mourned or mentioned again after the restoration",
            "Elihu's origin — he appears without introduction (ch. 32) and God neither commends nor condemns him",
            "Whether Leviathan and Behemoth are literal or symbolic — God describes them in detail but never classifies them",
            "Why the friends are condemned for saying God punishes sin — which is technically true, just misapplied",
        ],
        "unusual_characters": [
            {"name": "ha-Satan", "ref": "1:6", "detail": "Divine council member with prosecutorial role. Challenges Job's loyalty within YHWH's permission boundaries. A title, not yet a proper name.", "connections": ["zechariah", "1chronicles", "revelation"]},
            {"name": "Elihu", "ref": "32:2", "detail": "Appears from nowhere after the three friends fail. God neither endorses nor rebukes him. The most enigmatic figure in wisdom literature.", "connections": []},
            {"name": "Leviathan", "ref": "41:1", "detail": "Chaos creature only YHWH can control. Fire-breathing, armored, untamable. Cosmic evil personified.", "connections": ["psalms", "isaiah", "revelation"]},
        ],
        "patterns": [
            "Chiastic structure: prose prologue (1-2) -> dialogue cycles (3-31) -> Elihu (32-37) -> God speaks (38-41) -> prose epilogue (42)",
            "Three cycles of dialogue deteriorate: friends become harsher, arguments more circular, third cycle breaks down (Bildad's speech is only 6 verses, Zophar disappears)",
            "God's answer (38-41) asks 70+ unanswered questions — the divine response to human questioning is MORE questions, revealing the asymmetry between Creator and creature",
            "Double restoration (42:10) — Job receives twice what he lost, EXCEPT children (same number) because the first children still exist in Sheol",
        ],
        "mistranslations": [
            {"english": "Satan", "original": "ha-Satan", "issue": "Dropping the article turns a divine council title ('the adversary/accuser') into a proper name, importing later theology"},
            {"english": "monster/hippo/crocodile", "original": "Behemoth/Leviathan", "issue": "Naturalizing cosmic chaos creatures into ordinary animals strips the divine council cosmology from God's speech"},
            {"english": "Redeemer", "original": "go'el", "issue": "English loses the kinsman-redeemer legal framework — go'el is a specific role with obligations, not a generic title"},
        ],
    },

    "psalms": {
        "key_claim": "Psalm 82 is the Rosetta Stone of the divine council — YHWH stands in the assembly of El, judges the corrupt elohim assigned to nations under Deut 32:8, and sentences them to die like men, while Psalm 110 establishes the Melchizedekian priesthood that bypasses the entire Levitical system.",
        "contested_words": [
            {"word": "elohim", "hebrew": "אֱלֹהִים", "issue": "Ps 82:1, 6 — 'God stands in the assembly of God; among the gods he judges.' Same word for YHWH and the council members. Most translations obscure this.", "severity": "CRITICAL"},
            {"word": "adat-el", "hebrew": "עֲדַת אֵל", "issue": "'Assembly of God/El' (82:1) — the divine council itself. Not a metaphor for human judges but the actual heavenly assembly.", "severity": "CRITICAL"},
            {"word": "bene elyon", "hebrew": "בְּנֵי עֶלְיוֹן", "issue": "'Sons of the Most High' (82:6) — the allotted elohim of Deut 32:8. Jesus quotes this in John 10:34.", "severity": "CRITICAL"},
            {"word": "Adoni", "hebrew": "אֲדֹנִי", "issue": "'My Lord' (110:1) — YHWH speaks to David's Lord. Two distinct divine figures in one verse. Messianic crux.", "severity": "CRITICAL"},
            {"word": "ka'ari", "hebrew": "כָּאֲרִי", "issue": "'Like a lion' vs. 'they pierced' (22:16) — MT reads ka'ari ('like a lion'), LXX/DSS support 'pierced' (ka'aru). Crucifixion detail.", "severity": "CRITICAL"},
            {"word": "hesed", "hebrew": "חֶסֶד", "issue": "Covenant faithfulness/loyal love — appears 127 times in Psalms. No single English word captures it.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "deuteronomy", "why": "Ps 82 is the judicial sequel to Deut 32:8 — the gods given nations are now condemned for their corruption"},
            {"target": "john", "why": "Jesus quotes Ps 82:6 in John 10:34 to defend his divine claim — 'Is it not written in your Law, I said you are gods?'"},
            {"target": "hebrews", "why": "Ps 110:4 (Melchizedek priesthood) is the foundation of Hebrews 5-7; Ps 2:7 quoted in Heb 1:5"},
            {"target": "genesis", "why": "Melchizedek first appears in Gen 14:18; Ps 110 picks up the thread and makes it eternal and messianic"},
            {"target": "daniel", "why": "The territorial princes of Dan 10 are the same corrupt elohim being judged in Ps 82"},
            {"target": "revelation", "why": "The throne room worship of Rev 4-5 echoes the Psalms' vision of cosmic praise; Ps 2 fulfilled in Rev 19"},
            {"target": "acts", "why": "Ps 2:7 applied to the resurrection (Acts 13:33); Ps 16:10 ('you will not let your holy one see corruption') quoted by Peter at Pentecost"},
            {"target": "ephesians", "why": "Ps 68:18 ('he ascended on high, leading captives') quoted in Eph 4:8 for Christ's ascension gifts"},
        ],
        "what_it_doesnt_say": [
            "Who the 'gods' of Psalm 82 are specifically — the text assumes the audience knows the Deut 32:8 framework",
            "How the elohim will 'die like men' — divine beings sentenced to mortality with no mechanism explained",
            "Why the Psalter is arranged in five books — the structure mirrors the Torah but no editorial note explains why",
            "The identity of many psalm authors — 50 psalms have no attributed author",
        ],
        "unusual_characters": [
            {"name": "Melchizedek", "ref": "110:4", "detail": "Eternal priest-king order that supersedes Levi. Only two OT mentions (Gen 14, Ps 110) but becomes central to NT Christology.", "connections": ["genesis", "hebrews"]},
            {"name": "The corrupt elohim", "ref": "82:1-7", "detail": "Divine council members judged for failing to protect the vulnerable. Sentenced to die like mortals.", "connections": ["deuteronomy", "daniel", "1enoch"]},
            {"name": "The suffering righteous one", "ref": "22:1", "detail": "Describes crucifixion details 800+ years before the practice existed. Jesus quotes the opening line from the cross.", "connections": ["matthew", "mark", "john"]},
        ],
        "patterns": [
            "Five-book structure mirrors the Torah: Book I (1-41), II (42-72), III (73-89), IV (90-106), V (107-150) — each ending with a doxology",
            "Royal psalms (2, 18, 20, 21, 45, 72, 89, 101, 110, 132, 144) trace the Davidic covenant from promise to apparent failure (Ps 89) to eschatological fulfillment",
            "Hallel collections: Egyptian Hallel (113-118, Passover), Great Hallel (120-136), Final Hallel (146-150) — the Psalter builds toward unending praise",
            "Lament-to-praise arc: most lament psalms turn to trust/praise before ending, modeling the faith journey from suffering to hope",
        ],
        "mistranslations": [
            {"english": "God/judges", "original": "elohim", "issue": "Ps 82 — translating elohim as 'judges' or 'rulers' hides the divine council entirely. These are divine beings, not humans."},
            {"english": "like a lion they pierced", "original": "ka'ari/ka'aru", "issue": "Ps 22:16 — MT reads 'like a lion' but DSS/LXX support 'pierced.' The difference between an animal metaphor and a crucifixion prophecy."},
            {"english": "my Lord", "original": "Adoni", "issue": "Ps 110:1 — English 'Lord' hides the two-Yahweh theology. YHWH speaks to David's Adoni, a second divine figure."},
        ],
    },

    "proverbs": {
        "key_claim": "Lady Wisdom in Proverbs 8:22-31 is a pre-creation figure present when YHWH laid the foundations of the earth — the NT identifies her with Christ (John 1:1-3, Col 1:15-17, 1 Cor 1:24), making this the OT's clearest portrait of the pre-incarnate Son.",
        "contested_words": [
            {"word": "qanani", "hebrew": "קָנָנִי", "issue": "'Possessed me' or 'created me' (8:22)? The Arian controversy hinged on this. If 'created,' Wisdom/Christ is a creature; if 'possessed,' eternally with God.", "severity": "CRITICAL"},
            {"word": "chokmah", "hebrew": "חָכְמָה", "issue": "Wisdom — feminine noun personified as a woman. Pre-creation figure who 'delights in the sons of men' (8:31). Christological implications.", "severity": "CRITICAL"},
            {"word": "eshet chayil", "hebrew": "אֵשֶׁת חַיִל", "issue": "'Woman of valor' (31:10) — chayil means military strength/wealth/capability. Not domestic virtue but warrior-strength. Many read her as incarnate Lady Wisdom.", "severity": "MAJOR"},
            {"word": "musar", "hebrew": "מוּסָר", "issue": "'Discipline/instruction' (1:2) — includes correction, training, chastening. Not punishment but formation. Shapes the book's entire pedagogy.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "john", "why": "John 1:1-3 (Logos at creation) echoes Prov 8:22-31 (Wisdom at creation) — the same pre-creation figure in both"},
            {"target": "colossians", "why": "Col 1:15-17 ('by him all things were created') maps directly onto Wisdom's role in Prov 8:27-30"},
            {"target": "1corinthians", "why": "'Christ the power of God and the WISDOM of God' (1 Cor 1:24) — Paul explicitly identifies Christ with chokmah"},
            {"target": "deuteronomy", "why": "The Two Ways (Lady Wisdom vs. Woman Folly) echoes Deut 30:15-19 ('I set before you life and death — choose life')"},
            {"target": "ecclesiastes", "why": "Ecclesiastes tests Proverbs' wisdom framework 'under the sun' and finds it insufficient without the fear of God"},
            {"target": "james", "why": "James 3:17 describes wisdom 'from above' — picking up Proverbs' Lady Wisdom as heavenly origin"},
        ],
        "what_it_doesnt_say": [
            "Whether Lady Wisdom is a person, a hypostasis, or a literary device — the text personifies but never explains the ontology",
            "How the 'Two Ways' relate to the tree of life and tree of knowledge — the Eden parallel is never made explicit",
            "Who collected and arranged the proverbs — editorial hands are acknowledged (25:1 'men of Hezekiah') but the process is obscure",
            "Why Agur (ch. 30) and Lemuel's mother (ch. 31) are included — non-Solomonic material with no explanation",
        ],
        "unusual_characters": [
            {"name": "Lady Wisdom", "ref": "8:1", "detail": "Pre-creation figure present when YHWH founded the earth. 'Rejoicing before him always, delighting in the sons of men.' NT identifies her with Christ.", "connections": ["john", "colossians", "1corinthians"]},
            {"name": "Woman Folly", "ref": "9:13", "detail": "Anti-Wisdom. Loud, seductive, leading to Sheol. The counterfeit that mimics Wisdom's invitation.", "connections": ["revelation"]},
            {"name": "Eshet Chayil", "ref": "31:10", "detail": "Woman of valor — 22-verse acrostic. Strength, business acumen, wisdom. Many scholars read her as Lady Wisdom incarnate in daily life.", "connections": ["ruth"]},
            {"name": "Agur son of Jakeh", "ref": "30:1", "detail": "Non-Israelite sage. Asks: 'Who has ascended to heaven and come down?' (30:4) — echoed in John 3:13.", "connections": ["john"]},
        ],
        "patterns": [
            "Acrostic structure: Eshet Chayil (31:10-31) uses all 22 Hebrew letters — the alphabet of wisdom completing the book",
            "Two invitations: Lady Wisdom (9:1-6) and Woman Folly (9:13-18) both say 'Come eat my food' — identical form, opposite destinations (life vs. Sheol)",
            "Numerical sayings (30:15-31): 'Three things... four things...' — a counting pattern unique in biblical literature",
            "Solomon-to-Solomon frame: begins with Solomon's proverbs (1:1), ends with a non-Solomonic woman who embodies everything Solomon taught but failed to live",
        ],
        "mistranslations": [
            {"english": "created me", "original": "qanani", "issue": "Prov 8:22 — 'created' imports Arian theology. Hebrew qanah more commonly means 'possessed/acquired,' preserving Wisdom's eternal nature."},
            {"english": "virtuous woman", "original": "eshet chayil", "issue": "Domesticates a word (chayil) that means military valor, wealth, and capability — reducing a warrior-sage to a housewife."},
            {"english": "fear", "original": "yir'ah", "issue": "'Fear of the LORD' — English implies terror. Hebrew yir'ah includes awe, reverence, and covenant loyalty. It is relational, not cowering."},
        ],
    },

    "ecclesiastes": {
        "key_claim": "Hebel does not mean 'vanity' but 'vapor/breath' — Ecclesiastes is not nihilism but an honest investigation of life 'under the sun' (the earthly plane) that concludes the only stable reality is the fear of God, pointing beyond human wisdom to divine encounter.",
        "contested_words": [
            {"word": "hebel", "hebrew": "הֶבֶל", "issue": "'Vanity' is wrong — hebel literally means breath/vapor. Transient, fleeting, incomprehensible. 38 occurrences. Same word as Abel's name.", "severity": "CRITICAL"},
            {"word": "tachath hashamesh", "hebrew": "תַּחַת הַשָּׁמֶשׁ", "issue": "'Under the sun' (29 times) — frames the entire investigation as earthly, ground-level observation. The divine council operates ABOVE the sun.", "severity": "CRITICAL"},
            {"word": "Qoheleth", "hebrew": "קֹהֶלֶת", "issue": "'Preacher' or 'Assembler' — from qahal (assembly). One who gathers and addresses the assembly. Not a name but a title.", "severity": "MAJOR"},
            {"word": "yitron", "hebrew": "יִתְרוֹן", "issue": "'Profit/gain' (1:3) — commercial term. 'What yitron does a person have for all their toil under the sun?' The question is economic.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "romans", "why": "Rom 8:20 ('creation subjected to futility/mataiotes') is the Greek equivalent of hebel — Paul reads the cosmos through Ecclesiastes' lens"},
            {"target": "proverbs", "why": "Ecclesiastes stress-tests Proverbs' wisdom framework and finds it insufficient without the 'fear of God' conclusion"},
            {"target": "genesis", "why": "hebel = Abel's name (Gen 4:2). The first human death is named 'vapor' — Ecclesiastes' theme embedded in Genesis from the start"},
            {"target": "job", "why": "Both wrestle with the same question: does righteous living guarantee good outcomes? Both answer no — but from different angles"},
            {"target": "james", "why": "James 4:14 ('What is your life? A mist/vapor') echoes Ecclesiastes' hebel theology directly"},
        ],
        "what_it_doesnt_say": [
            "Who Qoheleth actually is — the text implies Solomon but never names him after 1:1",
            "Whether the 'under the sun' limitation is deliberate literary framing or genuine philosophical boundary",
            "Why this book is canonical — the rabbis debated whether to exclude it; no explanation for its inclusion is given",
            "What happens after death — 3:21 asks 'who knows?' and 12:7 says the spirit returns to God, but no details",
        ],
        "unusual_characters": [
            {"name": "Qoheleth", "ref": "1:1", "detail": "The Assembler — implied to be Solomon but never named after the superscription. Speaks from experience of having 'everything' and finding it hebel.", "connections": ["1kings"]},
        ],
        "patterns": [
            "Hebel refrain: 38 occurrences of hebel create a drumbeat of transience that structures the entire book",
            "'Under the sun' frame (29 times): every observation is explicitly bounded to the earthly plane, implying there IS something above the sun",
            "Enjoy-life refrains (2:24, 3:12-13, 3:22, 5:18-20, 8:15, 9:7-10): punctuate the investigation with permission to receive life as God's gift",
            "Envelope structure: 1:2 ('hebel of hebels') and 12:8 ('hebel of hebels') frame the entire investigation, with the editorial verdict (12:13-14) standing outside",
        ],
        "mistranslations": [
            {"english": "vanity", "original": "hebel", "issue": "KJV's 'vanity' imports moral emptiness. Hebrew hebel means vapor/breath — something real but transient and ungraspable. Not worthless, but fleeting."},
            {"english": "meaningless", "original": "hebel", "issue": "NIV's 'meaningless' is worse than 'vanity' — implies nihilism that the text explicitly rejects in 12:13"},
            {"english": "Preacher", "original": "Qoheleth", "issue": "Neither preacher nor teacher — Qoheleth means 'one who assembles/gathers,' from the root qahal (assembly). A convener, not a sermonizer."},
        ],
    },

    "song": {
        "key_claim": "Song of Solomon 8:6 contains the only possible divine name in the book — shalhevet-yah ('flame of YAH') — revealing that the source of love's invincible power is God himself, and the garden imagery throughout restores what was lost in Eden's fall.",
        "contested_words": [
            {"word": "shalhevet-yah", "hebrew": "שַׁלְהֶבֶתְיָה", "issue": "'Flame of YAH' (8:6) — is -yah a divine name suffix or just an intensifier ('mighty flame')? If divine, this is the book's only God-reference.", "severity": "CRITICAL"},
            {"word": "dodim", "hebrew": "דֹּדִים", "issue": "'Lovemaking/caresses' — explicit erotic language throughout. The same root (dod) as David's name. Love as both physical and covenantal.", "severity": "MAJOR"},
            {"word": "Shulammite", "hebrew": "שׁוּלַמִּית", "issue": "'The Shulammite' (6:13) — feminine of Solomon (Shelomoh)? From Shunem? The female counterpart to the king.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "genesis", "why": "Garden imagery (4:12-5:1) restores Eden — lovers in the garden, nakedness without shame, what Gen 3 destroyed"},
            {"target": "ephesians", "why": "Eph 5:25-32 reads marriage as Christ/church allegory — Song of Solomon provides the OT foundation"},
            {"target": "revelation", "why": "The marriage supper of the Lamb (Rev 19:7-9) is the eschatological fulfillment of the love Song celebrates"},
            {"target": "hosea", "why": "Both use marriage as covenant metaphor — Hosea shows the broken version, Song shows the ideal"},
            {"target": "psalms", "why": "Ps 45 is a royal wedding psalm with similar imagery — the king desires the bride's beauty"},
        ],
        "what_it_doesnt_say": [
            "God is never explicitly named — if shalhevet-yah is just an intensifier, there is zero divine reference in the entire book",
            "Whether the relationship is pre-marital or marital — the timeline is ambiguous and the boundaries unclear",
            "Why this book is canonical — no prophetic formula, no covenant language, no Torah",
            "Whether the allegory (YHWH-Israel / Christ-Church) was original intent or later interpretation",
        ],
        "unusual_characters": [
            {"name": "The Shulammite", "ref": "6:13", "detail": "Feminine counterpart to Solomon. Dark-skinned ('black and beautiful,' 1:5). The only woman in Scripture who pursues her beloved with equal agency.", "connections": ["ruth", "proverbs"]},
            {"name": "The Daughters of Jerusalem", "ref": "1:5", "detail": "Chorus figure — the audience within the poem. They witness and respond to the love story.", "connections": []},
        ],
        "patterns": [
            "Adjuration refrain: 'Do not stir up or awaken love until it pleases' (2:7, 3:5, 8:4) — love has its own timing and cannot be forced",
            "Seeking-and-finding: the beloved is lost and found repeatedly (3:1-4, 5:6-8) — love involves absence, longing, and reunion",
            "Garden-to-garden arc: the enclosed garden (4:12) opens to 'let my beloved come to his garden' (4:16) — from protection to invitation",
            "Military imagery for love: 'terrible as an army with banners' (6:4, 10) — love is not gentle but fierce, a force that conquers",
        ],
        "mistranslations": [
            {"english": "a mighty flame", "original": "shalhevet-yah", "issue": "Translating -yah as merely an intensifier rather than the divine name hides the only possible God-reference in the book."},
            {"english": "dark", "original": "shechorah", "issue": "'I am black/dark and beautiful' (1:5) — many translations add 'but' (dark BUT beautiful), importing a contrast the Hebrew does not make."},
        ],
    },

    # ═══════════════ MAJOR PROPHETS ═══════════════
    "isaiah": {
        "key_claim": "Isaiah contains both the most detailed messianic prophecy (the Suffering Servant of 52:13-53:12) and the divine council rebel backstory (Helel ben Shachar in 14:12-14) — the entire cosmic drama from Satan's fall to the Messiah's atoning death in one book.",
        "contested_words": [
            {"word": "almah", "hebrew": "עַלְמָה", "issue": "'Young woman' (7:14) vs. LXX parthenos ('virgin'). Matthew 1:23 follows the LXX. The virgin birth hinges on this word.", "severity": "CRITICAL"},
            {"word": "Helel ben Shachar", "hebrew": "הֵילֵל בֶּן שָׁחַר", "issue": "'Day Star, son of Dawn' (14:12) — behind the king of Babylon: a divine council rebel. Combined with Ezek 28: the nachash/Satan backstory.", "severity": "CRITICAL"},
            {"word": "ebed YHWH", "hebrew": "עֶבֶד יהוה", "issue": "'Servant of YHWH' — four Servant Songs (42:1-9, 49:1-7, 50:4-9, 52:13-53:12). Individual messiah or collective Israel? Both?", "severity": "CRITICAL"},
            {"word": "mashiach", "hebrew": "מָשִׁיחַ", "issue": "Cyrus called YHWH's 'anointed' (mashiach, 45:1) — a PAGAN king given the messianic title. Shatters ethnic exclusivism.", "severity": "CRITICAL"},
            {"word": "seraphim", "hebrew": "שְׂרָפִים", "issue": "'Burning ones' (6:2) — divine council beings with six wings. From saraph (to burn). Same root as the nachash seraph serpents (Num 21:6).", "severity": "MAJOR"},
            {"word": "go'el", "hebrew": "גֹּאֵל", "issue": "YHWH as kinsman-redeemer of Israel (41:14, 43:14, 44:6). The go'el concept applied to God himself.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "ezekiel", "why": "Isa 14:12-14 (Helel) + Ezek 28:11-19 (Prince of Tyre) together reconstruct the full nachash/Satan origin story"},
            {"target": "matthew", "why": "Virgin birth (Matt 1:23/Isa 7:14), Galilee prophecy (Matt 4:15-16/Isa 9:1-2), Servant Songs throughout the passion narrative"},
            {"target": "mark", "why": "Mark 1:3 ('voice crying in the wilderness') directly quotes Isa 40:3 — the New Exodus begins with John the Baptist"},
            {"target": "acts", "why": "Ethiopian eunuch reads Isa 53 (Acts 8:32-35); Paul's commission echoes the Servant calling (Acts 13:47/Isa 49:6)"},
            {"target": "romans", "why": "Rom 10:16 quotes Isa 53:1; Rom 9:27-29 quotes the remnant theology of Isa 10:22-23"},
            {"target": "revelation", "why": "Isa 6 throne room -> Rev 4; new heavens and new earth (Isa 65:17) -> Rev 21:1; Babylon's fall (Isa 13-14) -> Rev 17-18"},
            {"target": "1peter", "why": "1 Pet 2:22-25 applies the Suffering Servant (Isa 53) directly to Christ's atoning work"},
        ],
        "what_it_doesnt_say": [
            "Whether chapters 40-66 are by the same author as 1-39 — the so-called 'Two Isaiahs' debate; the text presents a unified voice",
            "How the Suffering Servant can be both Israel (49:3) AND someone who restores Israel (49:5-6) — the paradox is never resolved within Isaiah",
            "What the seraphim look like beyond their wings — six wings but the face and body are never described",
            "How Cyrus would know YHWH's name — 45:4 says 'I name you, though you do not know me'",
        ],
        "unusual_characters": [
            {"name": "Helel ben Shachar", "ref": "14:12", "detail": "Day Star, son of Dawn — a divine being who fell from heaven after claiming 'I will make myself like the Most High.' Behind the king of Babylon: the nachash backstory.", "connections": ["ezekiel", "revelation", "luke"]},
            {"name": "The Suffering Servant", "ref": "52:13", "detail": "Pierced for transgressions, crushed for iniquities. Bore the sin of many. The most detailed messianic prophecy in the OT.", "connections": ["matthew", "mark", "acts", "1peter"]},
            {"name": "Cyrus", "ref": "45:1", "detail": "A pagan Persian king called YHWH's 'anointed' (mashiach) by name — 150 years before his birth.", "connections": ["ezra", "daniel", "2chronicles"]},
            {"name": "Seraphim", "ref": "6:2", "detail": "Burning ones with six wings — divine council beings who cry 'Holy, holy, holy.' Same root as the fiery serpents (nachash seraph) of Numbers 21.", "connections": ["numbers", "revelation"]},
        ],
        "patterns": [
            "Three-part structure mirrors the exile-return-restoration arc: judgment (1-39), comfort (40-55), future glory (56-66) — 66 chapters parallel the 66 books of the Bible",
            "Four Servant Songs (42:1-9, 49:1-7, 50:4-9, 52:13-53:12) trace a progressive revelation: calling -> mission -> suffering -> atoning death and vindication",
            "Remnant theology: the stump of Jesse (11:1), the holy seed in the stump (6:13), a remnant shall return (shear-jashub, 7:3 — Isaiah names his son this)",
            "New Exodus motif (chs. 40-55): 'In the wilderness prepare the way of YHWH' — return from Babylon as a second exodus that surpasses the first",
        ],
        "mistranslations": [
            {"english": "Lucifer", "original": "Helel ben Shachar", "issue": "Latin Vulgate's 'Lucifer' became a proper name for Satan. Hebrew means 'Shining One, son of Dawn' — a divine council title, not a personal name."},
            {"english": "virgin/young woman", "original": "almah", "issue": "Isa 7:14 — almah means 'young woman of marriageable age.' LXX chose parthenos (virgin). The translation choice carries enormous theological weight."},
            {"english": "the LORD", "original": "YHWH", "issue": "Isaiah uses YHWH over 400 times. English 'LORD' hides the personal name behind a title, especially critical in passages about YHWH's unique identity."},
        ],
    },

    "jeremiah": {
        "key_claim": "Jeremiah 31:31-34 announces the new covenant — Torah written on hearts instead of stone — which Hebrews 8:8-12 quotes in full as the longest OT citation in the NT, establishing that the old covenant was always designed to be replaced by internal transformation.",
        "contested_words": [
            {"word": "berit chadashah", "hebrew": "בְּרִית חֲדָשָׁה", "issue": "'New covenant' (31:31) — the ONLY place in the OT that uses this exact phrase. Foundation of NT covenant theology.", "severity": "CRITICAL"},
            {"word": "sod", "hebrew": "סוֹד", "issue": "'Council' (23:18, 22) — 'Who has stood in the sod of YHWH?' The divine council's deliberation room. False prophets lack sod access.", "severity": "CRITICAL"},
            {"word": "shub", "hebrew": "שׁוּב", "issue": "'Return/repent' — Jeremiah's key verb. 111 occurrences. Both physical return from exile and spiritual turning. The book's central imperative.", "severity": "MAJOR"},
            {"word": "riv", "hebrew": "רִיב", "issue": "Covenant lawsuit — Jeremiah as covenant prosecutor bringing YHWH's case against a faithless nation.", "severity": "MAJOR"},
            {"word": "topheth", "hebrew": "תֹּפֶת", "issue": "'Topheth' (7:31-32) — the Valley of Hinnom where children were burned for Molech. Becomes ge-hinnom = Gehenna.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "hebrews", "why": "Heb 8:8-12 quotes Jer 31:31-34 in full — the longest OT quotation in the NT. The new covenant supersedes the old."},
            {"target": "deuteronomy", "why": "Jer 31:33 ('write it on their hearts') fulfills the Deut 30:6 promise of heart circumcision — what Moses foresaw, Jeremiah names"},
            {"target": "ezekiel", "why": "Ezek 36:26-27 ('new heart, new spirit') parallels Jer 31:31-34 — both prophets independently announce the same internal transformation"},
            {"target": "luke", "why": "Jesus at the Last Supper: 'This cup is the new covenant in my blood' (Luke 22:20) — directly invoking Jer 31:31"},
            {"target": "lamentations", "why": "Lamentations is the aftermath of what Jeremiah prophesied — the covenant curses of Deut 28 realized in real time"},
            {"target": "daniel", "why": "Daniel reads Jeremiah's 70-year prophecy (Dan 9:2, cf. Jer 25:11-12) and receives the 70-weeks revelation in response"},
        ],
        "what_it_doesnt_say": [
            "How the new covenant differs mechanically from the old — 'write it on their hearts' is metaphorical with no procedural explanation",
            "Why God chose Jeremiah before birth (1:5) — pre-natal calling with no rationale given",
            "Who the 'Righteous Branch' (23:5-6) is — messianic title with no identification in the text",
            "Why Jeremiah was forbidden to marry (16:2) — the command is given but the symbolic logic is only implied",
        ],
        "unusual_characters": [
            {"name": "Baruch", "ref": "36:4", "detail": "Jeremiah's scribe who wrote the scroll that the king burned. Preserved the prophet's words against royal destruction.", "connections": []},
            {"name": "Ebed-melech", "ref": "38:7", "detail": "Ethiopian eunuch who rescues Jeremiah from the cistern. A foreigner saves the prophet when Israel won't.", "connections": ["acts"]},
            {"name": "Hananiah", "ref": "28:1", "detail": "False prophet who breaks Jeremiah's yoke and says exile will end in two years. Dies within the year as Jeremiah predicted.", "connections": []},
        ],
        "patterns": [
            "Confessions of Jeremiah (11:18-12:6, 15:10-21, 17:14-18, 18:18-23, 20:7-18): raw prophetic anguish unmatched in Scripture — 'You deceived me, YHWH'",
            "Scroll destruction and rewriting (ch. 36): the king burns the scroll, God commands a second with 'many similar words added' — the Word cannot be destroyed",
            "Covenant lawsuit (riv) structure: accusation (chs. 2-6), warning (7-20), judgment (21-29), hope (30-33), narrative of fall (34-45), oracles against nations (46-51)",
            "Potter and clay (18:1-12): God reshapes nations — sovereignty and conditionality held in tension",
        ],
        "mistranslations": [
            {"english": "the LORD", "original": "YHWH", "issue": "Jeremiah uses YHWH's personal name in intimate dialogue — 'LORD' flattens the covenant relationship into a generic title"},
            {"english": "repent", "original": "shub", "issue": "English 'repent' carries guilt/penance overtones. Hebrew shub means 'turn/return' — directional, not emotional. Come home."},
            {"english": "hell", "original": "ge-hinnom/Topheth", "issue": "The Valley of Hinnom where children were burned (7:31-32) became 'Gehenna.' Understanding the literal horror is essential to Jesus' later use of the term."},
        ],
    },

    "lamentations": {
        "key_claim": "Lamentations is Deuteronomy 28 in real time — the covenant curses playing out in Jerusalem's destruction — yet at the mathematical center of the triple acrostic (3:22-23) stands the declaration that YHWH's hesed never ceases, making faithfulness the structural heart of devastation.",
        "contested_words": [
            {"word": "hesed", "hebrew": "חֶסֶד", "issue": "'Steadfast love' (3:22) — at the center of the book's center. Covenant faithfulness persists even when the covenant has been broken.", "severity": "CRITICAL"},
            {"word": "emunah", "hebrew": "אֱמוּנָה", "issue": "'Faithfulness' (3:23) — 'Great is your emunah.' God's reliability even amid his own judgment.", "severity": "MAJOR"},
            {"word": "eikhah", "hebrew": "אֵיכָה", "issue": "'How!' (1:1) — the opening cry. Same word God uses in Eden: 'Where are you?' (Gen 3:9, ayyekah). Exile echoes the first exile.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "deuteronomy", "why": "Every curse in Lamentations corresponds to Deut 28 covenant curses — siege, famine, cannibalism, exile. The treaty has been enforced."},
            {"target": "jeremiah", "why": "Lamentations is the aftermath of everything Jeremiah warned about — traditionally attributed to Jeremiah himself"},
            {"target": "genesis", "why": "Eikhah (1:1) echoes ayyekah (Gen 3:9) — Jerusalem's exile mirrors Adam's exile from Eden. Same root word, same devastation."},
            {"target": "psalms", "why": "The lament genre in Psalms (22, 44, 74, 79, 137) provides the liturgical framework Lamentations extends into an entire book"},
            {"target": "revelation", "why": "The fall of Babylon in Rev 18 uses language and structure echoing Lamentations — cosmic city destruction"},
        ],
        "what_it_doesnt_say": [
            "Who wrote it — traditionally Jeremiah, but the text is anonymous",
            "Whether restoration will come — the book ends with 'unless you have utterly rejected us' (5:22), leaving the question open",
            "How long the suffering will last — no timeline, no promise of return within the text itself",
        ],
        "unusual_characters": [
            {"name": "Daughter Zion", "ref": "1:6", "detail": "Jerusalem personified as a weeping woman — stripped, shamed, abandoned by her lovers (the false allies/gods she trusted).", "connections": ["hosea", "ezekiel"]},
        ],
        "patterns": [
            "Acrostic architecture: chapters 1, 2, 4 are 22-verse acrostics (Hebrew alphabet); chapter 3 is a TRIPLE acrostic (66 verses, 3 per letter); chapter 5 has 22 verses but breaks the acrostic — order dissolving",
            "hesed at the center: 3:22-23 sits at the mathematical midpoint of the central triple acrostic — faithfulness is structurally embedded at the heart of devastation",
            "YHWH as enemy: 2:4-5 describes God as Israel's adversary — the most shocking theological reversal in the OT. The protector became the destroyer.",
            "Descending hope: each chapter is more despairing until the acrostic itself breaks in ch. 5 — literary form mirrors theological collapse",
        ],
        "mistranslations": [
            {"english": "steadfast love", "original": "hesed", "issue": "No single English word captures hesed — covenant loyalty, faithful love, mercy, kindness all rolled into one. Every translation loses something."},
            {"english": "How!", "original": "eikhah", "issue": "A mere exclamation in English. In Hebrew it echoes ayyekah (Gen 3:9, 'where are you?') — linking Jerusalem's fall to Eden's fall."},
        ],
    },

    "ezekiel": {
        "key_claim": "Ezekiel contains the most elaborate divine council throne scene in Scripture (the Merkabah, ch. 1/10), the nachash origin story (28:11-19), and the glory departure-and-return motif that structures Israel's entire exile-restoration theology — YHWH's throne is MOBILE, not imprisoned in the Temple.",
        "contested_words": [
            {"word": "Merkabah", "hebrew": "מֶרְכָּבָה", "issue": "Throne chariot (ch. 1, 10) — wheels within wheels, four living creatures, sapphire throne. Foundation of Jewish mysticism. YHWH's throne is mobile.", "severity": "CRITICAL"},
            {"word": "kavod", "hebrew": "כָּבוֹד", "issue": "'Glory' — the visible manifestation of YHWH's presence. Departs the Temple in stages (10-11), returns from the east (43:1-5). The weight of God.", "severity": "CRITICAL"},
            {"word": "kerub", "hebrew": "כְּרוּב", "issue": "'Cherub/cherubim' (28:14) — anointed guardian cherub in Eden. NOT the chubby babies of Renaissance art. Throne guardians with terrifying form.", "severity": "CRITICAL"},
            {"word": "ophannim", "hebrew": "אוֹפַנִּים", "issue": "'Wheels' (1:15-21) — wheels within wheels, full of eyes. A class of divine council beings, not mere mechanical objects.", "severity": "MAJOR"},
            {"word": "chayyot", "hebrew": "חַיּוֹת", "issue": "'Living creatures' (1:5) — four faces (human, lion, ox, eagle), four wings. Identified as cherubim in ch. 10. Throne bearers.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "isaiah", "why": "Isa 14:12-14 (Helel/Satan) + Ezek 28:11-19 (guardian cherub in Eden) together reconstruct the full first rebellion narrative"},
            {"target": "genesis", "why": "Ezek 28:13-15 places the guardian cherub IN Eden — filling the gap Genesis 3 leaves about who the nachash was before the fall"},
            {"target": "revelation", "why": "The four living creatures of Rev 4:6-8 directly parallel Ezekiel's chayyot; Gog and Magog (Ezek 38-39) reappear in Rev 20:8"},
            {"target": "daniel", "why": "Daniel's throne scene (Dan 7:9-14) shares the same divine council throne room Ezekiel describes — thrones, fire, the Ancient of Days"},
            {"target": "matthew", "why": "Jesus enters Jerusalem from the east (Matt 21:1) — the same direction from which Ezekiel's kavod returns to the Temple (43:1-4)"},
            {"target": "john", "why": "John 12:41 says Isaiah saw Jesus' glory — Ezekiel's kavod theology provides the framework for the incarnation of divine glory"},
        ],
        "what_it_doesnt_say": [
            "What the cherub did wrong in Eden (28:15) — 'unrighteousness was found in you' with no specifics given",
            "Whether the new Temple vision (chs. 40-48) is literal, symbolic, or eschatological — the most debated section of Ezekiel",
            "How dry bones can live (37:3) — Ezekiel's answer is 'O Lord GOD, you know,' refusing to speculate on resurrection mechanics",
            "Why the glory departed in stages rather than all at once — the lingering departure suggests reluctance but the text never says so",
        ],
        "unusual_characters": [
            {"name": "The guardian cherub", "ref": "28:14", "detail": "Anointed cherub in Eden, adorned with precious stones, blameless until unrighteousness was found. The nachash/Satan before the fall.", "connections": ["genesis", "isaiah", "revelation"]},
            {"name": "The chayyot", "ref": "1:5", "detail": "Four living creatures with four faces each — human, lion, ox, eagle. Throne bearers identified as cherubim in ch. 10.", "connections": ["revelation", "isaiah"]},
            {"name": "Gog of Magog", "ref": "38:2", "detail": "Eschatological enemy from the north. An anti-divine-council figure who attacks restored Israel. Reappears in Rev 20:8.", "connections": ["revelation"]},
            {"name": "The son of man (ben adam)", "ref": "2:1", "detail": "God's address to Ezekiel — 'son of man' (ben adam) used 93 times. Emphasizes human frailty before divine majesty.", "connections": ["daniel", "matthew"]},
        ],
        "patterns": [
            "Glory departure in stages: cherubim -> threshold -> east gate -> Mount of Olives -> gone (10:4, 10:18-19, 11:22-23). Glory returns by the same route in 43:1-5.",
            "Sign-acts: Ezekiel performs more enacted prophecies than any other prophet — lying on his side 430 days (4:4-8), eating a scroll (3:1-3), shaving his head (5:1-4)",
            "The three-part structure mirrors exile theology: judgment on Israel (1-24), judgment on nations (25-32), restoration (33-48)",
            "Shepherds and sheep (ch. 34): bad shepherds condemned, YHWH himself becomes shepherd, then appoints 'my servant David' — messianic promise through pastoral imagery",
        ],
        "mistranslations": [
            {"english": "cherub", "original": "kerub", "issue": "English domesticates a terrifying divine being into Renaissance baby art. Biblical cherubim are multi-faced throne guardians with lethal holiness."},
            {"english": "prince of Tyre", "original": "melek Tsor", "issue": "Ezek 28:12 says 'king' (melek) not 'prince' — the shift from nagid (28:2) to melek (28:12) signals the move from human ruler to divine being behind the throne."},
            {"english": "glory", "original": "kavod", "issue": "English 'glory' is vague and ethereal. Hebrew kavod means 'weight, heaviness, substance' — the tangible, dangerous presence of God."},
        ],
    },

    "daniel": {
        "key_claim": "Daniel 7:13-14 is the christological linchpin — the 'one like a son of man' rides the clouds (exclusively divine prerogative) and receives universal dominion from the Ancient of Days, and when Jesus claims THIS title at his trial (Mark 14:62), the high priest tears his robes because he understands the DIVINE claim.",
        "contested_words": [
            {"word": "bar enash", "hebrew": "בַּר אֱנָשׁ", "issue": "'Son of man' (7:13, Aramaic) — a divine figure riding clouds, not just a human title. Jesus' self-designation claims THIS figure.", "severity": "CRITICAL"},
            {"word": "Attiq Yomin", "hebrew": "עַתִּיק יוֹמִין", "issue": "'Ancient of Days' (7:9, Aramaic) — YHWH as eternal judge. White hair, throne of fire, books opened. Two distinct divine figures in one vision.", "severity": "CRITICAL"},
            {"word": "sar", "hebrew": "שַׂר", "issue": "'Prince' (10:13, 20) — territorial divine beings (Prince of Persia, Prince of Greece). Deut 32:8 allotment in action. Not human rulers but council members.", "severity": "CRITICAL"},
            {"word": "mashiach", "hebrew": "מָשִׁיחַ", "issue": "'Anointed one' (9:25-26) — 'cut off' (yikkaret). Most detailed messianic timeline in the OT. The 70-weeks prophecy.", "severity": "CRITICAL"},
            {"word": "qaddishin", "hebrew": "קַדִּישִׁין", "issue": "'Holy ones' (7:18, Aramaic) — the 'saints of the Most High' who receive the kingdom. Divine council members? God's people? Both?", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "mark", "why": "Mark 14:62 — Jesus combines Dan 7:13 + Ps 110:1 at his trial. The high priest tears his robes because he understands the divine cloud-rider claim."},
            {"target": "deuteronomy", "why": "The territorial princes of Dan 10 are the bene elohim of Deut 32:8 — the same allotted divine beings governing nations"},
            {"target": "revelation", "why": "Dan 7 throne room -> Rev 4-5; the four beasts of Dan 7 -> the beast of Rev 13; the Son of Man receives the kingdom in both"},
            {"target": "ezekiel", "why": "Dan 7:9-14 shares the divine council throne room with Ezek 1/10 — fire, thrones, the presence of God. Same cosmic courtroom."},
            {"target": "jeremiah", "why": "Daniel reads Jeremiah's 70-year prophecy (Dan 9:2, cf. Jer 25:11-12) and receives the 70-weeks revelation in response"},
            {"target": "matthew", "why": "'Son of Man' is Jesus' most common self-designation in Matthew — every use points back to Dan 7:13-14"},
        ],
        "what_it_doesnt_say": [
            "Whether the 70 weeks are literal or symbolic — the calculation has generated more interpretive schemes than almost any other prophecy",
            "How the 'prince of Persia' detained Gabriel for 21 days — a divine council conflict with no military details",
            "Who the fourth figure in the furnace is (3:25) — 'like a son of the gods' but never identified",
            "Whether Daniel knew the full implications of his visions — he says 'I was appalled and did not understand' (8:27)",
        ],
        "unusual_characters": [
            {"name": "The Son of Man", "ref": "7:13", "detail": "Cloud-rider who receives universal dominion from the Ancient of Days. Cloud-riding is exclusively divine prerogative. Jesus claims this title.", "connections": ["mark", "matthew", "revelation"]},
            {"name": "Michael", "ref": "10:13", "detail": "Israel's guardian prince (sar) who fights the territorial prince of Persia. The only named archangel in the Protestant canon.", "connections": ["jude", "revelation"]},
            {"name": "The Prince of Persia", "ref": "10:13", "detail": "Territorial divine being who resists Gabriel for 21 days. Deut 32:8 allotment in visible action — the invisible war behind geopolitics.", "connections": ["deuteronomy", "ephesians"]},
            {"name": "The fourth in the furnace", "ref": "3:25", "detail": "'Like a son of the gods' — divine council member present in the fire. Nebuchadnezzar sees what the three Hebrews trusted.", "connections": []},
        ],
        "patterns": [
            "Bilingual structure: chs. 2-7 in Aramaic (the imperial language), chs. 1, 8-12 in Hebrew (the covenant language) — the book itself embodies the tension between empire and faith",
            "Chiasm in chs. 2-7: dream of statue (2) / fiery furnace (3) / tree dream (4) || writing on wall (5) / lion's den (6) / four beasts vision (7)",
            "Four-kingdom progression (2:31-45, 7:1-27): Babylon -> Medo-Persia -> Greece -> Rome — empires rise and fall but the kingdom of God endures",
            "Prayer-and-revelation pattern: Daniel prays (2:17-18, 9:3-19), and heaven responds with visions — the divine council responds to covenant faithfulness",
        ],
        "mistranslations": [
            {"english": "Son of Man", "original": "bar enash", "issue": "English makes it sound humble ('mere human'). In Dan 7 context, this figure rides clouds (divine prerogative), receives worship, and rules forever — it is a divine title."},
            {"english": "saints", "original": "qaddishin", "issue": "'Saints of the Most High' may include divine council members, not just human believers. The Aramaic qaddishin is used for holy ones/angels elsewhere in Daniel."},
            {"english": "prince", "original": "sar", "issue": "English 'prince' implies human royalty. These are divine territorial beings — the same class as the bene elohim of Deut 32:8, ruling nations."},
        ],
    },

    # ═══════════════ MINOR PROPHETS ═══════════════
    "hosea": {
        "key_claim": "Hosea's marriage to unfaithful Gomer IS the prophetic message — YHWH as heartbroken husband, Israel as adulterous wife — making this the most sustained and emotionally raw covenant-love metaphor in the OT.",
        "contested_words": [
            {"word": "hesed", "hebrew": "חֶסֶד", "issue": "Covenant love/loyalty — the word YHWH demands Israel return to. 'I desire hesed, not sacrifice' (6:6, quoted by Jesus in Matt 9:13).", "severity": "CRITICAL"},
            {"word": "zanah", "hebrew": "זָנָה", "issue": "'Play the harlot/commit adultery' — spiritual unfaithfulness described in explicitly sexual terms. Covenant breaking = marital betrayal.", "severity": "CRITICAL"},
            {"word": "da'at Elohim", "hebrew": "דַּעַת אֱלֹהִים", "issue": "'Knowledge of God' (4:1, 6:6) — da'at is the same verb as sexual intimacy (Gen 4:1). Covenant knowledge is not intellectual but relational.", "severity": "MAJOR"},
            {"word": "shub", "hebrew": "שׁוּב", "issue": "'Return' — Hosea's central imperative. Both physical return from exile and spiritual turning back to YHWH.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "matthew", "why": "Matt 2:15 ('Out of Egypt I called my son') quotes Hos 11:1; Matt 9:13 quotes Hos 6:6 ('I desire mercy, not sacrifice')"},
            {"target": "romans", "why": "Rom 9:25-26 quotes Hos 2:23 and 1:10 — Lo-Ammi ('not my people') reversed for Gentile inclusion"},
            {"target": "jeremiah", "why": "Jeremiah extends Hosea's marriage metaphor — the unfaithful wife who will receive a new covenant (Jer 31:31-34)"},
            {"target": "song", "why": "Song of Solomon shows the ideal marriage; Hosea shows the broken version. Both use covenant-marriage theology."},
            {"target": "revelation", "why": "The Bride of Christ (Rev 19:7-9, 21:2) is the restored marriage Hosea's broken relationship points toward"},
        ],
        "what_it_doesnt_say": [
            "Whether Gomer was a prostitute before marriage or became one after — 'wife of whoredom' (1:2) is ambiguous",
            "How Hosea felt — the emotional toll of the commanded marriage is never described from his perspective",
            "Who Lo-Ammi and Lo-Ruhamah grew up to be — the children named as prophetic signs disappear from the narrative",
        ],
        "unusual_characters": [
            {"name": "Gomer", "ref": "1:3", "detail": "Hosea's unfaithful wife — the living parable of Israel's covenant betrayal. Bought back from slavery (3:2) as YHWH redeems Israel.", "connections": []},
            {"name": "Lo-Ammi", "ref": "1:9", "detail": "'Not my people' — prophetic child whose name declares covenant severance. Reversed in 2:23: 'I will say to Lo-Ammi, You are my people.'", "connections": ["romans", "1peter"]},
        ],
        "patterns": [
            "Marriage metaphor structures the entire book: marriage (ch. 1), divorce (ch. 2), redemption/remarriage (ch. 3), then the theological unpacking (chs. 4-14)",
            "Name reversals: Lo-Ruhamah ('not pitied') becomes Ruhamah ('pitied'); Lo-Ammi ('not my people') becomes Ammi ('my people') — judgment reversed",
            "Hos 11:8 ('My heart is overturned within me') — YHWH experiences internal conflict over judgment. The most emotionally vulnerable divine speech in the OT.",
        ],
        "mistranslations": [
            {"english": "mercy", "original": "hesed", "issue": "'I desire hesed, not sacrifice' (6:6) — 'mercy' is too thin. Hesed is covenant faithfulness, loyal love, steadfast commitment."},
            {"english": "know", "original": "da'at", "issue": "'Knowledge of God' reduces relational intimacy to intellectual content. Hebrew da'at is the word for sexual knowing (Gen 4:1)."},
        ],
    },

    "joel": {
        "key_claim": "Joel 2:28-32 democratizes the Spirit — previously reserved for prophets, kings, and select individuals, the Spirit will be poured on ALL flesh (sons, daughters, servants, slaves), which Peter declares fulfilled at Pentecost (Acts 2:16-21).",
        "contested_words": [
            {"word": "ruach", "hebrew": "רוּחַ", "issue": "'Spirit' — poured out on ALL flesh (2:28). Previously restricted to prophets and kings. Pentecost fulfillment democratizes divine council access.", "severity": "CRITICAL"},
            {"word": "yom YHWH", "hebrew": "יוֹם יהוה", "issue": "'Day of YHWH' (1:15, 2:1, 2:11, 2:31, 3:14) — five occurrences in three chapters. Both near (locust plague) and far (eschatological) fulfillment.", "severity": "CRITICAL"},
        ],
        "hidden_connections": [
            {"target": "acts", "why": "Peter quotes Joel 2:28-32 at Pentecost (Acts 2:16-21) — the Spirit outpouring IS Joel's prophecy fulfilled"},
            {"target": "deuteronomy", "why": "Joel reverses the Deut 32:8 allotment — Spirit on ALL flesh, not just Israel's prophets, reclaims the nations"},
            {"target": "numbers", "why": "Moses wished 'that all YHWH's people were prophets' (Num 11:29) — Joel says it will happen"},
            {"target": "revelation", "why": "The Day of YHWH imagery (sun dark, moon to blood) reappears in Rev 6:12-17"},
        ],
        "what_it_doesnt_say": [
            "When Joel was written — no king named, no specific historical event identified. The most undatable book in the OT.",
            "Whether the locust plague is literal, metaphorical for an army, or both — the imagery shifts between natural and military",
        ],
        "unusual_characters": [
            {"name": "The locusts", "ref": "1:4", "detail": "Four types of locusts in succession — devastation as divine judgment. Whether literal insects or metaphorical army is debated.", "connections": ["revelation"]},
        ],
        "patterns": [
            "Crisis-to-cosmic escalation: locust plague (local) -> Day of YHWH (cosmic). The near event opens a window to the ultimate event.",
            "Before/after structure: devastation (1:1-2:17) then restoration (2:18-3:21) — the pivot is YHWH's pity (2:18)",
        ],
        "mistranslations": [
            {"english": "afterward", "original": "acharei-khen", "issue": "'Afterward I will pour out my Spirit' (2:28) — English timeline word hides the Hebrew emphasis: AFTER the devastation, restoration. Sequence matters."},
        ],
    },

    "amos": {
        "key_claim": "Amos 3:7 is the foundational text for prophetic access — YHWH does NOTHING without first revealing his sod (council/secret) to his servants the prophets — making prophecy not prediction but divine council intelligence disclosed to human agents.",
        "contested_words": [
            {"word": "sod", "hebrew": "סוֹד", "issue": "'Secret/council' (3:7) — the divine council's deliberation. YHWH reveals his sod to prophets. Both the council itself and its decisions.", "severity": "CRITICAL"},
            {"word": "mishpat", "hebrew": "מִשְׁפָּט", "issue": "'Justice' (5:24) — 'Let justice roll down like waters.' Not abstract fairness but concrete covenant faithfulness enacted for the vulnerable.", "severity": "CRITICAL"},
            {"word": "yada", "hebrew": "יָדַע", "issue": "'Known' (3:2) — 'You only have I KNOWN of all the families of the earth.' Covenant intimacy, not mere awareness. Election = heightened accountability.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "acts", "why": "Acts 15:16-17 quotes Amos 9:11-12 — James uses it to justify Gentile inclusion without circumcision. The 'fallen booth of David' restored."},
            {"target": "deuteronomy", "why": "Amos' social justice demands are grounded in Deuteronomic covenant law — the poor, the widow, the alien"},
            {"target": "micah", "why": "Amos and Micah are contemporary prophets with overlapping social justice themes — Mic 6:8 distills what Amos 5:24 demands"},
            {"target": "revelation", "why": "Amos' Day of YHWH imagery feeds into Revelation's judgment sequences"},
        ],
        "what_it_doesnt_say": [
            "Why a shepherd from Tekoa was chosen over a professional prophet — Amos insists 'I am no prophet' (7:14) but never explains the divine logic",
            "How the 'fallen booth of David' (9:11) will be rebuilt — the messianic promise is given without mechanism",
        ],
        "unusual_characters": [
            {"name": "Amos", "ref": "1:1", "detail": "Shepherd and fig-tree dresser from Tekoa — not a professional prophet. 'I am no prophet, nor a prophet's son' (7:14). God drafts from outside the system.", "connections": []},
            {"name": "Amaziah", "ref": "7:10", "detail": "Priest of Bethel who opposes Amos and reports him to the king — institutional religion silencing prophetic truth.", "connections": []},
        ],
        "patterns": [
            "Oracles against nations (1:3-2:16): seven nations judged with 'for three transgressions and for four' formula, then the surprise — Israel is the eighth, judged harshest",
            "Five visions (7:1-9:10): locusts, fire, plumb line, summer fruit, temple destruction — escalating from averting judgment to its inevitability",
            "Election-accountability paradox: 'You only have I known... THEREFORE I will punish you' (3:2) — chosen status increases judgment, not immunity",
        ],
        "mistranslations": [
            {"english": "secret", "original": "sod", "issue": "Amos 3:7 — 'secret' hides the divine council meaning. sod is both the council assembly and its deliberations. Prophets attend the council."},
            {"english": "justice", "original": "mishpat", "issue": "English abstraction. Hebrew mishpat is concrete: the legal rights of the poor, the verdict for the oppressed, the covenant enacted in courts."},
        ],
    },

    "obadiah": {
        "key_claim": "Obadiah cosmicizes the Esau-Jacob conflict — Edom's betrayal during Jerusalem's fall is not merely political but the latest chapter in a rivalry that began in the womb (Gen 25:23), and the climax declares 'the kingdom shall be YHWH's' (v. 21).",
        "contested_words": [
            {"word": "malkhut", "hebrew": "מַלְכוּת", "issue": "'The kingdom shall be YHWH's' (v. 21) — the final word. Cosmic sovereignty declared through the lens of one small nation's betrayal.", "severity": "CRITICAL"},
        ],
        "hidden_connections": [
            {"target": "genesis", "why": "The Esau-Jacob rivalry begins in Gen 25:23 ('the older shall serve the younger') — Obadiah is the latest chapter of that cosmic conflict"},
            {"target": "jeremiah", "why": "Jer 49:7-22 contains parallel oracles against Edom — shared source material or prophetic tradition"},
            {"target": "malachi", "why": "Mal 1:2-5 ('Jacob I loved, Esau I hated') interprets the same Edom theology Obadiah pronounces judgment on"},
            {"target": "revelation", "why": "'The kingdom shall be YHWH's' (v. 21) anticipates 'The kingdom of the world has become the kingdom of our Lord' (Rev 11:15)"},
        ],
        "what_it_doesnt_say": [
            "When Obadiah prophesied — the shortest book in the OT with no dating formula",
            "Which specific betrayal is in view — multiple occasions when Edom betrayed Judah",
        ],
        "unusual_characters": [],
        "patterns": [
            "Shortest book in the OT (21 verses) — the entire Esau-Jacob conflict compressed into one oracle. Brevity as prophetic intensity.",
            "Reversal structure: Edom's height (v. 3-4) -> brought low (v. 5-9) -> reason: betrayal of brother (v. 10-14) -> YHWH's kingdom (v. 15-21)",
        ],
        "mistranslations": [
            {"english": "pride", "original": "zadon", "issue": "Edom's 'pride' (v. 3) — zadon is presumption, arrogant overreach. Not mere self-esteem but active defiance of divine order."},
        ],
    },

    "jonah": {
        "key_claim": "Jonah is furious that God shows mercy to Nineveh and quotes Exodus 34:6-7 AS A COMPLAINT — the only prophet who runs from his calling and succeeds in his mission but considers the success a disaster, exposing Israel's exclusivism against YHWH's universal compassion.",
        "contested_words": [
            {"word": "da'ag", "hebrew": "דָּאַג", "issue": "Fish/sea creature — 'great fish' (dag gadol, 1:17). Not a whale. The species is irrelevant; the divine sovereignty over creation is the point.", "severity": "MAJOR"},
            {"word": "nacham", "hebrew": "נָחַם", "issue": "'Relented' (3:10) — God 'repented/changed his mind' about the judgment. Same word as Ex 32:14. Does God change his mind?", "severity": "CRITICAL"},
            {"word": "ra'ah", "hebrew": "רָעָה", "issue": "'Evil/calamity/wickedness' — used for BOTH Nineveh's wickedness (1:2) and Jonah's displeasure (4:1). Same word, different moral valence.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "matthew", "why": "Matt 12:39-41 — three days in fish = three days in tomb. 'Something greater than Jonah is here.' Resurrection typology."},
            {"target": "exodus", "why": "Jonah 4:2 quotes Ex 34:6-7 (YHWH's self-revelation) as a COMPLAINT — he knows God's character and resents it"},
            {"target": "nahum", "why": "Nahum is the sequel — mercy was offered to Nineveh (Jonah), Nineveh returned to violence, now judgment comes (Nahum)"},
            {"target": "luke", "why": "Luke 11:29-32 parallels Matt 12 — Nineveh repented at Jonah's preaching; this generation will not repent at something greater"},
        ],
        "what_it_doesnt_say": [
            "Why Jonah ran — the text assumes the audience understands Israelite resentment toward Assyria (Nineveh's empire)",
            "What happened to Jonah after the book ends — the final question ('Should I not pity Nineveh?') is unanswered; the reader must answer",
            "How the entire city repented — from king to cattle (3:7-8), with no explanation of how the message spread so fast",
        ],
        "unusual_characters": [
            {"name": "The pagan sailors", "ref": "1:16", "detail": "Fear YHWH and offer sacrifices after the sea calms — pagans convert while the prophet runs. Reversal of expectations.", "connections": []},
            {"name": "The Ninevites", "ref": "3:5", "detail": "Repent at five Hebrew words from a reluctant prophet — the fastest mass conversion in Scripture. Even the cattle fast.", "connections": ["nahum", "matthew"]},
        ],
        "patterns": [
            "Reversal upon reversal: the prophet runs, pagans convert, the enemy repents, the prophet rages — every expectation is inverted",
            "The book ends with an unanswered question (4:11) — the reader is the jury. 'Should I not pity Nineveh?' demands a response.",
            "Three-day pattern: three days in the fish (1:17), three days walking Nineveh (3:3) — prefigures three days in the tomb (Matt 12:40)",
        ],
        "mistranslations": [
            {"english": "whale", "original": "dag gadol", "issue": "'Great fish' — not a whale. The species is irrelevant to the text's point about divine sovereignty over creation."},
            {"english": "repented/relented", "original": "nacham", "issue": "'God relented' (3:10) — does God change his mind? nacham encompasses grief, comfort, and change of course. The English binary (did he / didn't he change his mind) misses Hebrew nuance."},
        ],
    },

    "micah": {
        "key_claim": "Micah 5:2 declares the Messiah's origin is 'from of old, from days of eternity' (yemei olam) — a pre-existent ruler from Bethlehem, the smallest village, collapsing the distance between humility and cosmic antiquity in one verse.",
        "contested_words": [
            {"word": "yemei olam", "hebrew": "יְמֵי עוֹלָם", "issue": "'Days of eternity/antiquity' (5:2) — the Messiah's goings forth are from eternity. Pre-existence or ancient lineage?", "severity": "CRITICAL"},
            {"word": "mishpat", "hebrew": "מִשְׁפָּט", "issue": "'Justice' (6:8) — 'Do justice, love mercy, walk humbly.' The most concise prophetic ethics summary. Concrete covenant faithfulness.", "severity": "CRITICAL"},
            {"word": "riv", "hebrew": "רִיב", "issue": "Covenant lawsuit (6:1-2) — 'Hear, you mountains, YHWH's riv.' The mountains are witnesses, as in Deut 30:19.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "matthew", "why": "Matt 2:4-6 quotes Mic 5:2 — the chief priests identify Bethlehem as the Messiah's birthplace from this text"},
            {"target": "amos", "why": "Contemporary prophets with overlapping social justice themes — Mic 6:8 distills what Amos 5:24 demands"},
            {"target": "isaiah", "why": "Mic 4:1-3 parallels Isa 2:2-4 almost verbatim — 'swords into plowshares.' Shared prophetic tradition."},
            {"target": "deuteronomy", "why": "The riv (covenant lawsuit) of Mic 6 uses the Deuteronomic treaty framework — mountains as witnesses per Deut 30:19"},
        ],
        "what_it_doesnt_say": [
            "How the Messiah can be from both Bethlehem (tiny village) and eternity — the paradox is stated but not explained",
            "When 'swords into plowshares' (4:3) will happen — eschatological promise with no timeline",
        ],
        "unusual_characters": [
            {"name": "The ruler from Bethlehem", "ref": "5:2", "detail": "Pre-existent Messiah from the smallest, most insignificant village. Origin 'from of old, from days of eternity.'", "connections": ["matthew", "john"]},
        ],
        "patterns": [
            "Three cycles of judgment and hope: doom (1-2) / hope (2:12-13), doom (3) / hope (4-5), doom (6:1-7:7) / hope (7:8-20)",
            "Mic 6:8 as prophetic summary: 'Do justice (mishpat), love mercy (hesed), walk humbly (hatznea lekhet)' — the entire prophetic ethic in one verse",
            "Cosmic courtroom (6:1-2): mountains and hills as jury — the covenant lawsuit uses creation as witnesses, echoing Deut 30:19",
        ],
        "mistranslations": [
            {"english": "justice", "original": "mishpat", "issue": "Abstract English. Micah's mishpat means concrete covenant action — defend the poor, correct the powerful, enact Torah in the courts."},
            {"english": "from ancient times", "original": "yemei olam", "issue": "Weakens 'days of eternity' to mere antiquity. The Hebrew allows — and the NT confirms — genuine pre-existence."},
        ],
    },

    "nahum": {
        "key_claim": "Nahum is Jonah's sequel — mercy was offered to Nineveh and received, but Nineveh returned to violence, and now divine judgment falls with the certainty of a cosmic warrior's advance, confirmed by the Babylon Chronicle's record of Nineveh's fall in 612 BC.",
        "contested_words": [
            {"word": "noqem", "hebrew": "נֹקֵם", "issue": "'Avenging' (1:2) — YHWH as avenger, used three times in one verse. Not vindictiveness but covenant enforcement against oppression.", "severity": "MAJOR"},
            {"word": "Deber and Resheph", "hebrew": "דֶּבֶר / רֶשֶׁף", "issue": "'Pestilence and Plague' (Hab 3:5, applied to Nahum's theology) — personified divine agents, not mere diseases. Council executioners.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "jonah", "why": "Nahum completes the Jonah arc — mercy offered (Jonah), mercy squandered, judgment executed (Nahum). Together they teach: grace has a shelf life when rejected."},
            {"target": "revelation", "why": "Nahum's language of divine warrior judgment feeds into Revelation's portrayal of Christ's return (Rev 19:11-16)"},
            {"target": "exodus", "why": "Nah 1:3 quotes Ex 34:6-7 — the same divine self-revelation Jonah complained about. Nahum applies the 'will not leave guilty unpunished' clause."},
        ],
        "what_it_doesnt_say": [
            "Whether any Ninevites repented a second time — no opportunity is mentioned, only judgment",
            "How Nahum received his oracle — no call narrative, no divine council vision, just 'the oracle concerning Nineveh'",
        ],
        "unusual_characters": [],
        "patterns": [
            "Acrostic poem (1:2-8): partial alphabetic acrostic describing YHWH as divine warrior — form dissolves as chaos overtakes Nineveh",
            "Jonah-Nahum theological pair: mercy (Jonah) then judgment (Nahum) — together they form a complete picture of YHWH's character from Ex 34:6-7",
        ],
        "mistranslations": [
            {"english": "jealous/vengeful", "original": "qanno/noqem", "issue": "English makes YHWH sound petty. Hebrew qanno is zealous covenant passion; noqem is righteous enforcement against oppression, not personal revenge."},
        ],
    },

    "habakkuk": {
        "key_claim": "Habakkuk 2:4 — 'the righteous shall live by his emunah (faith/faithfulness)' — quoted three times in the NT (Rom 1:17, Gal 3:11, Heb 10:38) and the spark that ignited the Reformation, making this the only prophetic book structured as a dialogue with God where 'trust' is the answer to theodicy.",
        "contested_words": [
            {"word": "emunah", "hebrew": "אֱמוּנָה", "issue": "'Faith/faithfulness' (2:4) — is it human faith IN God or human faithFULNESS? The Hebrew holds both. Quoted 3x in NT. Ignited the Reformation.", "severity": "CRITICAL"},
            {"word": "chazon", "hebrew": "חָזוֹן", "issue": "'Vision' (2:2) — 'Write the vision; make it plain on tablets.' The divine council revelation committed to writing. Prophetic disclosure.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "romans", "why": "Rom 1:17 quotes Hab 2:4 — 'the righteous shall live by faith.' Paul makes it the thesis of Romans."},
            {"target": "galatians", "why": "Gal 3:11 quotes Hab 2:4 — justification by faith, not by works of the law"},
            {"target": "hebrews", "why": "Heb 10:38 quotes Hab 2:4 — perseverance through suffering grounded in faith"},
            {"target": "job", "why": "Both wrestle with theodicy — righteous suffering under divine sovereignty. Both receive 'trust' rather than explanation as the answer."},
        ],
        "what_it_doesnt_say": [
            "Why God would use a MORE wicked nation (Babylon) to punish a LESS wicked one (Judah) — Habakkuk asks but the mechanism is never explained",
            "When the 'vision' (2:2-3) will be fulfilled — 'it awaits its appointed time; it will not lie'",
        ],
        "unusual_characters": [
            {"name": "Habakkuk", "ref": "1:1", "detail": "The only prophet who argues with God and receives a direct answer. The book is structured as a lawsuit (riv) with YHWH as both defendant and judge.", "connections": []},
        ],
        "patterns": [
            "Dialogue structure: complaint (1:2-4) -> God's answer (1:5-11) -> second complaint (1:12-2:1) -> God's answer (2:2-20) -> psalm of trust (ch. 3)",
            "Five woes (2:6-20): against the Babylonian oppressor. Even the instrument of judgment will itself be judged.",
            "Theophany hymn (ch. 3): YHWH as divine warrior striding across creation — the most vivid theophany outside the Pentateuch",
        ],
        "mistranslations": [
            {"english": "faith", "original": "emunah", "issue": "English splits 'faith' and 'faithfulness' into two concepts. Hebrew emunah holds both — trust in God expressed through covenant loyalty. The Reformation read it as 'faith alone' but the Hebrew includes faithful living."},
        ],
    },

    "zephaniah": {
        "key_claim": "Zephaniah describes the most comprehensive Day of YHWH — a cosmic un-creation that reverses Genesis 1 itself — yet at the center places YHWH singing over the remnant with joy (3:17), the divine warrior who unmakes creation also SINGS over those he saves.",
        "contested_words": [
            {"word": "yom YHWH", "hebrew": "יוֹם יהוה", "issue": "'Day of YHWH' (1:7, 14) — Zephaniah's version is the most comprehensive: sweeps away humans, animals, birds, fish. Genesis 1 in reverse.", "severity": "CRITICAL"},
            {"word": "yagil", "hebrew": "יָגִיל", "issue": "'He will rejoice/exult' (3:17) — YHWH rejoicing over his people with singing. The divine warrior sings. Most tender divine image in the prophets.", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "genesis", "why": "Zeph 1:2-3 reverses the Genesis 1 creation order — fish, birds, animals, humans swept away. Un-creation as judgment."},
            {"target": "joel", "why": "Both focus on the Day of YHWH — Joel's locust plague and Zephaniah's cosmic sweep are parallel visions of the same event"},
            {"target": "revelation", "why": "The comprehensive destruction of Zeph 1 anticipates Revelation's bowl judgments — total cosmic upheaval"},
        ],
        "what_it_doesnt_say": [
            "How the remnant survives the un-creation — total destruction is described but a remnant emerges without explanation",
            "Why YHWH sings — 3:17 is stunning but no context is given for the divine warrior's joy in the middle of judgment",
        ],
        "unusual_characters": [],
        "patterns": [
            "Un-creation structure (1:2-3): sweeps away humans, animals, birds, fish — reverse order of Genesis 1 creation. YHWH undoes his own work.",
            "Judgment-to-joy pivot: the book moves from total cosmic destruction (ch. 1) to YHWH singing over the remnant (3:17) — the most dramatic emotional reversal in the Twelve",
        ],
        "mistranslations": [
            {"english": "quiet you", "original": "yacharish", "issue": "'He will quiet you by his love' (3:17) — some render 'be silent' (with awe). The divine warrior is speechless with love, then breaks into song. Translation choice shapes whether God is calming Israel or overwhelmed himself."},
        ],
    },

    "haggai": {
        "key_claim": "Haggai's prophecy that 'the latter glory of this house shall be greater than the former' (2:9) remained unfulfilled for 500 years — until Christ himself entered the Second Temple, making the promise christological rather than architectural.",
        "contested_words": [
            {"word": "kavod", "hebrew": "כָּבוֹד", "issue": "'Glory' (2:9) — 'The latter glory of this house shall be greater than the former.' No glory-cloud filled the Second Temple. Fulfilled only in Christ's presence.", "severity": "CRITICAL"},
        ],
        "hidden_connections": [
            {"target": "ezekiel", "why": "Ezekiel's kavod departed the First Temple (Ezek 10-11); Haggai promises greater glory for the Second — the return Ezekiel foresaw"},
            {"target": "malachi", "why": "Mal 3:1 ('the Lord whom you seek will suddenly come to his temple') fulfills Haggai's promise of greater glory"},
            {"target": "john", "why": "Jesus in the Temple (John 2:13-22) — the glory greater than Solomon's is the incarnate Son"},
            {"target": "ezra", "why": "Haggai is the historical context for Ezra 5-6 — the prophetic push behind the Temple rebuilding"},
        ],
        "what_it_doesnt_say": [
            "How the Second Temple's glory would exceed the First — no Shekinah cloud, no ark, no Urim and Thummim. The promise seemed impossible.",
            "Why the people prioritized their own houses over God's (1:4) — the motivation for neglect is assumed, not explained",
        ],
        "unusual_characters": [
            {"name": "Zerubbabel", "ref": "2:23", "detail": "Called YHWH's 'signet ring' — the Davidic heir through whom the messianic line continues after exile. Royal authority compressed into a seal.", "connections": ["matthew", "luke"]},
        ],
        "patterns": [
            "Four dated oracles (1:1, 2:1, 2:10, 2:20): precisely dated to the month and day — the most chronologically specific book in the prophets",
            "Priorities rebuked: 'Is it time for you to dwell in paneled houses while this house lies in ruins?' (1:4) — the Temple-first principle",
        ],
        "mistranslations": [
            {"english": "glory", "original": "kavod", "issue": "Haggai's kavod is not abstract splendor but the tangible divine presence — weight, substance, the Shekinah. The Second Temple lacked it until Christ entered."},
        ],
    },

    "zechariah": {
        "key_claim": "Zechariah is the most christologically dense minor prophet — with 40+ NT quotations saturating the passion narratives: triumphal entry on a donkey (9:9), thirty pieces of silver (11:12-13), 'they will look on ME whom they have PIERCED' (12:10), and 'strike the shepherd' (13:7).",
        "contested_words": [
            {"word": "daqaru", "hebrew": "דָּקָרוּ", "issue": "'Pierced' (12:10) — 'they will look on ME whom they have pierced.' YHWH is the speaker — YHWH himself is pierced? Quoted in John 19:37.", "severity": "CRITICAL"},
            {"word": "tselach", "hebrew": "צֶלַח", "issue": "'Branch' (tsemach, 3:8, 6:12) — messianic title. The Branch who builds the Temple and is BOTH priest AND king. Unique dual-office figure.", "severity": "CRITICAL"},
            {"word": "ha-Satan", "hebrew": "הַשָּׂטָן", "issue": "'The adversary' (3:1) — ha-Satan accusing Joshua the high priest in the divine council courtroom. Same titled role as in Job.", "severity": "CRITICAL"},
            {"word": "shalosh", "hebrew": "שְׁלֹשִׁים", "issue": "'Thirty pieces of silver' (11:12) — the 'lordly price' (ironic). Fulfilled in Judas's betrayal (Matt 27:9).", "severity": "MAJOR"},
        ],
        "hidden_connections": [
            {"target": "matthew", "why": "Matt 21:5 (triumphal entry/Zech 9:9), Matt 26:31 ('strike the shepherd'/Zech 13:7), Matt 27:9 (thirty pieces of silver/Zech 11:12-13)"},
            {"target": "john", "why": "John 19:37 quotes Zech 12:10 — 'they will look on him whom they have pierced.' Applied directly to the crucifixion."},
            {"target": "job", "why": "ha-Satan in Zech 3:1 plays the same prosecutorial role as in Job 1-2 — accusing the righteous before the divine council"},
            {"target": "revelation", "why": "Rev 1:7 quotes Zech 12:10 ('every eye will see him, even those who pierced him'); the rider on a white horse echoes Zechariah's messianic warrior"},
            {"target": "hebrews", "why": "The priest-king Branch (Zech 6:12-13) who serves on his throne connects to the Melchizedekian priesthood of Hebrews"},
        ],
        "what_it_doesnt_say": [
            "How YHWH can be both the speaker ('they will look on ME') and the one pierced — the divine identity of the pierced one is stated but not explained",
            "Who the 'worthless shepherd' (11:17) is — anti-messianic figure with no identification",
            "How the Branch can be both priest AND king — the offices were always separated; Zechariah merges them without explanation",
        ],
        "unusual_characters": [
            {"name": "Joshua the high priest", "ref": "3:1", "detail": "Accused by ha-Satan in the divine council courtroom. YHWH acquits him and gives him clean garments. The most explicit council courtroom scene in the Twelve.", "connections": ["job", "revelation"]},
            {"name": "The Branch (Tsemach)", "ref": "3:8", "detail": "Messianic figure who is both priest and king — builds the Temple and rules from his throne. Dual-office Messiah.", "connections": ["hebrews", "isaiah", "jeremiah"]},
            {"name": "The pierced one", "ref": "12:10", "detail": "YHWH says 'they will look on ME whom they have pierced' — the divine figure who is wounded. Applied to Christ in John 19:37.", "connections": ["john", "revelation"]},
        ],
        "patterns": [
            "Eight night visions (1:7-6:8): horsemen, horns, measuring line, Joshua accused, lampstand, flying scroll, woman in basket, chariots — a complete divine council intelligence briefing",
            "Passion saturation: Zech 9-14 provides more raw material for the gospel passion narratives than any other OT section outside Isaiah 53",
            "Two-part structure: visions and oracles (1-8, dated) + apocalyptic oracles (9-14, undated) — the book shifts from current restoration to eschatological fulfillment",
        ],
        "mistranslations": [
            {"english": "they will look on him", "original": "ve-hibitu elai", "issue": "Zech 12:10 — the Hebrew says 'on ME' (elai), not 'on him.' YHWH is the speaker AND the pierced one. Most English translations soften this to avoid the christological implication."},
            {"english": "Branch", "original": "tsemach", "issue": "Generic English. Hebrew tsemach is a loaded messianic title appearing in Isaiah, Jeremiah, and Zechariah — each adding layers to the same figure."},
        ],
    },

    "malachi": {
        "key_claim": "Malachi is the last prophetic word before 400 years of silence — its final word is 'curse' (cherem), and the NT opens with 'grace' (charis), with John the Baptist breaking the silence as the 'Elijah' Malachi promised (4:5-6).",
        "contested_words": [
            {"word": "mal'akhi", "hebrew": "מַלְאָכִי", "issue": "'My messenger' (1:1, 3:1) — is Malachi a proper name or a title? 'I will send my mal'akh (messenger) to prepare the way' (3:1). The book may be anonymous.", "severity": "MAJOR"},
            {"word": "cherem", "hebrew": "חֵרֶם", "issue": "'Curse' (4:6) — the final word of the OT. Devoted destruction. The old covenant ends under the shadow of cherem; the new opens with charis (grace).", "severity": "CRITICAL"},
            {"word": "Eliyyahu", "hebrew": "אֵלִיָּהוּ", "issue": "'Elijah' (4:5) — 'I will send Elijah before the great Day of YHWH.' Fulfilled in John the Baptist (Matt 11:14, 17:12-13).", "severity": "CRITICAL"},
        ],
        "hidden_connections": [
            {"target": "matthew", "why": "Matt 11:14 and 17:12-13 — Jesus identifies John the Baptist as the Elijah Malachi promised (Mal 4:5-6)"},
            {"target": "mark", "why": "Mark 1:2 quotes Mal 3:1 ('I send my messenger before your face') combined with Isa 40:3 — the opening of the Gospel"},
            {"target": "luke", "why": "Luke 1:17 — the angel tells Zechariah that John will go 'in the spirit and power of Elijah' to fulfill Malachi's prophecy"},
            {"target": "romans", "why": "Rom 9:13 quotes Mal 1:2-3 ('Jacob I loved, Esau I hated') for the election argument"},
            {"target": "obadiah", "why": "Both address the Esau/Edom theology — Obadiah judges Edom, Malachi opens with 'Jacob I loved, Esau I hated'"},
        ],
        "what_it_doesnt_say": [
            "Why 400 years of prophetic silence follow — the last prophet speaks and then heaven goes silent with no explanation",
            "Whether Malachi is a name or a title — 'my messenger' could be the author's name or a description",
            "How Elijah would return — literal return or spiritual successor? The ambiguity allows for John the Baptist as fulfillment",
        ],
        "unusual_characters": [
            {"name": "The messenger of the covenant", "ref": "3:1", "detail": "Two figures: 'my messenger' who prepares the way (John the Baptist) and 'the Lord whom you seek' who comes to the Temple (Christ). Two advents in one verse.", "connections": ["matthew", "mark", "luke"]},
        ],
        "patterns": [
            "Disputation format: six dialogues where Israel challenges God and God responds — 'You say... But I say...' The people argue with YHWH.",
            "OT-to-NT bridge: last word 'curse' (cherem, 4:6) -> 400 years of silence -> first word of NT era: 'grace' (charis). The hinge of redemptive history.",
            "Tithing passage (3:10) — 'Test me in this' — the ONLY place YHWH invites being tested. Unique in all of Scripture.",
        ],
        "mistranslations": [
            {"english": "Malachi", "original": "mal'akhi", "issue": "Treated as a proper name but means 'my messenger.' The book may be anonymous — the 'author' is a title, not an identity."},
            {"english": "curse", "original": "cherem", "issue": "Generic 'curse' hides the specific meaning: devoted to destruction, total consecration to judgment. The weight of the OT's final word."},
        ],
    },
}


def inject_fields():
    with open(FILE, "r", encoding="utf-8") as f:
        content = f.read()

    for book_id, fields in FIELDS.items():
        # Find the entry by matching "id": 'book_id' followed by body_html and closing },
        # We need to insert the new fields between the end of body_html and the closing },

        # Pattern: find the body_html line for this book, then insert fields before the next },
        # Strategy: find "'id': '{book_id}'" then find the next "}," after body_html

        # Locate the entry
        id_pattern = f"\"id\": '{book_id}'"
        id_pos = content.find(id_pattern)
        if id_pos == -1:
            id_pattern = f"'id': '{book_id}'"
            id_pos = content.find(id_pattern)
        if id_pos == -1:
            print(f"WARNING: Could not find entry for {book_id}")
            continue

        # Check if this entry already has key_claim
        # Find the next entry or end of list
        next_id = content.find("\"id\":", id_pos + 10)
        if next_id == -1:
            next_id = content.find("'id':", id_pos + 10)
        if next_id == -1:
            next_id = len(content)

        entry_text = content[id_pos:next_id]
        if '"key_claim"' in entry_text or "'key_claim'" in entry_text:
            print(f"SKIP: {book_id} already has key_claim")
            continue

        # Find the closing of body_html for this entry
        # Look for the pattern: body_html': '''...''',\n    },
        # We need to find the },  that closes this entry

        # Find body_html start
        bh_pos = content.find("body_html", id_pos)
        if bh_pos == -1 or bh_pos > next_id:
            print(f"WARNING: No body_html for {book_id}")
            continue

        # Find the closing of the entry dict: look for "\n    }," after body_html
        # We need to find the }, that closes this specific entry
        search_start = bh_pos
        # Find the triple-quote close of body_html
        tq_pos = content.find("''',", search_start + 15)
        if tq_pos == -1 or tq_pos > next_id:
            # Try empty body_html
            tq_pos = content.find("'''''',", search_start)
            if tq_pos == -1 or tq_pos > next_id:
                print(f"WARNING: Could not find body_html close for {book_id}")
                continue

        # Find the next },  after the body_html close
        close_pos = content.find("},", tq_pos)
        if close_pos == -1 or close_pos > next_id:
            print(f"WARNING: Could not find entry close for {book_id}")
            continue

        # Build the fields string
        lines = []
        for key, value in fields.items():
            lines.append(f"        \"{key}\": {repr(value)},")

        fields_str = "\n".join(lines) + "\n"

        # Insert before the closing },
        # The close_pos points to "},". We want to insert before "    },"
        # Find the start of the line containing },
        line_start = content.rfind("\n", 0, close_pos) + 1

        insert_pos = line_start
        content = content[:insert_pos] + fields_str + content[insert_pos:]

        # Update next_id positions since we've inserted content
        print(f"OK: {book_id} — {len(fields)} fields injected")

    # Verify it compiles
    try:
        compile(content, "bible_analysis.py", "exec")
        print("\nCompilation: OK")
    except SyntaxError as e:
        print(f"\nCompilation FAILED: {e}")
        return False

    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\nFile written: {len(content)} bytes")
    return True

if __name__ == "__main__":
    inject_fields()
