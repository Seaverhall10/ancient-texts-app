"""
era_salvation_vs_reward.py -- The Critical Distinction (Chapters 1-2)

Most Western Christians have been taught two options: heaven or hell. The
texts actually describe something far more nuanced -- and far more motivating.
Salvation and reward are not the same thing, and the NT never conflates them.
Salvation is the entrance, given by grace through faith alone. Reward is what
you do with your life inside that relationship -- and it is evaluated,
differentiated, and permanent.

This era establishes the foundational distinction that governs everything
that follows. Without this distinction, the bema seat becomes terrifying
(if you think works earn salvation) or irrelevant (if you think everyone
gets the same thing regardless). The NT holds neither position. It maintains
both grace for salvation and evaluation for reward -- and the motivation it
produces is not fear or guilt but vision: the king is coming.

Two chapters covering:
  1. Salvation is Not Reward -- the NT never conflates the two
  2. Why This Distinction Matters -- wrong vs. right motivation
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 1: SALVATION IS NOT REWARD
    # =========================================================================
    {
        "id": "salvation-vs-reward-1",
        "ref": "Ephesians 2:8-9; Luke 23:42-43; 1 Corinthians 3:14-15",
        "chapter_num": 1,
        "title": "Salvation Is Not Reward",
        "era": "salvation_vs_reward",
        "type": "chapter",

        "synopsis": "The NT maintains a sharp, consistent distinction between "
                    "salvation and reward that most Western Christianity has "
                    "collapsed. Salvation is the entrance into the kingdom -- "
                    "given by grace through faith alone, demonstrated perfectly "
                    "by the thief on the cross who received paradise with zero "
                    "works, zero theology, zero track record. Reward is what "
                    "you do with your life inside the covenant relationship -- "
                    "and it is evaluated, differentiated, and permanent. These "
                    "are not the same category. Confusing them produces either "
                    "works-based anxiety or reward-irrelevant passivity -- both "
                    "of which the NT explicitly rejects.",

        "key_verse": {
            "ref": "Ephesians 2:8-9",
            "text": "For by grace you have been saved through faith. And this "
                    "is not your own doing; it is the gift of God, not a result "
                    "of works, so that no one may boast.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u03c7\u03ac\u03c1\u03b9\u03c2 (charis)",
                "meaning": "Grace, unmerited favor. The Greek word Paul uses for "
                           "the mechanism of salvation. Charis is not a reward "
                           "for performance -- it is a gift (doron, Eph 2:8) "
                           "that cannot be earned. The moment works enter the "
                           "equation, charis ceases to be charis (Rom 11:6). "
                           "Salvation operates entirely on this basis."
            },
            {
                "term": "\u03bc\u03b9\u03c3\u03b8\u03cc\u03c2 (misthos)",
                "meaning": "Wage, reward, recompense. The Greek word for what is "
                           "EARNED or awarded based on what was done. Used in "
                           "Matt 5:12 ('great is your reward in heaven'), "
                           "1 Cor 3:14 ('he will receive his reward'), Col 3:24 "
                           "('you will receive the inheritance as your reward'). "
                           "Misthos is the reward category -- fundamentally "
                           "different from charis."
            },
            {
                "term": "\u03c3\u03c9\u03c4\u03b7\u03c1\u03af\u03b1 (soteria)",
                "meaning": "Salvation, deliverance, rescue. This is the entrance "
                           "into the kingdom -- being rescued from judgment and "
                           "brought into covenant relationship with Yahweh. The "
                           "thief on the cross received soteria. What he could "
                           "not receive -- having no time left -- was misthos "
                           "for a life of faithfulness."
            }
        ],

        "ane_backdrop": "In ancient Near Eastern treaty frameworks, the relationship "
                        "between a suzerain and vassal involved two distinct categories: "
                        "the initial covenant grant (given by the suzerain's grace and "
                        "power) and the ongoing rewards for faithful vassal service. A "
                        "vassal did not earn the covenant -- the great king initiated it. "
                        "But within the covenant, faithful service was rewarded with "
                        "greater land, authority, and honor, while unfaithful service "
                        "resulted in loss of territory and privilege -- though not "
                        "necessarily expulsion from the covenant itself. The biblical "
                        "distinction between salvation (covenant entrance) and reward "
                        "(service evaluation) maps precisely onto this ANE pattern.",

        "second_temple": [
            {
                "source": "4 Ezra 7:33-35",
                "summary": "According to 4 Ezra, at the final judgment 'recompense "
                           "shall follow, and the reward shall be manifested.' The "
                           "text distinguishes between general judgment and specific "
                           "recompense for deeds -- reflecting the same two-category "
                           "framework the NT maintains.",
                "relevance": "Shows that Second Temple Judaism already distinguished "
                             "between eschatological vindication (being on the right "
                             "side of judgment) and differentiated reward for deeds. "
                             "This was not a Pauline innovation but a framework Paul "
                             "inherited and sharpened."
            },
            {
                "source": "1 Enoch 108:10-12",
                "summary": "According to 1 Enoch 108, the righteous who endured "
                           "suffering receive differentiated reward: 'I will bring "
                           "them out into the bright light, those who have loved my "
                           "holy name, and seat them each one by one upon the throne "
                           "of his honor.' Individual thrones. Differentiated honor.",
                "relevance": "The Enochic tradition anticipated differentiated reward "
                             "for the righteous -- not uniform blessing but individual "
                             "thrones of honor based on faithfulness. This parallels "
                             "Jesus' promise in Revelation 3:21 and the parable of "
                             "the minas."
            }
        ],

        "cross_refs": [
            {"ref": "Ephesians 2:8-9", "note": "Salvation by grace through faith, not works -- the clearest soteria text in the NT", "type": "nt"},
            {"ref": "Luke 23:42-43", "note": "The thief on the cross -- salvation with zero works, zero theology, zero track record. Grace in its purest expression", "type": "nt"},
            {"ref": "Romans 11:6", "note": "'If it is by grace, it is no longer on the basis of works; otherwise grace would no longer be grace' -- the categories are mutually exclusive", "type": "nt"},
            {"ref": "1 Corinthians 3:14-15", "note": "Work survives fire = reward. Work burned = loss. But the person is still saved -- 'though only as through fire'", "type": "nt"},
            {"ref": "Romans 14:10-12", "note": "'We will all stand before the judgment seat of God... each of us will give an account of himself' -- universal believer evaluation", "type": "nt"},
            {"ref": "Matthew 5:12", "note": "'Rejoice and be glad, for great is your reward (misthos) in heaven' -- reward language distinct from salvation language", "type": "nt"},
            {"ref": "Colossians 3:24", "note": "'You will receive the inheritance as your reward (misthos)' -- faithful service produces inheritance-reward", "type": "nt"},
            {"ref": "Titus 3:5", "note": "'He saved us, not because of works done by us in righteousness, but according to his own mercy' -- salvation is mercy, not merit", "type": "nt"}
        ],

        "divine_council_note": "The salvation-vs-reward distinction has direct divine "
                               "council implications. Salvation brings a person INTO the "
                               "family of God -- adopted as sons (huiothesia, Rom 8:15). "
                               "But reward determines what ROLE that family member will "
                               "carry in the age to come. The divine council positions "
                               "vacated by the fallen sons of God (Psalm 82) must be "
                               "filled. Every redeemed human is a potential council "
                               "member. But the degree of governing authority -- how "
                               "many cities, what scope of responsibility -- is "
                               "determined by faithfulness in the present age. Salvation "
                               "gets you into the family. Reward determines your seat "
                               "at the council table.",

        "sections": [
            {
                "heading": "The Floor and the Ceiling -- Two Categories, Not One",
                "body": "The Western tradition has largely collapsed two distinct NT "
                        "categories into one, producing confusion that distorts the "
                        "entire Christian life. Salvation (soteria) is the floor -- "
                        "the entrance into the kingdom, given by grace through faith "
                        "alone. The thief on the cross received this with zero works, "
                        "zero theological education, zero sanctification process. He "
                        "recognized the king and was promised paradise that same day "
                        "(Luke 23:43). That is charis -- unmerited favor operating "
                        "apart from human performance. 'For by grace you have been "
                        "saved through faith. And this is not your own doing; it is "
                        "the gift of God, not a result of works' (Eph 2:8-9). Paul "
                        "could not be more explicit. Salvation cannot be earned. "
                        "Reward (misthos) is entirely different. It is evaluated "
                        "based on what you did with your life. The same Paul who "
                        "wrote Ephesians 2:8-9 also wrote 1 Corinthians 3:14-15: "
                        "'If the work that anyone has built on the foundation "
                        "survives, he will receive a reward. If anyone's work is "
                        "burned up, he will suffer loss, though he himself will be "
                        "saved.' The person whose work burns is still saved -- "
                        "soteria is secure. But misthos is lost. These are not the "
                        "same category."
            },
            {
                "heading": "What the NT Actually Says -- Charis and Misthos",
                "body": "The Greek vocabulary itself enforces the distinction. Charis "
                        "(grace) is the mechanism of salvation. It is a gift (doron), "
                        "not a wage. Romans 11:6 makes the categories mutually "
                        "exclusive: 'If it is by grace, it is no longer on the basis "
                        "of works; otherwise grace would no longer be grace.' The "
                        "moment you introduce earning into salvation, you destroy "
                        "grace. But misthos (reward, wage) operates on a completely "
                        "different basis. Jesus tells his disciples, 'Rejoice and "
                        "be glad, for great is your misthos in heaven' (Matt 5:12). "
                        "Paul tells the Colossians, 'You will receive the "
                        "inheritance as your misthos' (Col 3:24). The writer of "
                        "Hebrews says God is 'a rewarder (misthapodotes) of those "
                        "who seek him' (Heb 11:6). Misthos is earned. It is "
                        "evaluated. It is differentiated. A person with great "
                        "misthos and a person with zero misthos are both saved -- "
                        "but they are not in the same position in the age to come. "
                        "Paul holds both categories simultaneously without "
                        "contradiction because they answer different questions: "
                        "charis answers 'How do I get in?' and misthos answers "
                        "'What did I do with my life once I was in?'"
            },
            {
                "heading": "Neither Purgatory Nor Equal Heaven",
                "body": "Western Christianity has produced two dominant errors by "
                        "collapsing the salvation-reward distinction. The first is "
                        "the Catholic purgatory model: salvation is not fully "
                        "accomplished at the Cross, so works (or post-mortem "
                        "purification) must complete what Christ's sacrifice did "
                        "not finish. This makes reward a component of salvation "
                        "and introduces fear-based performance as the engine of "
                        "the Christian life. But the NT is clear: 'It is finished' "
                        "(John 19:30, tetelestai -- a commercial term meaning 'paid "
                        "in full'). Christ's sacrifice is complete. Nothing is "
                        "added. The second error is the 'everyone equal in heaven' "
                        "model: since salvation is by grace, nothing you do matters "
                        "after conversion. Everyone gets the same thing. Reward is "
                        "irrelevant. But the NT explicitly teaches differentiated "
                        "reward: 'each will receive his own reward according to "
                        "his own labor' (1 Cor 3:8). Ten cities for one servant, "
                        "five for another (Luke 19:17-19). Stars differing in "
                        "glory (1 Cor 15:41-42). The texts maintain BOTH grace for "
                        "salvation AND evaluation for reward. Neither error "
                        "survives contact with the actual Greek vocabulary."
            },
            {
                "heading": "The Thief -- Grace at Its Purest",
                "body": "The thief on the cross (Luke 23:39-43) is the ultimate "
                        "test case for the salvation-reward distinction. He had no "
                        "time for works. No opportunity for sanctification. No "
                        "baptism, no communion, no theological training. He could "
                        "not attend a single gathering. He could not give a single "
                        "offering. He could not disciple a single person. He "
                        "recognized the king -- 'Jesus, remember me when you come "
                        "into your kingdom' -- and received the most extraordinary "
                        "promise in all of Scripture: 'Today you will be with me "
                        "in paradise.' That is salvation by grace through faith "
                        "alone in its purest expression. But notice what the thief "
                        "could not receive: reward for a life of faithfulness. "
                        "He enters the kingdom. He does not enter it with ten "
                        "cities of governing authority. He does not bring a crown "
                        "of rejoicing earned through lives he led to the king. He "
                        "does not carry treasure accumulated through decades of "
                        "faithful stewardship. He is saved. He is not rewarded. "
                        "And the distinction matters -- because what the thief "
                        "could not do, you still can."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 2: WHY THIS DISTINCTION MATTERS
    # =========================================================================
    {
        "id": "salvation-vs-reward-2",
        "ref": "1 Corinthians 15:58; 2 Timothy 4:7-8; Psalm 51:1-4",
        "chapter_num": 2,
        "title": "Why This Distinction Matters -- Motivation",
        "era": "salvation_vs_reward",
        "type": "chapter",

        "synopsis": "The salvation-reward distinction is not an academic exercise -- "
                    "it reshapes the entire motivation for the Christian life. Wrong "
                    "motivation (fear of hell, guilt, trying to earn salvation) "
                    "produces external compliance without internal transformation. "
                    "Right motivation (vision, stewardship, the king is coming) "
                    "produces the kind of person the king is preparing for governing "
                    "authority in the new creation. Paul's climactic statement after "
                    "the great resurrection chapter says it all: 'Your labor is NOT "
                    "in vain in the Lord' (1 Cor 15:58). Everything counts.",

        "key_verse": {
            "ref": "1 Corinthians 15:58",
            "text": "Therefore, my beloved brothers, be steadfast, immovable, "
                    "always abounding in the work of the Lord, knowing that in "
                    "the Lord your labor is not in vain.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u03ba\u03b5\u03bd\u03cc\u03c2 (kenos)",
                "meaning": "Empty, vain, without result. Paul says your labor is NOT "
                           "kenos -- not empty, not without effect, not purposeless. "
                           "Every act of faithfulness produces something permanent. "
                           "This is the opposite of futility -- it is the guarantee "
                           "that nothing done in the Lord evaporates."
            },
            {
                "term": "\u03ba\u03cc\u03c0\u03bf\u03c2 (kopos)",
                "meaning": "Toil, labor, hard work that costs something. Not casual "
                           "effort but exertion. Paul uses kopos for the actual work "
                           "of faithful living -- the kind of effort that requires "
                           "sacrifice. This labor, he says, is never kenos in the "
                           "Lord. The cost is real, but so is the result."
            },
            {
                "term": "\u03c0\u03b5\u03c1\u03b9\u03c3\u03c3\u03b5\u03cd\u03c9 (perisseuo)",
                "meaning": "To abound, overflow, exceed, have more than enough. "
                           "Paul commands believers to be 'always abounding' -- "
                           "perisseuontes -- in the work of the Lord. Not minimal "
                           "compliance but overflow. The motivation is not 'do "
                           "enough to avoid punishment' but 'abound because the "
                           "investment is worth it.'"
            }
        ],

        "ane_backdrop": "In the ancient Near Eastern royal court, servants who served "
                        "the king faithfully were rewarded with land grants, elevated "
                        "titles, and greater access to the king's presence. The Amarna "
                        "letters preserve examples of Egyptian vassal kings writing to "
                        "Pharaoh seeking reward for faithful service. The motivation "
                        "was not fear of execution (though that existed) but desire for "
                        "the king's favor and the tangible benefits that came with it. "
                        "The biblical reward framework operates similarly: the king is "
                        "coming, and faithful servants are preparing for an evaluation "
                        "that determines their role in the coming kingdom.",

        "second_temple": [
            {
                "source": "Wisdom of Solomon 3:1-9",
                "summary": "According to the Wisdom of Solomon, the righteous who "
                           "endured testing 'will govern nations and rule over "
                           "peoples, and the Lord will reign over them forever.' "
                           "Endurance in the present age leads to governing authority "
                           "in the age to come.",
                "relevance": "This text demonstrates the Second Temple expectation "
                             "that faithful endurance produces differentiated reward "
                             "in the form of governing authority -- precisely the "
                             "framework Jesus teaches in the parable of the minas."
            },
            {
                "source": "2 Baruch 51:1-6",
                "summary": "According to 2 Baruch, the righteous in the age to come "
                           "will be transformed and 'made like the angels and made "
                           "equal to the stars' -- with differentiated glory that "
                           "reflects their faithfulness.",
                "relevance": "Parallels Paul's differentiated resurrection glory in "
                             "1 Corinthians 15:41-42 and Daniel's 'shining like "
                             "stars' in Daniel 12:3. The Second Temple world "
                             "expected the new creation to be differentiated, not "
                             "uniform."
            }
        ],

        "cross_refs": [
            {"ref": "1 Corinthians 15:58", "note": "'Your labor is NOT in vain in the Lord' -- Paul's climactic motivation statement after the resurrection chapter", "type": "nt"},
            {"ref": "2 Timothy 4:7-8", "note": "'I have fought the good fight, I have finished the race... the crown of righteousness' -- Paul's personal example of vision-driven faithfulness", "type": "nt"},
            {"ref": "Psalm 51:1-4", "note": "David's model: catastrophic sin followed by running TOWARD Yahweh, not guilt-driven paralysis. Honest relationship, not performance", "type": "ot"},
            {"ref": "Matthew 6:10", "note": "'Your kingdom come' -- eltheto, aorist imperative: cause it to come. Not a vague wish but a command-prayer from genuine longing", "type": "nt"},
            {"ref": "Hebrews 11:6", "note": "'Without faith it is impossible to please him... he is a rewarder (misthapodotes) of those who seek him' -- God Himself is a rewarder", "type": "nt"},
            {"ref": "Philippians 3:13-14", "note": "'I press on toward the goal for the prize of the upward call of God in Christ Jesus' -- the race metaphor with eyes forward", "type": "nt"},
            {"ref": "Hebrews 12:1-2", "note": "'Let us run with endurance the race set before us, looking to Jesus' -- Jesus Himself ran for the joy set before him", "type": "nt"},
            {"ref": "1 John 2:28", "note": "'Abide in him, so that when he appears we may have confidence and not shrink from him in shame at his coming'", "type": "nt"}
        ],

        "divine_council_note": "The motivation question connects directly to the "
                               "divine council framework. The fallen sons of God in "
                               "Psalm 82 failed precisely because they served with "
                               "wrong motivation -- corrupting their stewardship for "
                               "self-aggrandizement rather than faithfully executing "
                               "Yahweh's purposes. Believers being prepared as their "
                               "replacements must develop the opposite character: "
                               "faithful stewardship motivated by love for the king "
                               "and vision for what he is building. The bema "
                               "evaluation is not merely about WHAT you did but WHO "
                               "you became in the process. Character, not just "
                               "output, is what qualifies a person for council "
                               "authority.",

        "sections": [
            {
                "heading": "The Wrong Motivations -- Fear, Guilt, and Earning",
                "body": "Three wrong motivations dominate Western Christianity, and "
                        "each one distorts the Christian life. The first is fear of "
                        "hell: 'Do the right thing or you will burn.' Fear is real "
                        "-- the fear of the Lord is the beginning of wisdom (Prov "
                        "9:10) -- but fear of punishment as the primary engine of "
                        "faithfulness produces external compliance without internal "
                        "transformation. A person doing the right thing only to "
                        "avoid punishment is not the kind of person the king is "
                        "preparing for governing authority. The second is guilt: "
                        "'You have failed, you are not enough, you should do more.' "
                        "Guilt produces paralysis and shame, not purposeful action. "
                        "David sinned catastrophically -- adultery and murder -- and "
                        "ran TOWARD Yahweh in Psalm 51, not away from him in guilt-"
                        "driven paralysis. 'Against you, you only, have I sinned' "
                        "(Ps 51:4). That is the model: honest relationship with the "
                        "covenant God, not performance-driven self-flagellation. The "
                        "third is earning salvation: 'I must work hard enough to "
                        "deserve heaven.' This contradicts grace entirely. If works "
                        "could earn the entrance, Christ died for nothing (Gal 2:21)."
            },
            {
                "heading": "The Right Motivation -- Vision, Not Pressure",
                "body": "The NT motivation for faithful living is not fear, guilt, "
                        "or earning -- it is vision. The king is coming. He gave "
                        "you something to steward. He expects it to have grown. "
                        "Not because you earn the kingdom by growing it -- grace "
                        "gives the entrance freely. But because what you do with "
                        "what you have been given shapes who you will be when he "
                        "returns and what role you will carry in the age to come. "
                        "Paul's climactic statement in 1 Corinthians 15:58 comes "
                        "immediately after the great resurrection chapter. After "
                        "establishing that Christ has risen, that death is defeated, "
                        "that resurrection bodies are coming, that the last enemy "
                        "is destroyed -- he says: 'Therefore, my beloved brothers, "
                        "be steadfast, immovable, always abounding in the work of "
                        "the Lord, knowing that in the Lord your labor is NOT in "
                        "vain.' The word 'therefore' (hoste) connects everything. "
                        "BECAUSE resurrection is real, BECAUSE the new creation is "
                        "coming, BECAUSE you will carry into it what you built here "
                        "-- abound. Overflow. Not because you are afraid but because "
                        "the investment is worth infinitely more than the cost."
            },
            {
                "heading": "Paul's Personal Example -- 2 Timothy 4:7-8",
                "body": "At the end of his life, facing execution, Paul writes his "
                        "final letter to Timothy. His words are not guilt-ridden "
                        "or fear-driven. They are triumphant: 'I have fought the "
                        "good fight, I have finished the race, I have kept the "
                        "faith. Henceforth there is laid up for me the crown of "
                        "righteousness, which the Lord, the righteous judge, will "
                        "award to me on that day' (2 Tim 4:7-8). Notice the "
                        "language. 'Fought the good fight' -- agon, the athletic "
                        "contest. 'Finished the race' -- dromos, the course. 'Kept "
                        "the faith' -- tereo, guarded, maintained. And then the "
                        "reward: a stephanos (crown) of righteousness. Paul is not "
                        "afraid of the bema. He is anticipating it. He ran the race "
                        "with his eyes on the prize (Phil 3:14) and is confident "
                        "that the righteous judge will award what was earned through "
                        "a life of faithful service. This is the tone the NT "
                        "produces when the salvation-reward distinction is properly "
                        "understood: not anxiety but anticipation. Not performance "
                        "pressure but purposeful confidence. The king is coming, "
                        "and what you built for him will be evaluated -- and if you "
                        "ran well, the evaluation is something to look forward to."
            },
            {
                "heading": "Your Labor Is Not in Vain -- The Guarantee",
                "body": "The word kenos (vain, empty) in 1 Corinthians 15:58 is the "
                        "lynchpin. Paul guarantees that labor done 'in the Lord' is "
                        "never kenos -- never without result, never purposeless, "
                        "never wasted. Every act of faithfulness counts. Every seed "
                        "planted. Every cup of cold water given in his name (Matt "
                        "10:42 -- 'he will by no means lose his misthos'). Every "
                        "child raised toward Yahweh. Every honest day of work. Every "
                        "person shown the love of the covenant God. It is all "
                        "permanently recorded, permanently evaluated, permanently "
                        "expressed in who you will be in the new creation. This is "
                        "the most ennobling truth in the entire biblical framework. "
                        "You are not waiting to die and float in a cloud. You are "
                        "training for a throne. You are being prepared for governing "
                        "authority in the renewed creation. What you do right now -- "
                        "today, this week, this year -- has weight that extends into "
                        "eternity. Not because you earn salvation by it, but because "
                        "the king who saved you by grace is also the righteous judge "
                        "who will reward faithfulness. That is not burden -- it is "
                        "the most extraordinary invitation ever extended to a human "
                        "being."
            }
        ]
    }
]
