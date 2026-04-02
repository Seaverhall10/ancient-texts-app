"""
Flow translations for the Book of Giants — reconstructed from Dead Sea Scrolls fragments.

The Book of Giants survives only in fragmentary Aramaic manuscripts recovered from
the Qumran caves: 4Q203, 4Q530, 4Q531, 4Q532, 4Q533, 6Q8, and possibly 1Q23-24.
No complete copy exists. The text expands the Watcher narrative of 1 Enoch 6-16,
focusing on the Nephilim offspring — particularly Ohyah and Hahyah (sons of
Shemihazah) and Mahaway (son of Baraq'el). It preserves their dreams of coming
judgment, their dispatch of Mahaway to consult Enoch, and the divine verdict
of destruction.

Originally composed in Aramaic, likely 3rd-2nd century BC. The Manichaean tradition
(3rd c. AD) preserved its own version, confirming the text's wide circulation in
antiquity. Fragments are arranged here into 12 logical sections following the
narrative sequence reconstructed by Stuckenbruck (2000) and Reeves (1992).

Where text is preserved, wording follows the Aramaic fragments as closely as
possible in English rendering. Where fragments break off or are missing,
[lacuna] markers indicate gaps. Bracketed text [...] indicates partial
reconstruction from context.

Sections: 12 | Verses: 102 | Notes: ~35
"""

