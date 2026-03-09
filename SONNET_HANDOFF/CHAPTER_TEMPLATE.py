"""
TEMPLATE: NT Era File
Copy this pattern for any new era file. Replace all placeholder content.
The hebrew_terms key is reused for Greek terms (NT compatibility).
"""

CHAPTERS = [
    {
        'type': 'chapter',
        'title': 'Chapter Title — Divine Council Subtitle',
        'ref': 'BookName 1-3',
        'period': 'ca. 55-60 AD',
        'summary': (
            'A 2-3 sentence summary of this chapter group. '
            'Must mention the divine council / governance angle.'
        ),
        'body': (
            '<p>Full scholarly body text. 3-5 paragraphs minimum.</p>'
            '<p>Should cover: (1) what the text says, (2) historical context, '
            '(3) how it connects to the divine council worldview, '
            '(4) key Greek terms the reader should know.</p>'
            '<p>Use <b>bold</b> for emphasis. Use &mdash; for em-dashes. '
            'Transliterate Greek in italics: <i>ekklesia</i>.</p>'
        ),
        'hebrew_terms': [
            {
                'term': '\u03b5\u03ba\u03ba\u03bb\u03b7\u03c3\u03af\u03b1',
                'transliteration': 'ekklesia',
                'meaning': (
                    'Often translated "church," but the Greek means "assembly" or '
                    '"called-out gathering." In the LXX (Greek Old Testament), this '
                    'word translates Hebrew qahal, the assembly of Israel before YHWH. '
                    'Paul\'s usage carries both meanings: a local gathering AND the '
                    'cosmic assembly of those called out of the nations back to YHWH.'
                )
            },
            {
                'term': '\u03bc\u03c5\u03c3\u03c4\u03ae\u03c1\u03b9\u03bf\u03bd',
                'transliteration': 'mysterion',
                'meaning': (
                    'NOT "mystery" in the modern sense of a puzzle to solve. A mysterion '
                    'is a divine council decision that was HIDDEN and has now been REVEALED. '
                    'The Aramaic equivalent raz appears in Daniel 2:18-19. Paul uses this '
                    'to describe God\'s plan to include Gentiles (Eph 3:3-9).'
                )
            }
        ],
        'sections': [
            {
                'heading': 'Key Passage Deep Dive',
                'body': (
                    '<p>Focus on a specific passage within this chapter range. '
                    'Explain the Greek, provide context, connect to OT roots.</p>'
                )
            },
            {
                'heading': 'What the Reader Should Know',
                'body': (
                    '<p>Proactive explanation of anything confusing. '
                    'Don\'t wait for the reader to be confused — explain it first.</p>'
                )
            }
        ],
        'ane_context': (
            'How this passage relates to the Ancient Near Eastern or Greco-Roman world. '
            'Imperial cult, Roman governance, Greek philosophy, mystery religions, etc.'
        ),
        'second_temple': (
            'How Second Temple Jewish thought illuminates this text. '
            'Pharisees, Sadducees, Essenes, apocalypticism, messianic expectations.'
        ),
        'divine_council_note': (
            'THE MOST IMPORTANT FIELD. How does this passage connect to the divine '
            'council framework? Principalities, powers, thrones, dominions, the '
            'Deuteronomy 32 worldview, Christ\'s authority over the council, '
            'the reclamation of the nations, cosmic warfare, etc.'
        ),
        'cross_refs': [
            {'ref': 'Psalm 82', 'note': 'Connection to the divine council'},
            {'ref': 'Deuteronomy 32:8-9', 'note': 'The nations allotted to lesser elohim'},
            {'ref': 'Daniel 7:13-14', 'note': 'Son of Man receiving authority over all nations'}
        ],
        'historical_note': (
            'Historical background: who wrote this, when, to whom, what was happening '
            'politically and culturally at the time.'
        ),
        'reader_note': (
            'A friendly, accessible note for first-time readers. Explain what they\'re '
            'about to read, why it matters, and what to watch for. This is the "study '
            'Bible margin note" equivalent.'
        )
    },
    # Add more chapter dicts following this same pattern...
]
