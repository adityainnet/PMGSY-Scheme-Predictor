"""
CSS styles for the Streamlit application.
Bold dark navy AI dashboard — high contrast, zero white-on-white issues.
"""

import streamlit as st


def apply_styles():
    """Apply custom CSS styles to the Streamlit app."""
    st.markdown("""
        <style>
            /* ─── Google Fonts ─── */
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

            /* ─── CSS Variables / Design Tokens ─── */
            :root {
                --font-main: 'Plus Jakarta Sans', 'Inter', sans-serif;
                --color-bg: #0b0f19;
                --color-surface: rgba(17, 24, 39, 0.75);
                --color-surface-solid: #111827;
                --color-border: rgba(99, 102, 241, 0.25);
                --color-border-strong: rgba(6, 182, 212, 0.45);
                --color-text-primary: #f8fafc;
                --color-text-secondary: #cbd5e1;
                --color-text-muted: #64748b;
                --color-accent: #6366f1;
                --color-accent-light: #06b6d4;
                --color-accent-glow: rgba(99, 102, 241, 0.25);
                --color-success: #10b981;
                --color-warning: #f59e0b;
                --color-error: #ef4444;
                --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
                --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
                --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.2), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
                --radius-sm: 10px;
                --radius-md: 16px;
                --radius-lg: 20px;
                --radius-xl: 28px;
                --transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
            }

            /* ─── Keyframes ─── */
            @keyframes fadeInUp {
                from { opacity: 0; transform: translateY(18px); }
                to   { opacity: 1; transform: translateY(0); }
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to   { opacity: 1; }
            }
            @keyframes shimmer {
                0%   { background-position: -200% center; }
                100% { background-position:  200% center; }
            }
            @keyframes pulse-ring {
                0%   { box-shadow: 0 0 0 0   rgba(99, 102, 241, 0.35); }
                70%  { box-shadow: 0 0 0 10px rgba(99, 102, 241, 0); }
                100% { box-shadow: 0 0 0 0   rgba(99, 102, 241, 0); }
            }
            @keyframes slideInLeft {
                from { opacity: 0; transform: translateX(-14px); }
                to   { opacity: 1; transform: translateX(0); }
            }
            @keyframes cardReveal {
                from { opacity: 0; transform: translateY(24px) scale(0.98); }
                to   { opacity: 1; transform: translateY(0)  scale(1); }
            }

            /* ─── Base & Background ─── */
            html, body, .stApp {
                font-family: var(--font-main) !important;
                background-color: var(--color-bg) !important;
                background-image:
                    radial-gradient(circle at 10% 20%, rgba(99, 102, 241, 0.12) 0%, transparent 50%),
                    radial-gradient(circle at 90% 80%, rgba(6, 182, 212, 0.08) 0%, transparent 50%) !important;
                color: var(--color-text-primary) !important;
                min-height: 100vh;
            }
            .main { background: transparent !important; padding-top: 0 !important; }

            section[data-testid="stSidebar"] {
                background: rgba(15, 23, 42, 0.95) !important;
                backdrop-filter: blur(12px) !important;
                border-right: 1px solid var(--color-border) !important;
            }

            /* ─── Typography ─── */
            h1, h2, h3, h4, h5, h6 {
                font-family: var(--font-main) !important;
                color: var(--color-text-primary) !important;
                letter-spacing: -0.025em;
            }
            p, label {
                font-family: var(--font-main) !important;
                color: var(--color-text-secondary);
            }

            /* ─── Hero Section ─── */
            .hero-section {
                background: linear-gradient(135deg, #111827 0%, #1e1b4b 60%, #0f172a 100%);
                border-radius: var(--radius-xl);
                padding: 36px 44px;
                margin: 0 0 28px 0;
                border: 1px solid var(--color-border);
                box-shadow: var(--shadow-lg);
                position: relative;
                overflow: hidden;
                animation: fadeInUp 0.55s ease both;
            }
            .hero-section img {
                background-color: #ffffff !important;
                padding: 10px 16px !important;
                border-radius: var(--radius-sm) !important;
                box-shadow: var(--shadow-sm) !important;
                display: block !important;
                margin: auto !important;
            }
            .hero-section::before {
                content: '';
                position: absolute;
                top: -60px; right: -60px;
                width: 220px; height: 220px;
                background: radial-gradient(circle, rgba(6, 182, 212, 0.15) 0%, transparent 70%);
                border-radius: 50%;
                pointer-events: none;
            }
            .hero-badge {
                display: inline-flex;
                align-items: center;
                gap: 6px;
                background: linear-gradient(90deg, rgba(99, 102, 241, 0.18), rgba(6, 182, 212, 0.18));
                border: 1px solid rgba(6, 182, 212, 0.35);
                color: var(--color-accent-light);
                font-size: 11px;
                font-weight: 700;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                padding: 5px 12px;
                border-radius: 100px;
                margin-bottom: 12px;
            }
            .hero-title {
                font-size: 30px;
                font-weight: 800;
                margin: 0 0 10px 0;
                line-height: 1.18;
                background: linear-gradient(135deg, #ffffff 30%, #a5b4fc 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            .hero-subtitle {
                font-size: 14.5px;
                color: var(--color-text-secondary);
                margin: 0;
                line-height: 1.6;
                font-weight: 400;
            }

            /* ─── Stat Cards ─── */
            .stats-section-label {
                font-size: 11px;
                font-weight: 700;
                letter-spacing: 0.10em;
                text-transform: uppercase;
                color: var(--color-text-muted);
                margin: 0 0 14px 2px;
                animation: fadeIn 0.4s ease both 0.2s;
            }
            .stat-card {
                background: var(--color-surface);
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border-radius: var(--radius-md);
                padding: 22px 18px;
                text-align: center;
                border: 1px solid var(--color-border);
                box-shadow: var(--shadow-sm);
                transition: var(--transition);
                animation: fadeInUp 0.5s ease both;
                position: relative;
                overflow: hidden;
            }
            .stat-card::before {
                content: '';
                position: absolute;
                top: 0; left: 0; right: 0;
                height: 3px;
                background: linear-gradient(90deg, var(--color-accent), var(--color-accent-light));
                opacity: 0;
                transition: var(--transition);
            }
            .stat-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); border-color: var(--color-border-strong); }
            .stat-card:hover::before { opacity: 1; }
            .stat-icon { font-size: 22px; margin-bottom: 8px; display: block; }
            .stat-value {
                font-size: 30px;
                font-weight: 800;
                color: var(--color-text-primary);
                margin: 4px 0 6px 0;
                letter-spacing: -0.03em;
                line-height: 1;
            }
            .stat-value.accent { color: var(--color-accent-light); }
            .stat-label {
                font-size: 11px;
                color: var(--color-text-muted);
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.08em;
            }

            /* ─── Model Metrics Expander ─── */
            [data-testid="stExpander"] {
                background: var(--color-surface) !important;
                backdrop-filter: blur(12px) !important;
                border-radius: var(--radius-md) !important;
                border: 1px solid var(--color-border) !important;
                box-shadow: var(--shadow-sm) !important;
                overflow: hidden;
            }
            [data-testid="stExpander"] summary span {
                color: var(--color-text-primary) !important;
            }
            [data-testid="stMetric"] {
                background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(6, 182, 212, 0.15) 100%) !important;
                padding: 18px !important;
                border-radius: var(--radius-sm) !important;
                box-shadow: none !important;
                border: 1px solid rgba(99,102,241,0.2) !important;
            }
            [data-testid="stMetricValue"] {
                color: var(--color-accent-light) !important;
                font-weight: 700 !important;
                font-size: 22px !important;
            }
            [data-testid="stMetricLabel"] {
                color: var(--color-text-secondary) !important;
            }

            /* ─── Section Titles ─── */
            .section-title {
                font-size: 15px;
                font-weight: 700;
                color: var(--color-text-primary);
                margin: 0 0 14px 0;
                display: flex;
                align-items: center;
                gap: 8px;
                letter-spacing: -0.01em;
            }

            /* ─── Quick Fill Banner ─── */
            .quickfill-banner {
                background: linear-gradient(135deg, rgba(245, 158, 11, 0.12) 0%, rgba(217, 119, 6, 0.08) 100%);
                border: 1px solid rgba(245, 158, 11, 0.40);
                border-radius: var(--radius-md);
                padding: 14px 18px;
                margin-bottom: 16px;
                animation: slideInLeft 0.4s ease both;
            }
            .quickfill-title { font-weight: 700; color: #f59e0b; font-size: 13px; }
            .quickfill-desc  { color: #fbbf24; font-size: 12px; margin: 4px 0 0; line-height: 1.5; }

            /* ─── Form Sections ─── */
            .form-section {
                background: var(--color-surface);
                backdrop-filter: blur(14px);
                -webkit-backdrop-filter: blur(14px);
                border-radius: var(--radius-md);
                padding: 24px 24px 20px;
                box-shadow: var(--shadow-sm);
                border: 1px solid var(--color-border);
                margin: 12px 0;
                transition: var(--transition);
                animation: fadeInUp 0.5s ease both;
            }
            .form-section:hover { box-shadow: var(--shadow-md); border-color: var(--color-border-strong); }
            .form-group-title {
                font-size: 13px;
                font-weight: 700;
                color: var(--color-text-secondary);
                margin: 0 0 18px 0;
                padding-bottom: 12px;
                border-bottom: 1px solid var(--color-border);
                letter-spacing: 0.02em;
            }

            /* ─── Inputs and Dropdowns Fix (Zero white-on-white) ─── */
            .stSelectbox > div > div,
            .stNumberInput > div > div > input {
                border-radius: var(--radius-sm) !important;
                border: 1.5px solid rgba(99, 102, 241, 0.35) !important;
                background-color: #111827 !important;
                color: #f8fafc !important;
                font-family: var(--font-main) !important;
                font-size: 14px !important;
                transition: var(--transition) !important;
            }
            .stSelectbox > div > div:focus-within,
            .stNumberInput > div > div > input:focus {
                border-color: var(--color-accent-light) !important;
                box-shadow: 0 0 0 3px rgba(6, 182, 212, 0.25) !important;
            }
            .stSelectbox label, .stNumberInput label,
            .stSelectbox > label, .stNumberInput > label {
                font-weight: 600 !important;
                color: var(--color-text-secondary) !important;
                font-size: 13px !important;
                letter-spacing: 0.01em !important;
            }

            /* Portals, Popups, Listboxes, Dropdowns (Strict Contrast Override) */
            div[data-baseweb="popover"], 
            div[data-baseweb="menu"],
            ul[role="listbox"],
            div[role="listbox"] {
                background-color: #111827 !important;
                border: 1px solid rgba(99, 102, 241, 0.45) !important;
            }
            div[role="option"],
            li[role="option"],
            [data-baseweb="menu"] li,
            [data-baseweb="menu"] div,
            [data-baseweb="select"] li,
            [data-baseweb="select"] div,
            span[data-baseweb="select"] {
                background-color: #111827 !important;
                color: #f8fafc !important;
            }
            div[role="option"]:hover,
            li[role="option"]:hover,
            [data-baseweb="menu"] li:hover,
            [data-baseweb="menu"] div:hover,
            [data-baseweb="select"] li:hover,
            [data-baseweb="select"] div:hover {
                background-color: rgba(99, 102, 241, 0.25) !important;
                color: #06b6d4 !important;
            }
            
            /* High-contrast options labels */
            div[role="option"] *,
            li[role="option"] *,
            [data-baseweb="menu"] *,
            [data-baseweb="select"] * {
                color: #f8fafc !important;
            }
            div[role="option"]:hover *,
            li[role="option"]:hover *,
            [data-baseweb="menu"] li:hover *,
            [data-baseweb="select"] li:hover * {
                color: #06b6d4 !important;
            }

            /* Fixes text color within dropdown inputs */
            div[data-baseweb="select"] > div,
            div[data-baseweb="select"] span {
                color: #f8fafc !important;
            }

            /* ─── Primary Button ─── */
            .stButton > button[kind="primary"],
            .stButton > button:not([kind="secondary"]) {
                background: linear-gradient(135deg, #6366f1 0%, #06b6d4 100%) !important;
                color: #ffffff !important;
                border: none !important;
                border-radius: var(--radius-md) !important;
                padding: 14px 32px !important;
                font-weight: 700 !important;
                font-size: 15px !important;
                font-family: var(--font-main) !important;
                transition: var(--transition) !important;
                box-shadow: 0 4px 20px rgba(99, 102, 241, 0.35) !important;
            }
            .stButton > button[kind="primary"]:hover,
            .stButton > button:not([kind="secondary"]):hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 8px 28px rgba(6, 182, 212, 0.45) !important;
                background: linear-gradient(135deg, #4f46e5 0%, #0891b2 100%) !important;
            }

            /* ─── Secondary Buttons ─── */
            .stButton > button[kind="secondary"] {
                background: #111827 !important;
                color: var(--color-text-secondary) !important;
                border: 1.5px solid rgba(99, 102, 241, 0.35) !important;
                border-radius: var(--radius-sm) !important;
                padding: 8px 14px !important;
                font-size: 12.5px !important;
                font-weight: 600 !important;
                font-family: var(--font-main) !important;
                box-shadow: var(--shadow-sm) !important;
                transition: var(--transition) !important;
            }
            .stButton > button[kind="secondary"]:hover {
                background: rgba(99, 102, 241, 0.15) !important;
                border-color: var(--color-accent-light) !important;
                color: #ffffff !important;
                transform: translateY(-1px) !important;
            }

            /* ─── Spinner ─── */
            .stSpinner > div { border-top-color: var(--color-accent-light) !important; }

            /* ─── Result Card ─── */
            .result-card {
                background: linear-gradient(135deg, #111827 0%, #1e1b4b 60%, #0f172a 100%);
                border-radius: var(--radius-xl);
                padding: 40px 32px;
                text-align: center;
                border: 1px solid rgba(99, 102, 241, 0.35);
                box-shadow: var(--shadow-lg);
                position: relative;
                overflow: hidden;
                animation: cardReveal 0.55s cubic-bezier(0.34,1.56,0.64,1) both;
            }
            .result-card::before {
                content: '';
                position: absolute;
                top: 0; left: 0; right: 0;
                height: 4px;
                background: linear-gradient(90deg, #6366f1, #06b6d4, #a5b4fc, #6366f1);
                background-size: 200% 100%;
                animation: shimmer 3s linear infinite;
            }
            .result-eyebrow {
                font-size: 11px;
                font-weight: 700;
                letter-spacing: 0.12em;
                text-transform: uppercase;
                color: var(--color-text-muted);
                margin: 0 0 12px 0;
            }
            .result-scheme-name {
                font-size: 30px;
                font-weight: 800;
                margin: 0 0 20px 0;
                letter-spacing: -0.03em;
                background: linear-gradient(135deg, #ffffff 30%, #cbd5e1 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }

            /* ─── Premium Card (generic) ─── */
            .premium-card {
                background: var(--color-surface);
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border-radius: var(--radius-md);
                padding: 24px;
                box-shadow: var(--shadow-sm);
                border: 1px solid var(--color-border);
                margin-bottom: 16px;
                transition: var(--transition);
                animation: fadeInUp 0.4s ease both;
            }
            .premium-card:hover {
                box-shadow: var(--shadow-md);
                border-color: var(--color-border-strong);
                transform: translateY(-2px);
            }

            /* ─── Confidence Badges ─── */
            .confidence-badge {
                display: inline-flex;
                align-items: center;
                gap: 6px;
                padding: 8px 18px;
                border-radius: 100px;
                font-weight: 700;
                font-size: 13.5px;
                letter-spacing: 0.01em;
                animation: pulse-ring 2s infinite;
            }
            .confidence-badge::before {
                content: '';
                display: inline-block;
                width: 7px; height: 7px;
                border-radius: 50%;
                background: currentColor;
            }
            .high-confidence {
                background: rgba(16, 185, 129, 0.15);
                color: var(--color-success);
                border: 1.5px solid rgba(16, 185, 129, 0.35);
            }
            .medium-confidence {
                background: rgba(245, 158, 11, 0.15);
                color: var(--color-warning);
                border: 1.5px solid rgba(245, 158, 11, 0.35);
            }
            .low-confidence {
                background: rgba(239, 68, 68, 0.15);
                color: var(--color-error);
                border: 1.5px solid rgba(239, 68, 68, 0.35);
            }

            /* ─── Alerts ─── */
            [data-testid="stAlert"] {
                background-color: #111827 !important;
                border-radius: var(--radius-md) !important;
                border-width: 1.5px !important;
                font-family: var(--font-main) !important;
                animation: fadeInUp 0.35s ease both !important;
            }
            [data-testid="stAlert"] div {
                color: var(--color-text-secondary) !important;
            }

            /* ─── Scrollbar ─── */
            ::-webkit-scrollbar { width: 6px; height: 6px; }
            ::-webkit-scrollbar-track { background: transparent; }
            ::-webkit-scrollbar-thumb { background: rgba(99,102,241,0.25); border-radius: 99px; }
            ::-webkit-scrollbar-thumb:hover { background: rgba(99,102,241,0.45); }

            /* ─── Footer ─── */
            .app-footer {
                text-align: center;
                padding: 28px 0 12px;
                color: var(--color-text-muted);
                font-size: 12px;
                font-weight: 500;
                animation: fadeIn 0.6s ease both;
            }

            /* ─── Hide Streamlit Chrome ─── */
            #MainMenu { visibility: hidden; }
            footer { visibility: hidden; }
            [data-testid="stToolbar"] { display: none; }

            /* ─── Divider ─── */
            .styled-divider {
                border: none;
                height: 1px;
                background: linear-gradient(90deg, transparent, var(--color-border), transparent);
                margin: 28px 0;
            }
        </style>
    """, unsafe_allow_html=True)
