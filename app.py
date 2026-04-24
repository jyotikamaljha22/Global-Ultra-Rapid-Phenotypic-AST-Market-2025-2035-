import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Ultra-Rapid Phenotypic AST Market | Strategic Dashboard",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# BRAND SYSTEM (Strategic Blue & Slate)
# -----------------------------
BLUE_DARK = "#1e3a8a"   # slate-900 / blue-900 mix
BLUE_PRIMARY = "#2563eb" # blue-600
BLUE_LIGHT = "#93c5fd"   # blue-300
BLUE_SOFT = "#eff6ff"    # blue-50
INK = "#0f172a"          # slate-900
SLATE = "#475569"        # slate-600
SLATE_LIGHT = "#94a3b8"  # slate-400
BORDER = "#e2e8f0"       # slate-200
BG = "#f8fafc"           # slate-50
WHITE = "#ffffff"

PRIMARY_PASSWORD = "SMR2026"
CLIENT_NAME = "Gradientech AB"

QUICK_METRICS = {
    "TAM 2035 (Broad Micro)": "$9.48B",
    "SOM 2035 (Ultra-Rapid)": "$264.5M",
    "SOM CAGR (25-35)": "12.3%",
    "Clinical Threshold": "≤ 4 Hours",
}

# -----------------------------
# DATA / CONTENT
# -----------------------------
CHAPTERS = {
    "1. Executive Overview & Strategic Snapshot": r'''
<div class="chapter-content">
<h1>1. Executive Overview & Strategic Snapshot</h1>
<p>Market estimates indicate a structural paradigm shift in microbiology, transitioning from routine overnight profiling toward time-critical, acute-care decision support where speed creates measurable clinical and economic value.</p>
<p>The global antimicrobial susceptibility testing (AST) market is vast, but the true strategic value lies in carving out the acute-care, speed-sensitive segment. The opportunity narrows from broad routine diagnostics to the high-premium, ultra-rapid phenotypic AST sector where platforms like Gradientech QuickMIC generate actionable clinical value. The data demonstrates a critical shift from legacy workflow automation to time-critical decision support in severe infections.</p>
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
            <td class="font-semibold text-blue-700">SAM</td>
            <td class="text-sm">Advanced / rapid AST market</td>
            <td>$1,186.0</td>
            <td>$1,945.0</td>
            <td>$3,189.9</td>
            <td>10.4%</td>
        </tr>
        <tr>
            <td class="font-bold text-blue-900 bg-blue-50">SOM</td>
            <td class="text-sm bg-blue-50">Ultra-rapid phenotypic AST core opportunity</td>
            <td class="font-bold bg-blue-50">$82.7</td>
            <td class="font-bold bg-blue-50">$169.3</td>
            <td class="font-bold bg-blue-50">$264.5</td>
            <td class="font-bold bg-blue-50">12.3%</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">Market estimates indicate that while TAM grows steadily, the ultra-rapid SOM scales at nearly double the rate (12.3% CAGR) due to escalating premium pricing power and ICU adoption. The opportunity narrows drastically from broad microbiology to speed-sensitive acute care.</div>
<p>Strategically, this indicates that participation requires distinct competencies. Ultra-rapid AST does not replace the routine lab, but rather commands a high-value clinical niche. Value creation is migrating rapidly toward specialized applications, requiring suppliers to navigate the divide between commoditized consumer diagnostics and high-value, premium acute-care subassemblies.</p>
<div class="insight-highlight">The transition toward ultra-rapid components redefines the AST value pool, shifting dependency away from broad lab throughput and toward time-sensitive mobility and stewardship investments.</div>
</div>
''',
    "2. Market Sizing, Geography & Epidemiology": r'''
<div class="chapter-content">
<h1>2. Market Sizing, Geography & Epidemiology</h1>
<p>The geographic distribution of ultra-rapid AST demand is driven by clinical workflow maturity and willingness to pay for time, rather than population size alone. Markets where blood culture utilization is high, microbiology labs operate on extended hours, and stewardship programs are embedded into care pathways generate disproportionately higher revenue per case.</p>
<p>This results in a clear prioritization pattern: United States and Western Europe yield the highest near-term monetization; select Asia-Pacific markets offer strong expansion potential; and emerging markets provide long-term volume upside with slower premium adoption. Revenue concentration follows clinical readiness—not epidemiological scale.</p>
<h2>Country-Level Speed-Sensitive Opportunity</h2>
<table>
    <thead>
        <tr>
            <th>Rank</th>
            <th>Country / Tier</th>
            <th>2025 ($Mn)</th>
            <th>2030 ($Mn)</th>
            <th>2035 ($Mn)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>1</td><td><strong>United States</strong> — Priority early market</td><td>$34.0</td><td>$110.0</td><td>$285.0</td></tr>
        <tr><td>2</td><td><strong>China</strong> — Scalable expansion market</td><td>$8.0</td><td>$28.0</td><td>$88.0</td></tr>
        <tr><td>3</td><td><strong>Germany</strong> — Priority early market</td><td>$10.0</td><td>$24.0</td><td>$58.0</td></tr>
        <tr><td>4</td><td><strong>Japan</strong> — Scalable expansion market</td><td>$7.0</td><td>$19.0</td><td>$52.0</td></tr>
        <tr><td>5</td><td><strong>Italy</strong> — Priority early market</td><td>$8.0</td><td>$22.0</td><td>$48.0</td></tr>
        <tr><td>6</td><td><strong>United Kingdom</strong> — Priority early market</td><td>$8.0</td><td>$21.0</td><td>$46.0</td></tr>
        <tr><td>7</td><td><strong>France</strong> — Priority early market</td><td>$7.0</td><td>$20.0</td><td>$44.0</td></tr>
        <tr><td>8</td><td><strong>South Korea</strong> — Priority early market</td><td>$4.0</td><td>$15.0</td><td>$41.0</td></tr>
        <tr><td>9</td><td><strong>Spain</strong> — Priority early market</td><td>$5.0</td><td>$14.0</td><td>$33.0</td></tr>
    </tbody>
</table>
<div class="post-table-insight">The United States remains the largest single opportunity, combining high clinical intensity with a healthcare system that is more receptive to premium diagnostics that demonstrate outcome and cost benefits. China and Japan represent important expansion markets, where scale and AMR pressure support long-term growth.</div>
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
<div class="insight-highlight">The market expands not through volume substitution, but through progressive clinical integration. Adoption begins in high-acuity ICUs and scales gradually into central hospital labs as clinical confidence in ultra-rapid results builds.</div>
</div>
''',
    "3. Speed Economics & Clinical Thresholds": r'''
<div class="chapter-content">
<h1>3. Speed Economics & Clinical Thresholds</h1>
<p>The economic value of ultra-rapid AST is not determined by speed alone, but by whether results arrive early enough to influence therapy before the next clinical decision point. In sepsis and bloodstream infections, treatment is initiated empirically, and the first opportunity to refine that decision occurs within a narrow window—typically during the next physician round, ICU review, or stewardship intervention.</p>
<p>Diagnostics that fall outside this window primarily confirm therapy. Those that fall within it can directly change escalation, de-escalation, or narrowing decisions, creating measurable clinical and financial impact. Speed creates value only when it aligns with clinical action—not when it merely shortens laboratory time.</p>
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
        <tr class="bg-blue-50">
            <td class="font-bold text-blue-900">Ultra-Rapid AST (2–4 hrs)</td>
            <td class="font-bold text-blue-900">Same-shift (broad window)</td>
            <td class="font-bold text-emerald-700">Highest probability of therapy change</td>
            <td class="font-bold text-blue-900">+50% to +90%</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The difference between a 7-hour and a 3-hour result is not incremental—it expands the proportion of cases where intervention is still possible within the same service window. This is particularly relevant in environments where clinical decisions are clustered around defined time points rather than continuous monitoring.</div>
<p>A 5–7 hour result may influence a subset of early-positive cases, but its impact remains dependent on laboratory timing and staffing patterns. In contrast, a 2–4 hour result captures a much larger share of cases within the actionable window, increasing both clinical relevance and economic return. Clinical and economic value is most concentrated in Intensive Care Units (ICUs), transplant settings, and hematology-oncology wards.</p>
<div class="insight-highlight">In high-acuity environments, earlier optimization reduces inappropriate antibiotic exposure, shortens ICU stay by up to 1-2 days, and lowers downstream complications—each contributing to higher willingness to pay for 2-4 hour diagnostics.</div>
</div>
''',
    "4. Competitive Landscape & Positioning": r'''
<div class="chapter-content">
<h1>4. Competitive Landscape & Positioning</h1>
<p>The rapid AST landscape is evolving around a central constraint: speed is valuable only when it preserves clinical trust. While multiple technological approaches are accelerating turnaround time, the market continues to prioritize phenotypic credibility and true MIC-linked interpretability as the basis for therapy decisions. The competitive battlefield is fragmented but consolidating around companies that can deliver True MIC results directly from positive blood cultures.</p>
<p>This section benchmarks Gradientech QuickMIC against direct challengers (QuantaMatrix, Q-linea, Accelerate) and incumbent giants (bioMérieux, BD). Market estimates indicate that true Minimum Inhibitory Concentration (MIC) output combined with ≤4 hour speed commands maximum pricing power.</p>
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
        <tr class="bg-blue-50">
            <td class="font-bold text-blue-900">QuickMIC (Gradientech)</td>
            <td class="font-bold text-emerald-600">2–4 hrs</td>
            <td class="font-bold text-blue-900">True Linear MIC</td>
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
<div class="post-table-insight">Gradientech’s continuous linear MIC measurement represents a notable differentiation versus traditional discrete dilution methods. This enables detection of low-level resistance shifts, more precise dosing decisions, and improved stewardship control in borderline susceptibility cases.</div>
<h2>Regulatory Confidence & Disruption Risk</h2>
<p>Regulatory confidence is the bridge between technical speed and routine clinical adoption. For ultra-rapid phenotypic AST, the market does not reward speed in isolation. Hospitals require evidence that a faster result remains aligned with reference methods (Essential Agreement and Categorical Agreement). QuickMIC's ~96% categorical agreement with broth microdilution provides the clinical trust required to displace legacy systems.</p>
<p>Europe offers the most immediate pathway because QuickMIC is already IVDR-certified and positioned for routine implementation. The United States remains the largest single market opportunity, but navigating FDA bottlenecks increases the importance of building strong European clinical evidence before full U.S. commercialization.</p>
<div class="insight-highlight">The competitive benchmark is not time alone—it is time multiplied by scale and trust. Gradientech's strongest defendable position is "Fastest actionable phenotypic AST for same-shift therapy optimization."</div>
</div>
''',
    "5. Strategic Playbook & Execution Roadmap": r'''
<div class="chapter-content">
<h1>5. Strategic Playbook & Execution Roadmap</h1>
<p>Converting technology into commercial scale requires executing a sequenced roadmap. Innovation alone does not displace entrenched incumbent monopolies; workflow integration and unassailable clinical health economics do. The growth trajectory of ultra-rapid AST will be determined by how effectively speed is translated into clinical action and repeat utilization.</p>
<p>For Gradientech, the opportunity lies not in competing broadly across all microbiology workflows, but in owning high-acuity decision windows where timing directly alters therapy. QuickMIC succeeds when positioned as a clinical decision-timing platform—not just a faster laboratory analyzer.</p>
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
<div style="border-left: 3px solid #3b82f6; padding-left: 20px; margin-bottom: 20px;">
    <h3 style="color: #1e3a8a; margin-bottom: 5px;">Phase 1: Validation & European Foothold (2025–2027)</h3>
    <p>Establish reference centers across CE-IVDR territories. Generate pivotal clinical utility and ICU economic evidence (HEOR). Secure FDA pathway milestones. Focus strictly on direct-from-positive blood culture testing for Gram-negative sepsis to build trust.</p>
</div>
<div style="border-left: 3px solid #93c5fd; padding-left: 20px; margin-bottom: 20px;">
    <h3 style="color: #1e3a8a; margin-bottom: 5px;">Phase 2: Geographic & U.S. Expansion (2028–2031)</h3>
    <p>Scale aggressive U.S. commercial entry post-FDA. Transition from early adopters to broader Tier 2 regional hospital penetration. Optimize distributor networks in APAC/MENA. Shift deeply into reagent rental business models to remove capital constraints.</p>
</div>
<div style="border-left: 3px solid #e2e8f0; padding-left: 20px; margin-bottom: 20px;">
    <h3 style="color: #1e3a8a; margin-bottom: 5px;">Phase 3: Category Leadership (2032–2035)</h3>
    <p>Exploit standard-of-care shift in acute guidelines. Expand menu beyond Gram-negative BSI. Defend speed commoditization through panel breadth and continuous innovation. Deepen recurring consumable utilization to protect margins against incumbent bundles.</p>
</div>
<div class="insight-highlight">The commercial model is anchored in depth of adoption within selected accounts, rather than broad but shallow placement. Each installed system must translate into high-frequency utilization to unlock recurring consumable revenue.</div>
</div>
'''
}

