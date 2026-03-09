/**
 * Hallelujah AI — Full-Screen Chat Logic
 * Bible-bound AI conversation with RAG knowledge integration.
 * Supports multiple modes: General, Bible Study, Berean Protocol, Dev Mode.
 *
 * "Test all things; hold fast what is good." — 1 Thessalonians 5:21
 */
(function() {
    'use strict';

    var API = window.location.origin;
    var chatMessages = document.getElementById('chatMessages');
    var chatInput = document.getElementById('chatInput');
    var sendBtn = document.getElementById('sendBtn');
    var modelBadge = document.getElementById('modelName');
    var modelDot = document.getElementById('modelDot');
    var modeBanner = document.getElementById('modeBanner');
    var modeBannerText = document.getElementById('modeBannerText');
    var modeBannerIcon = modeBanner ? modeBanner.querySelector('.mode-banner-icon') : null;

    // State
    var history = [];
    var isStreaming = false;
    var bibleBound = true;
    var analysisMode = true;
    var showAudit = false;
    var currentModel = null;
    var showWelcome = true;
    var currentMode = 'general';

    // Mode metadata
    var MODE_INFO = {
        general: {
            icon: '\uD83D\uDCAC',
            label: 'General',
            banner: 'General \u2014 versatile assistant, expert on Scripture and study content',
            placeholder: 'Ask about Scripture, Hebrew terms, prophecy, theology, or anything...',
            welcome: 'Ask about anything \u2014 Scripture, theology, Hebrew/Greek terms, prophecy, history, science, philosophy, or daily life. I speak with conviction and back every claim with evidence.'
        },
        bible_study: {
            icon: '\uD83D\uDCDC',
            label: 'Bible Study',
            banner: 'Bible Study \u2014 deep original text analysis, Hebrew/Greek, manuscripts',
            placeholder: 'Enter a passage, Hebrew/Greek word, or theological concept...',
            welcome: 'Bible Study Mode \u2014 deep dive into original text. I\'ll show you Hebrew/Greek words, Strong\'s numbers, ANE context, manuscript evidence, and what the text ACTUALLY means. Tables, cross-references, and scholarly analysis.'
        },
        berean: {
            icon: '\uD83D\uDD0D',
            label: 'Berean Protocol',
            banner: 'Berean Protocol \u2014 critical analysis, evidence over narrative',
            placeholder: 'Enter a claim, narrative, or topic to analyze critically...',
            welcome: 'Berean Protocol \u2014 rigorous evidence-based analysis. I\'ll state the mainstream claim, list assumptions, test against physical evidence, catalog anomalies, follow the money, and rate on the E1-E6 scale. No sacred cows. Truth over narrative.'
        },
        dev: {
            icon: '\uD83D\uDEE0',
            label: 'Dev Mode',
            banner: 'Dev Mode \u2014 improvement workshop, tune AI behavior',
            placeholder: 'Ask a question, then I\'ll help you improve how I respond...',
            welcome: 'Dev Mode \u2014 help me get better. Ask any question and after I respond, I\'ll ask YOU for feedback: What did you expect? Was the tone right? What was missing? Rate me 1-10. Together we\'ll build better reasoning patterns.'
        }
    };

    // ── Initialize ──────────────────────────────────
    function init() {
        checkHealth();
        loadHistory();
        bindEvents();
        updateModeUI();

        // Auto-focus input
        chatInput.focus();

        // Health check every 30s
        setInterval(checkHealth, 30000);
    }

    // ── Health Check ────────────────────────────────
    function checkHealth() {
        fetch(API + '/health')
            .then(function(r) { return r.json(); })
            .then(function(data) {
                if (data.ollama && data.ollama.status === 'connected') {
                    modelDot.className = 'chat-model-dot green';
                    var model = data.ollama.default_model || 'unknown';
                    if (data.ollama.models && data.ollama.models.length > 0) {
                        model = data.ollama.models[0];
                    }
                    modelBadge.textContent = model;
                    currentModel = model;
                } else {
                    modelDot.className = 'chat-model-dot';
                    modelBadge.textContent = 'offline';
                }
            })
            .catch(function() {
                modelDot.className = 'chat-model-dot';
                modelBadge.textContent = 'offline';
            });
    }

    // ── Event Bindings ──────────────────────────────
    function bindEvents() {
        // Send button
        sendBtn.addEventListener('click', sendMessage);

        // Enter to send (Shift+Enter for newline)
        chatInput.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });

        // Auto-resize textarea
        chatInput.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = Math.min(this.scrollHeight, 180) + 'px';
        });

        // Mode selector buttons
        document.querySelectorAll('.mode-btn').forEach(function(btn) {
            btn.addEventListener('click', function() {
                var newMode = this.dataset.mode;
                if (newMode === currentMode) return;

                // Update active state
                document.querySelectorAll('.mode-btn').forEach(function(b) {
                    b.classList.remove('active');
                });
                this.classList.add('active');

                currentMode = newMode;
                updateModeUI();
                saveModePreference();

                // Announce mode change in chat
                if (!showWelcome) {
                    addSystemMessage('Switched to ' + MODE_INFO[currentMode].label + ' mode');
                }
            });
        });

        // Toolbar toggles
        document.querySelectorAll('.toolbar-toggle').forEach(function(btn) {
            btn.addEventListener('click', function() {
                var toggle = this.dataset.toggle;
                if (!toggle) return; // Skip New Chat button
                this.classList.toggle('active');
                if (toggle === 'bible-bound') bibleBound = this.classList.contains('active');
                if (toggle === 'audit') {
                    showAudit = this.classList.contains('active');
                    document.querySelectorAll('.msg-audit').forEach(function(el) {
                        el.classList.toggle('visible', showAudit);
                    });
                }
            });
        });

        // Settings modal
        document.getElementById('settingsBtn').addEventListener('click', openSettings);
        document.getElementById('settingsClose').addEventListener('click', closeSettings);
        document.getElementById('settingsOverlay').addEventListener('click', function(e) {
            if (e.target === this) closeSettings();
        });

        // New chat
        document.getElementById('newChatBtn').addEventListener('click', function() {
            history = [];
            saveHistory();
            showWelcome = true;
            renderWelcome();
        });

        // Load saved mode preference
        loadModePreference();
    }

    // ── Mode UI Updates ─────────────────────────────
    function updateModeUI() {
        var info = MODE_INFO[currentMode];
        if (!info) return;

        // Update banner
        if (modeBannerIcon) modeBannerIcon.textContent = info.icon;
        if (modeBannerText) modeBannerText.textContent = info.banner;

        // Update banner color class
        if (modeBanner) {
            modeBanner.className = 'mode-banner mode-banner-' + currentMode;
        }

        // Update input placeholder
        chatInput.placeholder = info.placeholder;

        // Update welcome if showing
        if (showWelcome) renderWelcome();

        // Update analysis_mode based on mode
        analysisMode = (currentMode === 'berean');
    }

    function saveModePreference() {
        try { localStorage.setItem('hai-mode', currentMode); } catch(e) {}
    }

    function loadModePreference() {
        try {
            var saved = localStorage.getItem('hai-mode');
            if (saved && MODE_INFO[saved]) {
                currentMode = saved;
                document.querySelectorAll('.mode-btn').forEach(function(b) {
                    b.classList.toggle('active', b.dataset.mode === currentMode);
                });
                updateModeUI();
            }
        } catch(e) {}
    }

    // ── Send Message ────────────────────────────────
    function sendMessage() {
        var text = chatInput.value.trim();
        if (!text || isStreaming) return;

        // Remove welcome screen
        if (showWelcome) {
            showWelcome = false;
            chatMessages.innerHTML = '';
        }

        // Add user message
        addMessage('user', text);
        history.push({ role: 'user', content: text });

        // Clear input
        chatInput.value = '';
        chatInput.style.height = 'auto';

        // Start streaming response
        streamResponse(text);
    }

    // ── Stream Response from Backend ────────────────
    function streamResponse(message) {
        isStreaming = true;
        sendBtn.disabled = true;

        // Create assistant message placeholder
        var msgEl = addMessage('assistant', '', true);
        var contentEl = msgEl.querySelector('.msg-content');

        var fullResponse = '';

        fetch(API + '/chat/stream', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                message: message,
                history: history.slice(-20),  // Last 20 messages for context
                model: currentModel,
                temperature: 0.7,
                bible_bound: bibleBound,
                analysis_mode: analysisMode,
                study_context: null,
                mode: currentMode
            })
        })
        .then(function(response) {
            var reader = response.body.getReader();
            var decoder = new TextDecoder();
            var buffer = '';

            function readChunk() {
                reader.read().then(function(result) {
                    if (result.done) {
                        finishStream(msgEl, fullResponse);
                        return;
                    }

                    buffer += decoder.decode(result.value, { stream: true });
                    var lines = buffer.split('\n');
                    buffer = lines.pop();  // Keep incomplete line

                    lines.forEach(function(line) {
                        if (!line.startsWith('data: ')) return;
                        try {
                            var data = JSON.parse(line.substring(6));
                            if (data.token) {
                                fullResponse += data.token;
                                contentEl.innerHTML = renderMarkdown(fullResponse) +
                                    '<span class="typing-cursor"></span>';
                                scrollToBottom();
                            }
                            if (data.done) {
                                finishStream(msgEl, fullResponse, data.audit);
                            }
                            if (data.error) {
                                contentEl.innerHTML = '<em style="color:var(--label-u)">Error: ' +
                                    escHtml(data.error) + '</em>';
                                isStreaming = false;
                                sendBtn.disabled = false;
                            }
                        } catch (e) { /* ignore parse errors from partial chunks */ }
                    });

                    readChunk();
                });
            }

            readChunk();
        })
        .catch(function(err) {
            contentEl.innerHTML = '<em style="color:var(--label-u)">Connection error: ' +
                escHtml(err.message) + '</em>';
            isStreaming = false;
            sendBtn.disabled = false;
        });
    }

    function finishStream(msgEl, fullResponse, audit) {
        isStreaming = false;
        sendBtn.disabled = false;

        var contentEl = msgEl.querySelector('.msg-content');
        contentEl.innerHTML = renderMarkdown(fullResponse);

        // Add to history
        history.push({ role: 'assistant', content: fullResponse });
        saveHistory();

        // Show audit if enabled
        if (audit) {
            var auditEl = msgEl.querySelector('.msg-audit');
            if (auditEl) {
                auditEl.innerHTML = renderAudit(audit);
                if (showAudit) auditEl.classList.add('visible');
            }
        }

        scrollToBottom();
        chatInput.focus();
    }

    // ── Add Message to UI ───────────────────────────
    function addMessage(role, content, isPlaceholder) {
        var div = document.createElement('div');
        div.className = 'chat-msg ' + role;

        var roleLabel = role === 'user' ? 'You' : 'Hallelujah AI';
        if (role === 'assistant' && currentMode !== 'general') {
            roleLabel += ' \u2022 ' + MODE_INFO[currentMode].label;
        }

        var html = '<span class="msg-role">' + roleLabel + '</span>';
        html += '<div class="msg-content">';

        if (isPlaceholder) {
            html += '<span class="typing-cursor"></span>';
        } else {
            html += renderMarkdown(content);
        }

        html += '</div>';

        if (role === 'assistant') {
            html += '<div class="msg-audit"></div>';
        }

        div.innerHTML = html;
        chatMessages.appendChild(div);
        scrollToBottom();
        return div;
    }

    function addSystemMessage(text) {
        var div = document.createElement('div');
        div.className = 'chat-msg system';
        div.innerHTML = '<div class="msg-content">' + escHtml(text) + '</div>';
        chatMessages.appendChild(div);
        scrollToBottom();
    }

    // ── Render Markdown ─────────────────────────────
    function renderMarkdown(text) {
        if (!text) return '';

        var html = escHtml(text);

        // Bold
        html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
        // Italic
        html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');
        // Code blocks
        html = html.replace(/```(\w*)\n([\s\S]*?)```/g,
            '<pre style="background:rgba(0,0,0,0.3);padding:10px;border-radius:6px;overflow-x:auto;font-size:0.82em;margin:8px 0"><code>$2</code></pre>');
        // Inline code
        html = html.replace(/`([^`]+)`/g,
            '<code style="background:rgba(0,0,0,0.3);padding:1px 5px;border-radius:3px;font-size:0.88em">$1</code>');

        // Markdown tables
        html = renderTables(html);

        // Headers
        html = html.replace(/^#### (.+)$/gm, '<h5 style="color:var(--gold);margin:10px 0 3px;font-family:var(--font-heading);font-size:0.88em">$1</h5>');
        html = html.replace(/^### (.+)$/gm, '<h4 style="color:var(--gold);margin:12px 0 4px;font-family:var(--font-heading);font-size:0.95em">$1</h4>');
        html = html.replace(/^## (.+)$/gm, '<h3 style="color:var(--gold);margin:14px 0 6px;font-family:var(--font-heading);font-size:1.05em">$1</h3>');
        // Lists
        html = html.replace(/^- (.+)$/gm, '<div style="padding-left:16px;position:relative;margin:2px 0"><span style="position:absolute;left:4px;color:var(--gold)">&#x2022;</span>$1</div>');
        html = html.replace(/^\d+\)\s?(.+)$/gm, '<div style="padding-left:20px;margin:2px 0">$1</div>');
        html = html.replace(/^\d+\.\s?(.+)$/gm, '<div style="padding-left:20px;margin:2px 0">$1</div>');
        // Paragraphs
        html = html.replace(/\n\n/g, '</p><p style="margin:8px 0">');
        html = html.replace(/\n/g, '<br>');

        // Claim labels: [A], [B], [C], [U]
        html = html.replace(/\[A\]/g, '<span class="claim-label claim-label-a">[A]</span>');
        html = html.replace(/\[B\]/g, '<span class="claim-label claim-label-b">[B]</span>');
        html = html.replace(/\[C\]/g, '<span class="claim-label claim-label-c">[C]</span>');
        html = html.replace(/\[U\]/g, '<span class="claim-label claim-label-u">[U]</span>');

        // Evidence confidence labels: E1-E6
        html = html.replace(/\b(E[1-6])\b/g, '<span class="evidence-label">$1</span>');

        return '<p style="margin:8px 0">' + html + '</p>';
    }

    // ── Render Markdown Tables ──────────────────────
    function renderTables(html) {
        // Match markdown table blocks (header | separator | rows)
        var tableRegex = /^(\|.+\|)\n(\|[\s\-:|]+\|)\n((?:\|.+\|\n?)+)/gm;

        return html.replace(tableRegex, function(match, header, separator, body) {
            var headerCells = header.split('|').filter(function(c) { return c.trim(); });
            var bodyRows = body.trim().split('\n');

            var tableHtml = '<table class="md-table"><thead><tr>';
            headerCells.forEach(function(cell) {
                tableHtml += '<th>' + cell.trim() + '</th>';
            });
            tableHtml += '</tr></thead><tbody>';

            bodyRows.forEach(function(row) {
                var cells = row.split('|').filter(function(c) { return c.trim(); });
                tableHtml += '<tr>';
                cells.forEach(function(cell) {
                    tableHtml += '<td>' + cell.trim() + '</td>';
                });
                tableHtml += '</tr>';
            });

            tableHtml += '</tbody></table>';
            return tableHtml;
        });
    }

    // ── Render Audit Trail ──────────────────────────
    function renderAudit(audit) {
        if (!audit) return '';
        var html = '<div class="audit-labels">';
        var labels = audit.labels || {};
        html += '<span class="audit-label" style="color:var(--label-a)">A: ' + (labels.A || 0) + '</span>';
        html += '<span class="audit-label" style="color:var(--label-b)">B: ' + (labels.B || 0) + '</span>';
        html += '<span class="audit-label" style="color:var(--label-c)">C: ' + (labels.C || 0) + '</span>';
        html += '<span class="audit-label" style="color:var(--label-u)">U: ' + (labels.U || 0) + '</span>';
        if (audit.score !== undefined) {
            html += '<span style="margin-left:auto">Score: ' + audit.score + '/100</span>';
        }
        html += '</div>';
        if (audit.flags && audit.flags.length) {
            html += '<div style="margin-top:4px;color:var(--label-u);font-size:0.68rem">';
            audit.flags.forEach(function(f) { html += f + '<br>'; });
            html += '</div>';
        }
        return html;
    }

    // ── Welcome Screen ──────────────────────────────
    function renderWelcome() {
        var info = MODE_INFO[currentMode];
        chatMessages.innerHTML = '<div class="chat-welcome">' +
            '<div class="welcome-icon">' + info.icon + '</div>' +
            '<div class="welcome-title">Hallelujah AI</div>' +
            '<div class="welcome-mode-badge">' + info.label + ' Mode</div>' +
            '<div class="welcome-text">' + escHtml(info.welcome) + '</div>' +
            '<div class="welcome-stats">' +
            '<div class="welcome-stat"><strong>895</strong> chapters</div>' +
            '<div class="welcome-stat"><strong>553</strong> glossary terms</div>' +
            '<div class="welcome-stat"><strong>331K+</strong> interlinear words</div>' +
            '<div class="welcome-stat"><strong>41K</strong> flow verses</div>' +
            '<div class="welcome-stat"><strong>111</strong> prophecies</div>' +
            '</div></div>';
    }

    // ── Settings Modal ──────────────────────────────
    function openSettings() {
        var overlay = document.getElementById('settingsOverlay');
        overlay.classList.add('visible');
        loadModels();
        loadPolicies();
    }

    function closeSettings() {
        document.getElementById('settingsOverlay').classList.remove('visible');
    }

    function loadModels() {
        fetch(API + '/models')
            .then(function(r) { return r.json(); })
            .then(function(data) {
                var sel = document.getElementById('modelSelect');
                sel.innerHTML = '';
                (data.models || []).forEach(function(m) {
                    var opt = document.createElement('option');
                    opt.value = m;
                    opt.textContent = m;
                    if (m === currentModel) opt.selected = true;
                    sel.appendChild(opt);
                });
                sel.onchange = function() { currentModel = sel.value; };
            });
    }

    function loadPolicies() {
        fetch(API + '/policy')
            .then(function(r) { return r.json(); })
            .then(function(data) {
                var tabs = document.getElementById('policyTabs');
                var textarea = document.getElementById('policyTextarea');
                var policies = data.policies || {};
                var names = Object.keys(policies);
                tabs.innerHTML = '';

                if (names.length === 0) return;

                names.forEach(function(name, i) {
                    var btn = document.createElement('button');
                    btn.className = 'policy-tab' + (i === 0 ? ' active' : '');
                    btn.textContent = name.replace('.yaml', '').replace('.yml', '');
                    btn.dataset.file = name;
                    btn.onclick = function() {
                        tabs.querySelectorAll('.policy-tab').forEach(function(t) { t.classList.remove('active'); });
                        btn.classList.add('active');
                        textarea.value = policies[name];
                        textarea.dataset.file = name;
                    };
                    tabs.appendChild(btn);
                });

                textarea.value = policies[names[0]];
                textarea.dataset.file = names[0];
            });
    }

    // Save policy
    window.savePolicy = function() {
        var textarea = document.getElementById('policyTextarea');
        var filename = textarea.dataset.file;
        if (!filename) return;

        fetch(API + '/policy', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ filename: filename, content: textarea.value })
        })
        .then(function(r) { return r.json(); })
        .then(function() { alert('Policy saved: ' + filename); })
        .catch(function(e) { alert('Error saving: ' + e.message); });
    };

    // ── Chat History (localStorage) ─────────────────
    function saveHistory() {
        try {
            // Keep last 50 messages
            var save = history.slice(-50);
            localStorage.setItem('hai-chat-history', JSON.stringify(save));
        } catch (e) { /* localStorage might be full or unavailable */ }
    }

    function loadHistory() {
        try {
            var saved = localStorage.getItem('hai-chat-history');
            if (saved) {
                history = JSON.parse(saved);
                if (history.length > 0) {
                    showWelcome = false;
                    chatMessages.innerHTML = '';
                    history.forEach(function(msg) {
                        addMessage(msg.role, msg.content);
                    });
                    return;
                }
            }
        } catch (e) { /* ignore */ }

        renderWelcome();
    }

    // ── Utilities ───────────────────────────────────
    function escHtml(s) {
        var div = document.createElement('div');
        div.textContent = s;
        return div.innerHTML;
    }

    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // ── Start ───────────────────────────────────────
    init();
})();
