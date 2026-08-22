import json, pathlib, re

ROOT = pathlib.Path('.')
# Collect manual verification lists from reports and memory
# We'll generate for 10th to 50th

exams = []
for i in list(range(10,18)) + list(range(18,51)):
    # Handle naming: 11st,12nd,13rd etc. Need to map correctly
    # Use actual files present
    pass

# Instead discover via json files
json_files = sorted((ROOT / "data" / "processed" / "json").glob('*_bcs.json'))
if not json_files:
    json_files = sorted(ROOT.glob('*_bcs.json'))  # fallback for legacy flat
# filter 10th-50th
order = []
for p in json_files:
    m = re.match(r'(\d+)(?:st|nd|rd|th)_bcs\.json', p.name)
    if m:
        num = int(m.group(1))
        if 10 <= num <= 50:
            order.append((num, p))
order.sort()

html_parts = []
html_parts.append('<!DOCTYPE html><html lang="bn"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">')
html_parts.append('<title>BCS Manual Verification 10th-50th</title>')
html_parts.append('<style>body{font-family: Noto Sans Bengali, SolaimanLipi, sans-serif; max-width:1100px; margin:20px auto; padding:0 16px; background:#f9fafb; color:#111} h1{font-size:28px; margin:20px 0 8px} h2{font-size:22px; margin:28px 0 12px; border-bottom:3px solid #0ea5e9; padding-bottom:6px} h3{font-size:18px; margin:18px 0 8px} .card{background:#fff; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px; margin:10px 0; box-shadow:0 1px 2px rgba(0,0,0,.05)} .meta{font-size:12px; color:#6b7280; margin-bottom:6px} .q{font-weight:600; font-size:15px; white-space:pre-wrap} .opts{display:grid; grid-template-columns:1fr 1fr; gap:6px 12px; margin:10px 0} .opt{padding:6px 8px; background:#f3f4f6; border-radius:6px; font-size:14px} .opt.correct{background:#dcfce7; border:1px solid #86efac} .solve{font-size:13px; color:#374151; background:#fffbeb; padding:8px 10px; border-radius:6px; margin-top:8px; white-space:pre-wrap; border:1px solid #fde68a} .imgs img{max-width:220px; max-height:180px; border:1px solid #ddd; border-radius:6px; margin:4px} .badge{display:inline-block; font-size:11px; padding:2px 6px; border-radius:10px; background:#e0f2fe; color:#0369a1; margin-right:4px} .badge.warn{background:#fee2e2; color:#b91c1c} .badge.info{background:#fef9c3; color:#854d0e} .toc a{font-size:13px; margin-right:10px}</style>')
html_parts.append('</head><body>')
html_parts.append('<h1>BCS Question Bank — Manual Verification (10th–50th)</h1>')
html_parts.append('<p style="font-size:13px;color:#555">Generated from reports & memory.md — only questions needing human check (image-only / option-images / defective blanks) + recently fixed questions. Images shown from <code>images/&lt;exam&gt;/</code> if present. Correct answer letter highlighted.</p>')
# TOC
html_parts.append('<div class="toc"><strong>Jump:</strong> ')
for num,p in order:
    html_parts.append(f'<a href="#{p.stem}">{num}{p.stem.split("_")[0][-2:] if "_" in p.stem else ""} {p.stem}</a>')
html_parts.append('</div>')