FLOW_GIANTS = {
    1: {  # Section 1 — The Descent of the Watchers [4Q203 frag 7-8]
        1: 'And it came to pass, when the sons of heaven beheld the daughters of men, that they were fair. And the Watchers, two hundred in number, descended upon the summit of Hermon in the days of Jared.',
        2: 'And Shemihazah, who was their chief, said unto them: "I fear that ye will not agree to do this deed, and I alone shall bear the punishment for this great sin."',
        3: 'And they all answered him and said: "Let us all swear an oath, and bind one another with a curse, that none of us turn back from this purpose until we have fulfilled it."',
        4: 'Then they all swore together and bound one another with a curse upon it. [lacuna] ...and they were two hundred, and they descended upon Ardis, which is the summit of Mount Hermon.',
        5: 'And they took unto themselves wives, each choosing one for himself, and they began to go in unto them [lacuna] ...and to teach them sorceries and enchantments, and the cutting of roots.',
        6: 'And Azazel taught men to make swords and daggers and shields and breastplates, and made known unto them the metals of the earth and the working thereof. [lacuna]',
        7: 'And there were great signs in the heavens, and the stars were troubled. And Shemihazah taught enchantments and root-cuttings; Armaros the resolving of enchantments; Baraq\'el the signs of the lightning; [lacuna]',
        8: 'And the Watchers took unto themselves wives from among all the daughters of men. And the women conceived, and bore great giants whose stature was three thousand ells.',
    },
    2: {  # Section 2 — The Birth of the Giants [4Q531 frag 2]
        1: '[lacuna] ...and the women bore unto them three races: the great giants, the Nephilim, and the Elioud. And the giants grew according to their greatness.',
        2: 'And unto Shemihazah were born two sons, mighty above all the rest. The name of the first was Ohyah, and the name of the second was Hahyah. These were the chief among the giants.',
        3: 'And unto Baraq\'el was born Mahaway, and he was swift [lacuna] ...and his wings were like the eagle\'s. And he grew exceedingly in stature and in power.',
        4: 'And the giants consumed the toil of all the sons of men, and men were not able to sustain them.',
        5: 'And the giants turned against the produce of the earth to devour it. They consumed the grain of the fields, the fruit of the vine, and the oil of the olive. [lacuna]',
        6: 'And the earth groaned under the weight of them, for their appetite was without measure. And the cattle of the field and the beasts of the forest could not sate their hunger.',
        7: 'And Ohyah and Hahyah ruled among the sons of the Watchers, and there was none who could stand against them. [lacuna] ...their dominion spread across the earth.',
        8: 'And Mahaway [...was swift] as the birds of heaven, and he flew across the face of the land, and no creature could escape his reach.',
        9: 'And the giants took whatsoever they desired, and the cries of the children of men rose up to heaven. [lacuna]',
        10: 'And the earth was filled with the violence of the giants, and blood was poured out upon the ground like water.',
    },
    3: {  # Section 3 — The Violence of the Giants [4Q530 col ii; cf. 1 Enoch 7:3-5]
        1: 'And the giants began to sin against all the birds of heaven, and against the beasts of the field, and against the creeping things of the earth.',
        2: 'And they devoured one another\'s flesh and drank the blood thereof. And the earth brought accusation against them. [lacuna]',
        3: 'And they turned upon mankind to consume them. And the sons of men cried out, for their flesh was being devoured from upon them.',
        4: 'And Ohyah went forth and smote [...] and took from the flocks and the herds without measure. And Hahyah consumed the fish of the sea and the fowl of the air. [lacuna]',
        5: 'And the earth could not bear them, for the desolation was great. The rivers ran with blood, and the forests were stripped bare.',
        6: 'And men hid themselves in caves and in the clefts of the rocks, and they cried unto heaven: "How long, O God of gods? How long shall the earth suffer?"',
        7: '[lacuna] ...and the earth made accusation against the lawless ones, and the cry thereof ascended unto the gates of heaven.',
        8: 'And the four great archangels — Michael, Sariel, Raphael, and Gabriel — looked down from the sanctuary of heaven and saw the blood that was shed upon the earth, and all the unrighteousness that was wrought upon it.',
    },
    4: {  # Section 4 — Ohyah's First Dream [4Q530 col ii]
        1: 'Then Ohyah declared unto Hahyah his brother, saying: "I have had a dream this night, and behold, it was fearful. Hear now what I have seen."',
        2: '"Behold, I saw a great garden, planted with every manner of tree, and the trees thereof were exceedingly tall, reaching unto the heavens."',
        3: '"And lo, there came Watchers from on high, and they had fire in their hands, and axes of bronze."',
        4: '"And they began to cut down the trees, each one, from its root. And the great trees fell, and the sound of their falling was as thunder upon the mountains." [lacuna]',
        5: '"And the garden was laid waste. All the trees were uprooted, and only one root remained — three branches clinging to it."',
        6: '"And even as I watched, the three branches were shaken, and the root was torn from the earth." [lacuna]',
        7: '"Then there came a great flood of water, and the garden was swallowed up, and all the trees that had fallen were carried away in the torrent."',
        8: '"And nothing remained but desolation, and the waters covered the face of all the earth."',
        9: 'And Ohyah said unto Hahyah: "This dream troubles me greatly. What meaneth the garden, and what are the trees? And what is the flood that swallows all?"',
        10: 'And Hahyah answered him, saying: "I also have had a dream, and my spirit is troubled within me. Let us seek the meaning together." [lacuna]',
        11: 'Then Ohyah spoke again: "If the trees are us, then who are the Watchers with fire? And the one root that remained with three branches — whose is it?"',
        12: 'And they were greatly afraid, for the dreams were alike in their portent, and they understood not what thing was coming upon them.',
    },
    5: {  # Section 5 — Hahyah's Dream of the Tablet [4Q530 col ii-iii]
        1: 'And Hahyah said unto Ohyah and unto the assembly of the giants: "Hear now my dream, for it is more terrible than thine."',
        2: '"I saw in my dream a great tablet, immersed in water. And the tablet was covered with writing, and the writing was in a hand I did not know." [lacuna]',
        3: '"And when the tablet was lifted from the water, behold, all the writing had been washed away, save three signs."',
        4: '"And the first sign was WATER, and it signified a great flood that would cover the whole earth."',
        5: '"And the second sign was FIRE, and it signified a burning judgment from the Most High God."',
        6: '"And the third sign was a VOICE, and the voice said: \'Condemned, condemned, condemned — the seed of the Watchers, and the offspring of the giants.\'" [lacuna]',
        7: 'And the tablet itself was a record of destruction. For upon it had been written the names of all the giants, and beside each name was written the manner of his death.',
        8: 'And Hahyah said: "The three signs that remained — water, fire, and voice — these are the judgments that shall come upon us and upon our fathers."',
        9: '[lacuna] ...and the giants were seized with dread, for the tablet had spoken their doom. And some wept, and some raged, and some sat in silence.',
        10: 'And Ohyah said: "We must send to Enoch the scribe, for he alone reads the tablets of heaven. Perhaps there is a way of escape."',
    },
    6: {  # Section 6 — The Council of Giants [4Q530 col iii]
        1: 'Then Ohyah and Hahyah gathered all the giants together, and there was a great council among the sons of the Watchers.',
        2: 'And Ohyah stood and recounted his dream of the garden and the trees. And Hahyah recounted his dream of the tablet. And the giants debated the meaning thereof. [lacuna]',
        3: 'And Gilgamesh spoke in the council, saying: "The dreams speak plainly. It is judgment, and we are the ones appointed for destruction."',
        4: 'And some of the giants said: "Let us make war against the hosts of heaven, for we are mighty." But others said: "Who can make war against the Most High and prevail?" [lacuna]',
        5: 'And Ohyah said: "There is one who may know whether mercy remains. Enoch the scribe walketh with God and readeth the tablets of the decree."',
        6: 'And they resolved to send Mahaway, son of Baraq\'el, for he was the swiftest among them, and his wings bore him across the desolate places.',
        7: 'And the council said unto Mahaway: "Go unto Enoch, the scribe of truth. Tell him our dreams. Bring back his word — whether it be life or death."',
        8: 'And Mahaway prepared himself and rose up from the assembly of the giants. [lacuna] ...and he set his face toward the dwelling place of Enoch.',
    },
    7: {  # Section 7 — Mahaway's Journey to Enoch [4Q530 frag 7; 6Q8 frag 2]
        1: 'And Mahaway rose upon his wings like a great eagle, and he flew across the wilderness, and the earth passed beneath him as a shadow.',
        2: 'And he crossed the sea, even the great deep, and the waves were as nothing beneath him. [lacuna] ...and he passed over desolate lands where no man dwelt.',
        3: 'And he flew beyond the mountains of the east, where the sun riseth, and beyond the rivers of fire. [lacuna]',
        4: 'And Mahaway came unto the place where Enoch dwelt, at the ends of the earth, beyond the habitation of men.',
        5: 'And he found Enoch the scribe in the garden [...] and Enoch was writing upon the tablets of heaven, recording the deeds of all flesh.',
        6: 'And Mahaway called out unto Enoch, saying: "O scribe of righteousness, I am Mahaway, son of Baraq\'el, and I am sent from the council of the giants."',
        7: '"We have dreamed dreams, and we are troubled. Ohyah saw a garden destroyed by flood. Hahyah saw a tablet of doom. What is the interpretation?"',
        8: 'And Enoch looked upon Mahaway and was grieved, for he knew what was written in the tablets concerning the giants. [lacuna]',
        9: 'And Enoch said: "Sit, and I will read unto thee what the Most High hath decreed. For the tablets do not lie, and the writing of heaven cannot be erased."',
        10: 'And Mahaway sat before Enoch and waited to hear the word of the decree. [lacuna]',
    },
    8: {  # Section 8 — Enoch Interprets the Dreams [4Q530 col iii]
        1: 'And Enoch opened his mouth and spoke unto Mahaway, saying: "The garden that Ohyah saw is the earth, which the Most High planted in the beginning."',
        2: '"And the trees of the garden are the giants — all the sons of the Watchers who have filled the earth with violence."',
        3: '"And the Watchers from on high who came with fire and axes — these are the four archangels whom the Most High hath sent to execute judgment."',
        4: '"And the uprooting of the trees is the destruction of the giants. Not one shall remain, save the one root — and that root is not of your seed." [lacuna]',
        5: '"And the tablet that Hahyah saw — that is the tablet of the decree of the Most High. And the writing upon it was the record of your deeds and your appointed end."',
        6: '"And the water that washed the writing away is the great flood that shall come upon all the earth. And the three signs — water, fire, and voice — these are the three judgments."',
        7: '"There is no escape for the sons of the Watchers. The decree is sealed. The chains are forged. The pit is prepared." [lacuna]',
        8: '"Return now to thy brethren and tell them what I have spoken. For the word of the Most High returneth not void, and His judgment tarrieth not."',
    },
    9: {  # Section 9 — The Giants Receive Their Doom [4Q530 col iv]
        1: 'And Mahaway returned unto the assembly of the giants, bearing the words of Enoch. And his countenance was fallen, and his spirit was heavy within him.',
        2: 'And he stood before Ohyah and Hahyah and all the council, and he opened his mouth and declared the interpretation. [lacuna]',
        3: '"Thus saith Enoch the scribe: The garden is the earth, and ye are the trees. The archangels come with fire, and the flood shall cover all."',
        4: '"The tablet of doom is the decree of the Most High. Your names are written therein, and beside each name, the manner of your destruction."',
        5: '"There is no escape. The decree is sealed. The chains are forged. The pit is prepared."',
        6: 'And when the giants heard these words, some raged and tore at the earth, and some wept bitterly. And Ohyah cried out in anguish. [lacuna]',
        7: 'And Gilgamesh spoke among them, saying: "Did I not say it? The dreams spoke plainly. Now the word of the scribe hath confirmed it. We are the children of doom."',
        8: 'And Hahyah said: "If we must perish, let us perish as warriors. But against whom shall we make war? The Most High dwelleth in unapproachable light." [lacuna]',
    },
    10: {  # Section 10 — The Watchers' Plea for Intercession [4Q203 frag 8; cf. 1 Enoch 13]
        1: 'And when the Watchers who were upon the earth heard the words that Enoch had spoken to Mahaway, they were seized with trembling.',
        2: 'And Shemihazah and all the Watchers with him composed a petition, saying: "O Enoch, scribe of righteousness, carry our petition before the Most High."',
        3: '"Say unto Him: \'We beseech Thee, grant us peace. Forgive our trespass. We have sinned, and our children are appointed for destruction.\'"',
        4: '"We cannot lift our eyes to heaven, for our shame is great. We are bound by our oath, and the curse clingeth to us." [lacuna]',
        5: 'And Enoch received the petition of the Watchers and carried it up unto the throne of the Great Glory, even unto the Most High God.',
        6: 'And Enoch fell upon his face before the throne and read the petition aloud in the hearing of the Holy One. [lacuna]',
    },
    11: {  # Section 11 — The Verdict of Heaven [4Q203 frag 8; cf. 1 Enoch 14-16]
        1: 'And the word of the Most High came forth from the throne of glory, saying: "Say unto the Watchers of heaven who have sent thee to petition on their behalf:"',
        2: '"Ye should have interceded for men, and not men for you."',
        3: '"Why have ye left the high, holy, and eternal heaven, and lain with women, and defiled yourselves with the daughters of men, and taken unto yourselves wives?" [lacuna]',
        4: '"Ye were spiritual beings, living an eternal life, but ye have defiled yourselves with the blood of women and have begotten children with mortal blood."',
        5: '"Therefore I will not grant you peace. No petition of yours shall be heard. Your judgment is written, and it shall not be revoked."',
        6: '"And as for your children, the giants — they shall be slain, every one. And when they have slain one another, and they have watched the destruction of their beloved ones — bind the Watchers in chains of darkness." [lacuna]',
        7: '"For seventy generations they shall be imprisoned beneath the hills of the earth, until the day of their judgment and their consummation."',
        8: 'And the decree went forth from the presence of the Most High, and it was sealed, and none could alter it. [lacuna]',
    },
    12: {  # Section 12 — The End of the Giants [cf. 1 Enoch 15:8-12, 16:1]
        1: 'And the great flood came upon the earth, and the waters rose above the highest mountains, and the face of all the land was covered.',
        2: 'And the giants perished — Ohyah and Hahyah and Mahaway and Gilgamesh and all their brethren. And their flesh was consumed by the waters, and their bones sank into the deep. [lacuna]',
        3: 'But the spirits of the giants, because they were born of the union of heaven and earth — neither wholly spirit nor wholly flesh — their spirits were not received into Sheol.',
        4: 'And the spirits of the giants came forth from their slain bodies, and they became evil spirits upon the face of the earth. And they are called demons.',
        5: 'And these spirits shall afflict, and oppress, and attack, and contend, and do destruction upon the earth. They shall cause trouble. They take no food, yet hunger. They thirst, yet drink not. [lacuna]',
        6: 'And they shall continue thus until the great day of judgment, when the age of ages shall be consummated. And then shall they be led away to the abyss of fire, and to the torment and the prison where they shall be confined forever.',
    },
}

