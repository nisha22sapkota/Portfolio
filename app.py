import streamlit as st
import base64

def _img_b64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

PROFILE_IMG     = _img_b64("assets/profile.jpg")
MS150_IMG       = _img_b64("assets/ms150.jpg")
MS150_GROUP_IMG = _img_b64("assets/ms150_group.jpg")

st.set_page_config(
    page_title="Nisha Sapkota | Data Scientist, Agentic AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Design System & Global CSS ────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
  --bg:        #03050a;
  --surface:   #080d17;
  --card:      #0c1220;
  --border:    rgba(255,255,255,0.07);
  --border-h:  rgba(139,92,246,0.5);
  --text:      #e2e8f0;
  --muted:     #64748b;
  --subtle:    #94a3b8;
  --grad-a:    #818cf8;
  --grad-b:    #a78bfa;
  --grad-c:    #38bdf8;
  --accent:    #818cf8;
}

*, *::before, *::after { box-sizing: border-box; }
html { scroll-behavior: smooth; }
html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }
#MainMenu, footer, header { visibility: hidden; }

[data-testid="stAppViewContainer"] {
  background: var(--bg) !important;
}
[data-testid="stMainBlockContainer"] {
  padding: 0 2.5rem !important;
  max-width: 1180px !important;
}
[data-testid="stVerticalBlock"] { gap: 0.35rem !important; }
section[data-testid="stSidebar"] { display: none; }

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent); }

hr { border-color: rgba(255,255,255,0.05) !important; margin: 0.25rem 0 !important; }

