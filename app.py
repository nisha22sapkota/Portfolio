import streamlit as st
import base64

def _img_b64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

PROFILE_IMG = _img_b64("assets/profile.jpg")

st.set_page_config(
    page_title="Nisha Sapkota | Quant & AI Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS injection (works in Streamlit 1.45) ──────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stAppViewContainer"] { background: #0a0e1a !important; }
[data-testid="stMainBlockContainer"] { padding: 0 2rem !important; max-width: 1200px !important; }
[data-testid="stVerticalBlock"] { gap: 0.5rem !important; }
section[data-testid="stSidebar"] { display: none; }
</style>
""", unsafe_allow_html=True)

# ── HTML helpers (each call is self-contained) ───────────────────────────────
def stack_tags(tags: list) -> str:
    items = "".join(
        f'<span style="font-size:11px;background:rgba(79,255,176,0.07);'
        f'border:1px solid rgba(79,255,176,0.2);color:#4fffb0;padding:3px 8px;'
        f'border-radius:4px;font-family:JetBrains Mono,monospace;margin:2px 2px 0 0">{t}</span>'
        for t in tags
    )
    return (
        '<div style="display:flex;flex-wrap:wrap;gap:4px;margin-top:12px;'
        f'padding-top:12px;border-top:1px solid #21262d">{items}</div>'
    )

def exp_tags(tags: list) -> str:
    items = "".join(
        f'<span style="font-size:11px;background:rgba(33,38,45,0.8);border:1px solid #30363d;'
        f'color:#8b949e;padding:3px 8px;border-radius:4px;font-family:JetBrains Mono,monospace;'
        f'margin:2px 2px 0 0">{t}</span>'
        for t in tags
    )
    return f'<div style="display:flex;flex-wrap:wrap;gap:4px;margin-top:10px">{items}</div>'

def skill_group_html(group_title: str, skills: list) -> str:
    bars = "".join(f"""
        <div style="margin-bottom:12px">
            <div style="display:flex;justify-content:space-between;font-size:13px;
                        color:#c9d1d9;margin-bottom:5px">
                <span>{name}</span>
                <span style="color:#8b949e;font-family:'JetBrains Mono',monospace;
                             font-size:11px">{pct}%</span>
            </div>
            <div style="height:4px;background:#21262d;border-radius:2px;overflow:hidden">
                <div style="height:100%;width:{pct}%;background:linear-gradient(90deg,#4fffb0,#00d4aa);
                            border-radius:2px"></div>
            </div>
        </div>""" for name, pct in skills)
    return f"""
    <div style="background:#0d1117;border:1px solid #21262d;border-radius:10px;padding:22px">
        <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#4fffb0;
                    text-transform:uppercase;letter-spacing:1px;margin-bottom:16px;
                    font-weight:600">{group_title}</div>
        {bars}
    </div>"""

def project_card_html(p: dict) -> str:
    featured_banner = (
        '<div style="position:absolute;top:14px;right:14px;font-family:JetBrains Mono,monospace;'
        'font-size:9px;color:#4fffb0;background:rgba(79,255,176,0.1);'
        'border:1px solid rgba(79,255,176,0.3);padding:3px 8px;border-radius:4px;'
        'letter-spacing:1px">FEATURED</div>'
    ) if p["featured"] else ""
    border  = "rgba(79,255,176,0.4)" if p["featured"] else "#21262d"
    bg      = "linear-gradient(135deg,#0d1117 0%,#0a1e14 100%)" if p["featured"] else "#0d1117"
    bullets = "".join(
        f'<li style="font-size:12px;color:#8b949e;padding:3px 0 3px 14px;'
        f'position:relative;list-style:none">'
        f'<span style="position:absolute;left:0;color:#4fffb0;font-size:10px">▸</span>{h}</li>'
        for h in p["highlights"]
    )
    return f"""
    <div style="background:{bg};border:1px solid {border};border-radius:10px;
                padding:24px;position:relative;height:100%">
        {featured_banner}
        <div style="font-size:26px;margin-bottom:12px">{p['icon']}</div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:10px;color:#4fffb0;
                    text-transform:uppercase;letter-spacing:1.5px;margin-bottom:8px">{p['category']}</div>
        <div style="font-size:16px;font-weight:600;color:#f0f6fc;margin-bottom:10px;
                    line-height:1.3">{p['title']}</div>
        <div style="font-size:13px;color:#8b949e;line-height:1.65;margin-bottom:12px">{p['desc']}</div>
        <ul style="padding:0;margin:0">{bullets}</ul>
        {stack_tags(p['stack'])}
    </div>"""

# ════════════════════════════════════════════════════════════════════════════
# NAV
# ════════════════════════════════════════════════════════════════════════════
st.html("""
<div style="background:rgba(13,17,27,0.97);border-bottom:1px solid #21262d;
            padding:14px 0;display:flex;justify-content:space-between;align-items:center;
            margin:0 -2rem;padding-left:2rem;padding-right:2rem">
    <div style="font-family:'JetBrains Mono',monospace;font-size:16px;
                font-weight:500;color:#4fffb0">nisha.sapkota</div>
    <div style="font-size:13px;color:#8b949e;font-weight:500">
        About &nbsp;·&nbsp; Experience &nbsp;·&nbsp; Projects &nbsp;·&nbsp; Skills &nbsp;·&nbsp; Contact
    </div>
</div>
""")

# ════════════════════════════════════════════════════════════════════════════
# HERO
# ════════════════════════════════════════════════════════════════════════════
st.html(f"""
<div style="background:linear-gradient(135deg,#0d1117 0%,#0a1628 60%,#0d1117 100%);
            border:1px solid #21262d;border-radius:12px;padding:60px 52px 48px;
            position:relative;overflow:hidden;margin-top:16px">
    <div style="position:absolute;top:-20%;right:-10%;width:400px;height:400px;
                background:radial-gradient(circle,rgba(79,255,176,0.07) 0%,transparent 70%);
                pointer-events:none"></div>

    <div style="display:flex;align-items:center;justify-content:space-between;gap:40px;flex-wrap:wrap">

        <!-- Left: text -->
        <div style="flex:1;min-width:280px">
            <div style="display:inline-block;background:rgba(79,255,176,0.1);
                        border:1px solid rgba(79,255,176,0.3);color:#4fffb0;
                        font-family:'JetBrains Mono',monospace;font-size:11px;padding:4px 12px;
                        border-radius:20px;margin-bottom:20px;letter-spacing:1px">
                OPEN TO WORK · QUANT / AI / INVESTMENT STRATEGY · WEALTH TECH
            </div>

            <div style="font-size:50px;font-weight:700;color:#f0f6fc;line-height:1.1;
                        margin-bottom:10px;letter-spacing:-1px">Nisha Sapkota</div>

            <div style="font-size:19px;font-weight:400;color:#8b949e;margin-bottom:18px">
                Quant Researcher &amp;
                <span style="color:#4fffb0;font-weight:500">AI/ML Specialist</span> in Finance
            </div>

            <div style="font-size:14px;color:#8b949e;line-height:1.75;max-width:520px;margin-bottom:28px">
                MS Business Analytics candidate at UT Austin McCombs. I build AI-driven investment tools —
                from tax-loss harvesting engines to RAG-based AI systems — at the intersection of machine
                learning and quantitative finance.
            </div>

            <div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:28px">
                <span style="background:rgba(33,38,45,0.8);border:1px solid #30363d;color:#c9d1d9;
                             font-size:12px;padding:6px 12px;border-radius:6px;
                             font-family:'JetBrains Mono',monospace">🎓 UT Austin MSBA '26</span>
                <span style="background:rgba(33,38,45,0.8);border:1px solid #30363d;color:#c9d1d9;
                             font-size:12px;padding:6px 12px;border-radius:6px;
                             font-family:'JetBrains Mono',monospace">📍 Austin, TX</span>
                <span style="background:rgba(33,38,45,0.8);border:1px solid #30363d;color:#c9d1d9;
                             font-size:12px;padding:6px 12px;border-radius:6px;
                             font-family:'JetBrains Mono',monospace">💼 ex-RBC Capital Markets</span>
                <span style="background:rgba(33,38,45,0.8);border:1px solid #30363d;color:#c9d1d9;
                             font-size:12px;padding:6px 12px;border-radius:6px;
                             font-family:'JetBrains Mono',monospace">🤖 AI · Quant · WealthTech</span>
            </div>

            <div style="display:flex;gap:12px;flex-wrap:wrap">
                <a href="https://www.linkedin.com/in/nisha-sapkota-aidata/" target="_blank"
                   style="background:#4fffb0;color:#0d1117;font-weight:600;font-size:13px;
                          padding:10px 22px;border-radius:6px;text-decoration:none">
                    LinkedIn Profile ↗
                </a>
                <a href="mailto:nisha.sapkota.ai@gmail.com"
                   style="background:transparent;color:#c9d1d9;font-weight:500;font-size:13px;
                          padding:10px 22px;border-radius:6px;text-decoration:none;
                          border:1px solid #30363d">
                    Get In Touch →
                </a>
            </div>
        </div>

        <!-- Right: photo -->
        <div style="flex-shrink:0">
            <div style="width:220px;height:220px;border-radius:50%;overflow:hidden;
                        border:3px solid #4fffb0;
                        box-shadow:0 0 32px rgba(79,255,176,0.2)">
                <img src="data:image/jpeg;base64,{PROFILE_IMG}"
                     style="width:120%;height:120%;margin-left:-10%;margin-top:-5%;
                            object-fit:cover;object-position:center top"
                     alt="Nisha Sapkota">
            </div>
        </div>

    </div>
</div>
""")

# Stats row
st.markdown("---", help=None)
for col, number, label in zip(
    st.columns(4),
    ["5+", "6", "2", "10+"],
    ["Years of Experience", "Projects Built", "Industry Awards", "Tools & Languages"],
):
    with col:
        st.html(f"""
        <div style="background:#0d1117;border:1px solid #21262d;border-radius:10px;
                    padding:24px;text-align:center">
            <div style="font-size:34px;font-weight:700;color:#4fffb0;
                        font-family:'JetBrains Mono',monospace">{number}</div>
            <div style="font-size:11px;color:#8b949e;margin-top:6px;
                        text-transform:uppercase;letter-spacing:0.5px">{label}</div>
        </div>
        """)

# ════════════════════════════════════════════════════════════════════════════
# EXPERIENCE
# ════════════════════════════════════════════════════════════════════════════
st.html("""
<div style="padding:12px 0 4px">
    <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#4fffb0;
                letter-spacing:2px;text-transform:uppercase;margin-bottom:4px">CAREER</div>
    <div style="font-size:28px;font-weight:700;color:#f0f6fc;letter-spacing:-0.5px">Experience</div>
</div>
""")

experiences = [
    {
        "icon": "📈", "company": "Vise",
        "role": "Investment Specialist / Quant Researcher · Internship",
        "period": "Jan 2026 – Present",
        "desc": (
            "Designed and implemented a tax-loss harvesting simulation engine as part of the UT Austin "
            "MSBA Capstone. Built portfolio rebalancing strategies with threshold drift-band logic, lot "
            "tracking (FIFO/LIFO/TAX_OPTIMAL), short/long-term gain classification, and loss carry-forward. "
            "Delivered an institutional-grade Streamlit dashboard with backtesting and strategy comparison analytics."
        ),
        "tags": ["Python", "Streamlit", "Pandas", "Portfolio Optimization",
                 "Tax-Loss Harvesting", "Backtesting", "Plotly"],
    },
    {
        "icon": "🏦", "company": "RBC Capital Markets",
        "role": "Business Data Analyst · 2+ Years",
        "period": "May 2023 – Jun 2025",
        "desc": (
            "Developed executive-level dashboards and data pipelines for finance and operations teams. "
            "Delivered actionable insights through Tableau, NetSuite Analytics, and SQL, supporting "
            "data-driven decision making across capital markets operations."
        ),
        "tags": ["Tableau", "SQL", "NetSuite Analytics", "ETL", "Excel", "Data Visualization"],
    },
    {
        "icon": "💡", "company": "Logic (Acquired by Accenture)",
        "role": "Associate Consultant · 2+ Years",
        "period": "Apr 2021 – May 2023",
        "desc": (
            "Led cross-functional consulting engagements and enterprise solution delivery. "
            "Performed business analysis, process design, and stakeholder management across "
            "multiple industry verticals."
        ),
        "tags": ["Business Analysis", "Consulting", "Enterprise Solutions", "Stakeholder Management"],
    },
]

for exp in experiences:
    st.html(f"""
    <div style="display:flex;gap:20px;padding:18px 0;border-bottom:1px solid #21262d">
        <div style="width:42px;height:42px;border-radius:50%;background:rgba(79,255,176,0.1);
                    border:2px solid #4fffb0;display:flex;align-items:center;justify-content:center;
                    font-size:17px;flex-shrink:0;margin-top:2px">{exp['icon']}</div>
        <div style="flex:1">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;
                        flex-wrap:wrap;gap:6px;margin-bottom:3px">
                <div style="font-size:16px;font-weight:600;color:#f0f6fc">{exp['company']}</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#8b949e;
                            background:rgba(33,38,45,0.8);border:1px solid #30363d;
                            padding:2px 9px;border-radius:4px">{exp['period']}</div>
            </div>
            <div style="font-size:13px;color:#4fffb0;font-weight:500;margin-bottom:7px">{exp['role']}</div>
            <div style="font-size:13px;color:#8b949e;line-height:1.65">{exp['desc']}</div>
            {exp_tags(exp['tags'])}
        </div>
    </div>
    """)

# ════════════════════════════════════════════════════════════════════════════
# PROJECTS
# ════════════════════════════════════════════════════════════════════════════
st.html("""
<div style="padding:20px 0 8px">
    <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#4fffb0;
                letter-spacing:2px;text-transform:uppercase;margin-bottom:4px">WORK</div>
    <div style="font-size:28px;font-weight:700;color:#f0f6fc;letter-spacing:-0.5px">Projects</div>
</div>
""")

projects = [
    {
        "icon": "🧮", "featured": True,
        "category": "Quant Finance · Vise Capstone",
        "title": "Tax-Loss Harvesting & Portfolio Optimization Engine",
        "desc": (
            "Institutional-grade simulation engine for Vise's MSBA Capstone. Models after-tax portfolio "
            "returns with full lot tracking, rebalancing strategies, and a Bloomberg-terminal Streamlit dashboard."
        ),
        "highlights": [
            "ST/LT gain classification with loss carry-forward and $3k ordinary income offset",
            "Lot selection: FIFO, LIFO, TAX_OPTIMAL — daily through threshold drift-band rebalancing",
            "Strategy comparison: CAGR, Sharpe, max drawdown, tracking error, IR",
            "CI via GitHub Actions; Excel export; DRIP dividend reinvestment",
        ],
        "stack": ["Python", "Streamlit", "Pandas", "NumPy", "Plotly", "SciPy", "GitHub Actions"],
    },
    {
        "icon": "🏥", "featured": False,
        "category": "Generative AI · RAG · Great Learning",
        "title": "Medical Diagnostic RAG AI System",
        "desc": (
            "RAG-based AI using the Merck Medical Manuals to assist clinicians with diagnostic questions, "
            "drug info, and treatment plans. Addresses information overload in clinical decision-making."
        ),
        "highlights": [
            "Ingested and indexed Merck Manuals into a vector knowledge base",
            "Retrieval pipeline for diagnostic, drug, and treatment queries",
            "Natural language clinical Q&A with precision/recall evaluation",
        ],
        "stack": ["Python", "LLM / RAG", "Vector DB", "LangChain", "NLP"],
    },
    {
        "icon": "🌱", "featured": False,
        "category": "Computer Vision · Deep Learning · Great Learning",
        "title": "Plant Seedlings Classification (CNN)",
        "desc": (
            "Convolutional Neural Network to classify plant seedlings into 12 species from images. "
            "Built for the agricultural industry to automate crop/weed identification, reducing manual labor "
            "and enabling better crop yield decisions."
        ),
        "highlights": [
            "12-class image classification across species including Black-grass, Maize, Sugar beet, and more",
            "Custom CNN architecture built with TensorFlow / Keras on numpy image arrays",
            "Image preprocessing pipeline: normalization, reshaping, augmentation",
            "Dataset from Aarhus University (University of Southern Denmark collaboration)",
        ],
        "stack": ["Python", "TensorFlow", "Keras", "CNN", "NumPy", "Computer Vision"],
    },
    {
        "icon": "🏦", "featured": False,
        "category": "Neural Networks · Classification · Great Learning",
        "title": "Bank Customer Churn Prediction (Neural Network)",
        "desc": (
            "Neural network classifier to predict whether a bank customer will churn within 6 months. "
            "Built to help management prioritize retention strategies and improve service quality."
        ),
        "highlights": [
            "Final model: Adam optimizer + dropout (0.2) — AUC 0.83 on test set",
            "Recall of 70.9% — correctly identified ~71% of customers who actually churned",
            "Features: credit score, age, tenure, balance, number of products, geography",
            "Actionable insights: dormant member re-engagement, product diversification, tenure-based retention",
        ],
        "stack": ["Python", "Keras", "TensorFlow", "Neural Networks", "Scikit-learn", "Pandas"],
    },
    {
        "icon": "🛂", "featured": False,
        "category": "ML Classification · Ensemble Methods · Great Learning",
        "title": "EasyVisa — US Visa Approval Prediction",
        "desc": (
            "ML solution for the US Office of Foreign Labor Certification (OFLC) to predict visa "
            "certification outcomes and identify key approval drivers. Benchmarked 5 models."
        ),
        "highlights": [
            "Best model: XGBoost (oversampled) — Test Recall 87.3%, F1 81.9%, Accuracy 74.2%",
            "Outperformed AdaBoost, Random Forest, and two Gradient Boosting variants",
            "Top features: job experience, education level, continent, and prevailing wage type",
            "Handled class imbalance with SMOTE oversampling and undersampling strategies",
        ],
        "stack": ["Python", "XGBoost", "Scikit-learn", "SMOTE", "Pandas", "Seaborn"],
    },
    {
        "icon": "🍱", "featured": False,
        "category": "Python EDA · Data Analysis · Great Learning",
        "title": "FoodHub Order Analysis & Business Insights",
        "desc": (
            "Exploratory data analysis for a NYC food aggregator app to understand demand patterns, "
            "delivery performance, and customer satisfaction across restaurants and cuisine types."
        ),
        "highlights": [
            "10.54% of orders exceeded 60 min total time; 12.91% took exactly 60 min",
            "Weekday mean delivery time: 28.34 min vs weekend: 22.47 min (5.87 min gap)",
            "Identified underperforming restaurants by rating and cost-per-order analysis",
            "Recommendations: promote top-rated cuisines, flag low-rated partners, loyalty discounts",
        ],
        "stack": ["Python", "Pandas", "NumPy", "Matplotlib", "Seaborn", "EDA"],
    },
    {
        "icon": "💰", "featured": False,
        "category": "Quantitative Finance · UT Austin",
        "title": "Financial Analytics & Valuation Models",
        "desc": (
            "Interactive financial models for bond valuation, dividend analysis, and portfolio return "
            "calculation covering fixed income pricing and multi-asset return attribution."
        ),
        "highlights": [
            "Bond valuation with semi-annual coupons, YTM, and par value logic",
            "Dividend discount model with multi-stage growth assumptions",
            "Portfolio return calculator with asset allocation optimization",
        ],
        "stack": ["Python", "Finance Math", "Fixed Income", "NumPy", "Jupyter"],
    },
    {
        "icon": "📊", "featured": False,
        "category": "Executive Analytics · RBC Capital Markets",
        "title": "Capital Markets Executive Dashboard Suite",
        "desc": (
            "Executive dashboards for finance and operations leadership at RBC Capital Markets — "
            "real-time BI enabling data-driven decision-making across business units."
        ),
        "highlights": [
            "End-to-end ETL pipelines feeding Tableau dashboards",
            "NetSuite Analytics integration for financial operations reporting",
            "Reduced report turnaround time through automation",
        ],
        "stack": ["Tableau", "SQL", "NetSuite", "ETL", "Excel", "Power BI"],
    },
]

for i in range(0, len(projects), 2):
    row = projects[i:i + 2]
    cols = st.columns(len(row))
    for col, p in zip(cols, row):
        with col:
            st.html(project_card_html(p))

# ════════════════════════════════════════════════════════════════════════════
# SKILLS
# ════════════════════════════════════════════════════════════════════════════
st.html("""
<div style="padding:20px 0 8px">
    <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#4fffb0;
                letter-spacing:2px;text-transform:uppercase;margin-bottom:4px">CAPABILITIES</div>
    <div style="font-size:28px;font-weight:700;color:#f0f6fc;letter-spacing:-0.5px">
        Skills &amp; Technologies</div>
</div>
""")

skill_groups = [
    ("// Languages",        [("Python", 95), ("SQL", 90), ("R", 80)]),
    ("// ML / AI",          [("Scikit-learn / XGBoost", 90), ("LLMs / RAG / LangChain", 82), ("Deep Learning", 75)]),
    ("// Quant / Finance",  [("Portfolio Analytics", 90), ("Tax-Loss Harvesting", 88), ("Backtesting", 85)]),
    ("// Data & Viz",       [("Tableau / Power BI", 90), ("Pandas / NumPy / Plotly", 92), ("MySQL / MongoDB", 80)]),
    ("// Tools",            [("Streamlit", 88), ("GitHub / CI-CD", 82), ("Cloud (AWS/GCP)", 72)]),
    ("// Methods",          [("Statistical Modeling", 88), ("Time Series Analysis", 82), ("Optimization", 75)]),
]

for row_start in range(0, len(skill_groups), 3):
    row = skill_groups[row_start:row_start + 3]
    cols = st.columns(len(row))
    for col, (group_title, skills) in zip(cols, row):
        with col:
            st.html(skill_group_html(group_title, skills))

# ════════════════════════════════════════════════════════════════════════════
# EDUCATION & ACHIEVEMENTS
# ════════════════════════════════════════════════════════════════════════════
st.html("""
<div style="padding:20px 0 8px">
    <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#4fffb0;
                letter-spacing:2px;text-transform:uppercase;margin-bottom:4px">BACKGROUND</div>
    <div style="font-size:28px;font-weight:700;color:#f0f6fc;letter-spacing:-0.5px">
        Education &amp; Achievements</div>
</div>
""")

col_edu, col_ach = st.columns(2)

with col_edu:
    st.html("""
    <div style="background:#0d1117;border:1px solid #21262d;border-radius:10px;
                padding:22px;margin-bottom:12px">
        <div style="font-size:15px;font-weight:600;color:#f0f6fc;margin-bottom:4px">
            MS Business Analytics (Machine Learning)</div>
        <div style="font-size:13px;color:#4fffb0;margin-bottom:7px">
            University of Texas at Austin — McCombs School of Business</div>
        <div style="font-size:12px;color:#8b949e">Jul 2025 – Apr 2026 · Graduating April 2026</div>
        <div style="font-size:12px;color:#8b949e;margin-top:5px">
            Focus: ML applied to investment strategy, portfolio analytics, AI-driven decision-making</div>
    </div>
    <div style="background:#0d1117;border:1px solid #21262d;border-radius:10px;padding:22px">
        <div style="font-size:15px;font-weight:600;color:#f0f6fc;margin-bottom:4px">
            Data Analytics &amp; Visualization Boot Camp</div>
        <div style="font-size:13px;color:#4fffb0;margin-bottom:7px">University of Minnesota</div>
        <div style="font-size:12px;color:#8b949e">2020 · Foundations of analytics and visualization</div>
    </div>
    """)

with col_ach:
    achievements = [
        ("🏆", "100 Most Influential Women of Nepal", "Women with Vision", "2018"),
        ("🥇", "Open Data Hackathon Winner",           "Data-driven solution for public good", "2017"),
        ("🎤", "VP Membership — Toastmasters",         "Leadership & Public Speaking", "Ongoing"),
        ("📜", "Great Learning AI/ML Certifications",  "Generative AI, RAG, ML Deployment", "2025–2026"),
    ]
    html_blocks = "".join(f"""
        <div style="display:flex;gap:12px;padding:13px 0;border-bottom:1px solid #21262d">
            <div style="font-size:20px;flex-shrink:0">{icon}</div>
            <div>
                <div style="font-size:13px;color:#c9d1d9;font-weight:500">{title}</div>
                <div style="font-size:12px;color:#8b949e;margin-top:2px">{subtitle}</div>
                <div style="font-size:11px;color:#8b949e;font-family:'JetBrains Mono',monospace;
                            margin-top:2px">{year}</div>
            </div>
        </div>""" for icon, title, subtitle, year in achievements)
    st.html(f'<div style="background:#0d1117;border:1px solid #21262d;border-radius:10px;padding:20px">{html_blocks}</div>')

# ════════════════════════════════════════════════════════════════════════════
# CONTACT
# ════════════════════════════════════════════════════════════════════════════
st.html("""
<div style="padding:20px 0 8px">
    <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#4fffb0;
                letter-spacing:2px;text-transform:uppercase;margin-bottom:4px">CONNECT</div>
    <div style="font-size:28px;font-weight:700;color:#f0f6fc;letter-spacing:-0.5px">Let's Talk</div>
</div>
""")

col_links, col_open = st.columns(2)

with col_links:
    links_html = "".join(f"""
        <a href="{href}" target="_blank"
           style="display:flex;align-items:center;gap:12px;padding:13px 16px;
                  background:#0d1117;border:1px solid #21262d;border-radius:8px;
                  text-decoration:none;color:#c9d1d9;margin-bottom:10px;font-size:13px">
            <span style="font-size:17px">{icon}</span>
            <span>{label}</span>
        </a>""" for icon, label, href in [
        ("💼", "linkedin.com/in/nisha-sapkota-aidata", "https://www.linkedin.com/in/nisha-sapkota-aidata/"),
        ("📧", "nisha.sapkota.ai@gmail.com",              "mailto:nisha.sapkota.ai@gmail.com"),
        ("⚡", "github.com/nisha22sapkota",             "https://github.com/nisha22sapkota"),
    ])
    st.html(f"""
    <p style="color:#8b949e;font-size:13px;line-height:1.75;margin-bottom:18px">
        Actively seeking full-time roles in Quant Research, AI/ML, Investment Strategy,
        and Product Management at asset management and wealth tech companies.
        Open to NYC and remote-first positions.
    </p>
    {links_html}
    """)

with col_open:
    st.html("""
    <div style="background:#0d1117;border:1px solid #21262d;border-radius:10px;padding:26px">
        <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#4fffb0;
                    margin-bottom:16px;letter-spacing:1px">OPEN TO OPPORTUNITIES</div>
        <div style="font-size:13px;color:#8b949e;line-height:2.2">
            ✅ &nbsp;Quant Researcher / Analyst<br>
            ✅ &nbsp;AI/ML Engineer (Finance)<br>
            ✅ &nbsp;Data Scientist — WealthTech / FinTech<br>
            ✅ &nbsp;Investment Strategist<br>
            ✅ &nbsp;Product Manager — Asset Management<br>
            ✅ &nbsp;Investment Analytics<br>
            ✅ &nbsp;Portfolio Analytics &amp; Optimization
        </div>
        <div style="margin-top:18px;padding-top:18px;border-top:1px solid #21262d;
                    font-size:12px;color:#8b949e">
            📍 Austin, TX &nbsp;·&nbsp; Available from
            <strong style="color:#4fffb0">April 2026</strong>
        </div>
    </div>
    """)

# Footer
st.html("""
<div style="text-align:center;padding:28px 0;color:#484f58;font-size:12px;
            font-family:'JetBrains Mono',monospace;border-top:1px solid #21262d;margin-top:20px">
    Built with Python &amp; Streamlit &nbsp;·&nbsp; Nisha Sapkota &nbsp;·&nbsp; 2026
</div>
""")
