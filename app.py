import streamlit as st
import base64

def _img_b64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

PROFILE_IMG     = _img_b64("assets/profile.jpg")
MS150_IMG       = _img_b64("assets/ms150.jpg")
MS150_GROUP_IMG = _img_b64("assets/ms150_group.jpg")

st.set_page_config(
    page_title="Nisha Sapkota | Quant & AI Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stAppViewContainer"] { background: #0a0a0a !important; }
[data-testid="stMainBlockContainer"] {
    padding: 0 2rem !important;
    max-width: 1200px !important;
}
[data-testid="stVerticalBlock"] { gap: 0.4rem !important; }
section[data-testid="stSidebar"] { display: none; }

/* Custom scrollbar */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #0a0a0a; }
::-webkit-scrollbar-thumb { background: #30363d; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #60a5fa; }

/* Divider */
hr { border-color: #21262d !important; margin: 0.5rem 0 !important; }
</style>
""", unsafe_allow_html=True)

# ── Helpers ───────────────────────────────────────────────────────────────────
def stack_tags(tags):
    items = "".join(
        f'<span style="font-size:11px;background:rgba(96,165,250,0.08);'
        f'border:1px solid rgba(96,165,250,0.25);color:#93c5fd;padding:3px 8px;'
        f'border-radius:4px;font-family:JetBrains Mono,monospace;margin:2px 2px 0 0">{t}</span>'
        for t in tags
    )
    return f'<div style="display:flex;flex-wrap:wrap;gap:4px;margin-top:12px;padding-top:12px;border-top:1px solid #21262d">{items}</div>'

def exp_tags(tags):
    items = "".join(
        f'<span style="font-size:11px;background:rgba(33,38,45,0.8);border:1px solid #30363d;'
        f'color:#8b949e;padding:3px 8px;border-radius:4px;font-family:JetBrains Mono,monospace;'
        f'margin:2px 2px 0 0">{t}</span>'
        for t in tags
    )
    return f'<div style="display:flex;flex-wrap:wrap;gap:4px;margin-top:10px">{items}</div>'

def skill_group_html(group_title, skills):
    bars = "".join(f"""
        <div style="margin-bottom:14px">
            <div style="display:flex;justify-content:space-between;font-size:13px;color:#c9d1d9;margin-bottom:6px">
                <span>{name}</span>
                <span style="color:#60a5fa;font-family:'JetBrains Mono',monospace;font-size:11px">{pct}%</span>
            </div>
            <div style="height:4px;background:#21262d;border-radius:2px;overflow:hidden">
                <div style="height:100%;width:{pct}%;
                            background:linear-gradient(90deg,#60a5fa,#3b82f6);
                            border-radius:2px;
                            animation:fillBar 1.4s ease-out forwards"></div>
            </div>
        </div>""" for name, pct in skills)
    return f"""
    <style>
    @keyframes fillBar {{ from {{ width: 0% }} to {{ width: 100% }} }}
    </style>
    <div style="background:#111111;border:1px solid #21262d;border-radius:12px;padding:22px;
                transition:border-color 0.25s,box-shadow 0.25s;height:100%"
         onmouseover="this.style.borderColor='rgba(96,165,250,0.4)';this.style.boxShadow='0 8px 32px rgba(96,165,250,0.08)'"
         onmouseout="this.style.borderColor='#21262d';this.style.boxShadow='none'">
        <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#60a5fa;
                    text-transform:uppercase;letter-spacing:1px;margin-bottom:18px;font-weight:600">{group_title}</div>
        {bars}
    </div>"""

def project_card_html(p):
    featured_banner = (
        '<div style="position:absolute;top:14px;right:14px;font-family:JetBrains Mono,monospace;'
        'font-size:9px;color:#60a5fa;background:rgba(96,165,250,0.1);'
        'border:1px solid rgba(96,165,250,0.4);padding:3px 8px;border-radius:4px;'
        'letter-spacing:1px">FEATURED</div>'
    ) if p["featured"] else ""
    border = "rgba(96,165,250,0.35)" if p["featured"] else "#21262d"
    bg     = "linear-gradient(135deg,#0f172a 0%,#111827 100%)" if p["featured"] else "#111111"
    bullets = "".join(
        f'<li style="font-size:12px;color:#8b949e;padding:3px 0 3px 14px;position:relative;list-style:none">'
        f'<span style="position:absolute;left:0;color:#60a5fa;font-size:10px">▸</span>{h}</li>'
        for h in p["highlights"]
    )
    links_html = ""
    if p.get("github") or p.get("app_link"):
        btns = ""
        if p.get("github"):
            btns += (
                f'<a href="{p["github"]}" target="_blank" '
                f'style="font-size:11px;color:#93c5fd;background:rgba(96,165,250,0.08);'
                f'border:1px solid rgba(96,165,250,0.3);padding:6px 14px;border-radius:6px;'
                f'text-decoration:none;font-family:JetBrains Mono,monospace;'
                f'transition:all 0.2s" '
                f'onmouseover="this.style.background=\'rgba(96,165,250,0.18)\'" '
                f'onmouseout="this.style.background=\'rgba(96,165,250,0.08)\'">⬡ GitHub ↗</a>'
            )
        if p.get("app_link"):
            btns += (
                f'<a href="{p["app_link"]}" target="_blank" '
                f'style="font-size:11px;color:#000000;background:#60a5fa;'
                f'border:1px solid #60a5fa;padding:6px 14px;border-radius:6px;'
                f'text-decoration:none;font-family:JetBrains Mono,monospace;margin-left:8px;'
                f'font-weight:600;transition:all 0.2s" '
                f'onmouseover="this.style.background=\'#93c5fd\'" '
                f'onmouseout="this.style.background=\'#60a5fa\'">▶ Live App ↗</a>'
            )
        links_html = f'<div style="margin-top:16px;padding-top:14px;border-top:1px solid #21262d">{btns}</div>'
    return f"""
    <div style="background:{bg};border:1px solid {border};border-radius:12px;padding:26px;
                position:relative;height:100%;
                transition:transform 0.25s ease,box-shadow 0.25s ease,border-color 0.25s ease;
                cursor:default"
         onmouseover="this.style.transform='translateY(-5px)';this.style.boxShadow='0 20px 60px rgba(96,165,250,0.12)';this.style.borderColor='rgba(96,165,250,0.5)'"
         onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none';this.style.borderColor='{border}'">
        {featured_banner}
        <div style="font-size:28px;margin-bottom:14px">{p['icon']}</div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:10px;color:#60a5fa;
                    text-transform:uppercase;letter-spacing:1.5px;margin-bottom:8px">{p['category']}</div>
        <div style="font-size:16px;font-weight:600;color:#f0f6fc;margin-bottom:10px;line-height:1.3">{p['title']}</div>
        <div style="font-size:13px;color:#8b949e;line-height:1.7;margin-bottom:12px">{p['desc']}</div>
        <ul style="padding:0;margin:0">{bullets}</ul>
        {stack_tags(p['stack'])}
        {links_html}
    </div>"""

# ════════════════════════════════════════════════════════════════════════════
# STICKY NAV
# ════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
.topnav {
    position: sticky; top: 0; z-index: 999;
    background: rgba(10,10,10,0.96);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid #21262d;
    padding: 14px 2rem;
    display: flex; justify-content: space-between; align-items: center;
    margin: 0 -2rem;
}
.topnav-brand {
    font-family: 'JetBrains Mono', monospace;
    font-size: 16px; font-weight: 600; color: #ffffff;
    text-decoration: none;
}
.topnav-links { display: flex; gap: 28px; }
.topnav-links a {
    font-size: 13px; color: #8b949e; text-decoration: none;
    font-weight: 500; transition: color 0.2s ease;
    position: relative; padding-bottom: 2px;
}
.topnav-links a::after {
    content: ''; position: absolute; bottom: -2px; left: 0;
    width: 0; height: 2px; background: #60a5fa;
    transition: width 0.25s ease;
}
.topnav-links a:hover { color: #60a5fa; }
.topnav-links a:hover::after { width: 100%; }
</style>
<div class="topnav">
    <span class="topnav-brand">nisha.sapkota</span>
    <nav class="topnav-links">
        <a href="#about">About</a>
        <a href="#experience">Experience</a>
        <a href="#projects">Projects</a>
        <a href="#skills">Skills</a>
        <a href="#contact">Contact</a>
    </nav>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# HERO
# ════════════════════════════════════════════════════════════════════════════
st.html(f"""
<style>
@keyframes heroGlow {{
    0%   {{ background-position: 0% 50%; }}
    50%  {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}
@keyframes fadeUp {{
    from {{ opacity:0; transform:translateY(24px); }}
    to   {{ opacity:1; transform:translateY(0); }}
}}
.hero-badge {{
    display:inline-block;background:rgba(96,165,250,0.1);
    border:1px solid rgba(96,165,250,0.35);color:#93c5fd;
    font-family:'JetBrains Mono',monospace;font-size:11px;
    padding:5px 14px;border-radius:20px;margin-bottom:22px;letter-spacing:1px;
}}
.hero-btn-primary {{
    background:#60a5fa;color:#000000;font-weight:700;font-size:13px;
    padding:11px 26px;border-radius:8px;text-decoration:none;
    transition:all 0.2s ease;display:inline-block;
}}
.hero-btn-primary:hover {{ background:#93c5fd; transform:translateY(-2px); box-shadow:0 8px 24px rgba(96,165,250,0.3); }}
.hero-btn-secondary {{
    background:transparent;color:#c9d1d9;font-weight:500;font-size:13px;
    padding:11px 26px;border-radius:8px;text-decoration:none;
    border:1px solid #30363d;transition:all 0.2s ease;display:inline-block;
}}
.hero-btn-secondary:hover {{ border-color:#60a5fa; color:#60a5fa; transform:translateY(-2px); }}
.chip {{
    background:rgba(33,38,45,0.9);border:1px solid #30363d;color:#c9d1d9;
    font-size:12px;padding:6px 13px;border-radius:6px;
    font-family:'JetBrains Mono',monospace;
    transition:border-color 0.2s,color 0.2s;display:inline-block;
}}
.chip:hover {{ border-color:#60a5fa; color:#93c5fd; }}
</style>
<div id="home" style="
    background:linear-gradient(135deg,#0d1117 0%,#0a0a0a 50%,#0d1117 100%);
    border:1px solid #21262d;border-radius:16px;
    padding:64px 56px 56px;position:relative;overflow:hidden;margin-top:20px;
    animation:fadeUp 0.7s ease-out forwards;">

    <!-- Glow orbs -->
    <div style="position:absolute;top:-10%;right:5%;width:500px;height:500px;
                background:radial-gradient(circle,rgba(96,165,250,0.06) 0%,transparent 65%);
                pointer-events:none"></div>
    <div style="position:absolute;bottom:-20%;left:-5%;width:400px;height:400px;
                background:radial-gradient(circle,rgba(59,130,246,0.04) 0%,transparent 65%);
                pointer-events:none"></div>

    <div style="display:flex;align-items:center;justify-content:space-between;gap:48px;flex-wrap:wrap;position:relative">

        <div style="flex:1;min-width:300px">
            <div class="hero-badge">OPEN TO WORK · QUANT RESEARCH · AI/ML · PRODUCT MANAGEMENT · WEALTH TECH</div>

            <div style="font-size:54px;font-weight:700;color:#f0f6fc;line-height:1.05;
                        margin-bottom:12px;letter-spacing:-1.5px">Nisha Sapkota</div>

            <div style="font-size:20px;font-weight:400;color:#8b949e;margin-bottom:20px;line-height:1.4">
                Quant Researcher &amp; <span style="color:#60a5fa;font-weight:600">AI/ML Specialist</span>
                &nbsp;·&nbsp; <span style="color:#ffffff;font-weight:500">Product Manager</span> in FinTech/WealthTech
            </div>

            <div style="font-size:14px;color:#8b949e;line-height:1.85;max-width:540px;margin-bottom:32px">
                MS Business Analytics (Machine Learning) graduate from UT Austin McCombs.
                I build AI-driven investment tools — from tax-loss harvesting engines to
                RAG-based AI systems — at the intersection of machine learning and quantitative finance.
            </div>

            <div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:32px">
                <span class="chip">🎓 UT Austin McCombs MSBA</span>
                <span class="chip">📍 Austin, TX</span>
                <span class="chip">💼 ex-RBC Capital Markets</span>
                <span class="chip">🤖 AI · Quant · WealthTech</span>
                <span class="chip">📋 Product Strategy</span>
            </div>

            <div style="display:flex;gap:14px;flex-wrap:wrap">
                <a href="https://www.linkedin.com/in/nisha-sapkota-aidata/" target="_blank" class="hero-btn-primary">
                    LinkedIn Profile ↗
                </a>
                <a href="mailto:nisha.sapkota.ai@gmail.com" class="hero-btn-secondary">
                    Get In Touch →
                </a>
            </div>
        </div>

        <div style="flex-shrink:0">
            <div style="position:relative;width:230px;height:230px">
                <div style="position:absolute;inset:-4px;border-radius:50%;
                            background:linear-gradient(135deg,#60a5fa,#3b82f6,#1d4ed8);
                            animation:heroGlow 4s ease infinite;background-size:200% 200%"></div>
                <div style="position:absolute;inset:3px;border-radius:50%;
                            overflow:hidden;background:#0a0a0a">
                    <img src="data:image/jpeg;base64,{PROFILE_IMG}"
                         style="width:120%;height:120%;margin-left:-10%;margin-top:-5%;
                                object-fit:cover;object-position:center top"
                         alt="Nisha Sapkota">
                </div>
            </div>
        </div>

    </div>
</div>
""")

# ── Stats row ─────────────────────────────────────────────────────────────────
st.markdown("---")
for col, number, label, icon in zip(
    st.columns(4),
    ["5+", "10+", "2", "10+"],
    ["Years of Experience", "Projects Built", "Industry Awards", "Tools & Languages"],
    ["🏆", "🚀", "🥇", "🛠"],
):
    with col:
        st.html(f"""
        <div style="background:#111111;border:1px solid #21262d;border-radius:12px;
                    padding:26px;text-align:center;
                    transition:transform 0.25s,border-color 0.25s,box-shadow 0.25s"
             onmouseover="this.style.transform='translateY(-4px)';this.style.borderColor='rgba(96,165,250,0.4)';this.style.boxShadow='0 12px 32px rgba(96,165,250,0.1)'"
             onmouseout="this.style.transform='translateY(0)';this.style.borderColor='#21262d';this.style.boxShadow='none'">
            <div style="font-size:22px;margin-bottom:6px">{icon}</div>
            <div style="font-size:36px;font-weight:700;color:#60a5fa;
                        font-family:'JetBrains Mono',monospace">{number}</div>
            <div style="font-size:11px;color:#8b949e;margin-top:6px;
                        text-transform:uppercase;letter-spacing:0.5px">{label}</div>
        </div>
        """)

# ════════════════════════════════════════════════════════════════════════════
# ABOUT
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.html("""
<div style="padding:32px 0 12px">
    <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#60a5fa;
                letter-spacing:2px;text-transform:uppercase;margin-bottom:6px">WHO I AM</div>
    <div style="font-size:32px;font-weight:700;color:#f0f6fc;letter-spacing:-0.5px">About Me</div>
    <div style="width:48px;height:3px;background:linear-gradient(90deg,#60a5fa,#3b82f6);
                border-radius:2px;margin-top:10px"></div>
</div>
""")

col_about_text, col_about_img = st.columns([3, 2])

with col_about_text:
    st.html("""
    <div style="background:#111111;border:1px solid #21262d;border-radius:12px;padding:30px;height:100%;
                transition:border-color 0.25s"
         onmouseover="this.style.borderColor='rgba(96,165,250,0.3)'"
         onmouseout="this.style.borderColor='#21262d'">

        <p style="font-size:14px;color:#c9d1d9;line-height:1.9;margin-bottom:18px">
            At my core, I'm someone who builds things that help people — and
            <span style="color:#60a5fa;font-weight:500">wealth tech</span> is where that drive found
            its sharpest focus. Financial tools have historically been built <em>for</em> institutions,
            not individuals. I want to change that. Whether it's a tax-loss harvesting engine or an
            AI-driven portfolio optimizer, I'm motivated by the idea that better technology can give
            everyday investors access to strategies once reserved for the ultra-wealthy.
        </p>

        <p style="font-size:14px;color:#c9d1d9;line-height:1.9;margin-bottom:18px">
            That instinct to serve showed up early. In 2017, I won Nepal's
            <span style="color:#ffffff;font-weight:500">Open Data Hackathon</span> building a
            data-driven solution for public good. A year later, I was named one of
            <span style="color:#ffffff;font-weight:500">Nepal's 100 Most Influential Women</span> —
            recognition that pushed me to take my platform seriously and keep showing up for my community.
        </p>

        <p style="font-size:14px;color:#c9d1d9;line-height:1.9;margin-bottom:18px">
            Personal growth is something I chase deliberately. I don't wait to feel ready — I sign up
            first and figure it out. That mindset is what got me on a bike for the
            <span style="color:#ffffff;font-weight:500">MS 150</span>, a 150-mile charity ride raising
            funds for multiple sclerosis research. It's also what led me to Toastmasters (VP of
            Membership) and what drove me to earn my
            <span style="color:#60a5fa;font-weight:500">MS in Business Analytics</span> from
            UT Austin McCombs — specializing in machine learning at the intersection of AI and finance.
        </p>

        <p style="font-size:14px;color:#c9d1d9;line-height:1.9;margin:0">
            I believe the best work happens when technical rigor meets human empathy —
            and I try to bring both to everything I build.
        </p>

        <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:24px;padding-top:20px;border-top:1px solid #21262d">
            <span style="font-size:11px;background:rgba(96,165,250,0.08);border:1px solid rgba(96,165,250,0.25);
                         color:#93c5fd;padding:5px 12px;border-radius:6px;
                         font-family:'JetBrains Mono',monospace">🏆 100 Influential Women of Nepal</span>
            <span style="font-size:11px;background:rgba(96,165,250,0.08);border:1px solid rgba(96,165,250,0.25);
                         color:#93c5fd;padding:5px 12px;border-radius:6px;
                         font-family:'JetBrains Mono',monospace">🥇 Open Data Hackathon Winner</span>
            <span style="font-size:11px;background:rgba(96,165,250,0.08);border:1px solid rgba(96,165,250,0.25);
                         color:#93c5fd;padding:5px 12px;border-radius:6px;
                         font-family:'JetBrains Mono',monospace">🚴 Bike MS 150 Rider</span>
            <span style="font-size:11px;background:rgba(96,165,250,0.08);border:1px solid rgba(96,165,250,0.25);
                         color:#93c5fd;padding:5px 12px;border-radius:6px;
                         font-family:'JetBrains Mono',monospace">🎤 Toastmasters VP</span>
        </div>
    </div>
    """)

with col_about_img:
    st.html(f"""
    <div style="display:flex;flex-direction:column;gap:12px">
        <div style="border-radius:12px;overflow:hidden;border:1px solid #21262d;
                    position:relative;height:360px;transition:border-color 0.25s"
             onmouseover="this.style.borderColor='rgba(96,165,250,0.4)'"
             onmouseout="this.style.borderColor='#21262d'">
            <img src="data:image/jpeg;base64,{MS150_IMG}"
                 style="width:100%;height:100%;object-fit:cover;object-position:center 30%;display:block;
                        transition:transform 0.4s ease"
                 onmouseover="this.style.transform='scale(1.04)'"
                 onmouseout="this.style.transform='scale(1)'"
                 alt="Nisha at Bike MS 150 — 100 Miles milestone">
            <div style="position:absolute;bottom:0;left:0;right:0;
                        background:linear-gradient(transparent,rgba(0,0,0,0.9));
                        padding:18px 16px 14px">
                <div style="font-family:'JetBrains Mono',monospace;font-size:10px;color:#60a5fa;letter-spacing:1px">BIKE MS 150 · SOLO</div>
                <div style="font-size:12px;color:#c9d1d9;margin-top:2px">100 miles milestone</div>
            </div>
        </div>
        <div style="border-radius:12px;overflow:hidden;border:1px solid #21262d;
                    position:relative;height:360px;transition:border-color 0.25s"
             onmouseover="this.style.borderColor='rgba(96,165,250,0.4)'"
             onmouseout="this.style.borderColor='#21262d'">
            <img src="data:image/jpeg;base64,{MS150_GROUP_IMG}"
                 style="width:100%;height:100%;object-fit:cover;object-position:center 20%;display:block;
                        transition:transform 0.4s ease"
                 onmouseover="this.style.transform='scale(1.04)'"
                 onmouseout="this.style.transform='scale(1)'"
                 alt="MS 150 team ride">
            <div style="position:absolute;bottom:0;left:0;right:0;
                        background:linear-gradient(transparent,rgba(0,0,0,0.9));
                        padding:18px 16px 14px">
                <div style="font-family:'JetBrains Mono',monospace;font-size:10px;color:#60a5fa;letter-spacing:1px">BIKE MS 150 · TEAM</div>
                <div style="font-size:12px;color:#c9d1d9;margin-top:2px">Riding for MS research</div>
            </div>
        </div>
    </div>
    """)

# ════════════════════════════════════════════════════════════════════════════
# EXPERIENCE
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.html("""
<div style="padding:32px 0 12px">
    <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#60a5fa;
                letter-spacing:2px;text-transform:uppercase;margin-bottom:6px">CAREER</div>
    <div style="font-size:32px;font-weight:700;color:#f0f6fc;letter-spacing:-0.5px">Experience</div>
    <div style="width:48px;height:3px;background:linear-gradient(90deg,#60a5fa,#3b82f6);
                border-radius:2px;margin-top:10px"></div>
</div>
""")

experiences = [
    {
        "icon": "📈", "company": "Vise",
        "role": "Investment Specialist / Quant Researcher · Internship",
        "period": "Jan 2026 – Present",
        "desc": (
            "Identified after-tax return optimization as a critical gap in retail wealth management and "
            "led end-to-end product delivery: from problem definition and feature specification to "
            "backtesting infrastructure and stakeholder reporting. Built a simulation engine with "
            "threshold drift-band rebalancing, FIFO/LIFO/TAX_OPTIMAL lot tracking, ST/LT gain "
            "classification, and loss carry-forward. Delivered an institutional-grade Streamlit dashboard "
            "with strategy comparison analytics for Vise's investment team."
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
        "role": "Associate Product & Strategy Consultant · 2+ Years",
        "period": "Apr 2021 – May 2023",
        "desc": (
            "Led end-to-end product and solution delivery across enterprise engagements. "
            "Gathered requirements from C-suite and business stakeholders, translated them into "
            "technical specifications, and coordinated cross-functional teams through full delivery cycles. "
            "Delivered roadmaps, process redesigns, and data-driven recommendations that drove measurable "
            "operational improvements across financial services and tech verticals."
        ),
        "tags": ["Product Strategy", "Requirements Gathering", "Roadmapping", "Stakeholder Management",
                 "Agile / Scrum", "Business Analysis", "Process Design"],
    },
]

for exp in experiences:
    st.html(f"""
    <div style="display:flex;gap:20px;padding:22px;border:1px solid #21262d;border-radius:12px;
                margin-bottom:10px;background:#111111;
                transition:border-color 0.25s,box-shadow 0.25s,transform 0.25s"
         onmouseover="this.style.borderColor='rgba(96,165,250,0.35)';this.style.boxShadow='0 8px 32px rgba(96,165,250,0.08)';this.style.transform='translateX(4px)'"
         onmouseout="this.style.borderColor='#21262d';this.style.boxShadow='none';this.style.transform='translateX(0)'">
        <div style="width:44px;height:44px;border-radius:50%;background:rgba(96,165,250,0.1);
                    border:2px solid rgba(96,165,250,0.4);display:flex;align-items:center;
                    justify-content:center;font-size:18px;flex-shrink:0;margin-top:2px">{exp['icon']}</div>
        <div style="flex:1">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;
                        flex-wrap:wrap;gap:6px;margin-bottom:4px">
                <div style="font-size:17px;font-weight:700;color:#f0f6fc">{exp['company']}</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#60a5fa;
                            background:rgba(96,165,250,0.08);border:1px solid rgba(96,165,250,0.25);
                            padding:3px 10px;border-radius:6px">{exp['period']}</div>
            </div>
            <div style="font-size:13px;color:#93c5fd;font-weight:500;margin-bottom:8px">{exp['role']}</div>
            <div style="font-size:13px;color:#8b949e;line-height:1.7">{exp['desc']}</div>
            {exp_tags(exp['tags'])}
        </div>
    </div>
    """)

# ════════════════════════════════════════════════════════════════════════════
# PROJECTS
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.html("""
<div style="padding:32px 0 12px">
    <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#60a5fa;
                letter-spacing:2px;text-transform:uppercase;margin-bottom:6px">WORK</div>
    <div style="font-size:32px;font-weight:700;color:#f0f6fc;letter-spacing:-0.5px">Projects</div>
    <div style="width:48px;height:3px;background:linear-gradient(90deg,#60a5fa,#3b82f6);
                border-radius:2px;margin-top:10px"></div>
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
            "Product spec → backtesting engine → stakeholder dashboard delivered in 12-week capstone cycle",
            "ST/LT gain classification with loss carry-forward and $3k ordinary income offset",
            "Lot selection: FIFO, LIFO, TAX_OPTIMAL — daily through threshold drift-band rebalancing",
            "Strategy comparison: CAGR, Sharpe ratio, max drawdown, tracking error, information ratio",
            "Out-of-sample walk-forward validation; CI via GitHub Actions; Excel export; DRIP reinvestment",
        ],
        "stack": ["Python", "Streamlit", "Pandas", "NumPy", "Plotly", "SciPy", "GitHub Actions"],
        "github": "https://github.com/jringler30/portfolio-tlh-optimizer",
        "app_link": "https://portfolio-tlh-optimizer-msba-capstone.streamlit.app/",
    },
    {
        "icon": "🏦", "featured": True,
        "category": "ML · Banking · End-to-End App",
        "title": "Personal Loan Acceptance Predictor",
        "desc": (
            "End-to-end ML system for a banking institution to predict which customers are most "
            "likely to accept a personal loan offer — reducing unnecessary marketing spend and "
            "improving campaign ROI through data-driven targeting."
        ),
        "highlights": [
            "Built & compared Decision Tree, Random Forest, AdaBoost, XGBoost — tuned RF won on recall",
            "Engineered features: Income per Family, CC-to-Income Ratio, Engagement Score",
            "4-tier marketing prioritization: Very High / High / Medium / Low priority segments",
            "Batch scoring tab — upload a customer CSV, get scores + charts + downloadable results",
            "Interactive Streamlit app with real-time prediction, feature importance chart & gauge",
        ],
        "stack": ["Python", "Scikit-learn", "Random Forest", "XGBoost", "Streamlit", "Pandas"],
        "github": "https://github.com/nisha22sapkota/loan-acceptance-predictor",
        "app_link": "https://loan-acceptance-predictor-app.streamlit.app/",
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
            "Built for the agricultural industry to automate crop/weed identification."
        ),
        "highlights": [
            "12-class image classification across species including Black-grass, Maize, Sugar beet",
            "Custom CNN architecture built with TensorFlow / Keras on numpy image arrays",
            "Image preprocessing pipeline: normalization, reshaping, augmentation",
            "Dataset from Aarhus University (University of Southern Denmark collaboration)",
        ],
        "stack": ["Python", "TensorFlow", "Keras", "CNN", "NumPy", "Computer Vision"],
    },
    {
        "icon": "💹", "featured": False,
        "category": "Neural Networks · Classification · Great Learning",
        "title": "Bank Customer Churn Prediction (Neural Network)",
        "desc": (
            "Neural network classifier to predict whether a bank customer will churn within 6 months, "
            "helping management prioritize retention strategies."
        ),
        "highlights": [
            "Final model: Adam optimizer + dropout (0.2) — AUC 0.83 on test set",
            "Recall of 70.9% — correctly identified ~71% of customers who actually churned",
            "Features: credit score, age, tenure, balance, number of products, geography",
            "Actionable insights: dormant member re-engagement, product diversification",
        ],
        "stack": ["Python", "Keras", "TensorFlow", "Neural Networks", "Scikit-learn", "Pandas"],
    },
    {
        "icon": "🛂", "featured": False,
        "category": "ML Classification · Ensemble Methods · Great Learning",
        "title": "EasyVisa — US Visa Approval Prediction",
        "desc": (
            "ML solution for the US Office of Foreign Labor Certification to predict visa "
            "certification outcomes and identify key approval drivers. Benchmarked 5 models."
        ),
        "highlights": [
            "Best model: XGBoost (oversampled) — Test Recall 87.3%, F1 81.9%, Accuracy 74.2%",
            "Outperformed AdaBoost, Random Forest, and two Gradient Boosting variants",
            "Top features: job experience, education level, continent, prevailing wage type",
            "Handled class imbalance with SMOTE oversampling and undersampling strategies",
        ],
        "stack": ["Python", "XGBoost", "Scikit-learn", "SMOTE", "Pandas", "Seaborn"],
    },
    {
        "icon": "🍱", "featured": False,
        "category": "Python EDA · Data Analysis · Great Learning",
        "title": "FoodHub Order Analysis & Business Insights",
        "desc": (
            "Exploratory data analysis for a NYC food aggregator to understand demand patterns, "
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
            "Translated C-suite requirements into self-serve BI: eliminated recurring ad-hoc reports",
            "ETL pipelines feeding Tableau and Power BI dashboards used by 50+ stakeholders",
            "NetSuite Analytics integration for financial operations reporting",
            "Reduced report turnaround time from days to real-time through automation",
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
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.html("""
<div style="padding:32px 0 12px">
    <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#60a5fa;
                letter-spacing:2px;text-transform:uppercase;margin-bottom:6px">CAPABILITIES</div>
    <div style="font-size:32px;font-weight:700;color:#f0f6fc;letter-spacing:-0.5px">Skills &amp; Technologies</div>
    <div style="width:48px;height:3px;background:linear-gradient(90deg,#60a5fa,#3b82f6);
                border-radius:2px;margin-top:10px"></div>
</div>
""")

skill_groups = [
    ("// Languages",         [("Python", 95), ("SQL", 90), ("R", 80)]),
    ("// ML / AI",           [("Scikit-learn / XGBoost", 90), ("LLMs / RAG / LangChain", 82), ("Deep Learning", 75)]),
    ("// Quant / Finance",   [("Portfolio Analytics", 90), ("Tax-Loss Harvesting", 88), ("Backtesting", 85)]),
    ("// Data & Viz",        [("Tableau / Power BI", 90), ("Pandas / NumPy / Plotly", 92), ("MySQL / MongoDB", 80)]),
    ("// Tools",             [("Streamlit", 88), ("GitHub / CI-CD", 82), ("Cloud (AWS/GCP)", 72)]),
    ("// Product & Methods", [("Product Strategy / Roadmapping", 85), ("Statistical Modeling", 88), ("Agile / Scrum", 82)]),
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
<div style="padding:32px 0 12px">
    <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#60a5fa;
                letter-spacing:2px;text-transform:uppercase;margin-bottom:6px">BACKGROUND</div>
    <div style="font-size:32px;font-weight:700;color:#f0f6fc;letter-spacing:-0.5px">Education &amp; Achievements</div>
    <div style="width:48px;height:3px;background:linear-gradient(90deg,#60a5fa,#3b82f6);
                border-radius:2px;margin-top:10px"></div>
</div>
""")

col_edu, col_ach = st.columns(2)

with col_edu:
    st.html("""
    <div style="background:#111111;border:1px solid #21262d;border-radius:12px;padding:24px;
                margin-bottom:12px;transition:border-color 0.25s,box-shadow 0.25s"
         onmouseover="this.style.borderColor='rgba(96,165,250,0.4)';this.style.boxShadow='0 8px 24px rgba(96,165,250,0.08)'"
         onmouseout="this.style.borderColor='#21262d';this.style.boxShadow='none'">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
            <span style="font-size:22px">🎓</span>
            <div style="font-size:15px;font-weight:700;color:#f0f6fc">MS Business Analytics (Machine Learning)</div>
        </div>
        <div style="font-size:13px;color:#60a5fa;margin-bottom:6px;font-weight:500">
            University of Texas at Austin — McCombs School of Business</div>
        <div style="font-size:12px;color:#8b949e;margin-bottom:4px">Jul 2025 – Jun 2026 · Graduated</div>
        <div style="font-size:12px;color:#8b949e">
            Specialization: Machine Learning · AI-driven investment tools, portfolio analytics, quantitative finance</div>
    </div>
    <div style="background:#111111;border:1px solid #21262d;border-radius:12px;padding:24px;
                transition:border-color 0.25s,box-shadow 0.25s"
         onmouseover="this.style.borderColor='rgba(96,165,250,0.4)';this.style.boxShadow='0 8px 24px rgba(96,165,250,0.08)'"
         onmouseout="this.style.borderColor='#21262d';this.style.boxShadow='none'">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
            <span style="font-size:22px">📊</span>
            <div style="font-size:15px;font-weight:700;color:#f0f6fc">Data Analytics &amp; Visualization Boot Camp</div>
        </div>
        <div style="font-size:13px;color:#60a5fa;margin-bottom:6px;font-weight:500">University of Minnesota</div>
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
        <div style="display:flex;gap:14px;padding:15px 0;border-bottom:1px solid #21262d;
                    transition:background 0.2s;border-radius:6px;cursor:default"
             onmouseover="this.style.background='rgba(96,165,250,0.04)';this.style.paddingLeft='8px'"
             onmouseout="this.style.background='transparent';this.style.paddingLeft='0'">
            <div style="font-size:22px;flex-shrink:0;margin-top:1px">{icon}</div>
            <div>
                <div style="font-size:13px;color:#c9d1d9;font-weight:600">{title}</div>
                <div style="font-size:12px;color:#8b949e;margin-top:3px">{subtitle}</div>
                <div style="font-size:11px;color:#60a5fa;font-family:'JetBrains Mono',monospace;margin-top:3px">{year}</div>
            </div>
        </div>""" for icon, title, subtitle, year in achievements)
    st.html(f'<div style="background:#111111;border:1px solid #21262d;border-radius:12px;padding:22px;height:100%">{html_blocks}</div>')

# ════════════════════════════════════════════════════════════════════════════
# CONTACT
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.html("""
<div style="padding:32px 0 12px">
    <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#60a5fa;
                letter-spacing:2px;text-transform:uppercase;margin-bottom:6px">CONNECT</div>
    <div style="font-size:32px;font-weight:700;color:#f0f6fc;letter-spacing:-0.5px">Let's Talk</div>
    <div style="width:48px;height:3px;background:linear-gradient(90deg,#60a5fa,#3b82f6);
                border-radius:2px;margin-top:10px"></div>
</div>
""")

col_links, col_open = st.columns(2)

with col_links:
    links_html = "".join(f"""
        <a href="{href}" target="_blank"
           style="display:flex;align-items:center;gap:14px;padding:15px 18px;
                  background:#111111;border:1px solid #21262d;border-radius:10px;
                  text-decoration:none;color:#c9d1d9;margin-bottom:10px;font-size:13px;
                  transition:all 0.2s ease"
           onmouseover="this.style.borderColor='rgba(96,165,250,0.4)';this.style.color='#93c5fd';this.style.transform='translateX(4px)';this.style.boxShadow='0 4px 16px rgba(96,165,250,0.1)'"
           onmouseout="this.style.borderColor='#21262d';this.style.color='#c9d1d9';this.style.transform='translateX(0)';this.style.boxShadow='none'">
            <span style="font-size:18px">{icon}</span>
            <span>{label}</span>
            <span style="margin-left:auto;color:#60a5fa;font-size:12px">↗</span>
        </a>""" for icon, label, href in [
        ("💼", "linkedin.com/in/nisha-sapkota-aidata", "https://www.linkedin.com/in/nisha-sapkota-aidata/"),
        ("📧", "nisha.sapkota.ai@gmail.com",           "mailto:nisha.sapkota.ai@gmail.com"),
        ("⚡", "github.com/nisha22sapkota",            "https://github.com/nisha22sapkota"),
    ])
    st.html(f"""
    <p style="color:#8b949e;font-size:14px;line-height:1.8;margin-bottom:20px">
        Actively seeking full-time roles in Quant Research, AI/ML, Investment Strategy,
        and Product Management at asset management and wealth tech companies.
        Open to NYC and remote-first positions.
    </p>
    {links_html}
    """)

with col_open:
    st.html("""
    <div style="background:linear-gradient(135deg,#0f172a 0%,#111827 100%);
                border:1px solid rgba(96,165,250,0.25);border-radius:12px;padding:28px;
                transition:border-color 0.25s,box-shadow 0.25s"
         onmouseover="this.style.borderColor='rgba(96,165,250,0.5)';this.style.boxShadow='0 8px 32px rgba(96,165,250,0.1)'"
         onmouseout="this.style.borderColor='rgba(96,165,250,0.25)';this.style.boxShadow='none'">
        <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#60a5fa;
                    margin-bottom:18px;letter-spacing:1px">OPEN TO OPPORTUNITIES</div>
        <div style="font-size:13px;color:#8b949e;line-height:2.4">
            ✅ &nbsp;Quant Researcher / Analyst<br>
            ✅ &nbsp;<strong style="color:#ffffff">Product Manager — FinTech / WealthTech</strong><br>
            ✅ &nbsp;AI/ML Engineer (Finance)<br>
            ✅ &nbsp;Data Scientist — WealthTech / FinTech<br>
            ✅ &nbsp;Investment Strategist<br>
            ✅ &nbsp;Portfolio Analytics &amp; Optimization<br>
            ✅ &nbsp;Investment Analytics
        </div>
        <div style="margin-top:20px;padding-top:18px;border-top:1px solid #21262d;
                    font-size:12px;color:#8b949e;display:flex;align-items:center;gap:8px">
            <span>📍 Austin, TX</span>
            <span style="color:#30363d">·</span>
            <span>Available <strong style="color:#60a5fa">Immediately</strong></span>
        </div>
    </div>
    """)

# ── Footer ────────────────────────────────────────────────────────────────────
st.html("""
<div style="text-align:center;padding:36px 0 24px;border-top:1px solid #21262d;margin-top:24px">
    <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#484f58;margin-bottom:12px">
        Built with Python &amp; Streamlit &nbsp;·&nbsp; Nisha Sapkota &nbsp;·&nbsp; 2026
    </div>
    <a href="#home" style="font-size:11px;color:#60a5fa;text-decoration:none;
       font-family:'JetBrains Mono',monospace;
       transition:opacity 0.2s" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'">
        ↑ Back to top
    </a>
</div>
""")
