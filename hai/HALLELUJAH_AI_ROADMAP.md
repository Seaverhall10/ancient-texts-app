# HALLELUJAH AI — Roadmap

**Last Updated**: 2026-03-02

---

## SHORT TERM (This Week)

### Critical Path — Get It Running End-to-End

- [ ] **Fix Python PATH in LAUNCH_AI.bat** — Use full path to python.exe so batch file works without PATH configured
- [ ] **Rebuild the HTML** — Run `build.py` to compile new app.js/styles.css into output/AncientTextsStudy.html
- [ ] **Test chat in actual app** — Open PyWebView app, open chat drawer, send a message, verify streaming works
- [ ] **GPU acceleration check** — Verify Ollama is using GPU (NVIDIA or AMD) for faster inference
- [ ] **Improve A/B/C/U compliance** — Tune system prompt so Mistral actually labels claims consistently
- [ ] **Test context sync** — Click "Ask about this chapter" while viewing Genesis 1, verify context flows into prompt
- [ ] **Fix first-load timeout** — Pre-warm the model on server startup so first query doesn't take 90 seconds

### Quick Wins
- [ ] **Add conversation export** — Button to save current chat as Markdown file
- [ ] **Add model info badge** — Show model name + parameter count in chat header
- [ ] **Error handling polish** — Better error messages when Ollama is down or model not loaded
- [ ] **Keyboard shortcuts** — Alt+A to toggle chat (already coded), Ctrl+Enter to send, Esc to close

---

## MEDIUM TERM (This Month)

### Model Improvements
- [ ] **Try larger models** — Pull `llama3.1:8b`, `qwen2.5:14b`, or `mixtral:8x7b` for better label compliance
- [ ] **Custom Modelfile** — Create Ollama Modelfile with pre-baked system prompt for faster loading
- [ ] **Temperature tuning** — Test different temperatures for study vs. creative vs. counseling modes
- [ ] **Context window optimization** — Measure how much study context fits before quality degrades

### RAG (Retrieval-Augmented Generation)
- [ ] **SQLite FTS5 index** — Index all study content (750 chapters, 22K flow verses, 553 glossary terms)
- [ ] **Glossary auto-lookup** — When user mentions a Hebrew/Greek term, auto-inject glossary definition into context
- [ ] **Cross-reference injection** — When discussing a passage, auto-include related cross-refs from the app's database
- [ ] **Interlinear word lookup** — Pull original language words for any verse mentioned in conversation

### New Modes
- [ ] **Scholar Mode** — Deep Hebrew/Greek analysis with morphology parsing
- [ ] **Prophecy Mode** — Auto-activate when in prophecy sections, use fulfillment matrix
- [ ] **Scripture Finder** — "What does the Bible say about..." → curated verse list

### UI Enhancements
- [ ] **Message reactions** — Thumbs up/down on AI responses for quality tracking
- [ ] **Chat tabs** — Multiple simultaneous conversations (study, devotional, research)
- [ ] **Markdown copy button** — One-click copy of AI response as formatted Markdown
- [ ] **Source cards** — Show which study content was used in the response

---

## LONG TERM (Next 3 Months)

### Behavioral Analysis Engine
- [ ] **Conversation pattern tracking** — What topics come up repeatedly? What emotions surface?
- [ ] **Personality profiling** — Based on question style, vocabulary, concerns → biblical personality analysis
- [ ] **Growth metrics** — Track spiritual maturity indicators across sessions
- [ ] **Flaw identification** — Honest, loving diagnosis based on patterns (Proverbs-style)
- [ ] **Raw Mode** — Unfiltered input (voice-to-text, no-backspace) for authentic emotional analysis

### Study Planning Suite
- [ ] **Bible study planner** — Multi-week plans based on goals, interests, time
- [ ] **Quiet time planner** — Daily devotional generator with Scripture, reflection, prayer
- [ ] **Reading schedule** — Chronological, thematic, or custom Bible reading plans
- [ ] **Progress tracker** — What you've studied, what's left, streaks, milestones

### Self-Reflection Tool
- [ ] **Conversation analytics dashboard** — Visual breakdown of all chats: topics, emotions, frequency
- [ ] **Mirror mode** — AI reflects back what it sees in your patterns, honestly
- [ ] **Spiritual health score** — Composite metric: study consistency, question depth, emotional patterns
- [ ] **Accountability prompts** — Regular check-ins based on identified growth areas

### Multi-Domain Expert Modes
- [ ] **Biblical archaeology mode** — ANE context, artifact analysis, archaeological evidence
- [ ] **Genetics/DNA mode** — Nations table analysis, haplogroup mapping, Nephilim genetics discussion
- [ ] **Astrophysics mode** — Cosmic fine-tuning arguments, biblical cosmology, creation science
- [ ] **World religions comparison** — Side-by-side analysis through Scripture-first lens
- [ ] **Church history mode** — Patristics, councils, reformation, denominational analysis

### Technical Infrastructure
- [ ] **Conversation persistence** — Optional SQLite storage for chat history (encrypted at rest)
- [ ] **Multi-model routing** — Different models for different tasks (fast model for search, big model for study)
- [ ] **Plugin system** — Allow community-created policy files and mode extensions
- [ ] **Mobile app** — Convert to Capacitor/Cordova for iOS/Android with local model support
- [ ] **Offline Bible corpus** — Bundle KJV/ASV for full-text search without internet

---

## STRETCH GOALS (6+ Months)

### Security & Monitoring Suite
- [ ] **Home security integration** — Local camera feed analysis, motion detection alerts
- [ ] **Weather/solar tracker** — Space weather, solar flare alerts, geo-engineering analysis
- [ ] **Current events filter** — RSS/news feed analysis through biblical worldview lens
- [ ] **OSINT toolkit** — Open-source intelligence gathering, all local processing

### AI Training
- [ ] **Custom fine-tuning** — Fine-tune a model specifically on biblical texts and theological content
- [ ] **User feedback loop** — Use thumbs up/down data to improve responses over time
- [ ] **Multi-agent council** — Multiple specialized AI agents debating and refining answers

### Distribution
- [ ] **Standalone installer** — Single .exe that installs Python, Ollama, model, and app
- [ ] **USB-portable version** — Run from a USB drive with no installation needed
- [ ] **Family sharing** — Multi-user profiles with separate conversation histories

---

## Priority Matrix

| Priority | Item | Effort | Impact |
|----------|------|--------|--------|
| P0 | Fix PATH + rebuild HTML | 30 min | Must have — app won't work without it |
| P0 | Test in actual PyWebView app | 15 min | Must verify end-to-end |
| P1 | Improve A/B/C/U compliance | 2 hrs | Core value proposition |
| P1 | GPU acceleration check | 15 min | 5-10x speed improvement |
| P1 | Pre-warm model on startup | 30 min | UX — no 90s first-query delay |
| P2 | RAG index (SQLite FTS5) | 4 hrs | Massive quality improvement |
| P2 | Scholar Mode | 2 hrs | High user demand |
| P2 | Scripture Finder | 3 hrs | High practical value |
| P3 | Behavioral analysis engine | 8 hrs | Unique differentiator |
| P3 | Raw Mode | 4 hrs | Authentic spiritual insight tool |
| P3 | Study planner suite | 6 hrs | Practical daily use |
