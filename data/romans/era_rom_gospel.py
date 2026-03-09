"""
era_rom_gospel.py -- Romans 1-5: The Cosmic Gospel

The universal human predicament (1:18-3:20), justification by faith (3:21-4:25),
and the Adam-Christ typology (5:1-21). Paul establishes the gospel's cosmic
scope: all humanity guilty, all humanity offered grace, the entire human story
rewritten through the obedience of the one man, Jesus Christ.
"""

CHAPTERS = [
    {
        "id": "rom-gospel-1",
        "ref": "Romans 1:1-32",
        "chapter_num": 1,
        "title": "The Gospel of God and the Nations Given Over",
        "era": "rom_gospel",
        "type": "study",

        "synopsis": "Romans opens with Paul's self-introduction as 'a servant of Christ Jesus, called to "
                    "be an apostle, set apart for the gospel of God' (1:1). The gospel is defined "
                    "christologically: concerning God's Son, descended from David according to the flesh, "
                    "declared to be the Son of God in power by his resurrection from the dead (1:3-4). "
                    "Paul states the letter's thesis: 'the righteousness of God is revealed from faith for "
                    "faith, as it is written, The righteous shall live by faith' (1:17, quoting Hab 2:4). "
                    "Then comes the devastating indictment of Gentile humanity (1:18-32): they knew God "
                    "but did not honor him, exchanged his glory for idols, and were 'given over' "
                    "(paredoken) three times -- to impurity (1:24), to dishonorable passions (1:26), and "
                    "to a debased mind (1:28). This threefold giving-over echoes the Deuteronomy 32 "
                    "worldview: the nations abandoned to the corrupt governance of the sons of God.",

        "key_verse": {
            "ref": "Romans 1:16-17",
            "text": "For I am not ashamed of the gospel, for it is the power of God for salvation to everyone who believes, to the Jew first and also to the Greek. For in it the righteousness of God is revealed from faith for faith, as it is written, 'The righteous shall live by faith.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "euangelion (gospel/good news -- not just 'salvation information' but the royal proclamation of the king's victory; cf. Isa 52:7)",
            "dikaiosyne theou (the righteousness of God -- God's character, gift, and covenant faithfulness revealed in the gospel)",
            "ek pisteos eis pistin (from faith to/for faith -- the entire dynamic of salvation is faith: originating in God's faithfulness, received by human faith)",
            "apokalyptetai (is revealed -- present tense; the righteousness of God is being continuously unveiled in the gospel proclamation)",
            "orge theou (the wrath of God -- not emotional rage but judicial response to sin; God's settled opposition to evil)",
            "paredoken (gave over/handed over -- the divine judicial abandonment; God gave the nations over to the consequences of their rebellion)",
            "asebeia (ungodliness -- the vertical dimension: failure to worship the Creator)",
            "adikia (unrighteousness -- the horizontal dimension: failure to do justice among humans)",
            "aletheia (truth -- what the nations suppress; the revelation of God available in creation)",
            "eikona (image/likeness -- 1:23; they exchanged the glory of God for images; the reversal of the imago Dei)"
        ],

        "ane_backdrop": "The pattern of Romans 1:18-32 -- from knowledge of the true God to idolatry to "
                        "moral degradation -- parallels the Wisdom of Solomon 13-14 (a Second Temple Jewish "
                        "text that describes the Gentile descent into idol worship and its moral consequences). "
                        "The connection to Deuteronomy 32 is fundamental: when the nations rebelled at Babel "
                        "(Gen 11), God 'allotted' them to the sons of God (Deut 32:8-9 LXX/DSS: 'according "
                        "to the number of the sons of God'). This is the cosmic background to Paul's "
                        "threefold 'gave them over' (paredoken): God judicially handed the nations over to "
                        "the governance of the rebellious spiritual powers, with predictable results -- "
                        "idolatry, immorality, and societal collapse. The 'exchange' (1:23, 25, 26) language "
                        "echoes the 'exchange' pattern in ANE covenant violation: exchanging the covenant "
                        "Lord for false gods triggers the covenant curse. The vice list of 1:29-31 follows "
                        "Hellenistic moral philosophy conventions (Stoic vice catalogs) but is grounded in "
                        "the specifically Jewish understanding of idolatry as the root of all moral evil.",

        "second_temple": [
            {
                "source": "Wisdom of Solomon 13:1-14:31",
                "summary": "Describes the Gentile descent from knowing God through creation to worshiping "
                           "idols, leading to sexual immorality, murder, and societal chaos. The pattern -- "
                           "knowledge, rejection, idolatry, immorality -- closely parallels Romans 1:18-32.",
                "relevance": "Paul draws on this established Second Temple tradition of Jewish critique of "
                             "Gentile idolatry. The Wisdom of Solomon may be a direct source for Paul's "
                             "argument, or both may draw on common Jewish apologetic tradition."
            },
            {
                "source": "1 Enoch 99:6-9",
                "summary": "Describes the nations worshiping 'stones and graven images of gold and silver "
                           "and wood' and serving 'evil spirits and demons and every kind of error.'",
                "relevance": "Shows the Enochic tradition's connection between idol worship and demonic "
                             "governance -- the same link implied in Paul's 'giving over' language."
            },
            {
                "source": "Jubilees 11:4-5",
                "summary": "After the scattering at Babel, 'Mastema sent forth other spirits, those which "
                           "were put under his hand, to do all manner of wrong and sin, and all manner of "
                           "transgression, to corrupt and destroy.'",
                "relevance": "Jubilees explicitly connects the post-Babel situation with demonic governance "
                             "of the nations -- the theological framework underlying Rom 1:24-28."
            }
        ],

        "cross_refs": [
            {"ref": "Habakkuk 2:4", "note": "'The righteous shall live by his faith' -- the thesis verse of Romans, quoted in 1:17; also cited in Gal 3:11 and Heb 10:38", "type": "ot"},
            {"ref": "Deuteronomy 32:8-9", "note": "The nations allotted to the sons of God, Israel as YHWH's portion -- the cosmic background to the 'giving over' of Rom 1:24-28", "type": "ot"},
            {"ref": "Psalm 19:1-4", "note": "'The heavens declare the glory of God' -- the general revelation that leaves humanity 'without excuse' (Rom 1:20)", "type": "ot"},
            {"ref": "Genesis 1:26-27", "note": "'Let us make man in our image' -- the imago Dei that humanity exchanges for idolatrous images in Rom 1:23", "type": "ot"},
            {"ref": "Galatians 3:11", "note": "'The righteous shall live by faith' -- Paul's earlier use of Hab 2:4 in the justification argument", "type": "nt"},
            {"ref": "Acts 14:16", "note": "'In past generations he allowed all the nations to walk in their own ways' -- the Deuteronomy 32 situation restated by Paul in Acts", "type": "nt"},
            {"ref": "Acts 17:30", "note": "'The times of ignorance God overlooked, but now he commands all people everywhere to repent' -- the reversal of the 'giving over'", "type": "nt"},
            {"ref": "2 Samuel 7:12-14", "note": "The Davidic covenant -- Christ as David's seed (Rom 1:3) and Son of God (Rom 1:4)", "type": "ot"}
        ],

        "divine_council_note": "Romans 1:18-32 is the Deuteronomy 32 worldview applied to the Gentile "
                               "nations' present condition. The threefold 'gave them over' (paredoken, "
                               "1:24, 26, 28) describes God's judicial response to the nations' rebellion: "
                               "they refused to honor the Creator and were handed over to the consequences "
                               "of their choice. In the divine council framework, this 'giving over' is the "
                               "allotment of the nations to the sons of God at Babel (Deut 32:8-9). The "
                               "nations' idolatry -- exchanging the glory of God for images of creatures "
                               "(1:23) -- is the worship of the territorial deities, the elohim who were "
                               "appointed over them but who led them into false worship. The descent from "
                               "idolatry to sexual immorality to societal chaos (1:24-31) traces the "
                               "inevitable result of being governed by corrupt spiritual powers rather than "
                               "the true God. The 'truth' (aletheia) that is 'suppressed' (1:18) is the "
                               "revelation of God available in creation (1:19-20) -- general revelation that "
                               "leaves humanity 'without excuse' (anapologetos, 1:20). The gospel that Paul "
                               "proclaims is the reversal of this situation: the righteousness of God "
                               "revealed (apokalyptetai, 1:17) to reclaim the nations from the sons of God "
                               "and bring them back under YHWH's direct governance through Christ.",

        "sections": [
            {
                "heading": "The Gospel Defined: David's Son, God's Son (1:1-7)",
                "body": "Paul opens with his fullest self-identification: 'Paul, a servant (doulos -- slave) "
                        "of Christ Jesus, called to be an apostle, set apart for the gospel of God' (1:1). "
                        "The gospel is immediately defined christologically in a pre-Pauline creedal formula "
                        "that reveals two-stage Christology: 'concerning his Son, who was descended from David "
                        "according to the flesh (kata sarka) and was declared to be the Son of God in power "
                        "(en dynamei) according to the Spirit of holiness (kata pneuma hagiosynes) by his "
                        "resurrection from the dead' (1:3-4). The two stages: (1) Christ as David's descendant "
                        "-- his human identity, the fulfillment of the Davidic covenant (2 Sam 7:12-14). "
                        "(2) Christ declared Son of God in power by the resurrection -- his divine identity, "
                        "the enthronement at God's right hand (Psalm 110:1). The word 'declared' (horisthentos "
                        "-- 'appointed, designated') does not mean Christ BECAME the Son of God at the "
                        "resurrection; it means his resurrection DEMONSTRATED publicly what was always true. "
                        "The purpose of Paul's apostleship: 'to bring about the obedience of faith for the "
                        "sake of his name among all the nations (pasin tois ethnesin)' (1:5). The scope is "
                        "Deuteronomy 32 reversal: the nations allotted to the sons of God are now the target "
                        "of the gospel mission."
            },
            {
                "heading": "The Thesis: The Righteousness of God Revealed (1:16-17)",
                "body": "The letter's thesis is compressed into two verses: 'For I am not ashamed of the "
                        "gospel, for it is the power (dynamis) of God for salvation (soterian) to everyone "
                        "who believes (panti to pisteuonti), to the Jew first and also to the Greek. For in "
                        "it the righteousness of God (dikaiosyne theou) is revealed (apokalyptetai) from "
                        "faith for faith (ek pisteos eis pistin), as it is written, The righteous shall live "
                        "by faith (ho dikaios ek pisteos zesetai)' (1:16-17). Every term is loaded: the "
                        "gospel is not advice but POWER (dynamis -- the same word used for spiritual might in "
                        "the divine council hierarchy). Salvation is for 'everyone who believes' -- the "
                        "universality of access. 'To the Jew first and also to the Greek' establishes the "
                        "priority of Israel (YHWH's portion from Deut 32:9) while extending the gospel to "
                        "the nations. The 'righteousness of God' (dikaiosyne theou) is revealed (apokalyptetai "
                        "-- the same root as apokalypsis, 'apocalypse') -- the gospel is an apocalyptic event, "
                        "an unveiling of God's saving action. The Habakkuk 2:4 quotation serves as the "
                        "scriptural anchor: the righteous one lives by faithfulness -- God's faithfulness and "
                        "the human faith that responds to it."
            },
            {
                "heading": "The Nations Given Over: Idolatry and Its Consequences (1:18-32)",
                "body": "The argument turns dark: 'For the wrath of God (orge theou) is revealed (apokalyptetai "
                        "-- the same verb as 1:17, creating a deliberate parallel: both God's righteousness "
                        "AND God's wrath are being revealed) from heaven against all ungodliness (asebeian) "
                        "and unrighteousness (adikian) of men, who by their unrighteousness suppress the truth "
                        "(aletheian)' (1:18). The indictment begins: God's invisible attributes have been "
                        "clearly perceived in creation 'so that they are without excuse (anapologetous)' "
                        "(1:20). The descent is traced in three exchanges: (1) They 'exchanged (ellaxan) the "
                        "glory of the immortal God for images resembling mortal man and birds and animals' "
                        "(1:23) -- the reversal of Genesis 1:26-27, where humanity, made in God's image, "
                        "now makes gods in humanity's image. (2) They 'exchanged (metellaxan) the truth about "
                        "God for a lie and worshiped and served the creature rather than the Creator' (1:25). "
                        "(3) Their 'women exchanged (metellaxan) natural relations for those that are contrary "
                        "to nature' (1:26). Each exchange triggers a divine 'giving over': 'God gave them over "
                        "(paredoken) to the lusts of their hearts, to impurity' (1:24); 'God gave them over "
                        "(paredoken) to dishonorable passions' (1:26); 'God gave them over (paredoken) to a "
                        "debased mind' (1:28). The threefold paredoken is not vindictive punishment but "
                        "judicial consequence: God allows the nations to experience the full weight of their "
                        "choice to abandon him. The vice catalog of 1:29-31 is comprehensive: wickedness, evil, "
                        "covetousness, malice, envy, murder, strife, deceit, maliciousness, gossip, slander, "
                        "hatred of God, insolence, arrogance, boasting, invention of evil, disobedience to "
                        "parents, foolishness, faithlessness, heartlessness, ruthlessness. The climax: 'they "
                        "not only do them but give approval to those who practice them' (1:32) -- the final "
                        "stage of moral collapse, where evil is celebrated rather than merely tolerated."
            }
        ]
    },

    {
        "id": "rom-gospel-2",
        "ref": "Romans 2:1-3:20",
        "chapter_num": 2,
        "title": "The Impartial Judge -- Jews and Gentiles Under Judgment",
        "era": "rom_gospel",
        "type": "study",

        "synopsis": "Having indicted the Gentile world (1:18-32), Paul turns the indictment on the Jewish "
                    "interlocutor: 'You have no excuse, O man, every one of you who judges. For in passing "
                    "judgment on another you condemn yourself' (2:1). The argument proceeds through Jewish "
                    "privilege (circumcision, Torah, the covenant) and demonstrates that none of these provide "
                    "immunity from judgment. God judges impartially (2:11) -- by deeds, not by ethnic identity. "
                    "The chapter introduces the shocking claim that 'a Jew is one inwardly, and circumcision "
                    "is a matter of the heart' (2:29). Chapter 3 opens with the question 'What advantage has "
                    "the Jew?' (3:1) -- answering 'Much in every way' (3:2) while maintaining that Jewish "
                    "unfaithfulness does not nullify God's faithfulness. The section climaxes with the catena "
                    "of Old Testament quotations in 3:10-18: 'None is righteous, no, not one.' The verdict: "
                    "'the whole world (pas ho kosmos) may be held accountable (hypodikos) to God' (3:19).",

        "key_verse": {
            "ref": "Romans 3:19-20",
            "text": "Now we know that whatever the law says it speaks to those who are under the law, so that every mouth may be stopped, and the whole world may be held accountable to God. For by works of the law no human being will be justified in his sight, since through the law comes knowledge of sin.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "prosopolempsia (partiality/favoritism -- literally 'face-receiving'; 2:11; God shows no favoritism based on ethnic identity)",
            "peritome (circumcision -- the covenant sign of Genesis 17; Paul redefines it as 'of the heart' in 2:29)",
            "nomos (law/Torah -- the Mosaic covenant; possessing it does not guarantee righteousness; it must be DONE)",
            "logia tou theou (the oracles of God -- 3:2; Israel's great privilege: the divine revelation entrusted to them)",
            "pistin tou theou (the faithfulness of God -- 3:3; God's covenant loyalty that is not nullified by human unfaithfulness)",
            "hypodikos (accountable/liable to judgment -- 3:19; a legal term: the whole world stands as a defendant before the divine judge)",
            "ergon nomou (works of the law -- 3:20; deeds performed in obedience to Torah; insufficient for justification)",
            "epignosis hamartias (knowledge of sin -- 3:20; the law's function: not to save but to reveal the depth of the problem)",
            "krima tou theou (the judgment of God -- 2:2; the impartial, righteous verdict that falls on Jew and Gentile alike)",
            "syneidesis (conscience -- 2:15; the moral awareness that functions as an internal law even for those without Torah)"
        ],

        "ane_backdrop": "Paul's argument about God's impartial judgment engages a central tension in Jewish "
                        "theology: if Israel is God's chosen people (Deut 7:6-8), does that election provide "
                        "immunity from judgment? The prophetic tradition consistently answered no: Amos 3:2 "
                        "('You only have I known of all the families of the earth; therefore I will punish "
                        "you for all your iniquities'). The Deuteronomy 32 framework adds cosmic depth: "
                        "Israel's election was YHWH's response to the nations' rebellion -- God kept one "
                        "people for himself (Deut 32:9) while allotting the rest to the sons of God. But "
                        "Israel's failure to be faithful to YHWH (the golden calf, the high places, the "
                        "exile) meant that YHWH's own people were no better than the nations given over to "
                        "other gods. Paul's argument in Romans 2 is essentially the prophetic indictment "
                        "of Israel updated for the first century: covenant privilege without covenant "
                        "obedience brings greater condemnation, not less.",

        "second_temple": [
            {
                "source": "2 Baruch 48:38-40",
                "summary": "Asserts that possession of the Torah provides Israel an advantage at the "
                           "judgment: 'We have nothing now except the Mighty One and his Torah.' But it "
                           "also acknowledges that Torah obedience is the key, not mere possession.",
                "relevance": "Represents the Jewish position Paul engages: Torah possession as covenant "
                             "advantage -- which Paul both affirms (3:2) and qualifies (2:13: 'doers of the "
                             "law will be justified')."
            },
            {
                "source": "Wisdom of Solomon 15:1-5",
                "summary": "Argues that Israel, even if it sins, still 'belongs' to God and will not be "
                           "condemned like the nations, because Israel knows the true God.",
                "relevance": "The exact position Paul challenges in Rom 2:1-5 -- that knowledge of God "
                             "provides immunity from judgment."
            },
            {
                "source": "Qumran Community Rule (1QS 3:13-4:26)",
                "summary": "The Two Spirits doctrine: all humanity is governed by either the Spirit of Truth "
                           "or the Spirit of Falsehood, and their deeds reveal which spirit governs them.",
                "relevance": "Provides Second Temple context for Paul's emphasis on deeds revealing true "
                             "spiritual identity -- the same principle underlying Rom 2:6-10."
            }
        ],

        "cross_refs": [
            {"ref": "Amos 3:2", "note": "'You only have I known... therefore I will punish you' -- election intensifies accountability, exactly Paul's argument in Rom 2", "type": "ot"},
            {"ref": "Deuteronomy 10:16", "note": "'Circumcise therefore the foreskin of your heart' -- the OT precedent for Paul's 'circumcision of the heart' in Rom 2:29", "type": "ot"},
            {"ref": "Jeremiah 4:4", "note": "'Circumcise yourselves to the LORD; remove the foreskin of your hearts' -- Jeremiah's demand anticipated in Rom 2:29", "type": "ot"},
            {"ref": "Psalm 14:1-3", "note": "'There is none who does good, not even one' -- quoted in Rom 3:10-12 as part of the universal indictment", "type": "ot"},
            {"ref": "Psalm 51:4", "note": "'Against you, you only, have I sinned... so that you may be justified in your words' -- quoted in Rom 3:4", "type": "ot"},
            {"ref": "Ecclesiastes 7:20", "note": "'Surely there is not a righteous man on earth who does good and never sins' -- the wisdom tradition behind Rom 3:10", "type": "ot"},
            {"ref": "Isaiah 59:7-8", "note": "'Their feet run to evil... the way of peace they do not know' -- quoted in Rom 3:15-17", "type": "ot"},
            {"ref": "Galatians 2:15-16", "note": "'A person is not justified by works of the law but through faith in Jesus Christ' -- Paul's earlier, more polemical statement of Rom 3:20", "type": "nt"}
        ],

        "divine_council_note": "Romans 2-3 completes the cosmic indictment begun in chapter 1. Having shown "
                               "that the nations under the governance of the sons of God have descended into "
                               "idolatry and wickedness (1:18-32), Paul now demonstrates that Israel -- YHWH's "
                               "own portion (Deut 32:9) -- is no better. The chosen people who were supposed "
                               "to be 'a light to the nations' (Isa 42:6; 49:6) have instead blasphemed God's "
                               "name among the nations (2:24, quoting Isa 52:5). The result is total cosmic "
                               "condemnation: 'the whole world (pas ho kosmos) may be held accountable "
                               "(hypodikos) to God' (3:19). Both the nations under the sons of God AND Israel "
                               "under YHWH have failed. The universal verdict sets the stage for the universal "
                               "solution: the righteousness of God revealed 'apart from the law' (3:21) -- "
                               "a salvation that transcends both the ethnic boundary of Israel and the "
                               "territorial divisions of the sons of God.",

        "sections": [
            {
                "heading": "The Jewish Interlocutor Indicted (2:1-16)",
                "body": "Paul springs the rhetorical trap: 'Therefore you have no excuse, O man, every one "
                        "of you who judges (krinon). For in passing judgment on another you condemn yourself, "
                        "because you, the judge, practice the very same things' (2:1). The Jewish reader who "
                        "nodded along with the Gentile indictment of chapter 1 now finds the finger pointed "
                        "at himself. The theological principle is stated: 'God shows no partiality "
                        "(prosopolempsia)' (2:11). This was revolutionary in its context: the Jew had Torah, "
                        "circumcision, and covenant status. But Paul insists that 'it is not the hearers of "
                        "the law who are righteous before God, but the doers of the law who will be justified' "
                        "(2:13). The stunning claim of 2:14-15 extends the argument: 'when Gentiles, who do "
                        "not have the law, by nature do what the law requires, they are a law to themselves... "
                        "they show that the work of the law is written on their hearts, while their conscience "
                        "(syneidesis) also bears witness.' Gentiles who obey the moral law from the heart are "
                        "in better standing than Jews who possess Torah but disobey it. The criterion is "
                        "consistent: deeds, not identity."
            },
            {
                "heading": "Circumcision of the Heart (2:17-29)",
                "body": "Paul directly addresses the Jew who 'relies on the law and boasts in God' (2:17): "
                        "'You who teach others, do you not teach yourself? You who preach against stealing, "
                        "do you steal?' (2:21). The indictment cuts to the heart of covenant hypocrisy: "
                        "teaching one thing, doing another. The result: 'The name of God is blasphemed among "
                        "the nations (en tois ethnesin) because of you' (2:24, quoting Isa 52:5). Instead "
                        "of being a light to the nations, Israel has caused the nations to blaspheme. Paul "
                        "then radically redefines the covenant markers: 'circumcision indeed is of value if "
                        "you obey the law, but if you break the law, your circumcision becomes uncircumcision' "
                        "(2:25). The covenant sign without covenant obedience is empty. The climax: 'a Jew is "
                        "one inwardly (en to krypto Ioudaios), and circumcision is a matter of the heart "
                        "(peritome kardias), by the Spirit (en pneumati), not by the letter (ou grammati)' "
                        "(2:29). This redefines Israel's identity from ethnic to spiritual -- not abolishing "
                        "the covenant but interiorizing it, fulfilling the promise of Deut 30:6 ('the LORD "
                        "your God will circumcise your heart')."
            },
            {
                "heading": "Universal Guilt -- None Righteous, No, Not One (3:1-20)",
                "body": "The logical question follows: 'Then what advantage has the Jew? Or what is the value "
                        "of circumcision?' (3:1). Paul's answer: 'Much in every way. To begin with, the Jews "
                        "were entrusted with the oracles (logia) of God' (3:2). Israel's privilege is real -- "
                        "they received the divine revelation. But privilege does not guarantee faithfulness: "
                        "'What if some were unfaithful (episteusan)? Does their faithlessness nullify the "
                        "faithfulness of God (pistin tou theou)?' (3:3). 'By no means (me genoito)! Let God "
                        "be true though every one were a liar' (3:4). God's covenant faithfulness stands even "
                        "when Israel fails. The catena of 3:10-18 assembles a devastating chain of Old Testament "
                        "quotations (from Psalms, Ecclesiastes, Isaiah) to establish universal guilt: 'None is "
                        "righteous (dikaios), no, not one; no one understands; no one seeks for God' (3:10-11). "
                        "The verdict: 'so that every mouth may be stopped (phrage), and the whole world (pas "
                        "ho kosmos) may be held accountable (hypodikos) to God. For by works of the law (ex "
                        "ergon nomou) no human being (pasa sarx -- literally 'all flesh') will be justified "
                        "(dikaiothesetai) in his sight' (3:19-20). The law's function is not to save but to "
                        "diagnose: 'through the law comes knowledge (epignosis) of sin.' The cosmic courtroom "
                        "verdict is in: all humanity -- both the nations under the sons of God and Israel "
                        "under YHWH -- stands guilty."
            }
        ]
    },

    {
        "id": "rom-gospel-3",
        "ref": "Romans 3:21-4:25",
        "chapter_num": 3,
        "title": "The Righteousness of God Revealed -- Justification by Faith and Abraham's Example",
        "era": "rom_gospel",
        "type": "study",

        "synopsis": "Having established universal guilt (1:18-3:20), Paul now reveals the solution: 'But now "
                    "(nyni de) the righteousness of God has been manifested apart from the law' (3:21). The "
                    "'but now' marks the cosmic turning point of the letter. Christ is presented as the "
                    "hilasterion -- the mercy seat/propitiation (3:25) -- where God's wrath and mercy meet. "
                    "Justification is by faith 'apart from works of the law' (3:28), available to both Jew "
                    "and Gentile because 'God is one' (3:30). Chapter 4 provides the scriptural proof through "
                    "Abraham, who 'believed God, and it was counted to him as righteousness' (4:3, quoting "
                    "Gen 15:6). Abraham was justified BEFORE circumcision (4:10), making him 'the father of "
                    "all who believe without being circumcised' (4:11) -- the father of believing Gentiles "
                    "as well as believing Jews. Abraham's faith is defined as trusting God to bring life from "
                    "death (4:17-21), which Paul parallels to faith in Christ's resurrection (4:24-25).",

        "key_verse": {
            "ref": "Romans 3:23-26",
            "text": "For all have sinned and fall short of the glory of God, and are justified by his grace as a gift, through the redemption that is in Christ Jesus, whom God put forward as a propitiation by his blood, to be received by faith. This was to show God's righteousness, because in his divine forbearance he had passed over former sins. It was to show his righteousness at the present time, so that he might be just and the justifier of the one who has faith in Jesus.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "nyni de (but now -- the cosmic turning point; the transition from universal condemnation to universal offer of grace)",
            "dikaioumenoi (being justified -- present passive: justification as God's ongoing act of declaring righteous, not human achievement)",
            "dorean (freely/as a gift -- justification is gratis, without cost to the recipient; the same word used for 'for nothing' in secular Greek)",
            "apolytrosis (redemption -- the price paid to liberate a slave or prisoner; Christ's death as the ransom that frees humanity from sin's slavery)",
            "hilasterion (propitiation/mercy seat -- the kapporet of Yom Kippur; Christ as the place where God's wrath is satisfied and mercy is dispensed)",
            "paresis (passing over -- 3:25; God's temporary overlooking of sins in the OT era, now addressed definitively in Christ's death)",
            "logizomai (to reckon/count/credit -- 4:3; the accounting metaphor: faith is 'credited' to the believer's account as righteousness)",
            "adikos (ungodly -- 4:5; God 'justifies the ungodly'; the scandalous claim that God declares the unrighteous righteous through faith)",
            "kleronomos kosmou (heir of the world -- 4:13; Abraham's inheritance is not just Canaan but the entire cosmos; the Abrahamic promise in cosmic scope)",
            "eis to einai auton patera (so that he might be the father -- 4:11; Abraham's identity as patriarch of all believers, Jew and Gentile)"
        ],

        "ane_backdrop": "The hilasterion of 3:25 is the most concentrated atonement theology in the New "
                        "Testament. The word hilasterion is used in the LXX 22 times, 21 of which refer to "
                        "the kapporet -- the gold-covered lid of the Ark of the Covenant (Exod 25:17-22). "
                        "On the Day of Atonement (Lev 16), the high priest sprinkled sacrificial blood on "
                        "the kapporet seven times to atone for Israel's sins. The kapporet was the most "
                        "sacred object in Israel's worship -- the place where YHWH's presence dwelt between "
                        "the cherubim, where judgment and mercy intersected. By identifying Christ as the "
                        "hilasterion, Paul makes a staggering claim: the crucified Messiah is the new mercy "
                        "seat. The blood sprinkled on the old kapporet was animal blood; the blood of the "
                        "new hilasterion is Christ's own. The old kapporet was hidden behind the veil, "
                        "accessible only to the high priest once a year; the new hilasterion is 'put forward "
                        "publicly' (proetheto) -- open, visible, available to all who have faith. The "
                        "Abraham argument draws on the Genesis narrative and its Second Temple interpretation. "
                        "In Jewish tradition (Sirach 44:19-21; 1 Maccabees 2:52; Jubilees 23:10), Abraham's "
                        "righteousness was understood as the RESULT of his faithful obedience -- he was tested "
                        "and found faithful. Paul inverts this: Abraham's righteousness was CREDITED through "
                        "faith (Gen 15:6), BEFORE circumcision (Gen 17) and BEFORE the binding of Isaac "
                        "(Gen 22). Faith precedes works.",

        "second_temple": [
            {
                "source": "4QMMT (4Q394-399, Qumran)",
                "summary": "The halakhic letter from Qumran uses the phrase 'reckoned as righteousness' "
                           "(Gen 15:6 language) in the context of obedience to the 'works of the law' "
                           "(ma'asei ha-torah) -- the exact phrase Paul argues against in Rom 3:20, 28.",
                "relevance": "Provides the earliest Jewish usage of 'works of the law' (erga nomou) as a "
                             "technical phrase -- the same phrase Paul declares insufficient for justification."
            },
            {
                "source": "Sirach 44:19-21",
                "summary": "Praises Abraham: 'He kept the law of the Most High, and entered into a covenant "
                           "with him... when he was tested he proved faithful. Therefore the Lord assured him "
                           "with an oath that the nations would be blessed through his offspring.'",
                "relevance": "Represents the standard Second Temple Jewish view: Abraham was righteous because "
                             "he was obedient. Paul challenges this by insisting that righteousness was "
                             "credited BEFORE obedience (Gen 15:6 before Gen 17 and Gen 22)."
            },
            {
                "source": "1 Maccabees 2:52",
                "summary": "'Was not Abraham found faithful when tested, and it was reckoned to him as "
                           "righteousness?' -- combining Gen 15:6 (reckoning) with Gen 22 (testing).",
                "relevance": "Shows the standard Jewish conflation of Gen 15:6 and Gen 22 that Paul works to "
                             "separate: faith-reckoning (Gen 15) chronologically precedes the test (Gen 22)."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 15:6", "note": "'And he believed the LORD, and he counted it to him as righteousness' -- the foundational proof-text for justification by faith, quoted in Rom 4:3", "type": "ot"},
            {"ref": "Leviticus 16:2, 13-15", "note": "The Day of Atonement ritual: blood sprinkled on the kapporet (mercy seat) -- the OT background to Christ as hilasterion in Rom 3:25", "type": "ot"},
            {"ref": "Psalm 32:1-2", "note": "'Blessed is the one whose transgression is forgiven, whose sin is covered' -- David's testimony of imputed righteousness, quoted in Rom 4:7-8", "type": "ot"},
            {"ref": "Galatians 3:6-9", "note": "Paul's earlier Abraham argument: 'Abraham believed God, and it was counted to him as righteousness' -- the Galatians version of Rom 4", "type": "nt"},
            {"ref": "Hebrews 9:5", "note": "'The cherubim of glory overshadowing the mercy seat (hilasterion)' -- the only other NT use of hilasterion, confirming its kapporet meaning", "type": "nt"},
            {"ref": "James 2:21-24", "note": "'Was not Abraham our father justified by works when he offered up his son Isaac?' -- James's complementary perspective: faith is validated by works", "type": "nt"},
            {"ref": "Genesis 17:1-14", "note": "The institution of circumcision -- AFTER the faith-reckoning of Gen 15:6, as Paul argues in Rom 4:10-12", "type": "ot"}
        ],

        "divine_council_note": "The 'but now' (nyni de) of Romans 3:21 is the cosmic turning point of the "
                               "divine council drama. The universal condemnation of 1:18-3:20 described the "
                               "situation after Babel: the nations given over to the sons of God, Israel "
                               "unable to fulfill its covenant role. The 'but now' introduces God's direct "
                               "intervention: 'the righteousness of God has been manifested apart from the "
                               "law' (3:21) -- a righteousness that transcends both the ethnic boundaries of "
                               "Israel and the territorial divisions of the sons of God. Christ as the "
                               "hilasterion (3:25) is the new cosmic center of atonement -- no longer "
                               "localized in Jerusalem's Temple, no longer restricted to Israel's high priest, "
                               "but universally accessible by faith. The monotheistic claim of 3:29-30 -- "
                               "'since God is one' (heis ho theos), he justifies both circumcised and "
                               "uncircumcised by faith -- is the divine council foundation of universal "
                               "salvation. There is one God over all the council, and he is reclaiming all "
                               "the nations through one Messiah. Abraham as 'the father of all who believe' "
                               "(4:11) -- both uncircumcised Gentiles and circumcised Jews -- is the patriarchal "
                               "ground for the reunification of humanity under YHWH. The promise to Abraham "
                               "was that he would be 'heir of the world' (kleronomos kosmou, 4:13) -- not "
                               "just Canaan but the entire cosmos. This cosmic inheritance is received through "
                               "faith, not law, making it accessible to all nations.",

        "sections": [
            {
                "heading": "But Now -- The Righteousness of God Apart from Law (3:21-31)",
                "body": "The two most important words in Romans may be 'But now' (nyni de, 3:21). After the "
                        "devastating indictment of 1:18-3:20, the sentence changes: 'But now the righteousness "
                        "of God has been manifested apart from the law (choris nomou), although the Law and the "
                        "Prophets bear witness to it -- the righteousness of God through faith in Jesus Christ "
                        "(dia pisteos Iesou Christou) for all who believe' (3:21-22). The phrase 'dia pisteos "
                        "Iesou Christou' is debated: does it mean 'through faith IN Jesus Christ' (objective "
                        "genitive -- the standard Protestant reading) or 'through the faith/faithfulness OF "
                        "Jesus Christ' (subjective genitive -- emphasizing Christ's own faithfulness to God's "
                        "plan)? Both are grammatically possible, and both are theologically true. The universal "
                        "problem receives the universal solution: 'for all have sinned (pantes hemarton) and "
                        "fall short (hysterountai) of the glory (doxes) of God' (3:23). The 'glory' from which "
                        "humanity falls short is the divine glory -- the kavod that was shared with humanity in "
                        "Eden (Ps 8:5) and lost in the Fall. Justification is described as 'by his grace as "
                        "a gift (dorean), through the redemption (apolytrosis) that is in Christ Jesus' (3:24). "
                        "Three metaphors converge: legal (justification -- the judge's verdict), commercial "
                        "(redemption -- the slave's ransom), and cultic (propitiation -- the sacrifice's "
                        "atonement). Christ as hilasterion (3:25) is the cosmic mercy seat -- the place where "
                        "God's justice and mercy converge. God is simultaneously 'just' (dikaion -- his justice "
                        "is satisfied) 'and the justifier' (dikaiounta -- he declares the believing sinner "
                        "righteous). The conclusion: 'we hold that one is justified by faith apart from works "
                        "of the law' (3:28)."
            },
            {
                "heading": "Abraham -- Father of All Who Believe (4:1-25)",
                "body": "Paul turns to the scriptural proof: Abraham, the patriarch revered by all Jews. The "
                        "key text is Genesis 15:6: 'Abraham believed (episteusen) God, and it was counted "
                        "(elogisthe) to him as righteousness (dikaiosynen)' (4:3). Paul's exegetical move is "
                        "chronological: this faith-reckoning occurred in Genesis 15, BEFORE circumcision was "
                        "instituted in Genesis 17. Therefore, Abraham was justified while still uncircumcised "
                        "(4:10). Circumcision was 'a seal (sphragida) of the righteousness that he had by "
                        "faith while he was still uncircumcised' (4:11) -- a confirmation of what faith had "
                        "already accomplished, not its cause. This makes Abraham 'the father of all who "
                        "believe without being circumcised' (4:11) -- the patriarch of believing Gentiles. He "
                        "is also 'the father of the circumcised who... walk in the footsteps of the faith "
                        "that our father Abraham had before he was circumcised' (4:12) -- the patriarch of "
                        "believing Jews. Abraham's faith is then defined in cosmic terms: he believed in 'the "
                        "God who gives life to the dead (zoopoiountos tous nekrous) and calls into existence "
                        "the things that do not exist (kalountos ta me onta hos onta)' (4:17). Abraham trusted "
                        "the God who creates ex nihilo and raises the dead -- the same God who raised Jesus "
                        "from the dead (4:24). The chapter closes with the parallel: just as Abraham's faith "
                        "was credited as righteousness, so will ours be -- for we believe in 'him who raised "
                        "from the dead Jesus our Lord, who was delivered up (paredothe) for our trespasses and "
                        "raised for our justification (dikaiosin)' (4:24-25). The verb paredothe ('was handed "
                        "over') is the same root as paredoken ('gave over') in 1:24, 26, 28 -- the nations "
                        "were 'given over' to judgment; Christ was 'given over' to death for their salvation. "
                        "The verb of condemnation becomes the verb of redemption."
            }
        ]
    },

    {
        "id": "rom-gospel-4",
        "ref": "Romans 5:1-21",
        "chapter_num": 4,
        "title": "Peace with God and the Adam-Christ Typology -- One Man's Obedience",
        "era": "rom_gospel",
        "type": "study",

        "synopsis": "Chapter 5 is the theological bridge between justification (chapters 1-4) and "
                    "sanctification (chapters 6-8). In 5:1-11, Paul describes the present blessings of "
                    "justification: peace with God, access to grace, hope of glory, and the love of God "
                    "poured into hearts by the Holy Spirit. In 5:12-21, Paul introduces the Adam-Christ "
                    "typology -- the most sweeping framework for understanding salvation in the entire "
                    "letter. Through one man (Adam) sin entered the world, and death through sin, and so "
                    "death spread to all (5:12). Through one man (Christ) the free gift of righteousness "
                    "leads to justification and life for all (5:18). 'As by the one man's disobedience "
                    "the many were made sinners, so by the one man's obedience the many will be made "
                    "righteous' (5:19). The cosmic scope is breathtaking: the entire human story -- from "
                    "Adam to the eschaton -- is determined by two representative acts.",

        "key_verse": {
            "ref": "Romans 5:18-19",
            "text": "Therefore, as one trespass led to condemnation for all men, so one act of righteousness leads to justification and life for all men. For as by the one man's disobedience the many were made sinners, so by the one man's obedience the many will be made righteous.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "eirene (peace -- 5:1; not merely absence of conflict but the positive state of restored relationship with God; the shalom of the covenant)",
            "prosagoge (access -- 5:2; the right to enter the king's presence; a court term for introduction to royalty; believers have permanent access to grace)",
            "kauchaomai (to boast/exult -- 5:2, 3, 11; not proud arrogance but confident, joyful celebration of God's work)",
            "thlipsis (tribulation/affliction -- 5:3; suffering that produces endurance, character, and hope; the refining process)",
            "agape (love -- 5:5, 8; God's love poured out through the Spirit; demonstrated in Christ dying for the ungodly)",
            "typos (type/pattern -- 5:14; Adam as a type (prefigurement) of Christ; the first man points forward to the last man)",
            "paraptoma (trespass/transgression -- 5:15-20; a 'falling beside,' a deviation from the path; Adam's sin that brought death to all)",
            "charisma (free gift/grace-gift -- 5:15-16; the gift that overflows from the one man Jesus Christ; grace that exceeds the trespass)",
            "kathistemi (to appoint/constitute -- 5:19; 'the many were made sinners' and 'will be made righteous'; constituted in a new status through representative action)",
            "hyperperisseuo (to super-abound -- 5:20; 'where sin increased, grace abounded all the more'; grace not merely matching sin but exceeding it immeasurably)"
        ],

        "ane_backdrop": "The Adam-Christ typology (5:12-21) engages the ancient Near Eastern concept of "
                        "corporate representation -- the king or progenitor whose actions determine the "
                        "fate of his people. In Mesopotamian royal ideology, the king's righteousness "
                        "brought prosperity to the land, and the king's sin brought divine punishment on "
                        "the nation. The same principle operates in Israel's history: Adam's sin brings "
                        "death to all his descendants, and the Davidic king's actions affect the entire "
                        "nation (cf. 2 Sam 24, where David's census brings plague on Israel). Paul's "
                        "innovation is to apply this representative principle cosmically: Adam represents "
                        "ALL humanity in his disobedience, and Christ represents ALL humanity in his "
                        "obedience. The language of 'reign' (basileuein) in 5:14, 17, 21 connects to the "
                        "divine council framework: death 'reigned' (ebasileusen) from Adam to Moses (5:14), "
                        "implying that death functions as a cosmic ruler -- a power that has seized control "
                        "of humanity. Grace 'reigns' (basileuse) through righteousness (5:21), establishing "
                        "a rival kingship that displaces death's dominion.",

        "second_temple": [
            {
                "source": "4 Ezra 3:7, 21-22; 7:116-118",
                "summary": "The author of 4 Ezra laments: 'O Adam, what have you done? For though it was "
                           "you who sinned, the fall was not yours alone, but ours also who are your "
                           "descendants.' The idea of Adamic solidarity -- all humanity sharing in Adam's "
                           "consequences -- is a prominent Second Temple Jewish concern.",
                "relevance": "Provides direct Jewish precedent for Paul's Adam theology in Rom 5:12-21 -- "
                             "the entire human race affected by Adam's sin."
            },
            {
                "source": "2 Baruch 54:15, 19",
                "summary": "'Adam is therefore not the cause, save only of his own soul, but each of us "
                           "has been the Adam of his own soul.' While affirming Adamic influence, 2 Baruch "
                           "emphasizes individual responsibility.",
                "relevance": "Shows the diversity of Second Temple views on Adam's sin: Paul's position "
                             "(corporate solidarity) was one view among several. The tension between "
                             "corporate and individual responsibility continues in Rom 5-8."
            },
            {
                "source": "1 Corinthians 15:21-22, 45-49",
                "summary": "Paul's earlier Adam-Christ typology: 'For as in Adam all die, so also in Christ "
                           "shall all be made alive... The first man Adam became a living being; the last "
                           "Adam became a life-giving spirit.'",
                "relevance": "The 1 Cor 15 Adam-Christ typology focuses on resurrection (death/life); "
                             "the Rom 5 version focuses on justification (condemnation/righteousness). "
                             "Together they present the complete picture."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 3:1-19", "note": "The Fall -- Adam's disobedience that brought sin and death into the world, the event Paul traces the human predicament to in Rom 5:12", "type": "ot"},
            {"ref": "1 Corinthians 15:21-22, 45-49", "note": "Paul's earlier Adam-Christ typology focused on resurrection: 'as in Adam all die, so also in Christ shall all be made alive'", "type": "nt"},
            {"ref": "Genesis 3:15", "note": "The protoevangelium: 'he shall bruise your head' -- the seed of the woman who will undo the serpent's work, fulfilled in the 'one man's obedience' of Rom 5:19", "type": "ot"},
            {"ref": "Isaiah 53:11", "note": "'By his knowledge shall the righteous one, my servant, make many to be accounted righteous' -- the Servant's representative righteousness, paralleling Rom 5:19", "type": "ot"},
            {"ref": "Philippians 2:8", "note": "'He humbled himself by becoming obedient to the point of death, even death on a cross' -- Christ's obedience that reverses Adam's disobedience", "type": "nt"},
            {"ref": "Romans 8:1", "note": "'There is therefore now no condemnation for those who are in Christ Jesus' -- the consequence of the justification established in Rom 5", "type": "nt"}
        ],

        "divine_council_note": "Romans 5:12-21 provides the cosmic anthropology that undergirds the divine "
                               "council worldview. Adam's sin introduced not just personal guilt but cosmic "
                               "disorder: 'sin came into the world (kosmos) through one man, and death "
                               "(thanatos) through sin, and so death spread to all men' (5:12). Death is "
                               "not merely biological cessation but a cosmic power that 'reigned' (ebasileusen, "
                               "5:14, 17) over humanity -- death as a king, a ruler, a usurping authority. "
                               "In the divine council framework, death's reign is the consequence of the "
                               "cosmic rebellion: the serpent/nachash of Eden (a divine council member, Ezek "
                               "28:12-17) introduced death through deception, and death became the archon's "
                               "tool of governance. Paul's Adam-Christ typology is cosmic reversal: where "
                               "Adam's disobedience allowed death to reign, Christ's obedience allows grace "
                               "to reign 'through righteousness leading to eternal life' (5:21). The 'many' "
                               "who are 'made righteous' (5:19) are the new humanity -- the people being "
                               "reclaimed from the old Adam's domain, transferred from death's kingdom to "
                               "grace's kingdom. The 'much more' (pollo mallon) language of 5:15, 17 "
                               "emphasizes that grace does not merely reverse the damage but exceeds it: "
                               "'where sin increased, grace abounded all the more (hyperperisseusen)' (5:20). "
                               "The cosmic accounting is not balanced but tipped decisively toward grace.",

        "sections": [
            {
                "heading": "Peace, Access, and the Love of God (5:1-11)",
                "body": "The blessings of justification are enumerated: 'Therefore, since we have been "
                        "justified by faith, we have peace (eirenen) with God through our Lord Jesus Christ' "
                        "(5:1). The eirene is not subjective feeling but objective reality -- the state of "
                        "war between sinful humanity and the holy God has ended. 'Through him we have also "
                        "obtained access (prosagogen) by faith into this grace in which we stand' (5:2a). "
                        "The prosagoge is a court term: introduction into the king's presence. Believers have "
                        "permanent standing in grace -- not visiting but dwelling. 'And we rejoice (kauchometha) "
                        "in hope of the glory (doxes) of God' (5:2b) -- the glory lost in Adam's fall will be "
                        "restored. Paul then traces the refining process: 'tribulation produces endurance, and "
                        "endurance produces character (dokimen -- 'tested-ness, proven quality'), and character "
                        "produces hope, and hope does not put us to shame, because God's love (agape tou theou) "
                        "has been poured out (ekkechytai) into our hearts through the Holy Spirit who has been "
                        "given to us' (5:3-5). The Spirit is the means of experiential certainty: God's love "
                        "is not abstract doctrine but felt reality. The demonstration of that love: 'while we "
                        "were still weak, at the right time Christ died for the ungodly (aseboon)' (5:6). The "
                        "asebeis -- the same word used for the ungodliness of 1:18 -- are the objects of "
                        "Christ's death. 'God shows his love for us in that while we were still sinners, "
                        "Christ died for us' (5:8). The cross is the ultimate demonstration of divine love."
            },
            {
                "heading": "Adam and Christ -- The Two Representatives (5:12-21)",
                "body": "The theological climax of the first half of Romans: 'Therefore, just as sin came "
                        "into the world through one man (di henos anthropou), and death through sin, and so "
                        "death spread (dielthon) to all men because all sinned (eph ho pantes hemarton)' "
                        "(5:12). The phrase 'eph ho pantes hemarton' is one of the most debated in the NT. "
                        "Three main readings: (1) 'because all sinned' -- all humans participate individually "
                        "in Adam's sin pattern (Eastern Orthodox emphasis). (2) 'in whom all sinned' -- all "
                        "humanity was seminally present in Adam (Augustine's reading, following the Latin "
                        "translation). (3) 'with the result that all sinned' -- Adam's sin created the "
                        "condition of universal sinfulness. All three contain truth. Paul draws the parallel: "
                        "Adam is a 'type (typos) of the one who was to come' (5:14) -- a prefigurement of "
                        "Christ. But the parallel is asymmetric: 'the free gift is not like the trespass' "
                        "(5:15). The grace is greater: 'if many died through one man's trespass, much more "
                        "(pollo mallon) have the grace of God and the free gift by the grace of that one "
                        "man Jesus Christ abounded (eperisseusen) for many' (5:15). The contrast is "
                        "developed: the trespass brought condemnation (katakrima), the gift brings "
                        "justification (dikaioma, 5:16). Death reigned through Adam; 'those who receive the "
                        "abundance of grace and the free gift of righteousness' will 'reign in life through "
                        "the one man Jesus Christ' (5:17). The summary: 'as one trespass led to condemnation "
                        "for all men, so one act of righteousness (hen dikaioma) leads to justification and "
                        "life for all men (eis pantas anthropous)' (5:18). The 'one act of righteousness' "
                        "is Christ's entire life of obedience culminating in the cross. The chapter ends with "
                        "the famous dictum: 'where sin increased (epleonasen), grace abounded all the more "
                        "(hyperperisseusen)' (5:20) -- grace does not merely match sin but overwhelms it. "
                        "'So that, as sin reigned (ebasileusen) in death, grace also might reign "
                        "(basileuse) through righteousness leading to eternal life through Jesus Christ our "
                        "Lord' (5:21). Two kingdoms, two reigns, two destinies: death through Adam, life "
                        "through Christ."
            }
        ]
    }
]
