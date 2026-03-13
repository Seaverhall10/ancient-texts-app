"""
era_church_reformation.py -- The Reformation & Its Legacy (Chapters 13-15)

The sixteenth century tore Western Christendom apart -- and in tearing it, exposed
what had been buried for a millennium. Martin Luther's hammer on the Wittenberg
door was not the beginning of the Reformation; it was the moment a fracture that
had been growing for centuries finally broke through the surface. What followed
was a theological earthquake: five Solas, a counter-council at Trent, wars of
religion, and the Bible -- at last -- in the hands of common people.

This era covers:
  13. Luther, Calvin & the 95 Theses -- Sola Scriptura Returns
  14. The Counter-Reformation -- Rome Responds
  15. The Legacy -- Why It Still Matters

Methodology:
  - Evidence tiers throughout: [A] Direct Scripture, [B] Valid inference,
    [C] Historical parallel.
  - ESV baseline for all Scripture quotations.
  - Historical claims sourced from primary Reformation documents, conciliar
    decrees, and standard Reformation historiography.
  - Theological analysis is firm but fair: Rome's errors are named, but so
    are the Reformers'. Truth is the standard, not tribal loyalty.
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 13: LUTHER, CALVIN & THE 95 THESES
    # =========================================================================
    {
        "id": "church-luther-95-theses",
        "ref": "Romans 3:28",
        "chapter_num": 13,
        "title": "Luther, Calvin & the 95 Theses \u2014 Sola Scriptura Returns",
        "era": "church_reformation",
        "type": "chapter",

        "synopsis": "On October 31, 1517, an Augustinian monk named Martin Luther "
                    "nailed ninety-five propositions to the door of the Castle Church "
                    "in Wittenberg, Saxony. The immediate target was the sale of "
                    "indulgences -- the practice of purchasing reduction of time in "
                    "purgatory for oneself or the dead. But behind the indulgence "
                    "controversy lay a deeper question: by what authority does the "
                    "church define salvation? Luther's answer, forged through years "
                    "of agonized study of Paul's epistles, would shatter the medieval "
                    "consensus and reshape the Western world. Justification is by "
                    "grace alone, through faith alone, in Christ alone, as revealed "
                    "in Scripture alone, to the glory of God alone. Five propositions "
                    "-- five Solas -- against fifteen centuries of accumulated "
                    "tradition. The Reformation had begun.",

        "key_verse": {
            "ref": "Romans 3:28",
            "text": "For we hold that one is justified by faith apart from works "
                    "of the law.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u03c0\u03af\u03c3\u03c4\u03b9\u03c2 (pistis)",
                "meaning": "Faith, faithfulness, trust, conviction. The Greek noun "
                           "at the center of the Reformation debate. Paul uses pistis "
                           "to describe the instrument by which sinners receive the "
                           "righteousness of God. Luther read Romans 1:17 -- 'the "
                           "righteous shall live by faith' -- and understood that "
                           "pistis is not a human achievement but a receiving hand. "
                           "Faith does not earn justification; it receives the gift "
                           "that Christ's death purchased."
            },
            {
                "term": "\u03b4\u03b9\u03ba\u03b1\u03b9\u03bf\u03c3\u03cd\u03bd\u03b7 (dikaiosyne)",
                "meaning": "Righteousness, justice, right standing. The 'righteousness "
                           "of God' (dikaiosyne theou) in Romans 1:17 and 3:21 is not "
                           "God's demand that terrified Luther -- it is God's gift. The "
                           "righteousness by which sinners are declared just is Christ's "
                           "own righteousness, imputed (credited) to the believer. This "
                           "is the doctrine of imputation: an alien righteousness, not "
                           "our own, received through faith."
            },
            {
                "term": "\u03c7\u03ac\u03c1\u03b9\u03c2 (charis)",
                "meaning": "Grace, unmerited favor, gift. 'For by grace you have been "
                           "saved through faith. And this is not your own doing; it is "
                           "the gift of God' (Ephesians 2:8). Charis is the foundation "
                           "of sola gratia -- salvation originates entirely in God's "
                           "free decision to show mercy, not in any human merit, ritual "
                           "performance, or purchased indulgence."
            },
            {
                "term": "\u1f14\u03c1\u03b3\u03bf\u03bd (ergon)",
                "meaning": "Work, deed, action. Romans 3:28 declares justification "
                           "'apart from works (ergon) of the law.' The Reformers "
                           "insisted that works are the fruit and evidence of genuine "
                           "faith, not the ground of justification. Even James 2:17 "
                           "-- 'faith without works is dead' -- describes works as "
                           "the demonstration of living faith, not the cause of "
                           "right standing before God."
            },
            {
                "term": "sola (Latin: alone)",
                "meaning": "Not a Greek or Hebrew term, but the Latin word that became "
                           "the signature vocabulary of the Reformation. Sola Scriptura "
                           "(Scripture alone as final authority), Sola Fide (faith alone "
                           "as instrument), Sola Gratia (grace alone as source), Solus "
                           "Christus (Christ alone as mediator), Soli Deo Gloria (to "
                           "God alone the glory). Five words that summarize the "
                           "Reformation's recovery of the Pauline gospel."
            }
        ],

        "ane_backdrop": "The medieval indulgence system that provoked Luther's protest "
                        "was rooted in a penitential theology that had developed over "
                        "centuries. The 'treasury of merit' doctrine held that the "
                        "superabundant merits of Christ, Mary, and the saints formed "
                        "a spiritual bank from which the pope could make withdrawals "
                        "on behalf of sinners. Johann Tetzel, the Dominican friar "
                        "whose indulgence sales triggered Luther's protest, reportedly "
                        "preached: 'As soon as the coin in the coffer rings, the soul "
                        "from purgatory springs.' This was not official doctrine, but "
                        "it was the practical reality. The theological infrastructure "
                        "assumed a works-based economy of salvation: sin created debt, "
                        "penance reduced debt, indulgences paid it off faster, and the "
                        "church administered the entire system. Luther's breakthrough "
                        "was recognizing that Paul's gospel operates on an entirely "
                        "different economy -- not debt and payment, but death and "
                        "resurrection, guilt and acquittal, wrath and grace.",

        "second_temple": [
            {
                "source": "Paul's Epistle to the Romans (c. AD 57)",
                "summary": "Romans 1-4 constitutes the most systematic treatment "
                           "of justification by faith in the New Testament. Paul "
                           "argues that all humanity -- Jew and Gentile alike -- "
                           "stands guilty before God (1:18-3:20), that righteousness "
                           "comes through faith in Christ apart from works of the "
                           "law (3:21-31), and that Abraham himself was justified by "
                           "faith, not works (chapter 4). This argument was written "
                           "1,460 years before Luther rediscovered it.",
                "relevance": "The Reformation was, at its core, a recovery of Paul. "
                             "Luther did not invent sola fide; he read it in Romans "
                             "and Galatians and recognized that the medieval church "
                             "had buried it under layers of institutional theology. "
                             "[A] Direct Scripture -- Romans 3:28 is explicit."
            },
            {
                "source": "Augustine of Hippo, On the Spirit and the Letter (AD 412)",
                "summary": "Augustine argued against Pelagianism that salvation is "
                           "entirely by God's grace, that human nature is fallen and "
                           "incapable of self-rescue, and that faith itself is a "
                           "gift of God. Luther was an Augustinian monk, and his "
                           "theology of grace drew heavily on Augustine's anti-"
                           "Pelagian writings.",
                "relevance": "The irony: Rome claimed Augustine as a church father, "
                             "but Luther followed Augustine's soteriology more "
                             "consistently than the medieval church did. The "
                             "Reformation was partly an Augustinian revival. [C] "
                             "Historical parallel."
            }
        ],

        "cross_refs": [
            {"ref": "Romans 1:17", "note": "'The righteous shall live by faith' -- the verse that broke Luther open. He had read it as God's terrifying demand for righteousness; he came to see it as God's gracious gift of righteousness received by faith", "type": "nt"},
            {"ref": "Romans 3:21-26", "note": "'The righteousness of God has been manifested apart from the law... through faith in Jesus Christ for all who believe' -- the theological engine of the Reformation", "type": "nt"},
            {"ref": "Ephesians 2:8-9", "note": "'For by grace you have been saved through faith. And this is not your own doing; it is the gift of God, not a result of works' -- the Pauline formula", "type": "nt"},
            {"ref": "Galatians 2:16", "note": "'A person is not justified by works of the law but through faith in Jesus Christ' -- Paul's confrontation with Peter prefigures Luther's confrontation with Rome", "type": "nt"},
            {"ref": "James 2:17", "note": "'Faith by itself, if it does not have works, is dead' -- not a contradiction of Paul but a complement: genuine faith produces works as evidence, not as cause of justification", "type": "nt"},
            {"ref": "Habakkuk 2:4", "note": "'The righteous shall live by his faith' -- the OT source text Paul quotes in Romans 1:17, the verse behind the entire Reformation breakthrough", "type": "ot"},
            {"ref": "Psalm 130:3-4", "note": "'If you, O LORD, should mark iniquities, O Lord, who could stand? But with you there is forgiveness' -- the cry of the penitent that indulgences could never satisfy", "type": "ot"}
        ],

        "divine_council_note": "The Reformation recovered the authority of Scripture over "
                               "human traditions -- a critical step. But the Reformers "
                               "inherited the same Augustinian cosmology that had dominated "
                               "Western theology since the fifth century. Augustine's "
                               "framework minimized the role of the divine council and the "
                               "territorial spiritual powers described in Deuteronomy 32:8-9 "
                               "and Daniel 10. Luther took spiritual warfare seriously -- he "
                               "famously threw an inkwell at the devil -- but he did not "
                               "recover the full divine council worldview. The cosmic scope "
                               "of the principalities and powers (Ephesians 6:12) was "
                               "acknowledged but not systematically integrated into Reformed "
                               "theology. This is not a criticism of the Reformers; they "
                               "did not have access to the Dead Sea Scrolls (discovered "
                               "1947) or Ugaritic texts (deciphered 1930s) that illuminate "
                               "the divine council background of Scripture. They recovered "
                               "soteriology. The full cosmic picture awaited later tools.",

        "sections": [
            {
                "heading": "The Tower Experience \u2014 Romans 1:17 Breaks Through",
                "body": "Before the 95 Theses, before the public confrontation, there "
                        "was a private crisis. Martin Luther, an Augustinian monk and "
                        "professor of theology at the University of Wittenberg, was "
                        "tormented by Romans 1:17: 'For in it the righteousness of "
                        "God is revealed from faith for faith, as it is written, \"The "
                        "righteous shall live by faith.\"' Luther hated the phrase "
                        "'righteousness of God.' He understood it as God's active, "
                        "punishing righteousness -- the standard by which sinners are "
                        "condemned. As a monk, he confessed for hours, fasted until "
                        "he collapsed, and still could not find peace. The medieval "
                        "system told him to try harder: more penance, more confession, "
                        "more merit. It was never enough. Then, studying in his tower "
                        "room (the Turmerlebnis, 'tower experience'), the text broke "
                        "open. The 'righteousness of God' in Romans 1:17 is not the "
                        "righteousness God demands from sinners but the righteousness "
                        "God gives to sinners through faith. It is a gift, not a "
                        "requirement. Luther later wrote: 'I felt that I was altogether "
                        "born again and had entered paradise itself through open gates.' "
                        "[A] Romans 1:17 and 3:21-26 are direct, explicit Scripture "
                        "on this point. The Reformation began not with a political act "
                        "but with a theological discovery: God justifies the ungodly "
                        "(Romans 4:5) by crediting them with Christ's righteousness "
                        "through faith."
            },
            {
                "heading": "October 31, 1517 \u2014 The 95 Theses and the Indulgence Crisis",
                "body": "The immediate catalyst was Johann Tetzel, a Dominican friar "
                        "selling indulgences to fund the construction of St. Peter's "
                        "Basilica in Rome. The theology behind indulgences was built "
                        "on the 'treasury of merit' concept: the superabundant merits "
                        "of Christ and the saints, administered by the pope, could be "
                        "applied to reduce temporal punishment for sin -- even for the "
                        "dead in purgatory. Luther's 95 Theses did not initially reject "
                        "indulgences outright; they challenged the abuses and asked "
                        "hard questions. Thesis 1: 'When our Lord and Master Jesus "
                        "Christ said \"Repent,\" He willed the entire life of believers "
                        "to be one of repentance.' Thesis 36: 'Every truly repentant "
                        "Christian has a right to full remission of penalty and guilt, "
                        "even without letters of pardon.' Thesis 62: 'The true treasure "
                        "of the church is the most holy gospel of the glory and the "
                        "grace of God.' Luther was not yet a Protestant. He was a "
                        "Catholic priest asking his own church to be honest about the "
                        "gospel. But the printing press -- Gutenberg's invention from "
                        "the 1440s -- turned a local academic dispute into an "
                        "international firestorm. Within two weeks, the 95 Theses had "
                        "spread across Germany. Within a month, across Europe. The "
                        "technology that would define the modern world delivered "
                        "its first viral document. [C] Historical parallel -- the "
                        "press did for the Reformation what the Roman road system "
                        "did for the early church: infrastructure serving gospel "
                        "proclamation."
            },
            {
                "heading": "The Diet of Worms \u2014 'Here I Stand'",
                "body": "By 1521, Luther had been excommunicated by Pope Leo X (the "
                        "bull Exsurge Domine, June 1520) and summoned before Emperor "
                        "Charles V at the Diet of Worms. The question was simple: "
                        "would Luther recant his writings? His answer, delivered on "
                        "April 18, 1521, defined the Reformation's stance toward "
                        "authority: 'Unless I am convinced by the testimony of the "
                        "Scriptures or by clear reason, I am bound by the Scriptures "
                        "I have quoted, and my conscience is captive to the Word of "
                        "God. I cannot and will not recant anything, since it is "
                        "neither safe nor right to go against conscience. Here I "
                        "stand. I can do no other. God help me.' Whether Luther "
                        "spoke exactly those words is debated by historians, but "
                        "the substance is confirmed by multiple contemporary "
                        "accounts. The principle is unmistakable: Scripture stands "
                        "above popes, councils, emperors, and tradition. This is "
                        "sola Scriptura -- not 'Scripture only' in the sense of "
                        "ignoring all other sources, but Scripture as the final, "
                        "supreme authority to which all other authorities must "
                        "submit. [B] Valid inference from 2 Timothy 3:16-17 -- "
                        "'All Scripture is breathed out by God and profitable for "
                        "teaching, for reproof, for correction, and for training "
                        "in righteousness, that the man of God may be complete, "
                        "equipped for every good work.' If Scripture equips the "
                        "believer for 'every good work,' no supplemental authority "
                        "is needed for salvation."
            },
            {
                "heading": "The Five Solas \u2014 The Reformation's Core",
                "body": "The five Solas were not formulated as a single statement "
                        "during the Reformation itself; they emerged gradually as "
                        "the key principles distilled from the Reformers' writings "
                        "and confessions. Together they form a complete soteriology. "
                        "Sola Scriptura: Scripture alone is the final authority for "
                        "faith and practice. Not tradition, not popes, not councils "
                        "-- unless they align with Scripture. Sola Fide: faith alone "
                        "is the instrument of justification. Good works follow "
                        "genuine faith but do not contribute to it. Sola Gratia: "
                        "grace alone is the source of salvation. No human merit, "
                        "no sacramental magic, no purchased indulgence initiates "
                        "or completes salvation. Solus Christus: Christ alone is "
                        "the mediator between God and humanity (1 Timothy 2:5). "
                        "No priest, saint, or Mary mediates access to God. Soli "
                        "Deo Gloria: all glory belongs to God alone. Salvation "
                        "from first to last is God's work, and the credit belongs "
                        "entirely to Him. These five propositions stand on Paul's "
                        "argument in Romans 3-5 and Ephesians 2:1-10. They are not "
                        "Reformation inventions; they are Pauline theology recovered "
                        "from under medieval additions. Luther added the word 'alone' "
                        "(allein) to his German translation of Romans 3:28 -- 'by "
                        "faith alone.' Catholics objected fiercely. But Paul's "
                        "argument in Romans 3-4 makes the 'alone' inescapable: "
                        "if justification is 'apart from works of the law,' then "
                        "faith is the sole instrument. Luther made explicit what "
                        "Paul made obvious. [A] Direct Scripture throughout."
            },
            {
                "heading": "Calvin, Zwingli & the Radical Reformers",
                "body": "The Reformation was never one man's movement. John Calvin "
                        "(1509-1564), a French lawyer turned theologian, produced the "
                        "Institutes of the Christian Religion (first edition 1536, "
                        "final edition 1559) -- the most systematic and influential "
                        "Protestant theology ever written. Calvin emphasized the "
                        "absolute sovereignty of God, predestination, and the "
                        "ordering of all things for divine glory. His model city "
                        "in Geneva became a center of Reformed theology, church "
                        "governance, and missionary training. Ulrich Zwingli "
                        "(1484-1531) led reform in Zurich independently of Luther, "
                        "arriving at similar conclusions about Scripture's authority "
                        "and justification by faith but diverging sharply on the "
                        "Lord's Supper. John Knox (c. 1514-1572) brought Reformed "
                        "theology to Scotland with fierce conviction. And the "
                        "Radical Reformers -- the Anabaptists -- argued that Luther "
                        "and Calvin had not gone far enough. They rejected infant "
                        "baptism, insisted on believer's baptism, advocated "
                        "separation of church and state, and often paid with their "
                        "lives. Menno Simons, Conrad Grebel, and Felix Manz "
                        "represent a stream of the Reformation that took sola "
                        "Scriptura more consistently than the magisterial "
                        "Reformers: if Scripture does not command infant baptism, "
                        "do not practice it. They were persecuted by Catholics "
                        "and Protestants alike -- drowned, burned, and imprisoned "
                        "for the crime of reading the Bible literally. [C] "
                        "Historical parallel -- the Anabaptists anticipated many "
                        "positions that modern evangelicals now take for granted."
            },
            {
                "heading": "The Printing Press \u2014 Technology Serves the Word",
                "body": "No technological revolution before the internet had a greater "
                        "impact on the spread of ideas than Johannes Gutenberg's "
                        "movable-type printing press, developed in Mainz in the "
                        "1440s. Gutenberg's first major printed work was the Bible "
                        "itself (the Gutenberg Bible, c. 1455). Before the press, "
                        "a single Bible cost the equivalent of a year's wages for "
                        "a skilled laborer. Manuscripts were hand-copied by monks "
                        "-- a process that could take over a year per volume. "
                        "Literacy was low, and access to Scripture was controlled "
                        "by the institutional church. The press changed everything. "
                        "Luther's writings were printed in massive quantities: "
                        "between 1518 and 1525, Luther's publications outsold all "
                        "other authors combined in the German-speaking world. His "
                        "German translation of the New Testament (1522) sold five "
                        "thousand copies in two weeks. The complete German Bible "
                        "followed in 1534. For the first time in European history, "
                        "ordinary people could read God's Word in their own language "
                        "without permission from a bishop. The principle of sola "
                        "Scriptura was meaningless without access to Scriptura. "
                        "The press made the principle practical. Providence arranged "
                        "that the technology arrived seventy years before the "
                        "Reformer who would need it most. [B] Valid inference -- "
                        "Acts 17:11 commends the Bereans for examining Scripture "
                        "daily. This requires access to Scripture, which the press "
                        "finally provided to the common people."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 14: THE COUNTER-REFORMATION -- ROME RESPONDS
    # =========================================================================
    {
        "id": "church-counter-reformation",
        "ref": "Galatians 1:8-9",
        "chapter_num": 14,
        "title": "The Counter-Reformation \u2014 Rome Responds",
        "era": "church_reformation",
        "type": "chapter",

        "synopsis": "The Protestant Reformation demanded a response, and the Roman "
                    "Catholic Church delivered one at the Council of Trent (1545-1563). "
                    "Over twenty-five sessions spanning eighteen years, Trent addressed "
                    "real abuses -- simony, absentee bishops, clerical ignorance -- and "
                    "defined Catholic doctrine with a precision the medieval church had "
                    "never achieved. But on the central questions the Reformers raised "
                    "-- the authority of Scripture, the nature of justification, the "
                    "role of works in salvation -- Trent drew the line and doubled down. "
                    "Scripture and Tradition were declared co-equal. Justification was "
                    "defined as a process involving faith, works, and sacraments. And "
                    "anyone who taught sola fide was officially cursed: 'let him be "
                    "anathema.' The Counter-Reformation was not merely defensive; it "
                    "launched the Jesuits, ignited missionary expansion, and produced "
                    "genuine reform. But it also triggered the Wars of Religion that "
                    "would devastate Europe for over a century.",

        "key_verse": {
            "ref": "Galatians 1:8-9",
            "text": "But even if we or an angel from heaven should preach to you "
                    "a gospel contrary to the one we preached to you, let him be "
                    "accursed. As we have said before, so now I say again: If anyone "
                    "is preaching to you a gospel contrary to the one you received, "
                    "let him be accursed.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u1f00\u03bd\u03ac\u03b8\u03b5\u03bc\u03b1 (anathema)",
                "meaning": "Cursed, devoted to destruction, placed under a ban. Paul "
                           "uses anathema in Galatians 1:8-9 to describe anyone who "
                           "preaches a different gospel. The Council of Trent used "
                           "the same word to condemn the Protestant position on "
                           "justification: 'If anyone says that the sinner is "
                           "justified by faith alone... let him be anathema' "
                           "(Session 6, Canon 9). The question is unavoidable: "
                           "whose anathema is valid -- Paul's or Trent's? If "
                           "sola fide IS the gospel Paul preached, then Trent "
                           "anathematized Paul's own doctrine."
            },
            {
                "term": "concilium (Latin: council)",
                "meaning": "An assembly of bishops convened to define doctrine and "
                           "discipline. The Catholic Church considers ecumenical "
                           "councils to be authoritative when confirmed by the pope. "
                           "Trent was the nineteenth ecumenical council and the most "
                           "doctrinally detailed in church history. For Protestants, "
                           "councils carry weight only insofar as they align with "
                           "Scripture -- they are not independently authoritative."
            },
            {
                "term": "traditio (Latin: tradition / handing down)",
                "meaning": "Trent declared that divine revelation comes through two "
                           "channels: Sacred Scripture and Sacred Tradition. This "
                           "directly contradicted sola Scriptura. Paul does speak of "
                           "paradosis (tradition/handing down) positively in 2 "
                           "Thessalonians 2:15 and 1 Corinthians 11:2 -- but the "
                           "traditions Paul commends are apostolic teaching, not "
                           "later ecclesiastical developments. The Reformers did "
                           "not reject all tradition; they rejected tradition's "
                           "claim to equal authority with Scripture."
            },
            {
                "term": "reformatio (Latin: restoration / reformation)",
                "meaning": "The term itself means 'to re-form,' to restore an "
                           "original shape. The Reformers did not claim to innovate; "
                           "they claimed to recover. Sola fide was not Luther's "
                           "invention but Paul's argument in Romans 3-4. Sola "
                           "Scriptura was not a new principle but an old one: the "
                           "Bereans of Acts 17:11 'examined the Scriptures daily "
                           "to see if these things were so.' The Reformation was, "
                           "in its own self-understanding, a return."
            },
            {
                "term": "Societas Iesu (Latin: Society of Jesus)",
                "meaning": "The Jesuits, founded in 1540 by Ignatius of Loyola. "
                           "A religious order organized with military discipline "
                           "and intellectual rigor for the defense and propagation "
                           "of Catholic doctrine. The Jesuits became the spearhead "
                           "of the Counter-Reformation: educators, missionaries, "
                           "theologians, and political advisors. Their global "
                           "missions to Asia, the Americas, and Africa were "
                           "genuinely remarkable -- brilliant and controversial "
                           "in equal measure."
            }
        ],

        "ane_backdrop": "The Council of Trent must be understood within the political "
                        "reality of sixteenth-century Europe. Emperor Charles V needed "
                        "religious unity to hold his empire together against the Ottoman "
                        "threat. Pope Paul III needed to demonstrate that the Catholic "
                        "Church could reform itself without Protestant help. The French "
                        "monarchy wanted to limit papal power. These competing interests "
                        "delayed Trent for decades (Luther first called for a council "
                        "in 1518; Trent did not convene until 1545, two years after "
                        "Luther's death). The council met in three phases: 1545-1547, "
                        "1551-1552, and 1562-1563, interrupted by plague, war, and "
                        "political maneuvering. The result was a monument of doctrinal "
                        "precision -- every major Protestant claim was identified, "
                        "analyzed, and formally rejected. Trent transformed Catholicism "
                        "from a relatively loose medieval institution into a doctrinally "
                        "rigid, centrally governed church that would endure for four "
                        "centuries until Vatican II (1962-1965).",

        "second_temple": [
            {
                "source": "Council of Trent, Session 6 (January 1547)",
                "summary": "The Decree on Justification -- Trent's most theologically "
                           "significant document. It defined justification as a process "
                           "that begins with prevenient grace, proceeds through faith "
                           "AND works AND sacraments, and can be lost through mortal "
                           "sin. Canon 9: 'If anyone says that the sinner is justified "
                           "by faith alone, meaning that nothing else is required to "
                           "cooperate in order to obtain the grace of justification... "
                           "let him be anathema.' Canon 12: 'If anyone says that "
                           "justifying faith is nothing other than trust in the divine "
                           "mercy... let him be anathema.'",
                "relevance": "Trent did not merely disagree with Luther; it formally "
                             "cursed his position. This is the sharpest doctrinal "
                             "division in church history. Either Paul teaches sola "
                             "fide (Romans 3:28) and Trent is wrong, or Trent is "
                             "right and the Reformers misread Paul. There is no "
                             "middle ground. [A] The text of Romans 3:28 must be "
                             "the judge."
            },
            {
                "source": "Council of Trent, Session 4 (April 1546)",
                "summary": "Trent declared that Scripture and unwritten traditions "
                           "received by the apostles from Christ himself or handed "
                           "down by the apostles under the dictation of the Holy "
                           "Spirit are to be received 'with equal devotion and "
                           "reverence' (pari pietatis affectu). The Latin Vulgate "
                           "was declared the authoritative Bible text. Access to "
                           "Scripture was implicitly controlled by making the "
                           "Vulgate normative over Greek and Hebrew manuscripts.",
                "relevance": "This decree directly contradicts sola Scriptura and "
                             "elevates church tradition to the same authority as "
                             "Scripture. It also privileged a translation (the "
                             "Vulgate) over the original-language texts -- a move "
                             "the Reformers rightly opposed. [B] Valid inference -- "
                             "if the original texts are God-breathed (2 Timothy "
                             "3:16), no translation can supersede them."
            }
        ],

        "cross_refs": [
            {"ref": "Galatians 1:8-9", "note": "Paul's own anathema: anyone preaching a different gospel is accursed. If sola fide IS Paul's gospel, then Trent's anathema against it falls under Paul's prior curse", "type": "nt"},
            {"ref": "Romans 4:4-5", "note": "'To the one who does not work but believes in him who justifies the ungodly, his faith is counted as righteousness' -- Paul's clearest statement: justification is for the one who does NOT work but BELIEVES", "type": "nt"},
            {"ref": "2 Thessalonians 2:15", "note": "'Stand firm and hold to the traditions that you were taught by us' -- Paul commends apostolic tradition, but these are HIS teachings, not later ecclesiastical developments", "type": "nt"},
            {"ref": "Colossians 2:8", "note": "'See to it that no one takes you captive by philosophy and empty deceit, according to human tradition' -- Paul warns against human tradition replacing divine revelation", "type": "nt"},
            {"ref": "Acts 17:11", "note": "The Bereans 'received the word with all eagerness, examining the Scriptures daily to see if these things were so' -- the Berean principle: every teaching, even apostolic, is tested by Scripture", "type": "nt"},
            {"ref": "1 Timothy 2:5", "note": "'There is one mediator between God and men, the man Christ Jesus' -- solus Christus: no priest, saint, or Mary mediates access to God", "type": "nt"},
            {"ref": "Mark 7:8-9", "note": "Jesus rebukes the Pharisees: 'You leave the commandment of God and hold to the tradition of men' -- the pattern of human tradition displacing divine authority predates Rome", "type": "nt"}
        ],

        "divine_council_note": "The Counter-Reformation reveals a pattern as old as Eden: "
                               "the institutional mediation of access to God. In the divine "
                               "council worldview, the seventy nations were placed under the "
                               "authority of the sons of God (Deuteronomy 32:8-9, LXX/DSS), "
                               "but these appointed rulers became corrupt and were judged "
                               "(Psalm 82). They interposed themselves between humanity and "
                               "YHWH. The medieval Catholic system -- however unintentionally "
                               "-- replicated this pattern: layers of mediation (priests, "
                               "saints, Mary, the pope) between the individual believer and "
                               "God. The Reformation's recovery of the priesthood of all "
                               "believers (1 Peter 2:9) was a partial dismantling of this "
                               "mediatorial structure. But the full cosmic picture -- that "
                               "Christ's victory disarmed the principalities and powers "
                               "(Colossians 2:15) and opened direct access to the Father "
                               "(Hebrews 4:16) -- requires the divine council framework "
                               "to be fully understood.",

        "sections": [
            {
                "heading": "The Council of Trent \u2014 Rome Defines Itself",
                "body": "The Council of Trent (1545-1563) was the Catholic Church's "
                        "most comprehensive doctrinal response to any challenge in "
                        "its history. Called by Pope Paul III after decades of delay, "
                        "it met in twenty-five sessions over three separate periods. "
                        "The council addressed two categories: doctrine and reform. "
                        "On reform, Trent was genuinely constructive: it condemned "
                        "simony (buying church offices), required bishops to reside "
                        "in their dioceses, established seminaries for proper clerical "
                        "training, and standardized liturgical practices. These were "
                        "real abuses the Reformers had rightly protested, and "
                        "Trent corrected them. On doctrine, Trent drew lines "
                        "that remain in place today. Session 4 (1546) declared that "
                        "Scripture and apostolic tradition are to be received with "
                        "'equal devotion and reverence.' Session 6 (1547) defined "
                        "justification as a cooperative process: God initiates with "
                        "prevenient grace, but the sinner must respond with faith, "
                        "hope, charity, repentance, and sacramental participation. "
                        "Justification can be increased by good works and lost by "
                        "mortal sin. Session 7 confirmed seven sacraments. Session "
                        "13 affirmed transubstantiation. Session 25 affirmed "
                        "purgatory and the invocation of saints. On every point the "
                        "Reformers challenged, Trent did not retreat. It clarified, "
                        "defined, and condemned the Protestant alternatives. [C] "
                        "Historical parallel -- Trent played the same role for the "
                        "Counter-Reformation that Nicaea played for Trinitarian "
                        "orthodoxy: it defined the boundaries permanently."
            },
            {
                "heading": "Trent's Anathemas \u2014 The Point of No Return",
                "body": "The most consequential moment in the Counter-Reformation "
                        "came in Session 6, the Decree on Justification. The council "
                        "issued thirty-three canons, each ending with the formula "
                        "'let him be anathema' (si quis dixerit... anathema sit). "
                        "Canon 9 is the sharpest: 'If anyone says that the sinner "
                        "is justified by faith alone, meaning that nothing else is "
                        "required to cooperate in order to obtain the grace of "
                        "justification, and that it is not at all necessary that he "
                        "be prepared and disposed by the action of his own will: "
                        "let him be anathema.' Canon 12 strikes at the heart of "
                        "fiducia (trust): 'If anyone says that justifying faith is "
                        "nothing other than trust in the divine mercy, which remits "
                        "sins for Christ's sake... let him be anathema.' These "
                        "canons officially placed the Protestant doctrine of "
                        "justification under a curse. The irony is devastating: "
                        "Paul himself pronounced anathema on anyone who preaches "
                        "'a gospel contrary to the one we preached to you' "
                        "(Galatians 1:8-9). If justification by faith alone IS "
                        "the gospel Paul preached -- and Romans 3-4 argues exactly "
                        "that -- then Trent's anathema falls under Paul's prior "
                        "curse. The council that intended to defend the gospel may "
                        "have cursed it. [A] Direct Scripture: Romans 3:28, 4:4-5, "
                        "and Galatians 1:8-9 are the texts that must judge Trent, "
                        "not the reverse."
            },
            {
                "heading": "The Jesuits \u2014 The Counter-Reformation's Spearhead",
                "body": "In 1540, Pope Paul III approved a new religious order that "
                        "would become the most powerful force in the Counter-"
                        "Reformation: the Society of Jesus, founded by Ignatius of "
                        "Loyola (1491-1556), a Basque soldier-turned-mystic. The "
                        "Jesuits combined military discipline, intellectual rigor, "
                        "and absolute obedience to the pope. Ignatius's Spiritual "
                        "Exercises -- a systematic program of meditation, prayer, "
                        "and self-examination -- became one of the most influential "
                        "devotional works in Christian history. The Jesuits founded "
                        "universities and schools across Europe, producing scholars "
                        "who could match any Protestant theologian in debate. They "
                        "sent missionaries to India (Francis Xavier), China (Matteo "
                        "Ricci), Japan, Brazil, and Paraguay, establishing the "
                        "Catholic Church on every inhabited continent. They also "
                        "became political advisors, confessors to kings, and "
                        "instruments of the Inquisition. The Jesuit record is "
                        "genuinely mixed: extraordinary educational and missionary "
                        "achievements alongside complicity in persecution and "
                        "political manipulation. They were suppressed by Pope "
                        "Clement XIV in 1773 (under pressure from European "
                        "monarchs) and restored in 1814. An honest assessment: "
                        "the Jesuits represent the best and worst of institutional "
                        "Christianity -- brilliant minds serving a system that, "
                        "at Trent, anathematized the Pauline gospel. [C] Historical "
                        "parallel -- their global impact is undeniable regardless "
                        "of theological disagreement."
            },
            {
                "heading": "Catholic Reform vs. Counter-Reformation",
                "body": "Historians distinguish between 'Catholic reform' (genuine "
                        "internal renewal that predated and paralleled the Protestant "
                        "Reformation) and 'Counter-Reformation' (the reactive, "
                        "defensive program aimed at stopping Protestantism). Both "
                        "were real. Catholic reform included figures like Erasmus "
                        "of Rotterdam (who published a Greek New Testament in 1516 "
                        "that Luther used for his translation), Cardinal Ximenes "
                        "de Cisneros (who reformed the Spanish church), and the "
                        "Oratory of Divine Love in Rome. These reformers wanted "
                        "to address abuses without breaking from Rome. The Counter-"
                        "Reformation, by contrast, was explicitly anti-Protestant: "
                        "the Index of Forbidden Books (1559), the Roman Inquisition "
                        "(reorganized 1542), and Trent's anathemas were designed "
                        "to suppress dissent. The tragedy is that both impulses "
                        "were needed but poorly balanced. Trent corrected real "
                        "abuses -- but it also hardened doctrinal positions that "
                        "the Reformers were right to challenge. Rome could have "
                        "cleaned house AND reconsidered its soteriology. It chose "
                        "to clean house while fortifying the doctrinal walls. The "
                        "result was a more disciplined church that remained "
                        "doctrinally distant from the Pauline gospel of Romans "
                        "3-4. [B] Valid inference -- reform of practice is good; "
                        "but if the core doctrine of justification is wrong, "
                        "cleaned-up practices serve a distorted gospel."
            },
            {
                "heading": "The Wars of Religion \u2014 When Theology Turns to Bloodshed",
                "body": "The Reformation was never merely theological. It triggered "
                        "some of the bloodiest conflicts in European history. The "
                        "German Peasants' War (1524-1525) was partly inspired by "
                        "Luther's rhetoric of Christian freedom, though Luther "
                        "himself condemned the peasants' violence in harsh terms "
                        "that remain controversial. The French Wars of Religion "
                        "(1562-1598) pitted Catholic and Huguenot (French Calvinist) "
                        "factions against each other in eight separate wars. The "
                        "worst atrocity was the St. Bartholomew's Day Massacre "
                        "(August 24, 1572): Catholic mobs, with royal sanction, "
                        "murdered an estimated 5,000 to 30,000 Huguenots across "
                        "France in a matter of weeks. The Thirty Years' War "
                        "(1618-1648) devastated central Europe; the population of "
                        "the German states may have dropped by 20-40 percent. The "
                        "Peace of Westphalia (1648) ended the wars by establishing "
                        "the principle cuius regio, eius religio -- 'whose realm, "
                        "his religion.' This was not religious liberty; it was "
                        "territorial religious monopoly. The blood on both sides -- "
                        "Catholic and Protestant -- is a permanent warning that "
                        "theological conviction without love produces atrocity. "
                        "Jesus told His disciples, 'By this all people will know "
                        "that you are my disciples, if you have love for one "
                        "another' (John 13:35). [A] That standard indicts "
                        "every party in the Wars of Religion."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 15: THE LEGACY -- WHY IT STILL MATTERS
    # =========================================================================
    {
        "id": "church-reformation-legacy",
        "ref": "Acts 17:11",
        "chapter_num": 15,
        "title": "The Legacy \u2014 Why It Still Matters",
        "era": "church_reformation",
        "type": "chapter",

        "synopsis": "The Reformation is five hundred years old, but its questions are "
                    "not settled. The denominational landscape it created -- hundreds "
                    "of Protestant traditions alongside Roman Catholicism and Eastern "
                    "Orthodoxy -- is messy, fragmented, and occasionally embarrassing. "
                    "But the alternative -- a single institution with unchecked "
                    "doctrinal authority -- produced the very abuses the Reformation "
                    "corrected. The Reformation's greatest legacy is the Bible in the "
                    "hands of common people: Tyndale's English translation (for which "
                    "he was executed), Luther's German Bible, and ultimately the King "
                    "James Version (1611) that shaped the English-speaking world. But "
                    "the Reformation is also unfinished. The Reformers recovered "
                    "justification by faith and Scripture's authority -- but they did "
                    "not recover everything. The divine council worldview, the Second "
                    "Temple context for reading the New Testament, and the cosmic "
                    "scope of Christ's victory over the principalities and powers -- "
                    "these still await full integration into the church's theology.",

        "key_verse": {
            "ref": "Acts 17:11",
            "text": "Now these Jews were more noble than those in Thessalonica; "
                    "they received the word with all eagerness, examining the "
                    "Scriptures daily to see if these things were so.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u1f10\u03ba\u03ba\u03bb\u03b7\u03c3\u03af\u03b1 (ekklesia)",
                "meaning": "Assembly, congregation, those called out. The word the NT "
                           "uses for 'church' is not a building, not an institution, "
                           "not a hierarchy. Ekklesia is the assembly of those called "
                           "out by God. Jesus said: 'Where two or three are gathered "
                           "in my name, there am I among them' (Matthew 18:20). The "
                           "Reformation recovered the principle that the ekklesia is "
                           "constituted by Christ's presence, not by papal authority "
                           "or apostolic succession."
            },
            {
                "term": "\u1f31\u03b5\u03c1\u03ac\u03c4\u03b5\u03c5\u03bc\u03b1 (hierateuma)",
                "meaning": "Priesthood. 1 Peter 2:9 declares: 'You are a chosen race, "
                           "a royal priesthood (hierateuma basileion), a holy nation.' "
                           "This is addressed to ALL believers, not to an ordained "
                           "clerical class. The Reformation recovered the 'priesthood "
                           "of all believers' -- every Christian has direct access to "
                           "God through Christ, without requiring a human priest as "
                           "mediator. This doctrine demolished the medieval clerical "
                           "monopoly on access to God."
            },
            {
                "term": "\u03b4\u03b9\u03b4\u03ac\u03c3\u03ba\u03b1\u03bb\u03bf\u03c2 (didaskalos)",
                "meaning": "Teacher, instructor. Jesus is called didaskalos throughout "
                           "the Gospels. The Reformation created a culture of teaching: "
                           "seminaries, catechisms, printed sermons, systematic "
                           "theologies. Calvin's Institutes remain a model of "
                           "theological pedagogy. But the Berean principle demands "
                           "that every teacher -- Luther, Calvin, the pope, your "
                           "pastor -- be tested against Scripture."
            },
            {
                "term": "sola (Latin: alone)",
                "meaning": "The permanent principle. Sola Scriptura is not a "
                           "sixteenth-century artifact; it is the consistent "
                           "methodology of every biblical author. The prophets "
                           "appealed to prior revelation ('Thus says the LORD'). "
                           "Jesus corrected Pharisaic tradition by Scripture "
                           "(Matthew 15:3-6). Paul proved his gospel from the "
                           "OT (Romans 4, Galatians 3). The Bereans tested "
                           "apostolic preaching by Scripture (Acts 17:11). Sola "
                           "Scriptura is not a Reformation invention. It is the "
                           "Bible's own hermeneutic."
            }
        ],

        "ane_backdrop": "The Reformation's insistence on Bible translation into "
                        "vernacular languages reversed a millennium of Latin monopoly "
                        "in the Western church. Before the Reformation, the Bible "
                        "existed in the common tongue only in fragments and unofficial "
                        "versions (the Wycliffe Bible in English, c. 1382, was condemned "
                        "as heretical). The Council of Toulouse (1229) explicitly "
                        "prohibited laypeople from possessing the Scriptures in the "
                        "vernacular. William Tyndale, whose English NT (1526) was the "
                        "first printed English Bible, was strangled and burned at the "
                        "stake in 1536. His alleged last words: 'Lord, open the King "
                        "of England's eyes.' Within three years, Henry VIII authorized "
                        "the Great Bible in English -- based largely on Tyndale's work. "
                        "The King James Version (1611), which drew heavily on Tyndale, "
                        "became the most influential English text ever published. "
                        "Luther's German Bible (1534) standardized the German language "
                        "itself. Bible translation was the Reformation's most concrete "
                        "and enduring achievement. It meant that every literate person "
                        "could test every doctrine against the text -- exactly what "
                        "Acts 17:11 commends.",

        "second_temple": [
            {
                "source": "The Berean Principle (Acts 17:10-11, c. AD 50)",
                "summary": "When Paul and Silas arrived in Berea, the Jewish community "
                           "there 'received the word with all eagerness, examining the "
                           "Scriptures daily to see if these things were so.' Luke "
                           "commends them as 'more noble' than the Thessalonians -- "
                           "not because they were skeptics but because they tested "
                           "even apostolic teaching against the written Word of God.",
                "relevance": "The Berean principle is the biblical foundation of sola "
                             "Scriptura. If first-century Jews were commended for "
                             "testing PAUL'S preaching against Scripture, then no "
                             "subsequent tradition -- Catholic, Orthodox, or Protestant "
                             "-- is above the same test. The principle is not anti-"
                             "tradition; it is pro-truth. [A] Direct Scripture."
            },
            {
                "source": "The Dead Sea Scrolls (discovered 1947-1956)",
                "summary": "The DSS revolutionized biblical studies by providing "
                           "Hebrew manuscripts a thousand years older than the "
                           "earliest medieval copies. They confirmed the remarkable "
                           "accuracy of the Masoretic text while also revealing "
                           "textual variants -- including the Deuteronomy 32:8 "
                           "reading 'sons of God' (b'nei 'elohim) rather than 'sons "
                           "of Israel,' a reading that illuminates the divine "
                           "council worldview throughout Scripture.",
                "relevance": "Neither the Reformers nor the Council of Trent had "
                             "access to these texts. The DSS demonstrate that the "
                             "Reformation was a necessary but incomplete recovery. "
                             "The Reformers recovered soteriology (justification "
                             "by faith). The DSS and Ugaritic texts now enable "
                             "the recovery of cosmology (the divine council, the "
                             "spiritual powers, the cosmic scope of Christ's "
                             "triumph). [C] Historical parallel -- ongoing "
                             "archaeological discovery continues the Reformation "
                             "principle: let the evidence speak."
            }
        ],

        "cross_refs": [
            {"ref": "Acts 17:11", "note": "The Bereans examined Scripture daily to test apostolic teaching -- the permanent model for every generation of believers", "type": "nt"},
            {"ref": "Matthew 18:20", "note": "'Where two or three are gathered in my name, there am I among them' -- the ekklesia is constituted by Christ's presence, not institutional authority", "type": "nt"},
            {"ref": "1 Peter 2:9", "note": "'You are a royal priesthood, a holy nation' -- the priesthood of ALL believers, not a clerical class", "type": "nt"},
            {"ref": "2 Timothy 3:16-17", "note": "'All Scripture is breathed out by God and profitable... that the man of God may be complete, equipped for every good work' -- the sufficiency of Scripture", "type": "nt"},
            {"ref": "Deuteronomy 32:8-9", "note": "'When the Most High gave to the nations their inheritance... he fixed the borders of the peoples according to the number of the sons of God' (DSS/LXX) -- the divine council passage the Reformers never recovered", "type": "ot"},
            {"ref": "Colossians 2:15", "note": "'He disarmed the rulers and authorities and put them to open shame, triumphing over them in him' -- Christ's cosmic victory over the principalities, a dimension of salvation the Reformers under-developed", "type": "nt"},
            {"ref": "Ephesians 6:12", "note": "'We do not wrestle against flesh and blood, but against the rulers, against the authorities, against the cosmic powers over this present darkness' -- the spiritual warfare framework", "type": "nt"},
            {"ref": "Psalm 82:1-8", "note": "'God has taken his place in the divine council; in the midst of the gods he holds judgment' -- the divine council that the Reformers acknowledged but did not systematically develop", "type": "ot"}
        ],

        "divine_council_note": "The Reformation recovered what was lost in the medieval "
                               "period: the authority of Scripture over human traditions "
                               "and the gospel of justification by grace through faith. "
                               "These recoveries were essential and permanent. But the "
                               "Reformers inherited the same Augustinian-Western framework "
                               "that had flattened the divine council worldview for a "
                               "millennium. They read Deuteronomy 32:8 in the Masoretic "
                               "text ('sons of Israel') rather than the DSS/LXX reading "
                               "('sons of God'). They acknowledged Ephesians 6:12 but "
                               "did not systematically develop its implications. They "
                               "knew Psalm 82 but read the 'gods' as human judges rather "
                               "than divine council members. The FULL recovery -- "
                               "soteriology AND cosmology, justification AND cosmic "
                               "Christology, sola Scriptura AND the divine council -- "
                               "requires tools the Reformers did not possess. The Dead "
                               "Sea Scrolls (1947), the Ugaritic texts (deciphered "
                               "1930s), and Second Temple Jewish literature now give "
                               "us what Luther and Calvin could not have known. The "
                               "Reformation is not over. It awaits its next chapter: "
                               "the recovery of the cosmic scope of the gospel.",

        "sections": [
            {
                "heading": "The Denominational Explosion \u2014 Failure or Feature?",
                "body": "The Reformation shattered Western Christendom's institutional "
                        "unity. Where there had been one church (at least in theory), "
                        "there were soon hundreds of denominations: Lutheran, Reformed, "
                        "Anglican, Baptist, Methodist, Pentecostal, and countless "
                        "independent fellowships. Critics -- both Catholic and secular "
                        "-- point to this fragmentation as proof that the Reformation "
                        "failed. If sola Scriptura produces such disagreement, how can "
                        "it be a reliable principle? The question is fair but the "
                        "conclusion is flawed. First, the pre-Reformation church was "
                        "not unified in the way the myth suggests: the Great Schism "
                        "of 1054 had already split East and West, the Western Schism "
                        "(1378-1417) produced rival popes, and theological diversity "
                        "existed even under Rome's umbrella. Second, denominational "
                        "diversity is partly the cost of theological freedom. A system "
                        "that allows no dissent (Rome before the Reformation) "
                        "suppresses error and truth alike. A system that permits "
                        "dissent (Protestantism) allows truth to compete in the open "
                        "-- and also allows error to proliferate. The mess is real. "
                        "But the alternative -- a single authority that cannot be "
                        "questioned -- is worse, because when that authority goes "
                        "wrong, there is no mechanism for correction. The Berean "
                        "principle (Acts 17:11) assumes the right to test and "
                        "question. [B] Valid inference -- diversity within unity "
                        "(Ephesians 4:3-6) is the NT model, not institutional "
                        "uniformity."
            },
            {
                "heading": "Bible Accessibility \u2014 The Greatest Legacy",
                "body": "If the Reformation produced only one lasting achievement, it "
                        "would be this: the Bible in the language of the people. Before "
                        "the sixteenth century, reading Scripture in your own tongue "
                        "could get you killed. John Wycliffe (c. 1328-1384) sponsored "
                        "the first complete English Bible translation; after his death, "
                        "his bones were exhumed and burned on the order of the Council "
                        "of Constance (1415). Jan Hus, who advocated Scripture in the "
                        "vernacular and communion in both kinds, was burned at the "
                        "stake in 1415. William Tyndale (c. 1494-1536) produced the "
                        "first printed English New Testament in 1526; he was strangled "
                        "and burned in Belgium in 1536. These men died so that others "
                        "could read what God had written. Luther's German New Testament "
                        "(1522) and complete Bible (1534) did more than translate "
                        "Scripture -- they standardized the German language and created "
                        "a reading culture. The King James Version (1611), built on "
                        "Tyndale's foundation, became the most influential English "
                        "text in history. The principle is simple: if God spoke in "
                        "Hebrew and Greek so that His people could understand, then "
                        "translation into every language is not a violation of "
                        "Scripture but its fulfillment. Restricting Bible access is "
                        "the real innovation. [A] Acts 2:8-11 -- at Pentecost, the "
                        "Spirit ensured every nation heard the gospel in their own "
                        "tongue. Bible translation extends Pentecost."
            },
            {
                "heading": "The Unfinished Reformation \u2014 Did They Go Far Enough?",
                "body": "A fair assessment of the Reformers must include their "
                        "failures. Luther kept infant baptism despite having no "
                        "clear scriptural command for it. He maintained a state "
                        "church model (the prince determines the religion of his "
                        "territory). His later writings against the Jews are "
                        "indefensible and horrifying. Calvin had Michael Servetus "
                        "burned at the stake for heresy in 1553 -- using the "
                        "coercive power of the state to enforce theological "
                        "conformity, exactly the crime he charged against Rome. "
                        "The magisterial Reformers persecuted the Anabaptists -- "
                        "the very group most consistently applying sola Scriptura "
                        "to ecclesiology. The Reformers recovered the gospel of "
                        "justification by faith, but they did not fully recover "
                        "the gospel of the kingdom. They reformed soteriology but "
                        "kept much of Rome's ecclesiology, eschatology, and "
                        "ceremonial practice. The question is not whether they were "
                        "right to reform -- they were. The question is whether they "
                        "went far enough. If sola Scriptura is the principle, then "
                        "every tradition must be tested -- including the Reformers' "
                        "own. Semper reformanda ('always reforming') is not just a "
                        "slogan. It is the logical consequence of sola Scriptura "
                        "applied honestly. [B] Valid inference -- if Scripture alone "
                        "is the final authority, then the Reformation itself is "
                        "subject to further reform by Scripture."
            },
            {
                "heading": "What Was Recovered \u2014 The Permanent Gains",
                "body": "Despite their inconsistencies, the Reformers recovered truths "
                        "that the church cannot afford to lose again. Justification by "
                        "faith: the sinner is declared righteous by God on the basis "
                        "of Christ's work, received through faith, not earned by works "
                        "or sacraments. Romans 3:28 and 4:4-5 are as clear as language "
                        "permits. Scripture's supreme authority: every tradition, every "
                        "council, every pope must submit to the written Word. The "
                        "Bereans of Acts 17:11 are the model. The priesthood of all "
                        "believers: 1 Peter 2:9 applies to every Christian, not a "
                        "clerical class. Every believer has direct access to God "
                        "through Christ (Hebrews 4:16) without requiring a human "
                        "priest as mediator. The sufficiency of Christ's sacrifice: "
                        "'It is finished' (John 19:30) means the work of atonement "
                        "is complete. No repetition in the Mass, no purgatorial "
                        "suffering, no indulgence can add to what Christ accomplished "
                        "on the cross. Hebrews 10:14 seals it: 'By a single offering "
                        "he has perfected for all time those who are being sanctified.' "
                        "These are not negotiable. They are Paul's gospel, and "
                        "surrendering them means surrendering the gospel itself. [A] "
                        "Direct Scripture throughout -- every point rests on explicit "
                        "NT texts."
            },
            {
                "heading": "What Still Needs Recovering \u2014 The Divine Council & Cosmic Christ",
                "body": "The Reformers recovered soteriology. They did not recover "
                        "cosmology. The divine council worldview -- God presiding over "
                        "a council of heavenly beings (Psalm 82:1, 1 Kings 22:19-22, "
                        "Job 1:6-12, Daniel 7:9-10), the allotment of nations to the "
                        "sons of God (Deuteronomy 32:8-9, DSS/LXX), the corruption "
                        "of those cosmic rulers (Psalm 82:6-7), and Christ's triumph "
                        "over them (Colossians 2:15, Ephesians 1:20-23) -- was not "
                        "part of the Reformation's recovery. The reasons are "
                        "understandable: the Dead Sea Scrolls were not discovered "
                        "until 1947. The Ugaritic texts from Ras Shamra were not "
                        "deciphered until the 1930s. The Second Temple Jewish "
                        "literature (1 Enoch, Jubilees, the Testaments of the Twelve "
                        "Patriarchs) was unknown or dismissed. The "
                        "Reformers read Scripture brilliantly but without the ANE "
                        "context that illuminates the cosmic "
                        "dimension of the biblical story. We now have that context. "
                        "Deuteronomy 32:8 in the DSS reads 'sons of God' (b'nei "
                        "'elohim), not 'sons of Israel' -- a reading that unlocks "
                        "the entire biblical storyline of God's reclamation of the "
                        "nations from corrupt heavenly rulers through Christ. The "
                        "Reformation recovered the vertical dimension "
                        "(God and the individual sinner). The divine council "
                        "worldview adds the horizontal and cosmic dimensions: "
                        "Christ's victory over the powers, the reclamation of "
                        "the nations, and the restoration of the entire created "
                        "order. [B] Valid inference from the combined testimony "
                        "of Deuteronomy 32, Psalm 82, Daniel 10, Colossians 2, "
                        "and Ephesians 1."
            },
            {
                "heading": "The Question for Today \u2014 The Berean Standard",
                "body": "Every Christian tradition -- Catholic, Orthodox, Protestant "
                        "-- has accumulated human traditions that need testing against "
                        "Scripture. The Catholic Church elevated tradition to co-equal "
                        "authority with Scripture and built a sacramental system with "
                        "no Pauline warrant. The Orthodox traditions preserve ancient "
                        "liturgy and theology but resist the reforming impulse that "
                        "Scripture itself demands. Protestant denominations have their "
                        "own traditions: altar calls, dispensational charts, worship "
                        "styles, and cultural preferences treated as biblical mandates. "
                        "The Berean principle plays no favorites. It does not ask, "
                        "'What does my tradition teach?' It asks, 'What do the "
                        "Scriptures say?' (Romans 4:3, Galatians 4:30). This is not "
                        "anti-tradition for its own sake. Good traditions preserve "
                        "and transmit truth. But tradition must always be the servant "
                        "of Scripture, never its master. Jesus Himself set the standard "
                        "when He told the Pharisees: 'You leave the commandment of God "
                        "and hold to the tradition of men' (Mark 7:8). The church is "
                        "not a building. It is not an institution. It is not a "
                        "hierarchy. The ekklesia is the assembly of those called out "
                        "by God, constituted by Christ's presence: 'Where two or three "
                        "are gathered in my name, there am I among them' (Matthew "
                        "18:20). The Reformation pointed back to this reality. The "
                        "recovery continues. [A] Direct Scripture: Acts 17:11, Mark "
                        "7:8, Matthew 18:20 -- the texts that anchor the permanent "
                        "Reformation principle."
            }
        ]
    }
]
