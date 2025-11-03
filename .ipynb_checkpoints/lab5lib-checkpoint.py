import html
import nltk

from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer('english')
stops = stopwords.words('english')

def search(query):
    return [ 'coffee-guide.doc', 'learn-python.doc', 'recipes.doc', 'running.doc', 'indoor-gardening.doc' ]

def make_snippets(query, ranks):
    keypairs = process_query(query)
    html_out = []
    for doc in ranks:
        description = snippet(keypairs, doc)
        block = (
            '<div class="snippet">'
            f'<div class="title">{html.escape(doc)}</div>'
            f'<a class="url" href="{html.escape(doc)}">{html.escape(doc)}</a>'
            f'<div class="description">{description}</div>'
            '</div>'
        )
        html_out.append(block)
    return "".join(html_out)

def process_query(query):
    tokens = nltk.word_tokenize(query.lower())
    keywords = [w for w in tokens if w.isalpha() and w not in stops]
    return [(kw, stemmer.stem(kw)) for kw in keywords]

def _highlight_spans(text, spans):
    if not spans:
        return html.escape(text)
    spans = sorted(spans)

    merged = [spans[0]]
    for s, e in spans[1:]:
        ls, le = merged[-1]
        if s <= le:
            merged[-1] = (ls, max(le, e))
        else:
            merged.append((s, e))

    out = []
    prev = 0
    for s, e in merged:
        out.append(html.escape(text[prev:s]))
        out.append("<mark>")
        out.append(html.escape(text[s:e]))
        out.append("</mark>")
        prev = e
    out.append(html.escape(text[prev:]))
    return "".join(out)

def snippet(keypairs, docname, max_length=250):
    scores = []

    try:
        with open(f"./docs/{docname}", "r", encoding="utf-8", errors="ignore") as f:
            doc = f.read()
    except Exception:
        return "…"

    sentences = nltk.sent_tokenize(doc)

    for i, sentence in enumerate(sentences):
        score, pos = score_sentence(keypairs, sentence)
        if score > 0:
            scores.append((score, i, sentence, pos))

    if not scores:
        flat = " ".join(sentences) if sentences else doc
        flat = flat.strip()
        if not flat:
            return "…"
        return html.escape(flat[:max_length]) + ("…" if len(flat) > max_length else "")

    scores.sort(key=lambda x: x[0], reverse=True)

    chosen = []
    total_len = 0
    for score, idx, sentence, pos in scores:
        s = sentence.strip()
        if not s:
            continue
        add_len = len(s) + (3 if chosen else 0)
        if total_len + add_len <= max_length or not chosen:
            chosen.append((idx, s, pos))
            total_len += add_len
        else:
            if not chosen:
                trunc = s[:max_length] + "…"
                chosen.append((idx, trunc, []))
            break

    chosen.sort(key=lambda x: x[0])

    parts = []
    last_idx = None
    for idx, s, pos in chosen:
        if last_idx is not None and idx != last_idx + 1:
            parts.append(" … ")
        parts.append(_highlight_spans(s, pos))
        last_idx = idx

    return "".join(parts)

def score_sentence(keywords, sentence):
    sentence_l = sentence.lower()
    words = nltk.word_tokenize(sentence_l)
    stems = [stemmer.stem(word) for word in words]

    score = 0
    keyword_positions = []

    for word, stem in keywords:
        matched = None
        try:
            idx = words.index(word)
            score += 10
            matched = word
        except ValueError:
            try:
                idx = stems.index(stem)
                score += 5
                matched = words[idx]  
            except ValueError:
                matched = None

        if matched:
            start = 0
            token = matched
            while True:
                pos = sentence_l.find(token, start)
                if pos == -1:
                    break
                keyword_positions.append((pos, pos + len(token)))
                start = pos + len(token)

    if len(keyword_positions) > 1:
        keyword_positions.sort()
        for i in range(len(keyword_positions) - 1):
            a_start, a_end = keyword_positions[i]
            b_start, _ = keyword_positions[i + 1]
            distance = max(0, b_start - a_end)
            if distance <= 50:
                score += 3

    return score, keyword_positions