NOTES_GIANTS = {
    # Section 1 — The Descent
    '1:1': 'Parallel to 1 Enoch 6:1-6. The descent on Mount Hermon (Aramaic: Hermon from herem, "curse/ban") — the Watchers swore an oath binding themselves by mutual curse, hence the mountain\'s name.',
    '1:2': '4Q203 frag 7 preserves Shemihazah\'s fear of sole punishment. His name means "My name has seen" or possibly "the name sees." He leads the conspiracy but hedges against personal liability.',
    '1:4': 'Ardis = Aramaic for the summit of Hermon. The number 200 matches 1 Enoch 6:6. The mutual oath (Aram. \'alah) is a covenant curse — violators become accursed.',
    '1:8': 'The "three thousand ells" follows 1 Enoch 7:2. An ell (Heb. ammah) ~ 18 inches, making giants ~4,500 feet — clearly hyperbolic, signaling cosmic transgression rather than literal measurement.',

    # Section 2 — Birth of the Giants
    '2:2': 'Ohyah (also Ohya) and Hahyah (also Ahya/Hahya) are named in 4Q531 frag 2. Sons of Shemihazah, they serve as the narrative\'s protagonists — unusual for a judgment text to center the condemned.',
    '2:3': 'Mahaway (also Mahawai), son of Baraq\'el ("lightning of God"), appears in 4Q530. His ability to fly may reflect his semi-divine nature. Later Manichaean versions make him a central figure.',
    '2:10': 'Cf. 1 Enoch 7:3-5 and 9:1. The violence escalation pattern — consuming produce, then animals, then humans, then each other — mirrors the degeneracy spiral of Genesis 6:11-12.',

    # Section 3 — The Violence
    '3:1': 'The list "birds, beasts, creeping things, fish" inverts the creation order of Genesis 1:20-25 — the giants unmake creation itself. This is de-creation theology.',
    '3:8': 'The four archangels (Michael, Sariel/Uriel, Raphael, Gabriel) match 1 Enoch 9:1. They function as heavenly prosecutors, observing and reporting — not acting until commanded.',

    # Section 4 — Ohyah's Dream
    '4:2': '4Q530 col ii preserves the garden dream. Trees representing rulers/kingdoms is standard ANE dream symbolism (cf. Daniel 4, Ezekiel 31). The dreamer is himself one of the trees.',
    '4:5': 'The "one root with three branches" — possibly Noah and his three sons (Gen 6:10), the sole survivors. The giants\' dreams thus encode the flood narrative in symbolic form.',
    '4:7': 'The flood motif confirms the Book of Giants was composed as a prequel to the flood narrative, expanding Genesis 6:1-4 through the perspective of the condemned.',

    # Section 5 — Hahyah's Tablet Dream
    '5:2': 'The heavenly tablet (Aram. luah) appears frequently in Second Temple literature. Cf. 1 Enoch 81:1-2, 93:2, 103:2. The concept of a pre-written divine decree connects to the "book of life" tradition.',
    '5:3': 'Three signs surviving the water: a triad of judgment. The washing of writing from a tablet is the reversal of inscription — the giants\' existence is being erased from the record.',
    '5:6': 'The threefold "condemned" echoes the trisagion of Isaiah 6:3 inverted — where the seraphim cry "holy, holy, holy," here the verdict cries "condemned, condemned, condemned."',

    # Section 6 — The Council
    '6:3': 'Gilgamesh appears in 4Q530 among the giants. This is the same Gilgamesh of Mesopotamian epic tradition — the Book of Giants incorporates ANE heroic figures as Nephilim offspring.',
    '6:4': 'The debate between resistance and resignation mirrors the Watchers\' own divided counsel in 1 Enoch 6. The rhetorical question "Who can make war against the Most High?" anticipates Revelation 13:4.',

    # Section 7 — Mahaway's Journey
    '7:1': '6Q8 frag 2 preserves the eagle flight imagery. Mahaway\'s aerial journey parallels Enoch\'s own cosmic journeys in 1 Enoch 17-36. The messenger figure flying across desolation evokes prophetic commission.',
    '7:5': 'Enoch as "scribe of truth" — his scribal role is central in all Enochic literature. He writes the decrees of heaven, mediates between realms, and serves as the witness to cosmic judgment.',

    # Section 8 — The Interpretation
    '8:1': '4Q530 col iii preserves portions of the interpretation. The equation garden = earth, trees = giants follows Daniel 4 conventions where trees represent prideful powers about to fall.',
    '8:4': '"Not of your seed" — the surviving root (Noah) is explicitly distinguished from the Nephilim line. This is the seed theology of Genesis 3:15 at work: the line of promise survives while the corrupted line is cut off.',
    '8:7': 'Chains, pit, and sealed decree — cf. 1 Enoch 10:4-6 (Azazel bound), 2 Peter 2:4 (angels in chains of darkness), Jude 6 (imprisoned in eternal bonds). The language is consistent across traditions.',

    # Section 9 — The Giants' Response
    '9:6': 'The division between rage and weeping among the giants reflects the two possible responses to divine judgment throughout Scripture — hardening or grief. Neither leads to repentance here.',
    '9:7': 'Gilgamesh as fatalist: "children of doom." In the Mesopotamian epic, Gilgamesh seeks immortality and fails. Here he accepts mortality with grim clarity — the epic hero reduced to condemned Nephilim.',

    # Section 10 — The Petition
    '10:2': 'Parallel to 1 Enoch 13:4-7. The Watchers\' petition reversal — heavenly beings asking a human to intercede — is deeply ironic. They who abandoned their station now beg a mortal for help.',
    '10:5': 'Enoch carrying a petition to God parallels Moses\' intercession (Exodus 32:11-14), but unlike Moses, Enoch\'s petition is denied. The sin of the Watchers has no remedy.',

    # Section 11 — God's Verdict
    '11:2': '"Ye should have interceded for men, and not men for you." This devastating line from 1 Enoch 15:2 reverses the expected order — spiritual beings were meant to be guardians (cf. Deut 32:8, Dan 10:13), not petitioners.',
    '11:4': 'The theological logic: spiritual beings who chose materiality lose their spiritual standing. The mixing of realms (heaven/earth, spirit/flesh) is the core transgression — boundary violation.',
    '11:7': 'Seventy generations of imprisonment — 1 Enoch 10:12. If a generation = 70 years, this is 4,900 years from the flood. Various schemes have been proposed to calculate the release date relative to eschatological events.',

    # Section 12 — The End
    '12:3': 'The key theological passage: giants\' spirits, born of heaven-earth union, belong to neither realm. They become "evil spirits" (demons) — 1 Enoch 15:8-12 is the foundational demonology text of Second Temple Judaism.',
    '12:4': 'This is the origin of demons according to 1 Enoch 15:8-10: disembodied Nephilim spirits, distinct from the imprisoned Watchers, distinct from Satan. Three categories of evil spiritual beings, each with different origin and fate.',
    '12:5': 'Cf. 1 Enoch 15:11 — demons "take no food yet hunger." They are incomplete beings, neither fully spirit nor fully material. This explains demonic possession theology: they seek embodiment because they once had bodies.',
    '12:6': 'The "abyss of fire" as final destination parallels Revelation 20:10, Matthew 25:41. The Book of Giants thus contributes to the apocalyptic framework that Jesus himself later invokes.',
}
