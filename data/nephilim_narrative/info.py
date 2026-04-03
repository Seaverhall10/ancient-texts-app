"""
The Nephilim Story — A Narrative with Adjustable Evidence Levels

A continuous timeline-article telling the full Nephilim story from Genesis 6
through the Conquest through David, with evidence-tier filtering that lets
readers choose their source level:

  [A] Canon Only — Hebrew Bible + NT (for conservative readers)
  [A+B] Canon + Inference — + Hebrew analysis, divine council framework
  [A+B+C] Full Picture — + 1 Enoch, DSS, ANE parallels, church history

The objective: by the end of [A] mode, a conservative reader would WANT
to look at 1 Enoch, because the canonical text raises questions only Enoch
answers.
"""

TEXT_INFO = {
    "display_name": "The Nephilim Story",
    "full_title": "The Nephilim Story: From Genesis 6 to the Last Giants of Gath",
    "category": "study",
    "is_narrative": True,

    "description": (
        "A continuous narrative tracing the Nephilim through Scripture, "
        "from the boundary violation of Genesis 6 through the giant clans "
        "of Canaan, David's battles with the last giants of Gath, and the "
        "New Testament's confirmation of the supernatural reading. Features "
        "an evidence-tier toggle so readers can start with canon only and "
        "progressively reveal deeper layers of evidence."
    ),

    "how_to_read": (
        "Start in Canon Only mode — read what your Bible actually says about "
        "the Nephilim, giants, and fallen angels. Let the text raise its own "
        "questions. Then switch to Canon + Inference to see what the Hebrew "
        "and Greek reveal beneath the English. Finally, unlock the Full Picture "
        "to see how 1 Enoch, the Dead Sea Scrolls, and ancient Near Eastern "
        "parallels complete the story."
    ),

    "evidence_tiers": {
        "a": {
            "label": "Canon Only",
            "description": "Hebrew Bible and New Testament passages only",
            "color": "#6aab73",
            "for_who": "Conservative readers, Bible-first students"
        },
        "b": {
            "label": "Canon + Inference",
            "description": "Hebrew/Greek analysis, divine council framework, theological connections",
            "color": "#5b8dbf",
            "for_who": "Serious students who want the original languages"
        },
        "c": {
            "label": "Full Picture",
            "description": "1 Enoch, Jubilees, Dead Sea Scrolls, ANE parallels, church history",
            "color": "#9b7ec8",
            "for_who": "Researchers who want everything"
        }
    },

    "theological_framework": (
        "This narrative operates within the three-rebellions framework: "
        "Eden (Nachash), Hermon (200 Watchers), and Babel (nations assigned "
        "to corrupt sons of God). These are three INDEPENDENT rebellions, "
        "not one continuous chain. The Nephilim are the physical legacy of "
        "the SECOND rebellion (Hermon), and their story runs from Genesis 6 "
        "through 2 Samuel 21."
    ),

    "reader_notes": [
        {
            "title": "Evidence Tiers Explained",
            "type": "context",
            "body": (
                "This study uses a three-tier evidence system throughout. "
                "[A] marks claims supported by direct canonical Scripture. "
                "[B] marks valid inferences from the Hebrew and Greek text, "
                "scholarly consensus, or theological framework. [C] marks "
                "ancient parallels from 1 Enoch, Dead Sea Scrolls, Josephus, "
                "and ancient Near Eastern texts. You can filter which tiers "
                "are visible using the toggle at the top of each chapter."
            )
        },
        {
            "title": "For the Skeptical Reader",
            "type": "context",
            "body": (
                "If the idea of 'giants in the Bible' sounds like mythology, "
                "start in Canon Only mode. Every claim in tier [A] comes from "
                "the ESV text of the Protestant canon — Genesis, Numbers, "
                "Deuteronomy, Joshua, 1-2 Samuel, Jude, 2 Peter. No extra-biblical "
                "sources. No speculation. Just what your Bible says, read in "
                "sequence for the first time."
            )
        }
    ]
}
