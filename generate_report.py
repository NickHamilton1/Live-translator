#!/usr/bin/env python3
"""Generate a polished DOCX executive summary report for the Spider-Man shirt launch."""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
import os

doc = Document()

# ── Styles ──────────────────────────────────────────────────────────────
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)
font.color.rgb = RGBColor(0x33, 0x33, 0x33)
style.paragraph_format.space_after = Pt(6)
style.paragraph_format.line_spacing = 1.15

for level in range(1, 4):
    hs = doc.styles[f'Heading {level}']
    hs.font.color.rgb = RGBColor(0x1a, 0x1a, 0x2e)
    hs.font.name = 'Calibri'
    if level == 1:
        hs.font.size = Pt(22)
        hs.paragraph_format.space_before = Pt(24)
    elif level == 2:
        hs.font.size = Pt(16)
        hs.paragraph_format.space_before = Pt(18)
    else:
        hs.font.size = Pt(13)
        hs.paragraph_format.space_before = Pt(12)

def add_table(headers, rows, col_widths=None):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = 'Light Grid Accent 1'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.bold = True
                run.font.size = Pt(10)
    for r_idx, row in enumerate(rows):
        for c_idx, val in enumerate(row):
            cell = table.rows[r_idx + 1].cells[c_idx]
            cell.text = str(val)
            for p in cell.paragraphs:
                for run in p.runs:
                    run.font.size = Pt(10)
    if col_widths:
        for i, w in enumerate(col_widths):
            for row in table.rows:
                row.cells[i].width = Cm(w)
    doc.add_paragraph()  # spacing after table


def bold_paragraph(text_pairs):
    """Add a paragraph with alternating bold/normal runs. text_pairs = [(text, bold), ...]"""
    p = doc.add_paragraph()
    for text, is_bold in text_pairs:
        run = p.add_run(text)
        run.bold = is_bold
    return p


# ── TITLE PAGE ──────────────────────────────────────────────────────────
doc.add_paragraph()
doc.add_paragraph()
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run('Spider-Man: Brand New Day\nShirt Launch')
run.font.size = Pt(36)
run.font.color.rgb = RGBColor(0x1a, 0x1a, 0x2e)
run.bold = True

subtitle = doc.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = subtitle.add_run('Feasibility & Strategy Report')
run.font.size = Pt(20)
run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

doc.add_paragraph()
date_line = doc.add_paragraph()
date_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = date_line.add_run('April 4, 2026  |  Confidential')
run.font.size = Pt(12)
run.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

doc.add_page_break()

# ── EXECUTIVE SUMMARY ───────────────────────────────────────────────────
doc.add_heading('Executive Summary', level=1)

doc.add_paragraph(
    'This report evaluates the feasibility of launching unofficial, fan-oriented '
    't-shirts timed to Spider-Man: Brand New Day (July 31, 2026). The concept targets '
    'nostalgia-driven fans aged 25\u201335 who grew up across three Spider-Man eras '
    '(Tobey 2002, Andrew 2012, Tom 2017) and are now attending the new film with '
    'partners and families.'
)

doc.add_heading('The Opportunity', level=2)

doc.add_paragraph(
    'Brand New Day is generating historically unprecedented hype. Its trailer broke '
    'every existing record with 718.6 million views in 24 hours and crossed 1 billion '
    'views in four days \u2014 the first movie trailer in history to do so. Box office '
    'projections sit at $2.54 billion worldwide. The audience is enormous, emotionally '
    'invested, and hungry for ways to express their fandom on opening night.'
)

doc.add_heading('The Verdict', level=2)

p = doc.add_paragraph()
run = p.add_run('This is viable and potentially very profitable \u2014 but only if the designs '
                'stay firmly in legally safe territory.')
run.bold = True

doc.add_paragraph(
    'At the base case (50,000 units, $6 blended CPA), the model produces $322K in net '
    'profit on $1.1M revenue. Even the conservative scenario (10,000 units) returns $39K. '
    'The optimistic case (100K units) reaches $819K. The business model works because '
    'unit economics are strong: ~$9 COGS, $22 sell price, $6 ad cost = $7 profit per shirt.'
)

doc.add_paragraph(
    'The primary risk is legal, not commercial. Disney/Marvel owns all Spider-Man '
    'merchandise rights and is one of the most aggressive IP enforcers in the world. '
    'The entire strategy depends on designs that evoke the Spider-Man cultural moment '
    'without using any trademarked names, logos, character likenesses, or catchphrases.'
)

doc.add_page_break()

# ── SECTION 1: LEGAL ────────────────────────────────────────────────────
doc.add_heading('1. Legal Landscape', level=1)