/* ── Sticky nav ── */
.topnav {
  position: sticky; top: 0; z-index: 1000;
  background: rgba(3,5,10,0.85);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-bottom: 1px solid rgba(255,255,255,0.06);
  padding: 15px 2.5rem;
  display: flex; justify-content: space-between; align-items: center;
  margin: 0 -2.5rem;
}
.topnav-brand {
  font-family: 'JetBrains Mono', monospace;
  font-size: 15px; font-weight: 600;
  background: linear-gradient(135deg, #818cf8, #38bdf8);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
  text-decoration: none;
}
.topnav-links { display: flex; gap: 32px; }
.topnav-links a {
  font-size: 13px; color: var(--muted); text-decoration: none;
  font-weight: 500; transition: color 0.2s ease;
  letter-spacing: 0.01em;
}
.topnav-links a:hover { color: var(--text); }

/* ── Gradient text utility ── */
.grad-text {
  background: linear-gradient(135deg, #818cf8 0%, #a78bfa 40%, #38bdf8 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* ── Section label ── */
.sec-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px; letter-spacing: 3px; text-transform: uppercase;
  background: linear-gradient(90deg, #818cf8, #38bdf8);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 8px; display: block;
}
.sec-title {
  font-size: 34px; font-weight: 800; color: var(--text);
  letter-spacing: -0.5px; margin-bottom: 14px; display: block;
}
.sec-bar {
  width: 40px; height: 3px;
  background: linear-gradient(90deg, #818cf8, #38bdf8);
  border-radius: 2px; margin-bottom: 32px;
}
</style>
""", unsafe_allow_html=True)

# ── Helpers ───────────────────────────────────────────────────────────────────
def stack_tags(tags):
    items = "".join(
        f'<span style="font-size:11px;'
        f'background:linear-gradient(135deg,rgba(129,140,248,0.1),rgba(56,189,248,0.1));'
        f'border:1px solid rgba(129,140,248,0.2);color:#a5b4fc;'
        f'padding:3px 9px;border-radius:20px;'
        f'font-family:JetBrains Mono,monospace;white-space:nowrap">{t}</span>'
        for t in tags
    )
    return f'<div style="display:flex;flex-wrap:wrap;gap:6px;margin-top:14px;padding-top:14px;border-top:1px solid rgba(255,255,255,0.06)">{items}</div>'

def exp_tags(tags):
    items = "".join(
        f'<span style="font-size:11px;background:rgba(255,255,255,0.04);'
        f'border:1px solid rgba(255,255,255,0.08);color:#64748b;'
        f'padding:3px 9px;border-radius:20px;font-family:JetBrains Mono,monospace">{t}</span>'
        for t in tags
    )
    return f'<div style="display:flex;flex-wrap:wrap;gap:6px;margin-top:12px">{items}</div>'

def skill_group_html(group_title, skills):
    bars = "".join(f"""
        <div style="margin-bottom:16px">
            <div style="display:flex;justify-content:space-between;font-size:13px;
                        color:#94a3b8;margin-bottom:7px">
                <span>{name}</span>
                <span style="font-family:'JetBrains Mono',monospace;font-size:11px;
                             background:linear-gradient(90deg,#818cf8,#38bdf8);
                             -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                             background-clip:text;">{pct}%</span>
            </div>
            <div style="height:3px;background:rgba(255,255,255,0.06);border-radius:2px;overflow:hidden">
                <div style="height:100%;width:{pct}%;
                            background:linear-gradient(90deg,#818cf8,#38bdf8);
                            border-radius:2px;animation:fillBar 1.6s ease-out"></div>
            </div>
        </div>""" for name, pct in skills)
    return f"""
    <style>@keyframes fillBar{{from{{width:0}}to{{width:100%}}}}</style>
    <div style="background:rgba(12,18,32,0.8);border:1px solid rgba(255,255,255,0.07);
                border-radius:16px;padding:24px;height:100%;
                transition:border-color 0.3s,transform 0.3s,box-shadow 0.3s;backdrop-filter:blur(10px)"
         onmouseover="this.style.borderColor='rgba(129,140,248,0.35)';this.style.transform='translateY(-3px)';this.style.boxShadow='0 16px 48px rgba(129,140,248,0.1)'"
         onmouseout="this.style.borderColor='rgba(255,255,255,0.07)';this.style.transform='translateY(0)';this.style.boxShadow='none'">
        <div style="font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:1.5px;
                    text-transform:uppercase;margin-bottom:20px;font-weight:600;
                    background:linear-gradient(90deg,#818cf8,#38bdf8);
                    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                    background-clip:text">{group_title}</div>
        {bars}
    </div>"""

def project_card_html(p):
    if p["featured"]:
        border_style = "border:1px solid rgba(129,140,248,0.25)"
        bg_style     = "background:linear-gradient(145deg,#0c1220 0%,#0f172a 60%,#0c1527 100%)"
        featured_badge = """
        <div style="position:absolute;top:16px;right:16px;
                    background:linear-gradient(135deg,rgba(129,140,248,0.15),rgba(56,189,248,0.1));
                    border:1px solid rgba(129,140,248,0.35);
                    color:#a5b4fc;font-family:JetBrains Mono,monospace;font-size:9px;
                    padding:4px 10px;border-radius:20px;letter-spacing:1.5px">FEATURED</div>"""
        hover_border = "rgba(129,140,248,0.5)"
    else:
        border_style = "border:1px solid rgba(255,255,255,0.06)"
        bg_style     = "background:rgba(12,18,32,0.6)"
        featured_badge = ""
        hover_border = "rgba(129,140,248,0.3)"

    bullets = "".join(
        f'<li style="font-size:12.5px;color:#64748b;padding:4px 0 4px 16px;'
        f'position:relative;list-style:none;line-height:1.6">'
        f'<span style="position:absolute;left:0;top:6px;width:6px;height:6px;border-radius:50%;'
        f'background:linear-gradient(135deg,#818cf8,#38bdf8);display:inline-block"></span>{h}</li>'
        for h in p["highlights"]
    )

    links_html = ""
    if p.get("github") or p.get("app_link") or p.get("write_up"):
        btns = ""
        if p.get("write_up"):
            btns += (
                f'<a href="{p["write_up"]}" target="_blank" '
                f'style="font-size:12px;color:#a5b4fc;'
                f'background:rgba(129,140,248,0.08);'
                f'border:1px solid rgba(129,140,248,0.2);'
                f'padding:7px 16px;border-radius:8px;text-decoration:none;'
                f'font-family:JetBrains Mono,monospace;font-weight:500;'
                f'transition:all 0.2s;display:inline-block;margin-right:10px" '
                f'onmouseover="this.style.background=\'rgba(129,140,248,0.18)\';this.style.borderColor=\'rgba(129,140,248,0.5)\'" '
                f'onmouseout="this.style.background=\'rgba(129,140,248,0.08)\';this.style.borderColor=\'rgba(129,140,248,0.2)\'">📄 Read Write-up ↗</a>'
            )
        if p.get("github"):
            btns += (
                f'<a href="{p["github"]}" target="_blank" '
                f'style="font-size:12px;color:#a5b4fc;'
                f'background:rgba(129,140,248,0.08);'
                f'border:1px solid rgba(129,140,248,0.2);'
                f'padding:7px 16px;border-radius:8px;text-decoration:none;'
                f'font-family:JetBrains Mono,monospace;font-weight:500;'
                f'transition:all 0.2s;display:inline-block" '
                f'onmouseover="this.style.background=\'rgba(129,140,248,0.18)\';this.style.borderColor=\'rgba(129,140,248,0.5)\'" '
                f'onmouseout="this.style.background=\'rgba(129,140,248,0.08)\';this.style.borderColor=\'rgba(129,140,248,0.2)\'">⬡ GitHub</a>'
            )
        if p.get("app_link"):
            btns += (
                f'<a href="{p["app_link"]}" target="_blank" '
                f'style="font-size:12px;color:#0c1220;font-weight:700;'
                f'background:linear-gradient(135deg,#818cf8,#38bdf8);'
                f'border:none;padding:7px 16px;border-radius:8px;'
                f'text-decoration:none;font-family:JetBrains Mono,monospace;'
                f'transition:all 0.2s;display:inline-block;margin-left:10px;'
                f'box-shadow:0 4px 16px rgba(129,140,248,0.25)" '
                f'onmouseover="this.style.boxShadow=\'0 6px 24px rgba(129,140,248,0.45)\';this.style.transform=\'translateY(-1px)\'" '
                f'onmouseout="this.style.boxShadow=\'0 4px 16px rgba(129,140,248,0.25)\';this.style.transform=\'translateY(0)\'">▶ Live App ↗</a>'
            )
        links_html = f'<div style="margin-top:18px;padding-top:16px;border-top:1px solid rgba(255,255,255,0.06);display:flex;align-items:center">{btns}</div>'

    return f"""
    <div style="{bg_style};{border_style};border-radius:18px;padding:28px;
                position:relative;height:100%;backdrop-filter:blur(10px);
                transition:transform 0.3s ease,box-shadow 0.3s ease,border-color 0.3s ease"
         onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 24px 64px rgba(129,140,248,0.15)';this.style.borderColor='{hover_border}'"
         onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none';this.style.borderColor='{'rgba(129,140,248,0.25)' if p['featured'] else 'rgba(255,255,255,0.06)'}'">
        {featured_badge}
        <div style="font-size:30px;margin-bottom:16px;line-height:1">{p['icon']}</div>
        <div style="font-size:10px;font-family:'JetBrains Mono',monospace;letter-spacing:2px;
                    text-transform:uppercase;margin-bottom:10px;font-weight:500;
                    background:linear-gradient(90deg,#818cf8,#38bdf8);
                    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                    background-clip:text">{p['category']}</div>
        <div style="font-size:17px;font-weight:700;color:#e2e8f0;margin-bottom:10px;
                    line-height:1.35;letter-spacing:-0.2px">{p['title']}</div>
        <div style="font-size:13px;color:#64748b;line-height:1.75;margin-bottom:14px">{p['desc']}</div>
        <ul style="padding:0;margin:0">{bullets}</ul>
        {stack_tags(p['stack'])}
        {links_html}
    </div>"""

# ════════════════════════════════════════════════════════════════════════════
# NAV
# ════════════════════════════════════════════════════════════════════════════
st.markdown("""
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
@keyframes pulse-ring {{
  0%   {{ transform: scale(1);   opacity: 0.6; }}
  50%  {{ transform: scale(1.06); opacity: 0.3; }}
  100% {{ transform: scale(1);   opacity: 0.6; }}
}}
@keyframes float {{
  0%, 100% {{ transform: translateY(0px); }}
  50%       {{ transform: translateY(-8px); }}
}}
@keyframes fadeUp {{
  from {{ opacity:0; transform:translateY(28px); }}
  to   {{ opacity:1; transform:translateY(0); }}
}}
.hero-wrap {{
  animation: fadeUp 0.8s ease-out forwards;
  position: relative; border-radius: 24px; overflow: hidden;
  border: 1px solid rgba(129,140,248,0.12);
  margin-top: 20px; padding: 72px 60px 64px;
  background: radial-gradient(ellipse 80% 60% at 70% -10%, rgba(129,140,248,0.07) 0%, transparent 60%),
              radial-gradient(ellipse 60% 50% at 10% 100%, rgba(56,189,248,0.05) 0%, transparent 55%),
              linear-gradient(160deg, #080d17 0%, #03050a 50%, #080d17 100%);
}}
.hero-wrap::before {{
  content:''; position:absolute; inset:0;
  background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23818cf8' fill-opacity='0.018'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  pointer-events: none; z-index: 0;
}}
.hero-content {{ position: relative; z-index: 1; }}
.status-pill {{
  display:inline-flex;align-items:center;gap:8px;
  background:rgba(129,140,248,0.08);
  border:1px solid rgba(129,140,248,0.2);
  padding:6px 16px; border-radius:30px; margin-bottom:28px;
}}
.status-dot {{
  width:7px;height:7px;border-radius:50%;
  background:linear-gradient(135deg,#818cf8,#38bdf8);
  animation:pulse-ring 2s ease-in-out infinite;
  box-shadow:0 0 0 0 rgba(129,140,248,0.4);
}}
.hero-name {{
  font-size:58px;font-weight:800;letter-spacing:-2px;line-height:1.0;
  margin-bottom:14px;
  background:linear-gradient(135deg,#f8fafc 0%,#e2e8f0 50%,#94a3b8 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}}
.hero-role {{
  font-size:20px;color:#64748b;margin-bottom:22px;line-height:1.5;font-weight:400;
}}
.hero-desc {{
  font-size:15px;color:#64748b;line-height:1.9;max-width:540px;margin-bottom:36px;font-weight:400;
}}
.chip-row {{ display:flex;flex-wrap:wrap;gap:8px;margin-bottom:36px; }}
.chip {{
  font-size:12px;color:#94a3b8;padding:6px 14px;border-radius:30px;
  background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);
  font-family:'JetBrains Mono',monospace;
  transition:all 0.2s;cursor:default;
}}
.chip:hover {{ border-color:rgba(129,140,248,0.4);color:#a5b4fc; }}
.btn-primary {{
  display:inline-block;
  background:linear-gradient(135deg,#818cf8,#38bdf8);
  color:#03050a;font-weight:700;font-size:13px;
  padding:12px 28px;border-radius:10px;text-decoration:none;
  transition:all 0.25s;box-shadow:0 4px 20px rgba(129,140,248,0.3);
  letter-spacing:0.01em;
}}
.btn-primary:hover {{
  box-shadow:0 8px 36px rgba(129,140,248,0.5);
  transform:translateY(-2px);
}}
.btn-secondary {{
  display:inline-block;
  background:rgba(255,255,255,0.04);
  color:#94a3b8;font-weight:500;font-size:13px;
  padding:12px 28px;border-radius:10px;text-decoration:none;
  border:1px solid rgba(255,255,255,0.1);
  transition:all 0.25s;letter-spacing:0.01em;
}}
.btn-secondary:hover {{
  border-color:rgba(129,140,248,0.4);
  color:#a5b4fc;transform:translateY(-2px);
}}
.photo-ring {{
  position:relative;width:240px;height:240px;flex-shrink:0;
  animation:float 5s ease-in-out infinite;
}}
.photo-ring::before {{
  content:'';position:absolute;inset:-3px;border-radius:50%;
  background:conic-gradient(from 0deg,#818cf8,#38bdf8,#a78bfa,#818cf8);
  animation:spin 6s linear infinite;
}}
@keyframes spin {{ to {{ transform:rotate(360deg); }} }}
.photo-ring::after {{
  content:'';position:absolute;inset:-1px;border-radius:50%;
  background:conic-gradient(from 0deg,rgba(129,140,248,0.6),rgba(56,189,248,0.6),rgba(167,139,250,0.6),rgba(129,140,248,0.6));
  filter:blur(8px);
  animation:spin 6s linear infinite;
  z-index:-1;
}}
.photo-inner {{
  position:absolute;inset:4px;border-radius:50%;overflow:hidden;background:#03050a;
}}
</style>

<div class="hero-wrap" id="home">
  <div class="hero-content" style="display:flex;align-items:center;justify-content:space-between;gap:48px;flex-wrap:wrap">

    <div style="flex:1;min-width:300px">
      <div class="status-pill">
        <div class="status-dot"></div>
        <span style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#a5b4fc;letter-spacing:0.5px">
          OPEN TO WORK &nbsp;·&nbsp; DATA SCIENCE · AGENTIC AI · LLM SYSTEMS
        </span>
      </div>

      <div class="hero-name">Nisha Sapkota</div>

      <div class="hero-role">
        <span style="background:linear-gradient(90deg,#818cf8,#38bdf8);-webkit-background-clip:text;
                     -webkit-text-fill-color:transparent;background-clip:text;font-weight:600">
          Data Scientist
        </span>
        &nbsp;·&nbsp; Agentic AI Systems &amp; LLM Evaluation
      </div>

      <div class="hero-desc">
        MS Business Analytics (Generative AI &amp; Financial Analytics) from UT Austin McCombs.
        I build agentic AI systems and evaluate frontier models — from a benchmark task in
        Terminal-Bench 3 that catches Claude and GPT in genuine reasoning failures, to a
        tax-loss harvesting engine built end-to-end with Claude Code and Codex — at the
        intersection of AI engineering and quantitative finance.
      </div>

      <div class="chip-row">
        <span class="chip">🤖 Agentic AI &amp; LLM Evaluation</span>
        <span class="chip">⚙️ Claude Code · Codex</span>
        <span class="chip">🎓 UT Austin McCombs MSBA</span>
        <span class="chip">💼 ex-RBC Capital Markets</span>
        <span class="chip">📍 Austin, TX</span>
      </div>

      <div style="display:flex;gap:14px;flex-wrap:wrap">
        <a href="https://www.linkedin.com/in/nisha-sapkota-aidata/" target="_blank" class="btn-primary">
          LinkedIn Profile ↗
        </a>
        <a href="mailto:nisha.sapkota.ai@gmail.com" class="btn-secondary">
          Get In Touch →
        </a>
      </div>
    </div>

    <div class="photo-ring">
      <div class="photo-inner">
        <img src="data:image/jpeg;base64,{PROFILE_IMG}"
             style="width:120%;height:120%;margin-left:-10%;margin-top:-5%;
                    object-fit:cover;object-position:center top"
             alt="Nisha Sapkota">
      </div>
    </div>

  </div>
</div>
""")

# ── Stats ─────────────────────────────────────────────────────────────────────
st.markdown("---")
for col, number, label, icon in zip(
    st.columns(4),
    ["4+", "10+", "2", "10+"],
    ["Years of Experience", "Projects Built", "Industry Awards", "Tools & Languages"],
    ["⚡", "🚀", "🏆", "🛠"],
):
    with col:
        st.html(f"""
        <div style="background:rgba(12,18,32,0.6);border:1px solid rgba(255,255,255,0.07);
                    border-radius:16px;padding:28px;text-align:center;
                    transition:all 0.3s ease;backdrop-filter:blur(8px)"
             onmouseover="this.style.borderColor='rgba(129,140,248,0.4)';this.style.transform='translateY(-5px)';this.style.boxShadow='0 20px 48px rgba(129,140,248,0.12)'"
             onmouseout="this.style.borderColor='rgba(255,255,255,0.07)';this.style.transform='translateY(0)';this.style.boxShadow='none'">
            <div style="font-size:24px;margin-bottom:8px">{icon}</div>
            <div style="font-size:38px;font-weight:800;letter-spacing:-1px;
                        background:linear-gradient(135deg,#818cf8,#38bdf8);
                        -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                        background-clip:text;font-family:'JetBrains Mono',monospace">{number}</div>
            <div style="font-size:11px;color:#64748b;margin-top:6px;
                        text-transform:uppercase;letter-spacing:1px;font-weight:500">{label}</div>
        </div>
        """)

# ════════════════════════════════════════════════════════════════════════════
# ABOUT
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.html("""
<div style="padding:40px 0 8px">
  <span class="sec-label">WHO I AM</span>
  <span class="sec-title">About Me</span>
  <div class="sec-bar"></div>
</div>
""")

col_about_text, col_about_img = st.columns([3, 2])

with col_about_text:
    st.html("""
    <div style="background:rgba(12,18,32,0.6);border:1px solid rgba(255,255,255,0.07);
                border-radius:20px;padding:32px;height:100%;backdrop-filter:blur(10px);
                transition:border-color 0.3s"
         onmouseover="this.style.borderColor='rgba(129,140,248,0.2)'"
         onmouseout="this.style.borderColor='rgba(255,255,255,0.07)'">

        <p style="font-size:14.5px;color:#94a3b8;line-height:1.95;margin-bottom:20px">
            At my core, I'm someone who builds things that help people — powerful tools have
            historically been built <em>for</em> institutions and experts, not everyday people, and
            I want to change that. It's shown up as a
            <span style="color:#a5b4fc;font-weight:500">tax-loss harvesting engine</span> giving
            everyday investors access to strategies once reserved for the ultra-wealthy, and it's
            the same instinct behind how I build and evaluate AI systems today.
        </p>

        <p style="font-size:14.5px;color:#94a3b8;line-height:1.95;margin-bottom:20px">
            That instinct to serve showed up early. In 2017, I was 1st Runner-Up at Nepal's
            <span style="color:#e2e8f0;font-weight:500">Open Data Hackathon</span> building a
            data-driven solution for public good. A year later, I was named one of
            <span style="color:#e2e8f0;font-weight:500">Nepal's 100 Most Influential Women</span> —
            recognition that pushed me to take my platform seriously and keep showing up for my community.
        </p>

        <p style="font-size:14.5px;color:#94a3b8;line-height:1.95;margin-bottom:20px">
            Personal growth is something I chase deliberately. I don't wait to feel ready — I sign up
            first and figure it out. That mindset is what got me on a bike for the
            <span style="color:#e2e8f0;font-weight:500">MS 150</span>, a 150-mile charity ride raising
            funds for multiple sclerosis research. It's also what drove me to earn my
            <span style="background:linear-gradient(90deg,#818cf8,#38bdf8);-webkit-background-clip:text;
                         -webkit-text-fill-color:transparent;background-clip:text;font-weight:600">
              MS in Business Analytics</span>
            from UT Austin McCombs — specializing in machine learning at the intersection of AI and finance.
        </p>

        <p style="font-size:14.5px;color:#94a3b8;line-height:1.95;margin-bottom:20px">
            Lately that means building with AI agents rather than just for them — I ship
            production systems end-to-end using <span style="color:#a5b4fc;font-weight:500">Claude Code
            and Codex</span>, and I've gone deep enough on evaluating frontier models that I designed
            an original benchmark task for <span style="color:#e2e8f0;font-weight:500">Terminal-Bench 3</span>,
            built specifically to catch agents like Claude and GPT in genuine reasoning failures.
        </p>

        <p style="font-size:14.5px;color:#94a3b8;line-height:1.95;margin:0">
            I believe the best work happens when technical rigor meets human empathy —
            and I try to bring both to everything I build.
        </p>

        <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:26px;padding-top:22px;
                    border-top:1px solid rgba(255,255,255,0.06)">
            <span style="font-size:12px;background:rgba(129,140,248,0.08);border:1px solid rgba(129,140,248,0.2);
                         color:#a5b4fc;padding:5px 13px;border-radius:20px;
                         font-family:'JetBrains Mono',monospace">🏆 100 Influential Women of Nepal</span>
            <span style="font-size:12px;background:rgba(129,140,248,0.08);border:1px solid rgba(129,140,248,0.2);
                         color:#a5b4fc;padding:5px 13px;border-radius:20px;
                         font-family:'JetBrains Mono',monospace">🥈 Open Data Hackathon — 1st Runner-Up</span>
            <span style="font-size:12px;background:rgba(129,140,248,0.08);border:1px solid rgba(129,140,248,0.2);
                         color:#a5b4fc;padding:5px 13px;border-radius:20px;
                         font-family:'JetBrains Mono',monospace">🚴 Bike MS 150 Rider</span>
            <span style="font-size:12px;background:rgba(129,140,248,0.08);border:1px solid rgba(129,140,248,0.2);
                         color:#a5b4fc;padding:5px 13px;border-radius:20px;
                         font-family:'JetBrains Mono',monospace">🎤 Toastmasters VP</span>
        </div>
    </div>
    """)

with col_about_img:
    st.html(f"""
    <div style="display:flex;flex-direction:column;gap:14px">
        <div style="border-radius:18px;overflow:hidden;border:1px solid rgba(255,255,255,0.07);
                    position:relative;height:340px;transition:border-color 0.3s,box-shadow 0.3s"
             onmouseover="this.style.borderColor='rgba(129,140,248,0.35)';this.style.boxShadow='0 16px 48px rgba(129,140,248,0.12)'"
             onmouseout="this.style.borderColor='rgba(255,255,255,0.07)';this.style.boxShadow='none'">
            <img src="data:image/jpeg;base64,{MS150_IMG}"
                 style="width:100%;height:100%;object-fit:cover;object-position:center 30%;display:block;
                        transition:transform 0.5s ease"
                 onmouseover="this.style.transform='scale(1.05)'"
                 onmouseout="this.style.transform='scale(1)'"
                 alt="Nisha at Bike MS 150">
            <div style="position:absolute;bottom:0;left:0;right:0;
                        background:linear-gradient(transparent,rgba(3,5,10,0.95));
                        padding:20px 18px 16px">
                <div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1.5px;
                            background:linear-gradient(90deg,#818cf8,#38bdf8);
                            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                            background-clip:text">BIKE MS 150 · SOLO</div>
                <div style="font-size:12px;color:#94a3b8;margin-top:3px">100 miles milestone</div>
            </div>
        </div>
        <div style="border-radius:18px;overflow:hidden;border:1px solid rgba(255,255,255,0.07);
                    position:relative;height:340px;transition:border-color 0.3s,box-shadow 0.3s"
             onmouseover="this.style.borderColor='rgba(129,140,248,0.35)';this.style.boxShadow='0 16px 48px rgba(129,140,248,0.12)'"
             onmouseout="this.style.borderColor='rgba(255,255,255,0.07)';this.style.boxShadow='none'">
            <img src="data:image/jpeg;base64,{MS150_GROUP_IMG}"
                 style="width:100%;height:100%;object-fit:cover;object-position:center 20%;display:block;
                        transition:transform 0.5s ease"
                 onmouseover="this.style.transform='scale(1.05)'"
                 onmouseout="this.style.transform='scale(1)'"
                 alt="MS 150 team">
            <div style="position:absolute;bottom:0;left:0;right:0;
                        background:linear-gradient(transparent,rgba(3,5,10,0.95));
                        padding:20px 18px 16px">
                <div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1.5px;
                            background:linear-gradient(90deg,#818cf8,#38bdf8);
                            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                            background-clip:text">BIKE MS 150 · TEAM</div>
                <div style="font-size:12px;color:#94a3b8;margin-top:3px">Riding for MS research</div>
            </div>
        </div>
    </div>
    """)

# ════════════════════════════════════════════════════════════════════════════
# EXPERIENCE
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.html("""
<div style="padding:40px 0 8px">
  <span class="sec-label">CAREER</span>
  <span class="sec-title">Experience</span>
  <div class="sec-bar"></div>
</div>
""")

experiences = [
    {
        "icon": "📈", "company": "Vise",
        "role": "Investment Specialist / Quant Researcher · Internship",
        "period": "Jan 2026 – May 2026",
        "desc": (
            "Identified after-tax return optimization as a critical gap in retail wealth management and "
            "led end-to-end product delivery: from problem definition and feature specification to "
            "backtesting infrastructure and stakeholder reporting, as part of a 5-person McCombs capstone "
            "team. Designed and built the rebalancing and tax-loss harvesting engine using Claude Code "
            "and Codex — threshold drift-band rebalancing, FIFO/LIFO/TAX_OPTIMAL lot tracking, ST/LT gain "
            "classification, and loss carry-forward — cutting realized tax drag 96% ($790 → $27) and "
            "generating 88 bps of after-tax alpha over a daily-rebalancing benchmark. Delivered an "
            "institutional-grade Streamlit dashboard with strategy comparison analytics for Vise's "
            "investment team; scored 100/100 on the capstone."
        ),
        "tags": ["Python", "Claude Code", "Codex", "Streamlit", "Pandas", "Portfolio Optimization",
                 "Tax-Loss Harvesting", "Backtesting", "Plotly"],
    },
    {
        "icon": "🏦", "company": "RBC Capital Markets",
        "role": "Data Scientist · 2+ Years",
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
        "role": "Junior Data Scientist / Associate Consultant · 2+ Years",
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
    <div style="display:flex;gap:22px;padding:24px 26px;
                border:1px solid rgba(255,255,255,0.07);border-radius:18px;
                margin-bottom:12px;background:rgba(12,18,32,0.5);
                backdrop-filter:blur(8px);
                transition:all 0.3s ease"
         onmouseover="this.style.borderColor='rgba(129,140,248,0.3)';this.style.transform='translateX(6px)';this.style.boxShadow='0 8px 40px rgba(129,140,248,0.08)';this.style.background='rgba(15,23,42,0.8)'"
         onmouseout="this.style.borderColor='rgba(255,255,255,0.07)';this.style.transform='translateX(0)';this.style.boxShadow='none';this.style.background='rgba(12,18,32,0.5)'">
        <div style="width:46px;height:46px;border-radius:14px;
                    background:linear-gradient(135deg,rgba(129,140,248,0.15),rgba(56,189,248,0.1));
                    border:1px solid rgba(129,140,248,0.25);
                    display:flex;align-items:center;justify-content:center;
                    font-size:20px;flex-shrink:0;margin-top:2px">{exp['icon']}</div>
        <div style="flex:1">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;
                        flex-wrap:wrap;gap:8px;margin-bottom:4px">
                <div style="font-size:17px;font-weight:700;color:#e2e8f0;letter-spacing:-0.2px">{exp['company']}</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:11px;
                            background:linear-gradient(90deg,rgba(129,140,248,0.12),rgba(56,189,248,0.1));
                            border:1px solid rgba(129,140,248,0.2);color:#a5b4fc;
                            padding:4px 12px;border-radius:20px;white-space:nowrap">{exp['period']}</div>
            </div>
            <div style="font-size:13px;color:#818cf8;font-weight:500;margin-bottom:9px">{exp['role']}</div>
            <div style="font-size:13.5px;color:#64748b;line-height:1.75">{exp['desc']}</div>
            {exp_tags(exp['tags'])}
        </div>
    </div>
    """)

def project_compact_html(p):
    tags = "".join(
        f'<span style="font-size:10px;background:rgba(255,255,255,0.04);'
        f'border:1px solid rgba(255,255,255,0.08);color:#64748b;'
        f'padding:2px 8px;border-radius:20px;font-family:JetBrains Mono,monospace;'
        f'white-space:nowrap">{t}</span>'
        for t in p["stack"]
    )
    return f"""
    <div style="display:flex;align-items:flex-start;gap:16px;padding:16px 20px;
                border:1px solid rgba(255,255,255,0.06);border-radius:14px;
                margin-bottom:10px;background:rgba(12,18,32,0.4);
                transition:border-color 0.25s,background 0.25s"
         onmouseover="this.style.borderColor='rgba(129,140,248,0.25)';this.style.background='rgba(12,18,32,0.7)'"
         onmouseout="this.style.borderColor='rgba(255,255,255,0.06)';this.style.background='rgba(12,18,32,0.4)'">
        <div style="font-size:20px;flex-shrink:0;margin-top:2px">{p['icon']}</div>
        <div style="flex:1;min-width:0">
            <div style="display:flex;align-items:baseline;gap:10px;flex-wrap:wrap">
                <span style="font-size:14px;font-weight:700;color:#e2e8f0">{p['title']}</span>
                <span style="font-size:10px;font-family:'JetBrains Mono',monospace;color:#64748b;
                             letter-spacing:0.5px;text-transform:uppercase">{p['category']}</span>
            </div>
            <div style="font-size:12.5px;color:#64748b;line-height:1.6;margin:5px 0 10px">{p['desc']}</div>
            <div style="display:flex;flex-wrap:wrap;gap:6px">{tags}</div>
        </div>
    </div>"""

# ════════════════════════════════════════════════════════════════════════════
# PROJECTS
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.html("""
<div style="padding:40px 0 8px">
  <span class="sec-label">WORK</span>
  <span class="sec-title">Projects</span>
  <div class="sec-bar"></div>
</div>
""")

st.html("""
<div style="margin-bottom:20px">
  <span style="font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:1.5px;
              text-transform:uppercase;font-weight:600;
              background:linear-gradient(90deg,#818cf8,#38bdf8);
              -webkit-background-clip:text;-webkit-text-fill-color:transparent;
              background-clip:text">Agentic AI &amp; Applied Builds</span>
</div>
""")

projects_agentic = [
    {
        "icon": "🧭", "featured": True,
        "category": "Applied HCI · Chrome Extension · Agentic AI UX",
        "title": "NeuroOS — Cognitive-Load-Aware AI Interface",
        "desc": (
            "Independent project exploring whether interaction behavior alone — no biometrics, "
            "no wearables — can approximate cognitive friction during AI chat sessions, and whether "
            "adapting the interface in response actually helps. Grounded in \"When Help Hurts: "
            "Verification Load and Fatigue with AI Coding Assistants\" (Fan, Liu, Pan & Zhang, "
            "CHI '26, Honorable Mention) — the paper proposes adaptive, load-aware interfaces as "
            "future design guidance; NeuroOS is a working instance of that direction, applied to "
            "chat rather than IDE sessions."
        ),
        "highlights": [
            "Rules-based load score (0–2 / 3–5 / 6+) from interaction signals only: prompt-rewrite churn, tab-switch rate, copy/paste churn, session length — no prompt or response text ever read or stored",
            "Shadow-DOM-isolated widget so the extension's own UI can't collide with host-page CSS, with selector fallbacks so ChatGPT/Claude DOM drift degrades gracefully instead of breaking",
            "Competitive scan against shipped biometric-wellness tools and academic fatigue-detection research to scope an honest, non-overlapping wedge before writing code",
            "Shipped end-to-end as a working Manifest V3 extension — signal capture → load score → dismissible intervention → local feedback logging",
            "First real user reported the interventions (calm mode, simplify nudge) genuinely reduced session friction — early signal, not yet a validated correlation",
        ],
        "stack": ["JavaScript", "Chrome Extension (MV3)", "Shadow DOM", "Behavioral Signal Design", "HCI Research"],
        "github": "https://github.com/nisha22sapkota/neuroos-extension",
    },
    {
        "icon": "🧠", "featured": False,
        "category": "Agentic AI · Evaluation · Terminal-Bench 3",
        "title": "Terminal-Bench 3 — Agent Harness & Benchmark Design",
        "desc": (
            "Designed and validated an original evaluation task for an open-source benchmark "
            "used to stress-test frontier coding agents (Claude Opus, GPT, Gemini) on multi-step, "
            "tool-using workflows."
        ),
        "highlights": [
            "Engineered three independently-necessary bugs across separate modules; proved independence via ablation trials",
            "Defined success criteria against oracle-solution and no-op control baselines",
            "Diagnosed a false-negative failure mode from raw agent run-logs — an instruction ambiguity a model exploited — and closed it with a targeted spec fix",
            "Ran regression + adversarial trials across Claude Opus, GPT, and Gemini, converting the task into 6+ reproducible model failures",
        ],
        "stack": ["Python", "Docker", "CI/CD", "LLM Agents", "Eval Harness Design"],
        "github": "https://github.com/nisha22sapkota/terminal-bench-3/tree/task/sliding-window-aggregator",
    },
    {
        "icon": "🧮", "featured": False,
        "category": "AI Agent-Built · Quant Finance · Vise Capstone",
        "title": "Tax-Loss Harvesting & Portfolio Rebalancing Engine",
        "desc": (
            "Institutional-grade simulation engine for Vise, an AI-driven asset manager, built end-to-end "
            "using Claude Code and Codex. Models after-tax portfolio returns with full lot tracking, "
            "rebalancing strategies, and a Bloomberg-style Streamlit dashboard."
        ),
        "highlights": [
            "Product spec → backtesting engine → stakeholder dashboard in 12-week capstone cycle, agent-built with Claude Code / Codex",
            "ST/LT gain classification with loss carry-forward and $3k ordinary income offset",
            "Lot selection: FIFO, LIFO, TAX_OPTIMAL — daily through threshold drift-band rebalancing",
            "Strategy comparison: CAGR, Sharpe ratio, max drawdown, tracking error, information ratio",
            "Out-of-sample walk-forward validation; CI via GitHub Actions; Excel export; DRIP reinvestment",
        ],
        "stack": ["Python", "Claude Code", "Codex", "Streamlit", "Pandas", "NumPy", "Plotly", "GitHub Actions"],
        "github": "https://github.com/jringler30/portfolio-tlh-optimizer",
        "app_link": "https://portfolio-tlh-optimizer-msba-capstone.streamlit.app/",
    },
    {
        "icon": "🗣️", "featured": False,
        "category": "Generative AI · Embedding Retrieval",
        "title": "Natural Language → SQL: Schema Retrieval",
        "desc": (
            "Embedding-based system that identifies the relevant database tables for a "
            "plain-English question — the schema-retrieval step underneath NL-to-SQL — "
            "benchmarked on the Instacart Market Basket dataset (3M+ orders, 5 core tables). "
            "Co-authored with Franco Salinas and Aileen Li."
        ),
        "highlights": [
            "19-query benchmark across easy (1-table), medium (2–3 table), and hard (3–4 table) difficulty tiers",
            "all-MiniLM-L6-v2 sentence embeddings (384-dim), cosine similarity, top-k retrieval",
            "Diagnosed a recurring orders vs. order_products confusion, then fixed it via targeted contrastive-pair fine-tuning (v1 → v2)",
            "Overall Recall@3: 0.890 → 0.956; medium +11.1 pts, hard +11.7 pts after the targeted fix",
        ],
        "stack": ["Python", "Embeddings", "Similarity Search", "Fine-Tuning", "SQL"],
        "write_up": "https://francosalinas.netlify.app/posts/2026-03-14-natural-language-to-sql-schema-retrieval/",
    },
    {
        "icon": "🏥", "featured": False,
        "category": "Generative AI · RAG",
        "title": "Medical Diagnostic RAG AI System",
        "desc": (
            "RAG-based AI using the Merck Medical Manuals to assist clinicians with diagnostic questions, "
            "drug info, and treatment plans."
        ),
        "highlights": [
            "Ingested and indexed Merck Manuals into a vector knowledge base",
            "Retrieval pipeline for diagnostic, drug, and treatment queries",
            "Natural language clinical Q&A with precision/recall evaluation",
        ],
        "stack": ["Python", "LLM / RAG", "Vector DB", "LangChain", "NLP"],
    },
]

for p in projects_agentic:
    st.html(project_card_html(p))
    st.html('<div style="height:20px"></div>')

st.html("""
<div style="margin:36px 0 16px">
  <span style="font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:1.5px;
              text-transform:uppercase;font-weight:600;color:#64748b">
      Additional ML &amp; Analytics Coursework</span>
</div>
""")

projects_coursework = [
    {
        "icon": "🏦", "featured": False,
        "category": "ML · Banking · Great Learning",
        "title": "Personal Loan Acceptance Predictor",
        "desc": (
            "End-to-end ML system for a banking institution to predict which customers are most "
            "likely to accept a personal loan offer."
        ),
        "stack": ["Scikit-learn", "XGBoost", "Streamlit"],
        "github": "https://github.com/nisha22sapkota/loan-acceptance-predictor",
        "app_link": "https://loan-acceptance-predictor-app.streamlit.app/",
    },
    {
        "icon": "🌱", "featured": False,
        "category": "Computer Vision · Deep Learning · Great Learning",
        "title": "Plant Seedlings Classification (CNN)",
        "desc": (
            "CNN classifying plant seedlings into 12 species to automate crop/weed identification "
            "and improve agricultural yield decisions."
        ),
        "highlights": [
            "12-class image classification including Black-grass, Maize, Sugar beet",
            "Custom CNN with TensorFlow / Keras; numpy image array pipeline",
            "Normalization, reshaping, augmentation preprocessing",
            "Dataset from Aarhus University / University of Southern Denmark",
        ],
        "stack": ["Python", "TensorFlow", "Keras", "CNN", "NumPy", "Computer Vision"],
    },
    {
        "icon": "💹", "featured": False,
        "category": "Neural Networks · Classification · Great Learning",
        "title": "Bank Customer Churn Prediction",
        "desc": (
            "Neural network classifier predicting bank customer churn within 6 months, "
            "helping management prioritize retention strategies."
        ),
        "highlights": [
            "Adam optimizer + dropout (0.2) — AUC 0.83 on test set",
            "Recall 70.9% — correctly identified ~71% of churning customers",
            "Features: credit score, age, tenure, balance, products held, geography",
            "Insights: dormant re-engagement, product diversification, tenure-based retention",
        ],
        "stack": ["Python", "Keras", "TensorFlow", "Neural Networks", "Scikit-learn", "Pandas"],
    },
    {
        "icon": "🛂", "featured": False,
        "category": "ML Classification · Ensemble Methods · Great Learning",
        "title": "EasyVisa — US Visa Approval Prediction",
        "desc": (
            "ML solution for OFLC predicting visa certification outcomes "
            "and identifying key approval drivers across 5 benchmarked models."
        ),
        "highlights": [
            "XGBoost (oversampled): Test Recall 87.3%, F1 81.9%, Accuracy 74.2%",
            "Outperformed AdaBoost, Random Forest, two Gradient Boosting variants",
            "Top drivers: job experience, education level, continent, prevailing wage",
            "Class imbalance handled with SMOTE oversampling and undersampling",
        ],
        "stack": ["Python", "XGBoost", "Scikit-learn", "SMOTE", "Pandas", "Seaborn"],
    },
    {
        "icon": "🍱", "featured": False,
        "category": "Python EDA · Data Analysis · Great Learning",
        "title": "FoodHub Order Analysis & Business Insights",
        "desc": (
            "Exploratory data analysis for a NYC food aggregator to surface demand patterns, "
            "delivery bottlenecks, and customer satisfaction drivers."
        ),
        "highlights": [
            "10.54% of orders exceeded 60 min; weekday delivery 5.87 min slower than weekends",
            "Identified underperforming restaurants by rating and cost-per-order",
            "Recommendations: top-rated cuisine promotion, low-rated partner flagging",
        ],
        "stack": ["Python", "Pandas", "NumPy", "Matplotlib", "Seaborn", "EDA"],
    },
    {
        "icon": "💰", "featured": False,
        "category": "Quantitative Finance · UT Austin",
        "title": "Financial Analytics & Valuation Models",
        "desc": (
            "Interactive financial models for bond valuation, dividend analysis, and portfolio "
            "return calculation covering fixed income and multi-asset attribution."
        ),
        "highlights": [
            "Bond valuation with semi-annual coupons, YTM, par value logic",
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
            "Executive dashboards for RBC Capital Markets leadership — real-time BI that "
            "eliminated recurring ad-hoc requests across 50+ stakeholders."
        ),
        "highlights": [
            "Self-serve BI: eliminated recurring ad-hoc report requests from C-suite",
            "ETL pipelines feeding Tableau and Power BI dashboards for 50+ stakeholders",
            "NetSuite Analytics integration for financial operations reporting",
            "Reduced turnaround from days to real-time through pipeline automation",
        ],
        "stack": ["Tableau", "SQL", "NetSuite", "ETL", "Excel", "Power BI"],
    },
]

for p in projects_coursework:
    st.html(project_compact_html(p))

# ════════════════════════════════════════════════════════════════════════════
# SKILLS
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.html("""
<div style="padding:40px 0 8px">
  <span class="sec-label">CAPABILITIES</span>
  <span class="sec-title">Skills &amp; Technologies</span>
  <div class="sec-bar"></div>
</div>
""")

skill_groups = [
    ("// Languages",           [("Python", 95), ("SQL", 90), ("R", 80)]),
    ("// Agentic AI & Eval",   [("LLM Agents / Tool-Use", 88), ("Evaluation & Harness Design", 85), ("Claude Code / Codex", 92)]),
    ("// ML / AI",             [("Scikit-learn / XGBoost", 90), ("LLMs / RAG / LangChain", 82), ("Deep Learning", 75)]),
    ("// Quant / Finance",     [("Portfolio Analytics", 90), ("Tax-Loss Harvesting", 88), ("Backtesting", 85)]),
    ("// Data & Viz",          [("Tableau / Power BI", 90), ("Pandas / NumPy / Plotly", 92), ("MySQL / MongoDB", 80)]),
    ("// Tools",               [("Streamlit", 88), ("GitHub / CI-CD", 82), ("Cloud (AWS/GCP)", 72)]),
]

for row_start in range(0, len(skill_groups), 3):
    row = skill_groups[row_start:row_start + 3]
    cols = st.columns(len(row))
    for col, (title, skills) in zip(cols, row):
        with col:
            st.html(skill_group_html(title, skills))

# ════════════════════════════════════════════════════════════════════════════
# EDUCATION & ACHIEVEMENTS
# ════════════════════════════════════════════════════════════════════════════
st.html("""
<div style="padding:40px 0 8px">
  <span class="sec-label">BACKGROUND</span>
  <span class="sec-title">Education &amp; Achievements</span>
  <div class="sec-bar"></div>
</div>
""")

col_edu, col_ach = st.columns(2)

with col_edu:
    for edu in [
        {
            "emoji": "🎓",
            "title": "MS Business Analytics (Generative AI & Financial Analytics)",
            "school": "University of Texas at Austin — McCombs School of Business",
            "period": "Jul 2025 – May 2026 · Graduated",
            "detail": "Specialization: Machine Learning · AI-driven investment tools, portfolio analytics, quantitative finance"
        },
        {
            "emoji": "📊",
            "title": "Data Analytics & Visualization Boot Camp",
            "school": "University of Minnesota",
            "period": "2020",
            "detail": "Foundations of analytics and data visualization"
        },
    ]:
        st.html(f"""
        <div style="background:rgba(12,18,32,0.6);border:1px solid rgba(255,255,255,0.07);
                    border-radius:18px;padding:26px;margin-bottom:12px;
                    backdrop-filter:blur(8px);
                    transition:all 0.3s"
             onmouseover="this.style.borderColor='rgba(129,140,248,0.35)';this.style.boxShadow='0 12px 40px rgba(129,140,248,0.1)';this.style.transform='translateY(-3px)'"
             onmouseout="this.style.borderColor='rgba(255,255,255,0.07)';this.style.boxShadow='none';this.style.transform='translateY(0)'">
            <div style="display:flex;align-items:flex-start;gap:14px">
                <div style="width:44px;height:44px;border-radius:12px;flex-shrink:0;
                            background:linear-gradient(135deg,rgba(129,140,248,0.15),rgba(56,189,248,0.1));
                            border:1px solid rgba(129,140,248,0.2);
                            display:flex;align-items:center;justify-content:center;font-size:20px">{edu['emoji']}</div>
                <div>
                    <div style="font-size:15px;font-weight:700;color:#e2e8f0;margin-bottom:5px">{edu['title']}</div>
                    <div style="font-size:13px;font-weight:500;margin-bottom:5px;
                                background:linear-gradient(90deg,#818cf8,#38bdf8);
                                -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                                background-clip:text">{edu['school']}</div>
                    <div style="font-size:12px;color:#64748b;margin-bottom:5px">{edu['period']}</div>
                    <div style="font-size:12px;color:#64748b">{edu['detail']}</div>
                </div>
            </div>
        </div>
        """)

with col_ach:
    achievements = [
        ("🏆", "100 Most Influential Women of Nepal", "Women with Vision", "2018"),
        ("🥈", "Open Data Hackathon — 1st Runner-Up",  "Data-driven solution for public good", "2017"),
        ("🎤", "VP Membership — Toastmasters",         "Leadership & Public Speaking", "Ongoing"),
        ("📜", "Great Learning AI/ML Certifications",  "Generative AI, RAG, ML Deployment", "2025–2026"),
    ]
    rows = "".join(f"""
        <div style="display:flex;gap:16px;padding:16px 12px;border-radius:12px;
                    border-bottom:1px solid rgba(255,255,255,0.05);
                    transition:all 0.2s;cursor:default"
             onmouseover="this.style.background='rgba(129,140,248,0.05)';this.style.paddingLeft='18px'"
             onmouseout="this.style.background='transparent';this.style.paddingLeft='12px'">
            <div style="width:40px;height:40px;border-radius:10px;flex-shrink:0;
                        background:linear-gradient(135deg,rgba(129,140,248,0.12),rgba(56,189,248,0.08));
                        border:1px solid rgba(129,140,248,0.15);
                        display:flex;align-items:center;justify-content:center;font-size:18px">{icon}</div>
            <div>
                <div style="font-size:13.5px;color:#e2e8f0;font-weight:600;margin-bottom:3px">{title}</div>
                <div style="font-size:12px;color:#64748b;margin-bottom:3px">{sub}</div>
                <div style="font-size:11px;font-family:'JetBrains Mono',monospace;
                            background:linear-gradient(90deg,#818cf8,#38bdf8);
                            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                            background-clip:text">{yr}</div>
            </div>
        </div>""" for icon, title, sub, yr in achievements)
    st.html(f"""
    <div style="background:rgba(12,18,32,0.6);border:1px solid rgba(255,255,255,0.07);
                border-radius:18px;padding:16px;height:100%;backdrop-filter:blur(8px)">{rows}</div>
    """)

# ════════════════════════════════════════════════════════════════════════════
# CONTACT
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.html("""
<div style="padding:40px 0 8px">
  <span class="sec-label">CONNECT</span>
  <span class="sec-title">Let's Talk</span>
  <div class="sec-bar"></div>
</div>
""")

col_links, col_open = st.columns(2)

with col_links:
    links = [
        ("💼", "linkedin.com/in/nisha-sapkota-aidata", "https://www.linkedin.com/in/nisha-sapkota-aidata/"),
        ("📧", "nisha.sapkota.ai@gmail.com",           "mailto:nisha.sapkota.ai@gmail.com"),
        ("⚡", "github.com/nisha22sapkota",            "https://github.com/nisha22sapkota"),
    ]
    links_html = "".join(f"""
        <a href="{href}" target="_blank"
           style="display:flex;align-items:center;gap:14px;padding:16px 20px;
                  background:rgba(12,18,32,0.6);border:1px solid rgba(255,255,255,0.07);
                  border-radius:14px;text-decoration:none;color:#94a3b8;
                  margin-bottom:10px;font-size:13px;backdrop-filter:blur(8px);
                  transition:all 0.25s"
           onmouseover="this.style.borderColor='rgba(129,140,248,0.35)';this.style.color='#a5b4fc';this.style.transform='translateX(5px)';this.style.boxShadow='0 4px 20px rgba(129,140,248,0.1)'"
           onmouseout="this.style.borderColor='rgba(255,255,255,0.07)';this.style.color='#94a3b8';this.style.transform='translateX(0)';this.style.boxShadow='none'">
            <span style="font-size:19px">{icon}</span>
            <span>{label}</span>
            <span style="margin-left:auto;font-size:14px;opacity:0.4">↗</span>
        </a>""" for icon, label, href in links)
    st.html(f"""
    <p style="color:#64748b;font-size:14px;line-height:1.85;margin-bottom:22px">
        Actively seeking full-time roles as an AI Systems / Applied AI Engineer —
        building agentic systems, LLM applications, and evaluation infrastructure,
        with a differentiated edge in quantitative finance. Open to SF, NYC, and
        remote-first positions.
    </p>
    {links_html}
    """)

with col_open:
    roles = [
        ("AI Systems / Applied AI Engineer", True),
        ("Agentic AI Engineer — LLM Systems", True),
        ("AI/ML Engineer (Finance)", False),
        ("Quant Researcher / Analyst", False),
        ("Data Scientist — WealthTech / FinTech", False),
        ("Portfolio Analytics & Optimization", False),
    ]
    role_rows = "".join(
        f'<div style="display:flex;align-items:center;gap:10px;padding:9px 0;'
        f'border-bottom:1px solid rgba(255,255,255,0.04);font-size:13px">'
        f'<span style="width:18px;height:18px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;'
        f'background:linear-gradient(135deg,#818cf8,#38bdf8);font-size:9px;color:#03050a">✓</span>'
        f'<span style="color:{"#e2e8f0" if bold else "#94a3b8"};font-weight:{"600" if bold else "400"}">{role}</span>'
        f'</div>'
        for role, bold in roles
    )
    st.html(f"""
    <div style="background:linear-gradient(145deg,#0c1220,#0f172a);
                border:1px solid rgba(129,140,248,0.2);border-radius:18px;
                padding:28px;backdrop-filter:blur(10px);
                box-shadow:0 0 60px rgba(129,140,248,0.05)">
        <div style="font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:2px;
                    text-transform:uppercase;margin-bottom:20px;
                    background:linear-gradient(90deg,#818cf8,#38bdf8);
                    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                    background-clip:text">OPEN TO OPPORTUNITIES</div>
        {role_rows}
        <div style="margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,0.06);
                    font-size:12px;color:#64748b;display:flex;align-items:center;gap:8px">
            <span>📍 Austin, TX</span>
            <span style="opacity:0.3">·</span>
            <span>Available
                <span style="background:linear-gradient(90deg,#818cf8,#38bdf8);
                             -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                             background-clip:text;font-weight:600">Immediately</span>
            </span>
        </div>
    </div>
    """)

# ── Footer ────────────────────────────────────────────────────────────────────
st.html("""
<div style="text-align:center;padding:40px 0 28px;border-top:1px solid rgba(255,255,255,0.05);margin-top:28px">
    <div style="background:linear-gradient(135deg,#818cf8,#38bdf8);
                -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                background-clip:text;font-family:'JetBrains Mono',monospace;
                font-size:16px;font-weight:600;margin-bottom:8px">nisha.sapkota</div>
    <div style="font-size:12px;color:#1e293b;font-family:'JetBrains Mono',monospace;margin-bottom:16px">
        Built with Python &amp; Streamlit · 2026
    </div>
    <a href="#home" style="font-size:12px;color:#64748b;text-decoration:none;
       font-family:'JetBrains Mono',monospace;
       transition:color 0.2s;border:1px solid rgba(255,255,255,0.07);
       padding:6px 16px;border-radius:20px"
       onmouseover="this.style.color='#a5b4fc';this.style.borderColor='rgba(129,140,248,0.3)'"
       onmouseout="this.style.color='#64748b';this.style.borderColor='rgba(255,255,255,0.07)'">
        ↑ back to top
    </a>
</div>
""")
