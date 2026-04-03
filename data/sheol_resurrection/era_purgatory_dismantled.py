"""
era_purgatory_dismantled.py -- Purgatory: A Doctrine Without a Text (Chapters 1-2)

Purgatory -- a place of temporal purification after death where believers who
were not fully sanctified are cleansed before entering heaven -- is one of the
most significant doctrines in Christian history to rest on the thinnest
textual foundation. The word purgatorium does not appear until the late 12th
century. The doctrine was formally defined at the Council of Florence (1439)
and confirmed at Trent (1563). Luther's 95 Theses (1517) were specifically
against the selling of indulgences -- certificates that reduced time in
purgatory.

This era examines the historical development, the texts used to support it,
and the two decisive texts that dismantle it: Hebrews 10:14 (teteleioken --
perfected for all time) and John 19:30 (tetelestai -- it is finished).

Two chapters covering:
  1. The historical development and the texts used to support purgatory
  2. Hebrews 10:14 and John 19:30 -- the two texts that end the argument
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 1: A DOCTRINE WITHOUT A TEXT
    # =========================================================================
    {
        "id": "purgatory-dismantled-1",
        "ref": "2 Maccabees 12:43-45; Matthew 12:32; 1 Corinthians 3:13-15",
        "chapter_num": 1,
        "title": "Purgatory \u2014 Historical Development and the Texts Used",
        "era": "purgatory_dismantled",
        "type": "chapter",

        "synopsis": "No Hebrew word exists for purgatory. No Greek word exists for "
                    "purgatory. The Latin word purgatorium does not appear until the "
                    "late 12th century. The doctrine was defined formally at the "
                    "Council of Florence (1439) and confirmed at Trent (1563). Before "
                    "1000 AD, there was no formal doctrine of purgatory in the church. "
                    "This chapter traces its historical development and examines the "
                    "three primary texts used to support it -- 2 Maccabees 12, Matthew "
                    "12:32, and 1 Corinthians 3:13-15 -- showing that none of them "
                    "actually describe purgatory.",

        "key_verse": {
            "ref": "1 Corinthians 3:15",
            "text": "If anyone's work is burned up, he will suffer loss, though he "
                    "himself will be saved, but only as through fire.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "purgatorium (Latin)",
                "meaning": "A place of purging, purification. The Latin term does not "
                           "appear in theological literature until the late 12th "
                           "century (earliest documented use c. 1170s). There is no "
                           "Hebrew equivalent. No Greek equivalent. No Aramaic "
                           "equivalent. The concept is a medieval Latin construction."
            },
            {
                "term": "\u03c0\u03c5\u03c1\u03cc\u03c9 (pyroo)",
                "meaning": "To burn, to test by fire. Used in 1 Corinthians 3:13 for "
                           "the fire that tests each person's WORK (ergon), not their "
                           "soul. The fire does not purify the person -- it evaluates "
                           "the ministry. The person is saved; the work is tested."
            },
            {
                "term": "\u03b1\u1f30\u03ce\u03bd (aion)",
                "meaning": "Age, eon, world-age. In Matthew 12:32, Jesus says the sin "
                           "against the Holy Spirit will not be forgiven 'in this age "
                           "or in the age to come.' Catholic interpretation reads "
                           "this as implying some sins CAN be forgiven after death. "
                           "The actual idiom means NEVER -- the same construction "
                           "as 'neither by day nor by night.'"
            }
        ],

        "ane_backdrop": "The idea of post-mortem purification has scattered precedents in "
                        "the ancient world. Some Orphic-Pythagorean traditions in Greece "
                        "described cycles of reincarnation and purification. Plato's myth "
                        "of Er (Republic, Book 10) describes souls being punished and "
                        "purified between incarnations. Virgil's Aeneid (Book 6) depicts "
                        "a place where souls are purged of earthly stains before entering "
                        "Elysium. These Greco-Roman purification afterlife concepts provided "
                        "the philosophical soil in which the Christian doctrine of purgatory "
                        "could grow. Notably, the Hebrew tradition has no parallel -- Sheol "
                        "is a place of waiting, not purification.",

        "second_temple": [
            {
                "source": "2 Maccabees 12:43-45",
                "summary": "According to 2 Maccabees, Judas Maccabeus collects money "
                           "for a sin offering for fallen soldiers found carrying "
                           "idolatrous amulets, making atonement for the dead 'that "
                           "they might be delivered from their sin.' This is the "
                           "primary Catholic proof text for purgatory.",
                "relevance": "Two critical problems with using this text for purgatory: "
                             "(1) 2 Maccabees is deuterocanonical -- not in the Hebrew "
                             "canon and not in the DSS canon at Qumran. (2) Even "
                             "granting the text authority, it describes prayer for the "
                             "dead and a sin offering -- not a place of purification, "
                             "not fire, not duration, not a process. The text does not "
                             "describe purgatory."
            },
            {
                "source": "Testament of Abraham 12-14 (Recension A)",
                "summary": "According to the Testament of Abraham, souls are judged at "
                           "death by Abel, and those whose deeds are evenly balanced "
                           "between good and evil are held in a middle state until the "
                           "final judgment, when Michael's intercession may rescue them.",
                "relevance": "The 'middle state' in the Testament of Abraham is the "
                             "closest pre-Christian parallel to purgatory -- a temporary "
                             "holding condition for ambiguous cases. But even here, there "
                             "is no purification by fire, no temporal punishment, no "
                             "payment of remaining debt. The concept is significantly "
                             "different from the formal doctrine."
            }
        ],

        "cross_refs": [
            {"ref": "2 Maccabees 12:43-45", "note": "The primary Catholic proof text -- prayer for the dead and sin offerings. Not in the Hebrew or Protestant canon. Does not describe purgatory as a place or process.", "type": "deuterocanonical"},
            {"ref": "Matthew 12:32", "note": "'Whoever speaks against the Holy Spirit will not be forgiven, either in this age or in the age to come.' 'Neither in this age NOR in the age to come' = Hebrew idiom for NEVER.", "type": "nt"},
            {"ref": "1 Corinthians 3:13-15", "note": "'Each one's WORK will become manifest... if anyone's work is burned up, he will suffer loss, though he himself will be saved, but only as through fire.' The fire tests WORK, not the person.", "type": "nt"},
            {"ref": "Hebrews 9:27", "note": "'It is appointed for man to die once, and after that comes judgment.' Death, then judgment. No intermediate purification stage mentioned.", "type": "nt"},
            {"ref": "Luke 16:26", "note": "'Between us and you a great chasm has been fixed.' The chasm in the intermediate state is permanent -- no crossing from torment to comfort. No process of purification moving souls from one to the other.", "type": "nt"},
            {"ref": "2 Corinthians 5:10", "note": "'We must all appear before the judgment seat of Christ.' The Bema Seat evaluates works and rewards. This is what 1 Cor 3:13-15 describes -- not purgatorial purification.", "type": "nt"},
            {"ref": "Romans 8:1", "note": "'There is therefore now NO condemnation for those who are in Christ Jesus.' No condemnation. Not reduced condemnation. Not condemnation that must be worked off after death.", "type": "nt"},
            {"ref": "Colossians 2:13-14", "note": "'Having forgiven us all our trespasses, by canceling the record of debt that stood against us... nailing it to the cross.' ALL trespasses. The debt is CANCELED.", "type": "nt"},
            {"ref": "Ephesians 2:8-9", "note": "'By grace you have been saved through faith. And this is not your own doing; it is the gift of God, not a result of works.' Salvation is a gift, not a process requiring post-mortem contribution.", "type": "nt"}
        ],

        "divine_council_note": "The development of purgatory is an example of how Greek "
                               "philosophical categories (Platonic soul-body dualism, "
                               "Orphic-Pythagorean purification cycles) infiltrated and "
                               "reshaped Christian theology. In the divine council framework, "
                               "this represents the ongoing influence of the Hellenistic "
                               "worldview that was assigned to the nations at Babel (Deuteronomy "
                               "32:8-9) -- the very thought-systems Christ's work was meant to "
                               "overthrow. The Hebrew framework has no purification afterlife "
                               "because the Hebrew framework understands atonement as something "
                               "GOD does, not something the dead person contributes to.",

        "sections": [
            {
                "heading": "What Purgatory Is and Where It Came From",
                "body": "Purgatory, in formal Catholic teaching, is a place or state of "
                        "temporal purification after death where believers who died in God's "
                        "grace but were not fully sanctified are cleansed of remaining "
                        "temporal punishment before entering heaven. The distinction between "
                        "'eternal punishment' (forgiven at justification) and 'temporal "
                        "punishment' (remaining even after forgiveness) is crucial to the "
                        "doctrine. The historical development is traceable. Before 1000 AD, "
                        "there is no formal doctrine of purgatory as a defined teaching. "
                        "Early church fathers like Clement of Alexandria and Origen speak of "
                        "purifying fire in general terms, but these are influenced by their "
                        "Platonic philosophical commitments, not by a systematic reading of "
                        "Scripture. Augustine (354-430 AD) discusses the possibility of "
                        "post-mortem purification but never with the precision of the later "
                        "doctrine. Gregory I (590 AD) promotes the concept more explicitly, "
                        "connecting it to Masses said for the dead. The word purgatorium "
                        "itself does not appear in theological literature until the late "
                        "12th century. The Council of Florence (1439) formally defined the "
                        "doctrine. The Council of Trent (1563) confirmed it. And the selling "
                        "of indulgences -- certificates that reduced time in purgatory -- "
                        "became the immediate cause of Luther's 95 Theses in 1517."
            },
            {
                "heading": "2 Maccabees 12 \u2014 Prayer for the Dead Is Not Purgatory",
                "body": "The primary biblical text used to support purgatory is 2 Maccabees "
                        "12:43-45, in which Judas Maccabeus collects money to provide a sin "
                        "offering for soldiers who had died carrying idolatrous amulets, "
                        "'that they might be delivered from their sin.' The text concludes: "
                        "'Therefore he made atonement for the dead, that they might be "
                        "delivered from their sin.' Two immediate problems arise. First, "
                        "2 Maccabees belongs to the deuterocanonical books -- accepted as "
                        "Scripture by the Catholic and Orthodox traditions but not part of "
                        "the Hebrew canon that Jesus and Paul used, and not found among the "
                        "Dead Sea Scrolls at Qumran. The Protestant tradition, following "
                        "Jerome's own reservations, does not grant it canonical authority. "
                        "Second, and more fundamentally: even granting the text full "
                        "authority, it does not describe purgatory. It describes prayer for "
                        "the dead and a sin offering for the dead. There is no mention of a "
                        "PLACE of purification. No mention of FIRE. No mention of DURATION. "
                        "No mention of temporal PUNISHMENT being worked off. No mention of "
                        "a PROCESS. Judas prays for the dead. That is all. The leap from "
                        "'prayer for the dead' to 'a place of temporal purification where "
                        "souls pay off remaining punishment through suffering' is enormous, "
                        "and the text does not make it."
            },
            {
                "heading": "Matthew 12:32 \u2014 'Neither in This Age nor in the Age to Come'",
                "body": "The second text used for purgatory is Matthew 12:32, where Jesus "
                        "says: 'Whoever speaks against the Holy Spirit will not be forgiven, "
                        "either in this age or in the age to come.' The Catholic argument: "
                        "the phrase 'the age to come' implies that SOME sins CAN be forgiven "
                        "after death -- otherwise, why mention the age to come at all? If no "
                        "post-death forgiveness exists, the phrase is redundant. Therefore, "
                        "there must be a place where post-death forgiveness happens -- "
                        "purgatory. The problem: this reading misunderstands a Hebrew idiom. "
                        "'Neither in this age nor in the age to come' is a standard ancient "
                        "Hebrew/Aramaic construction for NEVER. It is the same pattern as "
                        "'neither by day nor by night' (which means never, not that something "
                        "might happen during twilight), or 'neither in heaven nor on earth' "
                        "(which means nowhere, not that it might happen in Sheol). Jesus is "
                        "making the most absolute statement possible: this sin will NEVER be "
                        "forgiven. Not in the present. Not in the future. Not anywhere. Not "
                        "ever. The phrase closes the door completely. It does not open a "
                        "window for post-death forgiveness. It is an emphatic denial, not a "
                        "qualified one."
            },
            {
                "heading": "1 Corinthians 3:13-15 \u2014 The Fire Tests the Work, Not the Soul",
                "body": "The third and most commonly cited text is 1 Corinthians 3:13-15: "
                        "'Each one's work will become manifest, for the Day will disclose "
                        "it, because it will be revealed by fire, and the fire will test "
                        "what sort of work each one has done. If the work that anyone has "
                        "built on the foundation survives, he will receive a reward. If "
                        "anyone's work is burned up, he will suffer loss, though he himself "
                        "will be saved, but only as through fire.' The Catholic reading: "
                        "the fire that purifies is purgatorial fire that cleanses the soul "
                        "after death. The actual context: Paul is addressing the Corinthian "
                        "church about ministry quality. He has laid the foundation (Christ); "
                        "others build on it with gold, silver, precious stones, wood, hay, "
                        "straw (3:12). The fire does not purify the PERSON. It tests the "
                        "WORK -- the ministry, the spiritual fruit, the deeds. The person "
                        "is saved regardless -- 'he himself will be saved' -- but his work "
                        "may be burned up. He escapes 'as through fire' -- the image is a "
                        "man fleeing a burning building with nothing but the clothes on his "
                        "back. He survives, but everything he built is gone. This is the "
                        "Bema Seat judgment (2 Corinthians 5:10) -- the evaluation of "
                        "believers' works at Christ's return. It is not a place. It is not "
                        "a process. It is not purification. It is evaluation."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 2: THE TWO DECISIVE TEXTS
    # =========================================================================
    {
        "id": "purgatory-dismantled-2",
        "ref": "Hebrews 10:14; John 19:30; Hebrews 10:17-18; Romans 8:1",
        "chapter_num": 2,
        "title": "Teteleioken and Tetelestai \u2014 The Two Words That End the Argument",
        "era": "purgatory_dismantled",
        "type": "chapter",

        "synopsis": "The deepest problem with purgatory is not historical or textual "
                    "but theological. The doctrine requires that Christ's atoning work "
                    "is INCOMPLETE for most believers -- that temporal punishment "
                    "remains after death even after justification, and the soul must "
                    "contribute to its own purification. Two texts demolish this "
                    "framework with surgical precision. Hebrews 10:14: teteleioken -- "
                    "'He has perfected for all time those who are being sanctified.' "
                    "John 19:30: tetelestai -- 'It is finished.' If something remains "
                    "owing after the Cross, these words do not mean what they say.",

        "key_verse": {
            "ref": "Hebrews 10:14",
            "text": "For by a single offering he has perfected for all time those who "
                    "are being sanctified.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u03c4\u03b5\u03c4\u03b5\u03bb\u03b5\u03af\u03c9\u03ba\u03b5\u03bd (teteleioken)",
                "meaning": "He has perfected -- perfect tense in Greek, indicating a "
                           "completed action with ongoing results. From teleioo, 'to "
                           "bring to completion, to perfect, to make whole.' The "
                           "perfect tense is decisive: the perfecting is DONE. Not "
                           "ongoing. Not requiring supplementation. Not awaiting "
                           "post-mortem contribution. Finished, with permanent results."
            },
            {
                "term": "\u03c4\u03b5\u03c4\u03ad\u03bb\u03b5\u03c3\u03c4\u03b1\u03b9 (tetelestai)",
                "meaning": "It is finished, it has been completed, it is accomplished. "
                           "Perfect tense, passive voice. The word was written across "
                           "paid receipts in the ancient Greco-Roman world -- a debt "
                           "marked PAID IN FULL. Jesus' last word from the cross is "
                           "an accounting term: the debt is settled. Nothing remains."
            },
            {
                "term": "\u03b5\u1f30\u03c2 \u03c4\u1f78 \u03b4\u03b9\u03b7\u03bd\u03b5\u03ba\u03ad\u03c2 (eis to dienekes)",
                "meaning": "For all time, perpetually, continuously, in perpetuity. "
                           "Used in Hebrews 10:14 to modify 'perfected' -- He has "
                           "perfected eis to dienekes, FOR ALL TIME. Not temporarily. "
                           "Not until the remaining debt is paid. For all time. The "
                           "perfecting has no expiration date and no gap requiring "
                           "supplementation."
            },
            {
                "term": "\u03c0\u03c1\u03bf\u03c3\u03c6\u03bf\u03c1\u03ac (prosphora)",
                "meaning": "Offering, sacrifice. Hebrews 10:14 specifies: 'by a "
                           "SINGLE offering' (mia prosphora). Not multiple offerings. "
                           "Not a continuing process. Not an offering plus post-mortem "
                           "purification. A single offering that perfects for all time."
            }
        ],

        "ane_backdrop": "The concept of a single, sufficient sacrifice stands in sharp "
                        "contrast to the entire ancient Near Eastern sacrificial system. "
                        "In Mesopotamian, Egyptian, Canaanite, and Israelite temple "
                        "practice, sacrifices were repeated -- daily, weekly, annually. "
                        "The Day of Atonement (Yom Kippur) was an ANNUAL event precisely "
                        "because it did not permanently deal with sin (Hebrews 10:1-4). "
                        "The revolutionary claim of Hebrews is that one sacrifice has done "
                        "what the entire sacrificial system could not: perfected the "
                        "worshippers permanently. The repetition is over. If purgatory "
                        "requires additional purification after the cross, the author of "
                        "Hebrews would say it returns to the inadequacy of the old system "
                        "that could never perfect the worshipper (Hebrews 10:1).",

        "second_temple": [
            {
                "source": "4QMMT (4Q394-399, Dead Sea Scrolls)",
                "summary": "The Qumran community's 'Some Works of the Torah' letter "
                           "debates which works are necessary for covenant faithfulness. "
                           "The DSS community had a strict purity framework but never "
                           "developed a concept of post-mortem purification.",
                "relevance": "Even the most rigorous Second Temple Jewish community -- "
                             "the Essenes at Qumran, who had elaborate purity laws and "
                             "strict covenant boundaries -- did not teach purgatory. The "
                             "concept is absent from the entire Second Temple Jewish "
                             "landscape, appearing only in later medieval Christian "
                             "development."
            },
            {
                "source": "11QMelchizedek (11Q13)",
                "summary": "According to the Melchizedek scroll from Qumran, "
                           "Melchizedek is an exalted heavenly figure who will execute "
                           "judgment and 'atone for all the sons of light.' The "
                           "atonement is complete -- not supplemented by post-mortem "
                           "purification of the atoned.",
                "relevance": "The DSS Melchizedek tradition, which the author of "
                             "Hebrews draws on extensively, envisions atonement as "
                             "complete and definitive. The Melchizedekian priest perfects "
                             "those he atones for. This is the framework Hebrews 10:14 "
                             "operates within."
            }
        ],

        "cross_refs": [
            {"ref": "Hebrews 10:14", "note": "'By a single offering he has PERFECTED FOR ALL TIME those who are being sanctified.' Teteleioken -- perfect tense. Completed. Nothing lacking. For ALL TIME.", "type": "nt"},
            {"ref": "John 19:30", "note": "'It is finished.' Tetelestai -- the word written on paid receipts. PAID IN FULL. If purgatory exists, tetelestai means something other than 'finished.'", "type": "nt"},
            {"ref": "Hebrews 10:17-18", "note": "'I will remember their sins and their lawless deeds no more. Where there is forgiveness of these, there is NO LONGER ANY OFFERING FOR SIN.' No more offering. No remaining payment.", "type": "nt"},
            {"ref": "Hebrews 10:1-4", "note": "The old sacrifices could NEVER perfect the worshipper -- that is why they were repeated. Christ's sacrifice is unrepeatable because it WORKS. Adding purgatory returns to the old inadequacy.", "type": "nt"},
            {"ref": "Hebrews 7:27", "note": "'He has no need, like those high priests, to offer sacrifices daily... he did this ONCE FOR ALL when he offered up himself.' Once. For all. Not once-plus-purgatory.", "type": "nt"},
            {"ref": "Hebrews 9:12", "note": "'He entered once for all into the holy places... by means of his own blood, thus securing an ETERNAL redemption.' Eternal. Not temporal redemption requiring supplementation.", "type": "nt"},
            {"ref": "Romans 8:1", "note": "'There is therefore now NO condemnation for those who are in Christ Jesus.' No condemnation -- not reduced condemnation, not condemnation to be worked off after death.", "type": "nt"},
            {"ref": "Colossians 2:13-14", "note": "'Having forgiven us ALL our trespasses, by canceling the record of debt that stood against us... nailing it to the cross.' ALL trespasses. Debt CANCELED.", "type": "nt"},
            {"ref": "1 John 1:7", "note": "'The blood of Jesus his Son cleanses us from ALL sin.' All. Not most. Not all except the temporal punishment portion.", "type": "nt"},
            {"ref": "Romans 5:9", "note": "'Since we have now been justified by his blood, much more shall we be saved by him from the wrath of God.' Justified -- declared righteous. The legal standing is complete.", "type": "nt"}
        ],

        "divine_council_note": "The sufficiency of Christ's sacrifice is a divine council "
                               "victory declaration. Colossians 2:15 says Christ 'disarmed "
                               "the rulers and authorities and put them to open shame, "
                               "triumphing over them.' The 'record of debt' (cheirographon) "
                               "that stood against humanity was CANCELED and NAILED TO THE "
                               "CROSS. If temporal punishment remains owing after the cross, "
                               "the hostile powers have not been fully disarmed -- they still "
                               "hold a claim. But Paul says they have been put to 'open shame.' "
                               "Their claim is gone. The debt is paid. Tetelestai.",

        "sections": [
            {
                "heading": "Hebrews 10:14 \u2014 Perfected for All Time",
                "body": "The author of Hebrews makes the most devastating single-verse "
                        "argument against purgatory in the entire New Testament: 'For by "
                        "a single offering (mia prosphora) he has perfected (teteleioken) "
                        "for all time (eis to dienekes) those who are being sanctified' "
                        "(10:14). Every word is chosen with precision. 'Single offering' -- "
                        "not multiple sacrifices, not an ongoing process, not a sacrifice "
                        "followed by additional purification. One offering. 'Has perfected' "
                        "-- teteleioken is a perfect tense verb, indicating a completed "
                        "action with lasting results. The perfecting is DONE. It is not "
                        "in progress. It is not awaiting supplementation. It has been "
                        "accomplished. 'For all time' -- eis to dienekes, meaning 'in "
                        "perpetuity, without interruption, without end.' The perfecting "
                        "does not expire. It does not have a gap that must be filled by "
                        "post-mortem purification. It holds for all time. 'Those who are "
                        "being sanctified' -- the present tense here describes the ongoing "
                        "process of sanctification in THIS life, not purgatorial "
                        "purification. Believers are already perfected in their legal "
                        "standing (justified, teteleioken) while still being progressively "
                        "sanctified in practice. The perfecting before God is complete. "
                        "The growth in holiness continues in life. Neither requires "
                        "purgatory."
            },
            {
                "heading": "John 19:30 \u2014 Tetelestai: Paid in Full",
                "body": "Jesus' final word from the cross is not a gasp of exhaustion but "
                        "a declaration of completion. 'It is finished' -- tetelestai. The "
                        "word is in the perfect tense (completed action with ongoing "
                        "results) and passive voice (the action has been done TO completion). "
                        "In the Greco-Roman commercial world, tetelestai was the word "
                        "written across paid receipts. When a debt was fully discharged, "
                        "the creditor wrote tetelestai across the document -- PAID IN FULL. "
                        "No remaining balance. No further installments. No hidden fees to "
                        "be collected after the debtor's death. Jesus applies this word to "
                        "the atonement. The debt of sin is PAID IN FULL. If purgatory "
                        "requires that temporal punishment remains after death -- that the "
                        "soul must suffer additional purification to satisfy a remaining "
                        "obligation -- then tetelestai does not mean what Jesus said it "
                        "means. It would have to mean 'it is mostly finished' or 'the "
                        "eternal part is finished but the temporal part remains.' But that "
                        "is not what tetelestai means. It means finished. Complete. Done. "
                        "The entire argument of Hebrews builds on this: 'Where there is "
                        "forgiveness of these, there is NO LONGER ANY OFFERING FOR SIN' "
                        "(Hebrews 10:18). No more offering. No remaining payment. The ledger "
                        "is clear."
            },
            {
                "heading": "The Platonic Root \u2014 Purgatory Requires Greek Anthropology",
                "body": "Purgatory is only conceivable within the Platonic framework. If "
                        "the soul is an immortal, conscious entity that survives death "
                        "independently of the body, then it is possible to envision that "
                        "soul undergoing a process of purification after death and before "
                        "its final destination. But in the Hebrew framework, this is "
                        "impossible. Death in the Hebrew Bible is descent to Sheol -- "
                        "silence, diminishment, waiting. The dead are rephaim -- shades. "
                        "They are not undergoing active purification. They are resting, "
                        "waiting for the resurrection. In the Hebrew framework: death = "
                        "sleep, the dead = in Sheol waiting, resurrection = the final "
                        "state. There is no immortal soul floating around in conscious "
                        "torment being purified between death and heaven. That requires "
                        "Plato. Purgatory is one of the most visible theological fruits "
                        "of the Platonic contamination of Western Christianity. It requires "
                        "Greek anthropology (immortal soul surviving death) combined with a "
                        "view of atonement that leaves something owing after the cross. "
                        "The Hebrew text gives us neither. It gives us a whole person who "
                        "dies, descends to Sheol, and awaits resurrection -- an event that "
                        "the New Testament says is made possible by a single, sufficient, "
                        "completed sacrifice that perfects the believer for all time."
            },
            {
                "heading": "Luther's Starting Point \u2014 The Reformation Began Here",
                "body": "It is no accident that the Protestant Reformation began with "
                        "purgatory. Luther's 95 Theses (October 31, 1517) were specifically "
                        "directed against the selling of indulgences -- papal certificates "
                        "that purported to reduce time in purgatory for the living or the "
                        "dead. Johann Tetzel's famous sales pitch -- attributed to him by "
                        "his contemporaries -- claimed that the moment a coin dropped into "
                        "the collection box, a soul sprang from purgatory. Luther's "
                        "objection was initially pastoral and financial: poor people were "
                        "being exploited by a system that monetized their grief. But as he "
                        "went deeper into the Greek text of Hebrews and Romans, his "
                        "objection became theological. The texts do not support purgatory. "
                        "The sacrifice of Christ is sufficient. The debt is paid. To add "
                        "a system of post-mortem temporal punishment and then sell relief "
                        "from it is to build a doctrine without a text and then monetize "
                        "the fear it creates. The Council of Trent (1563) responded by "
                        "formally defining purgatory as dogma and anathematizing anyone "
                        "who denies it. But formal definition does not create textual "
                        "support. The word purgatorium remains absent from every Hebrew "
                        "manuscript, every Greek manuscript, and every Aramaic manuscript "
                        "in existence. On this specific point, the texts support Luther."
            }
        ]
    }
]