doc.add_heading('Who Owns What', level=2)
doc.add_paragraph(
    'Disney/Marvel owns 100% of Spider-Man merchandise rights, including apparel. Sony '
    'only holds film distribution rights. Any legitimate Spider-Man apparel license must '
    'come through Disney Consumer Products. "Spider-Man" is registered as a trademark in '
    'Class 25 (clothing) via multiple filings. Even "With great power comes great '
    'responsibility" is trademarked specifically for shirts (Reg. 5,054,732).'
)

doc.add_heading('What We Can and Cannot Do', level=2)

add_table(
    ['Safe (Green Zone)', 'Off-Limits (Will Get You Sued)'],
    [
        ['Generic spider imagery (not Marvel\'s logos)', '"Spider-Man" name in any form'],
        ['Web/spider-web patterns', 'Marvel\'s spider logos or similar designs'],
        ['Red & blue color schemes', 'Character likenesses (mask, costume, poses)'],
        ['Nostalgic year references ("Since 2002")', 'Movie titles ("No Way Home," "Brand New Day")'],
        ['Generic hero/superhero language', '"With great power comes great responsibility"'],
        ['Original spider-themed artwork', 'Fan art of the character in any style'],
        ['Movie-night / opening-night themes', 'Character names (Peter Parker, MJ, etc.)'],
    ],
    col_widths=[8.5, 8.5]
)

doc.add_heading('Risk Assessment', level=2)
doc.add_paragraph(
    'If designs stay in the green zone, the legal risk is low-to-moderate. The main exposure '
    'comes from scale and visibility \u2014 $600K in Meta ad spend during the movie\'s release '
    'window will attract attention. A Delaware LLC provides meaningful liability protection, '
    'and a $20K legal contingency fund covers a C&D response if needed.'
)

bold_paragraph([
    ('Recommended first step: ', True),
    ('Have a trademark attorney review the design concepts before any production commitment. '
     'Budget $3\u20135K for this. It\'s the single most important gate in the entire project.', False)
])

doc.add_page_break()

# ── SECTION 2: MARKET ───────────────────────────────────────────────────
doc.add_heading('2. Market Opportunity', level=1)

doc.add_heading('The Hype Is Real', level=2)

add_table(
    ['Metric', 'Number', 'Context'],
    [
        ['Trailer views (24 hours)', '718.6 million', 'Biggest ever (film or video game)'],
        ['Trailer views (total)', '1.1 billion+', 'First trailer to ever reach 1B'],
        ['Projected worldwide gross', '$2.54 billion', 'Would be highest-grossing Spider-Man'],
        ['Projected opening weekend', '$600M+ worldwide', 'Approaching Endgame territory'],
    ],
    col_widths=[5.5, 4, 7.5]
)

doc.add_heading('Fan Themes We Can Ride', level=2)
doc.add_paragraph(
    'The strongest emotional currents in the fandom right now:'
)
themes = [
    'Nostalgia / generational journey \u2014 "I was 10 in 2002, now I\'m bringing my kids"',
    'Memory and sacrifice \u2014 the No Way Home ending left fans devastated; Brand New Day is the resolution',
    'Romance \u2014 Will MJ remember Peter? The love story drives huge engagement',
    'Transformation / evolution \u2014 The Man-Spider teases in the trailer are generating massive theory content',
    'Opening night as an event \u2014 Fans want to mark the occasion, wear something special',
]
for t in themes:
    doc.add_paragraph(t, style='List Bullet')

doc.add_heading('Competitive Gap', level=2)
doc.add_paragraph(
    'The market is flooded with infringing merch that will get taken down. Licensed retailers '
    '(Hot Topic, BoxLunch) will sell official designs but won\'t offer couples sets, family '
    'packs, or opening-night event shirts. Nobody is doing what we\'re proposing:'
)
gaps = [
    'Couples matching shirts (the romance angle)',
    'Family bundle packs (generational nostalgia)',
    'Opening night "I was there" event merch',
    'Non-infringing, original spider-themed designs',
    'Limited-run urgency (pre-order window creates FOMO)',
]
for g in gaps:
    doc.add_paragraph(g, style='List Bullet')

doc.add_page_break()

# ── SECTION 3: PRODUCT ──────────────────────────────────────────────────
doc.add_heading('3. Product Strategy', level=1)

doc.add_paragraph(
    'We developed 15 design concepts across solo fan, couples, family, humor, and nostalgia '
    'categories. All are legally vetted against our design guardrails. Here are the top 5:'
)

