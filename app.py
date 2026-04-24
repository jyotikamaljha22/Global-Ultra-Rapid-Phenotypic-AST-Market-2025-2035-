import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# =========================
# Page config
# =========================
st.set_page_config(
    page_title="Ultra-Rapid Phenotypic AST Market | Strategic Dashboard",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================
# Theme Colors & Notes
# =========================
BURGUNDY = "#5B0F2E"
BURGUNDY_DARK = "#431022"
BURGUNDY_MID = "#7A1C41"
BURGUNDY_SOFT = "#A45A7B"
GOLD = "#C9A227"
ROSE = "#EEDBE4"
BG = "#F8F5F6"
CARD = "rgba(255, 255, 255, 0.85)"
INK = "#1A1014"
MUTED = "#6B5B63"
BORDER = "rgba(255, 255, 255, 0.9)"

# Consulting Chart Palette
CHART_BG = "#F5F6F8"
SLATE = "#475569"
SLATE_LIGHT = "#94a3b8"

PRIMARY_PASSWORD = "SMR2026"
CLIENT_NAME = "Gradientech AB"

QUICK_METRICS = {
    "TAM 2035 (Broad Micro)": "$9.48B",
    "SOM 2035 (Ultra-Rapid)": "$264.5M",
    "SOM CAGR (25-35)": "12.3%",
    "Clinical Threshold": "≤ 4 Hours",
}

# =========================
# CSS / UI polish (Ultra-Premium Glassmorphism)
# =========================
st.markdown(
    f"""
    <style>
    /* Premium Web Font */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: {INK} !important;
    }}

    /* UI HIDING FOR WHITE-LABELING */
    [data-testid="stToolbar"] {{ display: none !important; }}
    .viewerBadge_container, #viewerBadge_container {{ display: none !important; }}
    footer {{ display: none !important; }}
    header[data-testid="stHeader"] {{ background: transparent !important; box-shadow: none !important; }}

    /* CUSTOM ELEGANT SCROLLBAR */
    ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
    ::-webkit-scrollbar-track {{ background: transparent; }}
    ::-webkit-scrollbar-thumb {{ background: rgba(91,15,46,0.15); border-radius: 10px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: rgba(91,15,46,0.3); }}

    /* LIVING GRADIENT BACKGROUND */
    .stApp {{
      background: radial-gradient(circle at 15% 0%, rgba(201,162,39,0.04) 0%, transparent 40%),
                  radial-gradient(circle at 85% 100%, rgba(91,15,46,0.03) 0%, transparent 40%),
                  linear-gradient(180deg, #FCFAFB 0%, #F4ECEF 100%);
      background-attachment: fixed;
    }}

    /* SIDEBAR REFINEMENT */
    [data-testid="stSidebar"] {{
        background: rgba(255,255,255,0.6) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(91,15,46,0.08) !important;
    }}

    /* SLEEK BUTTON STYLING */
    .stButton > button {{
        background: linear-gradient(135deg, {BURGUNDY} 0%, {BURGUNDY_MID} 100%) !important;
        color: white !important; border: none !important; border-radius: 10px !important;
        padding: 10px 24px !important; font-weight: 700 !important; font-size: 0.9rem !important;
        letter-spacing: 0.02em; transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
        box-shadow: 0 4px 14px rgba(91,15,46,0.2) !important;
    }}
    .stButton > button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 24px rgba(91,15,46,0.3) !important;
    }}

    /* INPUT FIELDS */
    .stTextInput input {{
        border-radius: 8px !important; border: 1px solid rgba(91,15,46,0.15) !important;
        padding: 12px 14px !important; background: rgba(255,255,255,0.8) !important;
        transition: all 0.2s ease !important;
    }}
    .stTextInput input:focus {{
        border-color: {GOLD} !important; background: #fff !important;
        box-shadow: 0 0 0 3px rgba(201,162,39,0.15) !important;
    }}

    /* APP-LIKE NAVIGATION */
    [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"] {{
        padding: 10px 14px !important; margin-bottom: 6px !important; border-radius: 8px !important;
        transition: all 0.2s ease !important; cursor: pointer !important;
    }}
    [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"]:hover {{
        background: rgba(91,15,46,0.04) !important; transform: translateX(3px) !important;
    }}
    [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"]:has(input[checked]) {{
         background: #ffffff !important; border-left: 4px solid {BURGUNDY} !important;
         box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
    }}
    [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"] p {{
        font-weight: 600 !important; font-size: 0.92rem !important; color: {INK} !important;
    }}

    /* FROSTED BRANDING HEADER */
    .smr-brand {{
      background: rgba(255,255,255,0.7); border: 1px solid {BORDER}; border-radius: 16px;
      padding: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.03); margin-bottom: 24px;
      backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
    }}
    
    .hero {{
      background: linear-gradient(135deg, {BURGUNDY} 0%, {BURGUNDY_MID} 60%, {BURGUNDY_SOFT} 100%);
      color: white; border: 1px solid rgba(255,255,255,0.1); border-radius: 20px;
      padding: 34px 40px; box-shadow: 0 20px 40px rgba(61,16,33,0.15), inset 0 1px 0 rgba(255,255,255,0.2);
      margin-bottom: 24px; animation: floatIn 0.6s cubic-bezier(0.25, 0.8, 0.25, 1);
      position: relative; overflow: hidden;
    }}
    .hero::before {{
      content: ''; position: absolute; top: -50%; right: -10%; width: 60%; height: 200%;
      background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 60%);
      transform: rotate(-45deg);
    }}
    .hero-head {{
      display:flex; align-items:center; gap:18px; margin-bottom:8px; position: relative; z-index: 2;
    }}
    .hero h2 {{
      margin: 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -0.02em; text-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }}
    
    /* GLASSMORPHISM DATA CARDS */
    .metric-card {{
      background: {CARD}; backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
      border: 1px solid {BORDER}; border-radius: 16px; padding: 24px;
      box-shadow: 0 12px 36px rgba(91,15,46,0.03), 0 2px 8px rgba(0,0,0,0.02);
      min-height: 135px; animation: floatIn 0.6s cubic-bezier(0.25, 0.8, 0.25, 1);
      transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }}
    .metric-card:hover {{
      transform: translateY(-4px); box-shadow: 0 16px 40px rgba(91,15,46,0.08), 0 4px 12px rgba(0,0,0,0.03);
      border-color: rgba(201,162,39,0.3);
    }}
    .metric-label {{
      color: {MUTED}; font-size: 0.82rem; margin-bottom: 8px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;
    }}
    .metric-value {{
      color: {BURGUNDY}; font-size: 2.6rem; font-weight: 800; line-height: 1; letter-spacing: -0.02em; margin-bottom: 12px;
    }}
    .metric-foot {{
      color: {MUTED}; font-size: 0.85rem; line-height: 1.4;
    }}

    .section-card {{
      background: {CARD}; backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
      border: 1px solid {BORDER}; border-radius: 20px; padding: 24px;
      box-shadow: 0 12px 36px rgba(91,15,46,0.03); margin-bottom: 24px;
      animation: floatIn 0.6s cubic-bezier(0.25, 0.8, 0.25, 1);
    }}
    .section-title {{
      display: flex; justify-content: space-between; align-items: center;
      font-size: 1.4rem; font-weight: 800; color: {BURGUNDY}; margin-bottom: 6px; letter-spacing: -0.01em;
    }}
    .section-sub {{
      color: {MUTED}; font-size: 0.95rem; margin-bottom: 20px; line-height: 1.5;
    }}
    
    .insight-box {{
      background: #ffffff; border: 1px solid rgba(201,162,39,0.2); border-left: 6px solid {GOLD};
      border-radius: 12px; padding: 20px 24px; color: {INK}; font-size: 0.95rem; line-height: 1.6;
      margin-bottom: 24px; box-shadow: 0 8px 24px rgba(201,162,39,0.05); animation: floatIn 0.6s ease-out;
    }}
    
    .viewer-chip {{
      display:inline-block; padding:6px 12px; border-radius:999px; font-size:0.75rem; font-weight:700;
      background: rgba(91,15,46,0.06); border: 1px solid rgba(91,15,46,0.1); color: {BURGUNDY};
      margin-top:10px; margin-bottom: 10px;
    }}

    /* CHAPTER CONTENT FORMATTING */
    .chapter-content h1 {{
        font-size: 2.15rem; font-weight: 800; color: {INK}; margin-top: 0; margin-bottom: 1.5rem;
        border-bottom: 2px solid {BORDER}; padding-bottom: 0.55rem;
    }}
    .chapter-content h2 {{
        font-size: 1.5rem; font-weight: 700; color: {BURGUNDY_DARK}; margin-top: 2rem; margin-bottom: 1rem;
    }}
    .chapter-content p {{
        margin-bottom: 1.25rem; line-height: 1.8; color: {MUTED}; font-size: 0.99rem;
    }}
    .chapter-content table {{
        width: 100%; border-collapse: collapse; margin: 1.5rem 0; background-color: #ffffff;
        border-radius: 0.6rem; overflow: hidden; border: 1px solid {BORDER};
    }}
    .chapter-content th {{
        background: linear-gradient(180deg, {BURGUNDY} 0%, {BURGUNDY_DARK} 100%);
        color: #ffffff; font-weight: 700; text-align: left; padding: 0.85rem 1rem; font-size: 0.88rem;
    }}
    .chapter-content td {{
        padding: 0.8rem 1rem; border-bottom: 1px solid {BORDER}; color: {MUTED}; font-size: 0.88rem; vertical-align: top;
    }}
    .chapter-content tr:last-child td {{ border-bottom: none; }}
    .chapter-content tr:hover td {{ background-color: {ROSE}; }}

    @keyframes floatIn {{
      from {{ opacity: 0; transform: translateY(16px); }}
      to {{ opacity: 1; transform: translateY(0px); }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================
# DATA / CONTENT Dictionaries
# =========================
CHAPTERS_TOP = {
    "1. Executive Overview & Strategic Snapshot": r'''
<div class="chapter-content">
<h1>1. Executive Overview & Strategic Snapshot</h1>
<p>Market estimates indicate a structural paradigm shift in microbiology, transitioning from routine overnight profiling toward time-critical, acute-care decision support where speed creates measurable clinical and economic value.</p>
<p>The global antimicrobial susceptibility testing (AST) market is vast, but the true strategic value lies in carving out the acute-care, speed-sensitive segment. The opportunity narrows from broad routine diagnostics to the high-premium, ultra-rapid phenotypic AST sector where platforms like Gradientech QuickMIC generate actionable clinical value. The data demonstrates a critical shift from legacy workflow automation to time-critical decision support in severe infections.</p>
</div>
''',
    "2. Market Sizing, Geography & Epidemiology": r'''
<div class="chapter-content">
<h1>2. Market Sizing, Geography & Epidemiology</h1>
<p>The geographic distribution of ultra-rapid AST demand is driven by clinical workflow maturity and willingness to pay for time, rather than population size alone. Markets where blood culture utilization is high, microbiology labs operate on extended hours, and stewardship programs are embedded into care pathways generate disproportionately higher revenue per case.</p>
<p>This results in a clear prioritization pattern: United States and Western Europe yield the highest near-term monetization; select Asia-Pacific markets offer strong expansion potential; and emerging markets provide long-term volume upside with slower premium adoption. Revenue concentration follows clinical readiness—not epidemiological scale.</p>
</div>
''',
    "3. Speed Economics & Clinical Thresholds": r'''
<div class="chapter-content">
<h1>3. Speed Economics & Clinical Thresholds</h1>
<p>The economic value of ultra-rapid AST is not determined by speed alone, but by whether results arrive early enough to influence therapy before the next clinical decision point. In sepsis and bloodstream infections, treatment is initiated empirically, and the first opportunity to refine that decision occurs within a narrow window—typically during the next physician round, ICU review, or stewardship intervention.</p>
<p>Diagnostics that fall outside this window primarily confirm therapy. Those that fall within it can directly change escalation, de-escalation, or narrowing decisions, creating measurable clinical and financial impact. Speed creates value only when it aligns with clinical action—not when it merely shortens laboratory time.</p>
</div>
''',
    "4. Competitive Landscape & Positioning": r'''
<div class="chapter-content">
<h1>4. Competitive Landscape & Positioning</h1>
<p>The rapid AST landscape is evolving around a central constraint: speed is valuable only when it preserves clinical trust. While multiple technological approaches are accelerating turnaround time, the market continues to prioritize phenotypic credibility and true MIC-linked interpretability as the basis for therapy decisions. The competitive battlefield is fragmented but consolidating around companies that can deliver True MIC results directly from positive blood cultures.</p>
<p>This section benchmarks Gradientech QuickMIC against direct challengers (QuantaMatrix, Q-linea, Accelerate) and incumbent giants (bioMérieux, BD). Market estimates indicate that true Minimum Inhibitory Concentration (MIC) output combined with ≤4 hour speed commands maximum pricing power.</p>
</div>
''',
    "5. Strategic Playbook & Execution Roadmap": r'''
<div class="chapter-content">
<h1>5. Strategic Playbook & Execution Roadmap</h1>
<p>Converting technology into commercial scale requires executing a sequenced roadmap. Innovation alone does not displace entrenched incumbent monopolies; workflow integration and unassailable clinical health economics do. The growth trajectory of ultra-rapid AST will be determined by how effectively speed is translated into clinical action and repeat utilization.</p>
<p>For Gradientech, the opportunity lies not in competing broadly across all microbiology workflows, but in owning high-acuity decision windows where timing directly alters therapy. QuickMIC succeeds when positioned as a clinical decision-timing platform—not just a faster laboratory analyzer.</p>
</div>
'''
}

CHAPTERS_BOTTOM = {
    "1. Executive Overview & Strategic Snapshot": r'''
<div class="chapter-content">
<h2>Global TAM–SAM–SOM Forecast Definition ($Mn)</h2>
<table>
    <thead>
        <tr>
            <th>Market Layer</th>
            <th>Definition</th>
            <th>2025 ($Mn)</th>
            <th>2030 ($Mn)</th>
            <th>2035 ($Mn)</th>
            <th>25-35 CAGR</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="font-semibold text-slate-800">TAM</td>
            <td class="text-sm">Total AST + broad microbiology ecosystem</td>
            <td>$4,865.0</td>
            <td>$6,791.6</td>
            <td>$9,481.1</td>
            <td>6.9%</td>
        </tr>
        <tr>
            <td style="color:#7A1C41; font-weight:600;">SAM</td>
            <td class="text-sm">Advanced / rapid AST market</td>
            <td>$1,186.0</td>
            <td>$1,945.0</td>
            <td>$3,189.9</td>
            <td>10.4%</td>
        </tr>
        <tr>
            <td style="color:#5B0F2E; font-weight:800; background:#EEDBE4;">SOM</td>
            <td style="font-size:0.875rem; background:#EEDBE4;">Ultra-rapid phenotypic AST core opportunity</td>
            <td style="font-weight:700; background:#EEDBE4;">$82.7</td>
            <td style="font-weight:700; background:#EEDBE4;">$169.3</td>
            <td style="font-weight:700; background:#EEDBE4;">$264.5</td>
            <td style="font-weight:700; background:#EEDBE4;">12.3%</td>
        </tr>
    </tbody>
</table>
<div class="insight-box">Market estimates indicate that while TAM grows steadily, the ultra-rapid SOM scales at nearly double the rate (12.3% CAGR) due to escalating premium pricing power and ICU adoption. The opportunity narrows drastically from broad microbiology to speed-sensitive acute care.</div>
<p>Strategically, this indicates that participation requires distinct competencies. Ultra-rapid AST does not replace the routine lab, but rather commands a high-value clinical niche. Value creation is migrating rapidly toward specialized applications, requiring suppliers to navigate the divide between commoditized consumer diagnostics and high-value, premium acute-care subassemblies.</p>
</div>
''',
    "2. Market Sizing, Geography & Epidemiology": r'''
<div class="chapter-content">
<h2>Strategic Country-Level Prioritization</h2>
<table>
    <thead>
        <tr>
            <th>Rank</th>
            <th>Country</th>
            <th>Strategic Classification</th>
            <th>Market Priority</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>1</td><td><strong>United States</strong></td><td>Priority early market</td><td>Tier 1</td></tr>
        <tr><td>2</td><td><strong>China</strong></td><td>Scalable expansion market</td><td>Tier 1</td></tr>
        <tr><td>3</td><td><strong>Germany</strong></td><td>Priority early market</td><td>Tier 1</td></tr>
        <tr><td>4</td><td><strong>Japan</strong></td><td>Scalable expansion market</td><td>Tier 2</td></tr>
        <tr><td>5</td><td><strong>Italy</strong></td><td>Priority early market</td><td>Tier 2</td></tr>
        <tr><td>6</td><td><strong>United Kingdom</strong></td><td>Priority early market</td><td>Tier 2</td></tr>
        <tr><td>7</td><td><strong>France</strong></td><td>Priority early market</td><td>Tier 2</td></tr>
        <tr><td>8</td><td><strong>South Korea</strong></td><td>Priority early market</td><td>Tier 3</td></tr>
        <tr><td>9</td><td><strong>Spain</strong></td><td>Priority early market</td><td>Tier 3</td></tr>
    </tbody>
</table>
<div class="insight-box">The United States remains the largest single opportunity, combining high clinical intensity with a healthcare system that is more receptive to premium diagnostics that demonstrate outcome and cost benefits. China and Japan represent important expansion markets, where scale and AMR pressure support long-term growth. Detailed country-level sizing has been masked in this preview view for confidentiality.</div>
<h2>Global Market Forecast by Region</h2>
<table>
    <thead>
        <tr>
            <th>Region</th>
            <th>2025 ($Mn)</th>
            <th>2030 ($Mn)</th>
            <th>2035 ($Mn)</th>
            <th>CAGR (2025–2035)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>North America</td><td>$53.0</td><td>$165.0</td><td>$365.0</td><td>21.3%</td></tr>
        <tr><td>Europe</td><td>$49.0</td><td>$140.0</td><td>$305.0</td><td>20.1%</td></tr>
        <tr><td>Asia Pacific</td><td>$31.0</td><td>$96.0</td><td>$278.0</td><td>24.5%</td></tr>
        <tr><td>Rest of World</td><td>$12.0</td><td>$29.0</td><td>$102.0</td><td>23.9%</td></tr>
    </tbody>
</table>
<p>North America emerges as the largest revenue pool by 2035, supported by high ICU intensity and favorable reimbursement dynamics. Europe represents the most important early adoption and validation environment, where IVDR-aligned deployment provides a strong foundation for category formation. Asia Pacific shows the fastest growth trajectory (24.5%), driven by rising AMR burden and expansion of tertiary care infrastructure.</p>
</div>
''',
    "3. Speed Economics & Clinical Thresholds": r'''
<div class="chapter-content">
<h2>Speed Threshold & Clinical Impact</h2>
<table>
    <thead>
        <tr>
            <th>Segment</th>
            <th>Typical Result Timing</th>
            <th>Clinical Impact Window</th>
            <th>Willingness-to-Pay Premium</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Conventional AST (>24 hrs)</td>
            <td>Next day or later</td>
            <td>Primarily confirmatory</td>
            <td>Baseline</td>
        </tr>
        <tr>
            <td>Rapid AST (~7 hrs)</td>
            <td>Same day (early positives only)</td>
            <td>Moderate impact</td>
            <td>+15% to +25%</td>
        </tr>
        <tr>
            <td>Fast Rapid AST (~4 hrs)</td>
            <td>Same-shift (daytime cases)</td>
            <td>High probability of optimization</td>
            <td>+35% to +55%</td>
        </tr>
        <tr style="background:#EEDBE4;">
            <td style="font-weight:700; color:#5B0F2E;">Ultra-Rapid AST (2–4 hrs)</td>
            <td style="font-weight:700; color:#5B0F2E;">Same-shift (broad window)</td>
            <td style="font-weight:700; color:#059669;">Highest probability of therapy change</td>
            <td style="font-weight:700; color:#5B0F2E;">+50% to +90%</td>
        </tr>
    </tbody>
</table>
<div class="insight-box">The difference between a 7-hour and a 3-hour result is not incremental—it expands the proportion of cases where intervention is still possible within the same service window. This is particularly relevant in environments where clinical decisions are clustered around defined time points rather than continuous monitoring.</div>
<p>A 5–7 hour result may influence a subset of early-positive cases, but its impact remains dependent on laboratory timing and staffing patterns. In contrast, a 2–4 hour result captures a much larger share of cases within the actionable window, increasing both clinical relevance and economic return. Clinical and economic value is most concentrated in Intensive Care Units (ICUs), transplant settings, and hematology-oncology wards.</p>
</div>
''',
    "4. Competitive Landscape & Positioning": r'''
<div class="chapter-content">
<h2>Device Benchmarking — Core Competitive Set</h2>
<table>
    <thead>
        <tr>
            <th>System (Company)</th>
            <th>Time-to-Result</th>
            <th>Output</th>
            <th>Status (2026)</th>
            <th>Positioning</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background:#EEDBE4;">
            <td style="font-weight:700; color:#5B0F2E;">QuickMIC (Gradientech)</td>
            <td style="font-weight:700; color:#059669;">2–4 hrs</td>
            <td style="font-weight:700; color:#5B0F2E;">True Linear MIC</td>
            <td>CE-IVDR; U.S. 510(k) pending</td>
            <td>Fastest phenotypic AST disruptor</td>
        </tr>
        <tr>
            <td>dRAST (QuantaMatrix)</td>
            <td>~4–6 hrs</td>
            <td>Discrete MIC</td>
            <td>CE-IVDR</td>
            <td>Fast, direct sepsis-focused</td>
        </tr>
        <tr>
            <td>ASTar (Q-linea)</td>
            <td>~6 hrs</td>
            <td>Discrete MIC</td>
            <td>FDA cleared</td>
            <td>Fully automated U.S. competitor</td>
        </tr>
        <tr>
            <td>VITEK REVEAL (bioMérieux)</td>
            <td>5.5–6 hrs</td>
            <td>MIC-linked</td>
            <td>FDA cleared</td>
            <td>Incumbent-backed fast follower</td>
        </tr>
        <tr>
            <td>Pheno (Accelerate)</td>
            <td>~7 hrs</td>
            <td>Discrete MIC</td>
            <td>Premium+ / Early Mover</td>
            <td>Facing pressure from faster systems</td>
        </tr>
        <tr>
            <td>VITEK 2 / MicroScan</td>
            <td>16–24+ hrs</td>
            <td>Discrete MIC</td>
            <td>Standard of Care</td>
            <td>Vulnerable only in acute ICU cases</td>
        </tr>
    </tbody>
</table>
<div class="insight-box">Gradientech’s continuous linear MIC measurement represents a notable differentiation versus traditional discrete dilution methods. This enables detection of low-level resistance shifts, more precise dosing decisions, and improved stewardship control in borderline susceptibility cases.</div>
<h2>Regulatory Confidence & Disruption Risk</h2>
<p>Regulatory confidence is the bridge between technical speed and routine clinical adoption. For ultra-rapid phenotypic AST, the market does not reward speed in isolation. Hospitals require evidence that a faster result remains aligned with reference methods (Essential Agreement and Categorical Agreement). QuickMIC's ~96% categorical agreement with broth microdilution provides the clinical trust required to displace legacy systems.</p>
<p>Europe offers the most immediate pathway because QuickMIC is already IVDR-certified and positioned for routine implementation. The United States remains the largest single market opportunity, but navigating FDA bottlenecks increases the importance of building strong European clinical evidence before full U.S. commercialization.</p>
</div>
''',
    "5. Strategic Playbook & Execution Roadmap": r'''
<div class="chapter-content">
<h2>Where to Play & How to Win</h2>
<table>
    <thead>
        <tr>
            <th>Strategic Vector</th>
            <th>Primary Recommendation</th>
            <th>Key Rationale</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="font-semibold">Priority Geographies</td>
            <td>US, Germany, UK, Nordics</td>
            <td>Highest density of Tier 1 academic hospitals and willingness to pay premium ASPs.</td>
        </tr>
        <tr>
            <td class="font-semibold">Target User Persona</td>
            <td>ICU Directors + Stewardship</td>
            <td>Lab directors block capital; ICU directors demand speed to reduce mortality.</td>
        </tr>
        <tr>
            <td class="font-semibold">Workflow Defense</td>
            <td>Direct-from-positive BC focus</td>
            <td>Bypasses incumbent sub-culture moat; creates an immediate, untethered testing lane.</td>
        </tr>
        <tr>
            <td class="font-semibold">Commoditization Risk</td>
            <td>Defend via clinical trust (True MIC)</td>
            <td>Rely on the accuracy of phenotypic MIC vs pure prediction from AI or Genotypic testing.</td>
        </tr>
    </tbody>
</table>

<h2>Execution Roadmap (2025–2035)</h2>
<div style="border-left: 4px solid #5B0F2E; padding-left: 20px; margin-bottom: 20px; background: #fff; padding-top:10px; padding-bottom:10px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
    <h3 style="color: #431022; margin-top:0; margin-bottom: 5px;">Phase 1: Validation & European Foothold (2025–2027)</h3>
    <p style="margin-bottom:0; font-size:0.9rem;">Establish reference centers across CE-IVDR territories. Generate pivotal clinical utility and ICU economic evidence (HEOR). Secure FDA pathway milestones. Focus strictly on direct-from-positive blood culture testing for Gram-negative sepsis to build trust.</p>
</div>
<div style="border-left: 4px solid #C9A227; padding-left: 20px; margin-bottom: 20px; background: #fff; padding-top:10px; padding-bottom:10px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
    <h3 style="color: #431022; margin-top:0; margin-bottom: 5px;">Phase 2: Geographic & U.S. Expansion (2028–2031)</h3>
    <p style="margin-bottom:0; font-size:0.9rem;">Scale aggressive U.S. commercial entry post-FDA. Transition from early adopters to broader Tier 2 regional hospital penetration. Optimize distributor networks in APAC/MENA. Shift deeply into reagent rental business models to remove capital constraints.</p>
</div>
<div style="border-left: 4px solid #A45A7B; padding-left: 20px; margin-bottom: 20px; background: #fff; padding-top:10px; padding-bottom:10px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
    <h3 style="color: #431022; margin-bottom: 5px;">Phase 3: Category Leadership (2032–2035)</h3>
    <p style="margin-bottom:0; font-size:0.9rem;">Exploit standard-of-care shift in acute guidelines. Expand menu beyond Gram-negative BSI. Defend speed commoditization through panel breadth and continuous innovation. Deepen recurring consumable utilization to protect margins against incumbent bundles.</p>
</div>
</div>
'''
}


# =========================
# UI Component Helpers
# =========================
def card_metric(label: str, value: str, foot: str):
    st.markdown(f'<div class="metric-card"><div class="metric-label">{label}</div><div class="metric-value">{value}</div><div class="metric-foot">{foot}</div></div>', unsafe_allow_html=True)

def section_open(title: str, subtitle: str = ""):
    st.markdown(
        f'<div class="section-card"><div class="section-title">{title}</div><div class="section-sub">{subtitle}</div>',
        unsafe_allow_html=True,
    )

def section_close():
    st.markdown("</div>", unsafe_allow_html=True)

def apply_theme(fig: go.Figure, title: str) -> go.Figure:
    # Consulting Grade Theme: Light grey background, muted grid lines, crisp typography
    fig.update_layout(
        title=dict(text=title, x=0, font=dict(size=16, color=INK)),
        paper_bgcolor=CHART_BG,
        plot_bgcolor=CHART_BG,
        font=dict(color=INK, family="'Plus Jakarta Sans', sans-serif"),
        margin=dict(l=20, r=20, t=60, b=20),
        legend_title_text="",
        legend=dict(orientation="h", yanchor="bottom", y=1.05, xanchor="right", x=1),
        hoverlabel=dict(bgcolor="white", font_size=13, font_family="'Plus Jakarta Sans', sans-serif", bordercolor=BORDER),
    )
    fig.update_xaxes(showgrid=False, linecolor="rgba(0,0,0,0.1)", tickfont=dict(size=11, color=MUTED), title_font=dict(size=12, color=MUTED))
    fig.update_yaxes(gridcolor="rgba(0,0,0,0.05)", zeroline=False, tickfont=dict(size=11, color=MUTED), title_font=dict(size=12, color=MUTED))
    return fig

def brand_sidebar():
    st.sidebar.markdown(f'<div class="smr-brand"><h1 style="color:{BURGUNDY}; margin:0; font-size:1.1rem; font-weight:800; letter-spacing:-0.02em; line-height:1.2;">Strategic Market Research</h1><p style="color:{MUTED}; margin:4px 0 0 0; font-size:0.82rem; font-weight:500;">Ultra-Rapid Phenotypic AST<br>Preview Dashboard</p></div>', unsafe_allow_html=True)

def page_header(title: str, subtitle: str):
    st.markdown(f'<div class="hero"><div class="hero-head"><h2>{title}</h2></div><p style="font-size: 1rem; color: rgba(255,255,255,0.9); margin:0; max-width:900px; line-height:1.5;">{subtitle}</p></div>', unsafe_allow_html=True)

def page_footer():
    st.markdown(f'<div style="margin-top:30px; text-align:center; padding: 24px; color:{MUTED}; font-size:0.8rem; border-top: 1px solid rgba(0,0,0,0.06);"><strong>Confidential & Proprietary</strong> &copy; 2026 Strategic Market Research<br>To access the full report: info@strategicmarketresearch.com</div>', unsafe_allow_html=True)

# =========================
# Chart Rendering Functions (Consulting Grade)
# =========================
def render_market_layers_chart():
    years = ["2025", "2030", "2035"]
    tam = [4865.0, 6791.6, 9481.1]
    sam = [1186.0, 1945.0, 3189.9]
    som = [82.7, 169.3, 264.5]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=years, y=tam, name='TAM (Broad Micro)', marker_color=ROSE, text=tam, texttemplate='%{text:,.0f}', textposition='inside', insidetextanchor='middle', textfont=dict(color=INK)))
    fig.add_trace(go.Bar(x=years, y=sam, name='SAM (Adv AST)', marker_color=BURGUNDY_SOFT, text=sam, texttemplate='%{text:,.0f}', textposition='inside', insidetextanchor='middle', textfont=dict(color="white")))
    fig.add_trace(go.Bar(x=years, y=som, name='SOM (Ultra-Rapid)', marker_color=BURGUNDY, text=som, texttemplate='%{text:,.1f}', textposition='outside', textfont=dict(color=BURGUNDY, weight="bold")))

    fig.update_layout(barmode='group')
    fig.update_yaxes(title_text="Revenue ($Mn)")
    st.plotly_chart(apply_theme(fig, "Market Layers Expansion ($Mn)"), use_container_width=True, config={"displayModeBar": False})

def render_regional_chart():
    years = ["2025", "2030", "2035"]
    na = [53, 165, 365]
    eu = [49, 140, 305]
    apac = [31, 96, 278]
    row = [12, 29, 102]

    fig = go.Figure()
    # Using Stacked Area Chart (BCG Style)
    fig.add_trace(go.Scatter(x=years, y=row, name='Rest of World', mode='lines', stackgroup='one', line=dict(color=SLATE_LIGHT, width=0), fillcolor=SLATE_LIGHT))
    fig.add_trace(go.Scatter(x=years, y=apac, name='Asia Pacific', mode='lines', stackgroup='one', line=dict(color=GOLD, width=0), fillcolor=GOLD))
    fig.add_trace(go.Scatter(x=years, y=eu, name='Europe', mode='lines', stackgroup='one', line=dict(color=BURGUNDY_SOFT, width=0), fillcolor=BURGUNDY_SOFT))
    fig.add_trace(go.Scatter(x=years, y=na, name='North America', mode='lines', stackgroup='one', line=dict(color=BURGUNDY, width=0), fillcolor=BURGUNDY))

    fig.update_yaxes(title_text="Cumulative Revenue ($Mn)")
    st.plotly_chart(apply_theme(fig, "Regional SOM Growth Forecast"), use_container_width=True, config={"displayModeBar": False})

def render_country_index():
    # Masked Data: Indexing USA to 100 to protect raw numbers. Sorted descending to follow funnel logic preference.
    countries = ["United States", "China", "Germany", "Japan", "Italy", "UK", "France", "S. Korea", "Spain"]
    index_vals = [100, 31, 20, 18, 17, 16, 15, 14, 12]

    # Reversing for horizontal bar chart so biggest is at top
    countries.reverse()
    index_vals.reverse()

    fig = go.Figure(go.Bar(
        x=index_vals, 
        y=countries, 
        orientation='h', 
        marker_color=[BURGUNDY if c == "United States" else GOLD for c in countries],
        text=[f"{v}" for v in index_vals],
        textposition='outside'
    ))
    
    fig.update_layout(showlegend=False)
    fig.update_xaxes(title_text="Relative Opportunity Score (US = 100)")
    st.plotly_chart(apply_theme(fig, "Top 9 Markets (Relative Opportunity Index)"), use_container_width=True, config={"displayModeBar": False})

def render_speed_chart():
    labels = ['Conventional (>24h)', 'Pheno (~7h)', 'ASTar (~6h)', 'VITEK REVEAL (~5.5h)', 'dRAST (~4h)', 'QuickMIC (2-4h)']
    times = [24, 7, 6, 5.75, 4, 3]
    colors = [SLATE_LIGHT, SLATE_LIGHT, SLATE_LIGHT, SLATE_LIGHT, BURGUNDY_SOFT, BURGUNDY]

    # Reversing arrays so quickest is at the top of the chart
    labels.reverse()
    times.reverse()
    colors.reverse()

    fig = go.Figure(go.Bar(
        x=times, 
        y=labels, 
        orientation='h', 
        marker_color=colors,
        text=[f"{t} hrs" for t in times],
        textposition='outside',
        textfont=dict(weight="bold", color=INK)
    ))
    
    fig.update_layout(showlegend=False)
    fig.update_xaxes(title_text="Hours to Result", range=[0, 26])
    st.plotly_chart(apply_theme(fig, "Time-to-Result Benchmarking"), use_container_width=True, config={"displayModeBar": False})

def render_pricing_chart():
    labels = ['QuickMIC', 'Pheno', 'ASTar', 'REVEAL', 'dRAST', 'Conventional']
    prices = [100, 125, 105, 105, 95, 35]
    colors = [BURGUNDY, SLATE, SLATE, SLATE, SLATE, ROSE]

    fig = go.Figure(go.Bar(
        x=labels, 
        y=prices,
        marker_color=colors,
        text=[f"${p}" for p in prices],
        textposition='auto',
        textfont=dict(color="white", weight="bold")
    ))
    fig.update_layout(showlegend=False)
    fig.update_yaxes(title_text="Consumable ASP ($)")
    st.plotly_chart(apply_theme(fig, "Estimated Consumable Pricing Power"), use_container_width=True, config={"displayModeBar": False})

def render_competitor_scatter():
    comps = [
        {"name": "QuickMIC", "time": 3, "prem": 9, "color": BURGUNDY},
        {"name": "dRAST", "time": 4, "prem": 8, "color": BURGUNDY_SOFT},
        {"name": "VITEK REVEAL", "time": 5.75, "prem": 9.5, "color": SLATE},
        {"name": "ASTar", "time": 6, "prem": 7.5, "color": SLATE},
        {"name": "Pheno", "time": 7, "prem": 8, "color": SLATE_LIGHT},
        {"name": "Conventional", "time": 24, "prem": 2, "color": ROSE},
    ]

    fig = go.Figure()
    
    # Add Shaded "Premium Zone" Quadrant (Magic Quadrant Style)
    fig.add_shape(type="rect", x0=5, x1=-2, y0=7.5, y1=11, fillcolor="rgba(91,15,46,0.06)", line=dict(width=0), layer="below")
    fig.add_annotation(x=1.5, y=10.5, text="Premium Innovation Zone", showarrow=False, font=dict(color=BURGUNDY, size=14, weight="bold"))

    for c in comps:
        fig.add_trace(go.Scatter(
            x=[c["time"]], y=[c["prem"]],
            mode="markers+text",
            name=c["name"],
            text=[c["name"]],
            textposition="top center",
            marker=dict(size=16, color=c["color"], line=dict(width=2, color="white"))
        ))
    
    fig.update_layout(showlegend=False)
    fig.update_xaxes(title_text="Time to Result (Hours) ← Closer to 0 is Better", autorange="reversed", range=[26, -2], gridcolor="rgba(0,0,0,0.1)")
    fig.update_yaxes(title_text="Premium Pricing Power (Score)", range=[0, 11], gridcolor="rgba(0,0,0,0.1)")
    st.plotly_chart(apply_theme(fig, "Speed vs. Premium Positioning"), use_container_width=True, config={"displayModeBar": False})

def render_competitor_matrix():
    data = pd.DataFrame({
        "Speed": [5, 4, 3.5, 3.5, 3.5, 3],
        "Workflow": [3, 3, 4, 5, 4, 4],
        "Scale": [2, 2, 3, 5, 2, 5],
        "Installed Base": [1, 2, 2.5, 5, 1, 5],
    }, index=["QuickMIC", "dRAST", "ASTar", "REVEAL", "Selux", "Incumbents"])

    fig = px.imshow(
        data.values, x=data.columns, y=data.index, aspect="auto",
        color_continuous_scale=[[0, "#FAF5F7"], [0.5, GOLD], [1, BURGUNDY]],
        text_auto=True
    )
    fig.update_layout(coloraxis_showscale=False, margin=dict(l=10, r=10, t=50, b=10))
    st.plotly_chart(apply_theme(fig, "Capability & Threat Scorecard (1=Low, 5=High)"), use_container_width=True, config={"displayModeBar": False})


# =========================
# Main app logic & Security Gate
# =========================
def check_access():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        return True

    brand_sidebar()

    with st.sidebar:
        st.markdown("<h3 style='color:var(--ink); font-weight:700; margin-bottom:12px;'>🔐 Access Login</h3>", unsafe_allow_html=True)
        
        with st.form("login_form"):
            name = st.text_input("Name*")
            password = st.text_input("Access Code*", type="password")
            st.markdown("<br>", unsafe_allow_html=True)
            enter = st.form_submit_button("Secure Login", use_container_width=True)

    if enter:
        clean_name = name.strip()
        clean_pass = password.strip()
        
        if not clean_name or not clean_pass:
            st.sidebar.warning("⚠️ Please fill in your Name and Access Code.")
        elif clean_pass != PRIMARY_PASSWORD:
            st.sidebar.error("❌ Invalid Access Code. Please try again.")
        else:
            st.session_state.authenticated = True
            st.session_state.viewer_name = clean_name
            try:
                st.rerun()
            except AttributeError:
                st.experimental_rerun()

    if not st.session_state.authenticated:
        st.markdown(
            f"""
            <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; height:60vh;">
                <h2 style='color:{BURGUNDY}; font-weight:800; font-size:2.4rem;'>Dashboard Secured</h2>
                <p style='color:{MUTED}; font-size:1.1rem;'>Please use the sidebar to authenticate and load the market view.</p>
            </div>
            """, unsafe_allow_html=True)
        st.stop()
    return True

check_access()

# =========================
# Authenticated Shell
# =========================
brand_sidebar()

# Identify User
viewer_name = st.session_state.get("viewer_name", "Guest")
st.sidebar.markdown(f'<div class="viewer-chip">Verified: {viewer_name} | {CLIENT_NAME}</div>', unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)

nav_options = ["Executive Overview"] + list(CHAPTERS_TOP.keys())
page = st.sidebar.radio("Navigate", nav_options, label_visibility="collapsed")

st.sidebar.markdown("---")
if st.sidebar.button("End Session", use_container_width=True):
    st.session_state.authenticated = False
    st.session_state.viewer_name = ""
    try:
        st.rerun()
    except AttributeError:
        st.experimental_rerun()

st.markdown('<div class="main-shell">', unsafe_allow_html=True)

# Router
if page == "Executive Overview":
    page_header("Executive Overview & Metrics", f"Demand expansion, speed economics, geographic scaling, and competitive benchmarking.")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: card_metric("TAM 2035", QUICK_METRICS["TAM 2035 (Broad Micro)"], "Total AST Ecosystem")
    with c2: card_metric("SOM 2035", QUICK_METRICS["SOM 2035 (Ultra-Rapid)"], "Core Market Opportunity")
    with c3: card_metric("SOM CAGR", QUICK_METRICS["SOM CAGR (25-35)"], "High-growth trajectory")
    with c4: card_metric("Threshold", QUICK_METRICS["Clinical Threshold"], "Required for same-shift change")

    st.markdown("<br>", unsafe_allow_html=True)
    
    colA, colB = st.columns([1.1, 1])
    with colA:
        section_open("Market Trajectory", "SOM grows significantly faster than broader TAM.")
        render_market_layers_chart()
        section_close()
    with colB:
        section_open("Time-to-Result Economics", "Only sub-4hr TAT unlocks peak pricing power.")
        render_speed_chart()
        section_close()
        
    page_footer()

else:
    # 100% Safe rendering logic (no HTML splits, no hidden tags)
    st.markdown(
        f"""
        <div class="report-shell">
            <div class="report-card">
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(CHAPTERS_TOP[page], unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Inject the specific charts dynamically
    if "1. " in page:
        render_market_layers_chart()
    elif "2. " in page:
        c1, c2 = st.columns([1.2, 1])
        with c1: render_regional_chart()
        with c2: render_country_index()
    elif "3. " in page:
        render_speed_chart()
    elif "4. " in page:
        c1, c2 = st.columns([1.2, 1])
        with c1: render_competitor_scatter()
        with c2: render_pricing_chart()
        st.markdown("<br>", unsafe_allow_html=True)
        render_competitor_matrix()
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(CHAPTERS_BOTTOM[page], unsafe_allow_html=True)
    
    st.markdown("</div></div><br>", unsafe_allow_html=True)
    
    # Footer Navigation
    idx = nav_options.index(page)
    col1, col2 = st.columns([1, 1])
    with col1:
        if idx > 0:
            if st.button("⬅ Previous"):
                st.session_state["nav_choice"] = nav_options[idx - 1]
                try: st.rerun()
                except AttributeError: st.experimental_rerun()
    with col2:
        if idx < len(nav_options) - 1:
            if st.button("Next ➡"):
                st.session_state["nav_choice"] = nav_options[idx + 1]
                try: st.rerun()
                except AttributeError: st.experimental_rerun()
                
    page_footer()

st.markdown('</div>', unsafe_allow_html=True)