# -----------------------------
# CSS INJECTION
# -----------------------------
def inject_css(login_mode: bool = False) -> None:
    sidebar_login_hide = "section[data-testid='stSidebar'] {display:none !important;}" if login_mode else ""
    st.markdown(
        f"""
        <style>
            #MainMenu {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            header {{visibility: hidden;}}
            [data-testid="stToolbar"] {{display:none !important;}}
            [data-testid="stDecoration"] {{display:none !important;}}
            .stDeployButton {{display:none !important;}}
            button[data-testid="baseButton-headerNoPadding"] {{display:none !important;}}
            {sidebar_login_hide}

            /* Hide all standard secondary buttons so we don't see dev artifacts */
            button[kind="secondary"] {{display:none;}}

            .stApp {{
                background-color: {BG};
            }}

            html, body, [class*="css"] {{
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                color: {INK};
            }}

            section[data-testid="stSidebar"] {{
                background: {BLUE_DARK};
                border-right: 1px solid rgba(255,255,255,0.05);
            }}

            section[data-testid="stSidebar"] * {{
                color: {BLUE_SOFT} !important;
            }}

            [data-testid="stSidebarNav"] {{
                display:none !important;
            }}

            div[data-baseweb="select"] > div,
            div[data-baseweb="input"] > div {{
                border-radius: 8px !important;
            }}

            .main-shell {{
                max-width: 1360px;
                margin: 0 auto;
                padding-bottom: 2rem;
            }}

            .hero-card {{
                position: relative;
                overflow: hidden;
                background: linear-gradient(135deg, {BLUE_DARK} 0%, {BLUE_PRIMARY} 100%);
                border-radius: 16px;
                padding: 34px 38px;
                color: white;
                box-shadow: 0 10px 25px rgba(30,58,138,0.15);
                border: 1px solid rgba(255,255,255,0.1);
                margin-bottom: 18px;
            }}

            .hero-card:before {{
                content: "";
                position: absolute;
                right: -50px;
                top: -100px;
                width: 300px;
                height: 300px;
                background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);
            }}

            .hero-kicker {{
                font-size: 12px;
                font-weight: 800;
                letter-spacing: 0.16em;
                text-transform: uppercase;
                color: {BLUE_LIGHT};
                margin-bottom: 12px;
            }}

            .hero-title {{
                font-size: 2.6rem;
                line-height: 1.15;
                font-weight: 800;
                margin-bottom: 12px;
            }}

            .hero-subtitle {{
                font-size: 1.1rem;
                color: {BLUE_SOFT};
                max-width: 780px;
            }}

            .metric-card {{
                background: rgba(255,255,255,0.96);
                border: 1px solid {BORDER};
                border-radius: 12px;
                padding: 18px;
                min-height: 140px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            }}

            .metric-label {{
                font-size: 12px;
                text-transform: uppercase;
                letter-spacing: 0.1em;
                color: {SLATE_LIGHT};
                font-weight: 800;
                margin-bottom: 10px;
            }}

            .metric-value {{
                font-size: 1.9rem;
                line-height: 1.1;
                color: {BLUE_DARK};
                font-weight: 800;
                margin-bottom: 8px;
            }}

            .metric-note {{
                font-size: 13px;
                color: {SLATE};
            }}

            .sidebar-brand {{
                background: rgba(255,255,255,0.05);
                border: 1px solid rgba(255,255,255,0.1);
                border-radius: 12px;
                padding: 16px;
                margin-bottom: 10px;
            }}

            .sidebar-kicker {{
                font-size: 11px;
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 0.12em;
                color: {BLUE_LIGHT} !important;
                margin-bottom: 6px;
            }}

            .sidebar-title {{
                font-size: 18px;
                line-height: 1.25;
                font-weight: 800;
                margin-bottom: 6px;
            }}

            .sidebar-sub {{
                font-size: 12px;
                color: {BLUE_SOFT} !important;
            }}

            .sidebar-user {{
                background: rgba(255,255,255,0.03);
                border-radius: 8px;
                padding: 12px;
                border: 1px solid rgba(255,255,255,0.05);
                margin: 10px 0 14px;
                font-size: 13px;
            }}

            .section-title {{
                font-size: 1.3rem;
                font-weight: 800;
                color: {INK};
                margin: 0 0 0.35rem 0;
            }}

            .section-subtitle {{
                color: {SLATE};
                font-size: 0.95rem;
                margin-bottom: 1rem;
            }}

            .report-shell {{
                background: {WHITE};
                border: 1px solid {BORDER};
                border-radius: 16px;
                box-shadow: 0 10px 25px rgba(15,23,42,0.05);
                overflow: hidden;
                margin-top: 16px;
            }}

            .report-banner {{
                background: {BLUE_SOFT};
                border-bottom: 1px solid {BORDER};
                padding: 18px 26px;
            }}

            .report-title {{
                font-size: 1.5rem;
                font-weight: 800;
                color: {BLUE_DARK};
            }}

            .report-card {{
                padding: 26px 30px 30px 30px;
            }}

            .chapter-content h1 {{
                font-size: 2rem;
                font-weight: 800;
                color: {INK};
                margin-top: 0;
                margin-bottom: 1.2rem;
                border-bottom: 2px solid {BORDER};
                padding-bottom: 0.5rem;
            }}

            .chapter-content h2 {{
                font-size: 1.4rem;
                font-weight: 700;
                color: {BLUE_DARK};
                margin-top: 2rem;
                margin-bottom: 1rem;
            }}

            .chapter-content p {{
                margin-bottom: 1.2rem;
                line-height: 1.75;
                color: {SLATE};
                font-size: 0.98rem;
            }}

            .chapter-content table {{
                width: 100%;
                border-collapse: collapse;
                margin: 1.5rem 0;
                background-color: {WHITE};
                border-radius: 8px;
                overflow: hidden;
                border: 1px solid {BORDER};
            }}

            .chapter-content th {{
                background: {BLUE_DARK};
                color: {WHITE};
                font-weight: 600;
                text-align: left;
                padding: 0.75rem 1rem;
                font-size: 0.85rem;
            }}

            .chapter-content td {{
                padding: 0.75rem 1rem;
                border-bottom: 1px solid {BORDER};
                color: {SLATE};
                font-size: 0.85rem;
                vertical-align: top;
            }}

            .chapter-content tr:last-child td {{
                border-bottom: none;
            }}

            .chapter-content tr:hover td {{
                background-color: {BLUE_SOFT};
            }}

            .insight-highlight {{
                background-color: {BLUE_SOFT};
                border-left: 4px solid {BLUE_PRIMARY};
                padding: 1rem 1.25rem;
                margin: 1.5rem 0;
                font-style: italic;
                color: {BLUE_DARK};
                font-weight: 500;
                border-radius: 0 8px 8px 0;
            }}

            .post-table-insight {{
                background-color: #f8fafc;
                border: 1px solid {BORDER};
                padding: 1rem;
                margin-top: -1rem;
                margin-bottom: 1.5rem;
                font-size: 0.88rem;
                color: {SLATE};
                border-radius: 0 0 8px 8px;
            }}

            [data-testid="stForm"] {{
                border: none !important;
                padding: 0 !important;
            }}

            [data-testid="stTextInput"] label {{
                font-weight: 600 !important;
                color: {INK} !important;
            }}
            
            .stButton > button {{
                background: {BLUE_PRIMARY};
                color: white;
                border: none;
                border-radius: 8px;
                padding: 0.6rem 1rem;
                font-weight: 600;
                box-shadow: 0 4px 6px rgba(37,99,235,0.2);
            }}

            .stButton > button:hover {{
                filter: brightness(1.1);
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# HELPERS & CHARTS
# -----------------------------
def metric_card(label: str, value: str, note: str) -> None:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def section_intro(title: str, subtitle: str) -> None:
    st.markdown(f'<div class="section-title">{title}</div><div class="section-subtitle">{subtitle}</div>', unsafe_allow_html=True)

def style_plot(fig: go.Figure, title: str, height: int = 360) -> go.Figure:
    fig.update_layout(
        title=dict(text=title, x=0, font=dict(size=16, color=BLUE_DARK)),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(family="Inter, sans-serif", color=SLATE),
        margin=dict(l=10, r=10, t=50, b=10),
        height=height,
        legend=dict(orientation="h", yanchor="bottom", y=1.05, xanchor="right", x=1),
    )
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(gridcolor=BORDER, zeroline=False)
    return fig

def render_market_layers_chart():
    years = ["2025", "2030", "2035"]
    tam = [4865.0, 6791.6, 9481.1]
    sam = [1186.0, 1945.0, 3189.9]
    som = [82.7, 169.3, 264.5]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=years, y=tam, name='TAM (Broad Micro)', marker_color=BORDER))
    fig.add_trace(go.Bar(x=years, y=sam, name='SAM (Adv AST)', marker_color=BLUE_LIGHT))
    fig.add_trace(go.Bar(x=years, y=som, name='SOM (Ultra-Rapid)', marker_color=BLUE_PRIMARY))

    fig.update_layout(barmode='group')
    fig.update_yaxes(title_text="Revenue ($Mn)")
    style_plot(fig, "Market Layers Expansion ($Mn)")
    st.plotly_chart(fig, use_container_width=True)

def render_regional_chart():
    years = ["2025", "2030", "2035"]
    na = [53, 165, 365]
    eu = [49, 140, 305]
    apac = [31, 96, 278]
    row = [12, 29, 102]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=na, name='North America', mode='lines+markers', line=dict(color=BLUE_DARK, width=3)))
    fig.add_trace(go.Scatter(x=years, y=eu, name='Europe', mode='lines+markers', line=dict(color=BLUE_PRIMARY, width=3)))
    fig.add_trace(go.Scatter(x=years, y=apac, name='Asia Pacific', mode='lines+markers', line=dict(color=BLUE_LIGHT, width=3)))
    fig.add_trace(go.Scatter(x=years, y=row, name='Rest of World', mode='lines+markers', line=dict(color=SLATE_LIGHT, width=3)))

    fig.update_yaxes(title_text="Revenue ($Mn)")
    style_plot(fig, "Regional SOM Growth Forecast")
    st.plotly_chart(fig, use_container_width=True)

def render_speed_chart():
    labels = ['Conventional', 'Pheno', 'ASTar', 'VITEK REVEAL', 'dRAST', 'QuickMIC']
    times = [24, 7, 6, 5.75, 4, 3]
    colors = [SLATE_LIGHT, '#f97316', '#f59e0b', '#fbbf24', '#10b981', '#059669']

    fig = go.Figure(go.Bar(
        x=times, 
        y=labels, 
        orientation='h', 
        marker_color=colors,
        text=[f"{t} hrs" for t in times],
        textposition='outside'
    ))
    fig.update_xaxes(title_text="Hours to Result", max=26)
    style_plot(fig, "Time-to-Result Benchmarking")
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

def render_pricing_chart():
    labels = ['QuickMIC', 'Pheno', 'ASTar', 'REVEAL', 'dRAST', 'Conventional']
    prices = [100, 125, 105, 105, 95, 35]
    colors = [BLUE_DARK, SLATE, SLATE, SLATE, SLATE, BORDER]

    fig = go.Figure(go.Bar(
        x=labels, 
        y=prices,
        marker_color=colors,
        text=[f"${p}" for p in prices],
        textposition='auto'
    ))
    fig.update_yaxes(title_text="Consumable ASP ($)")
    style_plot(fig, "Estimated Consumable Pricing Power")
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

def render_competitor_scatter():
    comps = [
        {"name": "QuickMIC", "time": 3, "prem": 9, "color": BLUE_DARK},
        {"name": "dRAST", "time": 4, "prem": 8, "color": BLUE_PRIMARY},
        {"name": "VITEK REVEAL", "time": 5.75, "prem": 9.5, "color": SLATE},
        {"name": "ASTar", "time": 6, "prem": 7.5, "color": SLATE_LIGHT},
        {"name": "Pheno", "time": 7, "prem": 8, "color": "#f97316"},
        {"name": "Conventional", "time": 24, "prem": 2, "color": BORDER},
    ]

    fig = go.Figure()
    for c in comps:
        fig.add_trace(go.Scatter(
            x=[c["time"]], y=[c["prem"]],
            mode="markers+text",
            name=c["name"],
            text=[c["name"]],
            textposition="top center",
            marker=dict(size=14, color=c["color"])
        ))
    
    fig.update_xaxes(title_text="Time to Result (Hours) ← Closer to 0 is Better", autorange="reversed", range=[25, 0])
    fig.update_yaxes(title_text="Premium Pricing Power (Score)", range=[0, 11])
    style_plot(fig, "Speed vs. Premium Positioning")
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# PAGE RENDERERS
# -----------------------------
def render_hero() -> None:
    st.markdown(
        f"""
        <div class="hero-card">
            <div class="hero-kicker">Strategic Market Research</div>
            <div class="hero-title">Global Ultra-Rapid Phenotypic AST Market (2025–2035)</div>
            <div class="hero-subtitle">Prepared for {CLIENT_NAME}. Demand expansion, speed economics, geographic scaling, and competitive benchmarking for ultra-rapid workflows.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_overview() -> None:
    render_hero()

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("TAM 2035 (Broad Micro)", QUICK_METRICS["TAM 2035 (Broad Micro)"], "Total AST Ecosystem")
    with c2:
        metric_card("SOM 2035 (Ultra-Rapid)", QUICK_METRICS["SOM 2035 (Ultra-Rapid)"], "Core Market Opportunity")
    with c3:
        metric_card("SOM CAGR (25-35)", QUICK_METRICS["SOM CAGR (25-35)"], "High-growth trajectory")
    with c4:
        metric_card("Clinical Threshold", QUICK_METRICS["Clinical Threshold"], "Required for same-shift change")

    st.markdown("<br>", unsafe_allow_html=True)
    section_intro("Dashboard Overview", "Use the sidebar to explore the full 5-chapter boardroom report covering market sizing, competitive dynamics, and the commercial playbook.")

    colA, colB = st.columns([1, 1])
    with colA:
        render_market_layers_chart()
    with colB:
        render_speed_chart()

def render_prev_next(options: list[str], current: str) -> None:
    idx = options.index(current)
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if idx > 0:
            if st.button("⬅ Previous"):
                st.session_state["nav_choice"] = options[idx - 1]
                st.rerun()

    with col2:
        if idx < len(options) - 1:
            if st.button("Next ➡"):
                st.session_state["nav_choice"] = options[idx + 1]
                st.rerun()

def render_chapter_page(title: str, nav_options: list[str]) -> None:
    st.markdown(
        f"""
        <div class="report-shell">
            <div class="report-banner">
                <div class="report-title">{title}</div>
            </div>
            <div class="report-card">
        """,
        unsafe_allow_html=True,
    )
    
    html_content = CHAPTERS[title]
    
    # Safely split by the marker
    parts = html_content.split("")
    
    st.markdown(parts[0], unsafe_allow_html=True)
    
    if len(parts) > 1:
        # Render the specific inline chart based on chapter
        if title.startswith("1. "):
            render_market_layers_chart()
        elif title.startswith("2. "):
            render_regional_chart()
        elif title.startswith("3. "):
            render_speed_chart()
        elif title.startswith("4. "):
            colA, colB = st.columns(2)
            with colA:
                render_competitor_scatter()
            with colB:
                render_pricing_chart()

        st.markdown(parts[1], unsafe_allow_html=True)

    st.markdown("</div></div><br>", unsafe_allow_html=True)
    render_prev_next(nav_options, title)

    st.markdown("""
    ---
    **Confidential & Proprietary** © 2026 Strategic Market Research  

    To access the full report:  
    📩 info@strategicmarketresearch.com
    """)

def render_login() -> None:
    inject_css(login_mode=True)
    
    _, col, _ = st.columns([1, 1.2, 1])
    
    with col:
        st.markdown("<div style='margin-top: 120px;'></div>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown(f"""
                <h2 style='text-align: center; color: {BLUE_DARK}; padding-bottom: 15px;'>
                    SMR BOARDROOM ACCESS
                </h2>
            """, unsafe_allow_html=True)
            
            name = st.text_input("Name", placeholder="Enter your name")
            password = st.text_input("Password", type="password", placeholder="Enter password")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("Enter Dashboard", type="primary", use_container_width=True):
                if password == PRIMARY_PASSWORD:
                    st.session_state.authenticated = True
                    st.session_state.visitor_name = name.strip()
                    st.session_state.nav_choice = "Overview"
                    st.rerun()
                else:
                    st.error("Incorrect password")

# -----------------------------
# APP ROUTING
# -----------------------------
if not st.session_state.authenticated:
    render_login()
    st.stop()

inject_css(login_mode=False)

nav_options = ["Overview"] + list(CHAPTERS.keys())

st.sidebar.markdown(
    f"""
    <div class="sidebar-brand">
        <div class="sidebar-kicker">Strategic Market Research</div>
        <div class="sidebar-title">Ultra-Rapid AST Market</div>
        <div class="sidebar-sub">Client: {CLIENT_NAME}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    f"""
    <div class="sidebar-user">
        Viewing as <strong>{st.session_state.visitor_name}</strong><br>
        Premium Boardroom Briefing
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.radio(
    "Navigate",
    nav_options,
    key="nav_choice",
    label_visibility="collapsed",
)

st.sidebar.caption("Confidential & Proprietary")
st.sidebar.caption("© 2026 Strategic Market Research")
if st.sidebar.button("Logout", type="primary", use_container_width=True):
    st.session_state.authenticated = False
    st.session_state.visitor_name = ""
    st.session_state.nav_choice = "Overview"
    st.rerun()

st.markdown('<div class="main-shell">', unsafe_allow_html=True)
if st.session_state.nav_choice == "Overview":
    render_overview()
else:
    render_chapter_page(st.session_state.nav_choice, nav_options)
st.markdown('</div>', unsafe_allow_html=True)