add_table(
    ['Rank', 'Design', 'Category', 'Why It Works'],
    [
        ['1', '"Since 2002"', 'Nostalgia', 'Simple, powerful, zero legal risk. The anchor shirt.'],
        ['2', '"Opening Night Crew"', 'Event', 'Creates urgency \u2014 need it BEFORE July 31.'],
        ['3', '"I Remember Everything"', 'Emotional', 'Gut-punch for No Way Home fans. Minimal, premium feel.'],
        ['4', '"You\'re My Hero / Universe"', 'Couples Set', 'Biggest market gap. No one else is doing this.'],
        ['5', '"Heroes Raising Heroes"', 'Family Pack', 'The generational story. Parents + kids matching.'],
    ],
    col_widths=[1.5, 4.5, 3, 8]
)

doc.add_heading('Pricing & Bundles', level=2)

add_table(
    ['Product', 'Price', 'Discount', 'Margin/Unit'],
    [
        ['Single shirt', '$22', '\u2014', '~$7.50'],
        ['Couples bundle (2 shirts)', '$38', '14% off', '~$6.50/shirt'],
        ['Family 3-pack', '$52', '21% off', '~$5.50/shirt'],
        ['Family 4-pack', '$68', '23% off', '~$5.00/shirt'],
    ],
    col_widths=[5, 3, 3, 4]
)

doc.add_paragraph(
    'Bundles sacrifice $1\u20132.50/unit but dramatically increase average order value. '
    'A $68 family order is 3x the revenue of a single shirt at roughly the same ad cost.'
)

doc.add_page_break()

# ── SECTION 4: FINANCIALS ───────────────────────────────────────────────
doc.add_heading('4. Financial Model', level=1)

add_table(
    ['Scenario', 'Units', 'Revenue', 'Ad Spend', 'Net Profit', 'Net Margin', 'ROI'],
    [
        ['Conservative', '10,000', '$220K', '$60K', '$39K', '18%', '66%'],
        ['Base Case', '50,000', '$1.1M', '$300K', '$322K', '29%', '107%'],
        ['Optimistic', '100,000', '$2.2M', '$500K', '$819K', '37%', '164%'],
        ['Home Run', '200,000', '$4.0M', '$800K', '$1.67M', '42%', '209%'],
    ],
    col_widths=[3, 2, 2, 2, 2.5, 2.5, 2]
)

doc.add_heading('Unit Economics', level=2)

add_table(
    ['Component', 'Cost'],
    [
        ['Blank shirt (Gildan 5000)', '$2.00\u2013$4.00'],
        ['Printing (Virginia facility)', '$2.50\u2013$3.00'],
        ['Shopify fees (2.9% + $0.30)', '$0.94'],
        ['Shipping (net of customer charge)', '$1.50'],
        ['Packaging', '$0.12'],
        ['Total COGS', '~$9/unit'],
        ['Sell price', '$22'],
        ['Gross margin/unit', '~$13'],
        ['After $6 CPA', '~$7 profit/unit'],
    ],
    col_widths=[8, 5]
)

doc.add_heading('Break-Even', level=2)
doc.add_paragraph(
    'The model breaks even at approximately $13 CPA. Above that, we lose money on every '
    'shirt. Our target of $6 blended CPA is achievable based on 2026 Meta benchmarks for '
    'apparel ($18\u201345 average CPA, but apparel enjoys the lowest CPC on Meta at $0.45). '
    'The key is a strong retargeting funnel: cold traffic will likely cost $8\u201312 CPA, '
    'but retargeting converts at $2\u20135, blending to ~$6 overall.'
)

doc.add_page_break()

# ── SECTION 5: EXECUTION ────────────────────────────────────────────────
doc.add_heading('5. Execution Plan', level=1)

doc.add_heading('Operations Model', level=2)
doc.add_paragraph(
    'Pre-order via Shopify \u2192 batch print at Virginia facility (100K+/day capacity, '
    '~$3/unit) \u2192 ship direct to customers via USPS. Meta ads drive all traffic. '
    'Delaware LLC for liability protection. Total setup cost: ~$500\u2013$900.'
)

doc.add_heading('Critical Path Timeline', level=2)

add_table(
    ['Phase', 'Dates', 'Key Milestones'],
    [
        ['Legal & Entity Setup', 'Apr 7\u201320', 'LLC formed, attorney reviews designs, Go/No-Go #1'],
        ['Design & Infrastructure', 'Apr 21 \u2013 May 4', '15 designs finalized, Shopify store built, Meta account verified'],
        ['Production Prep', 'May 5\u201318', 'Printer confirmed, test ads running, pixel installed'],
        ['Blank Procurement', 'May 19 \u2013 Jun 1', '10K blanks ordered and shipped to printer'],
        ['Pre-Launch Warmup', 'Jun 2\u201315', 'Ad account ramped, blanks arrive at printer'],
        ['PRE-ORDERS OPEN', 'Jun 16', 'Ads go live at $300/day, orders start flowing'],
        ['Testing & Validation', 'Jun 16\u201329', 'CPA validated by Jun 23 (Go/No-Go #3)'],
        ['Scale Phase', 'Jul 14\u201331', 'Ads scale to $12K/day, all pre-orders ship by Jul 28'],
        ['Opening Night', 'Jul 31', 'Spider-Man: Brand New Day opens'],
        ['Wind Down', 'Aug 1\u20137', 'Sell remaining inventory, pause ads, reconcile finances'],
    ],
    col_widths=[4, 3.5, 9.5]
)