total_cards = 0
for num, p in order:
    data = json.loads(p.read_text(encoding='utf-8'))
    exam = data.get('exam', {})
    title = exam.get('title', p.stem)
    # Load report if exists
    report_path = ROOT / 'output' / f'{p.stem}_report.md'
    report_text = ''
    if report_path.exists():
        report_text = report_path.read_text(encoding='utf-8')
    # Determine manual questions: those with has_image=1 or empty options or blank answer (defective) or mentioned in report
    qs = data.get('questions', [])
    manual = []
    fixed = []
    # Collect from report "Image questions" and "Manual/human check" via memory parsing: we will include has_image or empty option
    for q in qs:
        qn = q['question_number']
        has_q_img = q.get('has_question_image',0)==1
        empty_q = not q.get('question','').strip()
        empty_opt = any(not q.get(f'option_{c}','').strip() for c in ['a','b','c','d'])
        blank_ans = q.get('correct_answer','') == ''
        is_image_only = empty_q and has_q_img
        # Strict manual verification: image-only OR empty options OR blank answer (defective)
        is_manual = is_image_only or empty_opt or blank_ans
        is_fixed = False
        ans_path = ROOT / 'output' / f'{p.stem}_answers.json'
        if ans_path.exists():
            try:
                ans_data = json.loads(ans_path.read_text(encoding='utf-8'))
                if str(qn) in ans_data and ans_data[str(qn)] is not None:
                    is_fixed = True
            except: pass
        if is_manual:
            manual.append(q)
        elif is_fixed:
            # fixed but not manual → still show for context
            fixed.append(q)
    # Also include fixed regardless for review section
    # If no manual and no fixed, skip exam
    if not manual and not fixed:
        continue
    html_parts.append(f'<h2 id="{p.stem}">{title} — {exam.get("date","")} / {exam.get("set_code","")} <span style="font-weight:400; font-size:13px">({len(qs)} Qs, manual {len(manual)}, fixed {len(fixed)})</span></h2>')
    # Show manual first
    if manual:
        html_parts.append('<h3>Needs manual verification</h3>')
        for q in manual:
            total_cards += 1
            qn = q['question_number']
            subj = f"{q.get('subject_en','')} ({q.get('subject_bn','')})"
            badges = []
            if q.get('has_question_image'): badges.append('<span class="badge">question image</span>')
            if q.get('has_solve_note_image'): badges.append('<span class="badge">solve image</span>')
            if any(not q.get(f'option_{c}','').strip() for c in ['a','b','c','d']): badges.append('<span class="badge warn">empty option(s)</span>')
            if q.get('correct_answer','')=='': badges.append('<span class="badge warn">blank answer (defective)</span>')
            if not q.get('question','').strip() and q.get('question_image_paths'): badges.append('<span class="badge info">image-only question</span>')
            # Check if was fixed recently
            ans_path = ROOT / 'output' / f'{p.stem}_answers.json'
            was_fixed = False
            if ans_path.exists():
                try:
                    ad = json.loads(ans_path.read_text(encoding='utf-8'))
                    if str(qn) in ad:
                        was_fixed = True
                        badges.append('<span class="badge info">recently fixed</span>')
                except: pass
            html_parts.append('<div class="card">')
            html_parts.append(f'<div class="meta">Q{qn} • {subj} {" ".join(badges)}</div>')
            html_parts.append(f'<div class="q">{q.get("question","(empty question text)")}</div>')
            html_parts.append('<div class="opts">')
            for c in ['a','b','c','d']:
                key = f'option_{c}'
                val = q.get(key,'')
                is_correct = q.get('correct_answer','').upper() == c.upper()
                cls = 'opt correct' if is_correct and val.strip() else 'opt'
                html_parts.append(f'<div class="{cls}"><strong>{c.upper()}.</strong> {val if val.strip() else "<em style=color:#999>empty</em>"}</div>')
            html_parts.append('</div>')
            # images
            qimgs = q.get('question_image_paths',[]) or []
            simgs = q.get('solve_note_image_paths',[]) or []
            if qimgs or simgs:
                html_parts.append('<div class="imgs">')
                for path in qimgs:
                    html_parts.append(f'<div><small>Q image: {path}</small><br><img src="{path}" alt="q{qn} image" loading="lazy"></div>')
                for path in simgs:
                    html_parts.append(f'<div><small>Solve image: {path}</small><br><img src="{path}" alt="solve q{qn}" loading="lazy"></div>')
                html_parts.append('</div>')
            if q.get('solve_note','').strip():
                html_parts.append(f'<div class="solve"><strong>Solve:</strong> {q.get("solve_note","")}</div>')
            else:
                if simgs:
                    html_parts.append('<div class="solve"><em>Solve is image-only (see solve image above)</em></div>')
                else:
                    html_parts.append('<div class="solve"><em>No solve note</em></div>')
            html_parts.append(f'<div class="meta">correct_answer: <strong>{q.get("correct_answer","(blank)")}</strong></div>')
            html_parts.append('</div>')
    if fixed:
        html_parts.append('<h3>Recently fixed (for context)</h3>')
        for q in fixed:
            total_cards += 1
            qn = q['question_number']
            html_parts.append('<div class="card" style="opacity:.95">')
            html_parts.append(f'<div class="meta">Q{qn} • {q.get("subject_en","")} <span class="badge info">fixed</span></div>')
            html_parts.append(f'<div class="q">{q.get("question","")}</div>')
            html_parts.append('<div class="opts">')
            for c in ['a','b','c','d']:
                val = q.get(f'option_{c}','')
                is_correct = q.get('correct_answer','').upper() == c.upper()
                cls = 'opt correct' if is_correct else 'opt'
                html_parts.append(f'<div class="{cls}"><strong>{c.upper()}.</strong> {val}</div>')
            html_parts.append('</div>')
            html_parts.append(f'<div class="solve"><strong>Solve:</strong> {q.get("solve_note","")[:600]}</div>')
            html_parts.append('</div>')

html_parts.append(f'<p style="margin-top:30px; font-size:12px; color:#888">Total cards: {total_cards} • Generated via generate_manual_html.py • UTF-8</p>')
html_parts.append('</body></html>')
out = ROOT / 'manual_verification_10th_50th.html'
out.write_text('\n'.join(html_parts), encoding='utf-8')
print(f'Wrote {out} with {total_cards} cards, exams {len(order)}')