doc.add_heading('Required Upfront Capital', level=2)
doc.add_paragraph(
    'Approximately $80K\u2013$150K is needed before significant revenue flows back. This covers '
    'blank shirt inventory ($22\u201366K), Meta ad spend during testing and validation ($15K), '
    'legal costs ($5K), and the ramp to scale. Shopify Payments returns money within 2\u20133 '
    'business days, so cash flow turns positive quickly once pre-orders are live.'
)

doc.add_page_break()

# ── SECTION 6: RISKS ────────────────────────────────────────────────────
doc.add_heading('6. Key Risks', level=1)

add_table(
    ['Risk', 'Likelihood', 'Impact', 'Mitigation'],
    [
        ['C&D from Disney/Marvel', 'Medium (if designs are clean)', 'High \u2014 must pull affected designs',
         'Stay in green zone. Attorney review. $20K legal fund. Kill-switch to pull designs in minutes.'],
        ['CPA exceeds $10', 'Medium', 'High \u2014 model becomes unprofitable',
         'Test with $4K before committing. Go/No-Go at day 7. Shift to bundles to raise AOV.'],
        ['Platform shutdown (Shopify/Stripe)', 'Low (if designs are clean)', 'Very High \u2014 can\'t sell or collect money',
         'Clean designs + clean marketing copy. No IP in any customer-facing content.'],
        ['Printer can\'t fulfill on time', 'Low', 'High \u2014 missed delivery before opening night',
         'Confirm capacity early. Have 3PL backup identified. Ship in waves, not all at once.'],
        ['Meta account spending limits', 'Medium', 'Medium \u2014 can\'t scale ads fast enough',
         'Start account setup in April. Run small test campaigns May\u2013June to build trust.'],
    ],
    col_widths=[4, 2.5, 3.5, 7]
)

doc.add_page_break()

# ── SECTION 7: RECOMMENDATION ───────────────────────────────────────────
doc.add_heading('7. Recommendation', level=1)

p = doc.add_paragraph()
run = p.add_run('Proceed to the first gate: attorney review.')
run.bold = True
run.font.size = Pt(13)

doc.add_paragraph(
    'The commercial opportunity is strong. The hype is historically unprecedented, the market '
    'gaps are real (couples, families, event merch), and the unit economics work at reasonable '
    'CPA targets. The question is entirely legal.'
)

doc.add_heading('Immediate Next Steps', level=2)

steps = [
    ('Engage a trademark attorney', ' to review the design guardrails and top 15 concepts. '
     'Budget $3\u20135K. This is the single most important action item and determines whether '
     'the project lives or dies. Target completion: April 18.'),
    ('Form the Delaware LLC', ' \u2014 same-day filing, $190. Do this regardless of the attorney\'s '
     'outcome; it\'s cheap insurance. Can be done this week.'),
    ('Set up Meta Business Manager', ' and submit for business verification immediately. '
     'This takes 1\u20135 days and is on the critical path for ad scaling.'),
    ('Confirm Virginia printer capacity', ' \u2014 can they handle 100K+ units in a 3-week window? '
     'Can they ship direct to customers? Get this in writing.'),
    ('Secure $80\u2013150K in available capital', ' (cash or credit line) to fund inventory and '
     'ad spend before revenue ramps.'),
]

for bold_text, normal_text in steps:
    p = doc.add_paragraph(style='List Number')
    run = p.add_run(bold_text)
    run.bold = True
    p.add_run(normal_text)

doc.add_paragraph()

doc.add_heading('The Bottom Line', level=2)

p = doc.add_paragraph()
run = p.add_run(
    'If the attorney greenlights the designs, this is a $300K\u2013$800K profit opportunity '
    'on a 6-week sprint with $80\u2013150K upfront capital. The risk is manageable with proper '
    'LLC structure and legal guardrails. The window is narrow \u2014 the clock starts now.'
)
run.font.size = Pt(12)

# ── SAVE ────────────────────────────────────────────────────────────────
output_path = '/home/user/Live-translator/Spider-Man-Shirt-Launch-Report.docx'
doc.save(output_path)
print(f'Report saved to {output_path}')
print(f'File size: {os.path.getsize(output_path):,} bytes')
