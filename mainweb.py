import streamlit as st

# Page config
st.set_page_config(
    page_title="We've Moved",
    page_icon="🚀",
    layout="centered",
)

# Custom CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Syne:wght@700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .main {
            background-color: #0d0d0d;
        }

        .block-container {
            padding-top: 5rem;
            padding-bottom: 5rem;
        }

        .hero-tag {
            font-family: 'Inter', sans-serif;
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            color: #7DF9C2;
            margin-bottom: 1.2rem;
        }

        .hero-title {
            font-family: 'Syne', sans-serif;
            font-size: clamp(2.4rem, 6vw, 4rem);
            font-weight: 800;
            color: #F5F5F0;
            line-height: 1.1;
            margin-bottom: 1.5rem;
        }

        .hero-title span {
            color: #7DF9C2;
        }

        .hero-body {
            font-size: 1.05rem;
            color: #999;
            line-height: 1.8;
            max-width: 520px;
            margin-bottom: 2.5rem;
        }

        .link-card {
            background: #161616;
            border: 1px solid #2a2a2a;
            border-radius: 12px;
            padding: 1.4rem 1.8rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1rem;
        }

        .link-label {
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            color: #555;
            margin-bottom: 0.3rem;
        }

        .link-url {
            font-family: 'Syne', sans-serif;
            font-size: 1.1rem;
            font-weight: 700;
            color: #F5F5F0;
        }

        .cta-button {
            display: inline-block;
            background: #7DF9C2;
            color: #0d0d0d;
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            font-size: 0.95rem;
            padding: 0.85rem 2rem;
            border-radius: 8px;
            text-decoration: none;
            transition: opacity 0.2s ease;
        }

        .cta-button:hover {
            opacity: 0.85;
            color: #0d0d0d;
        }

        .divider {
            border: none;
            border-top: 1px solid #1e1e1e;
            margin: 2.5rem 0;
        }

        .footer-note {
            font-size: 0.82rem;
            color: #444;
            line-height: 1.6;
        }

        .dot {
            display: inline-block;
            width: 8px;
            height: 8px;
            background: #7DF9C2;
            border-radius: 50%;
            margin-right: 0.5rem;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }
    </style>
""", unsafe_allow_html=True)

# Hero section
st.markdown('<p class="hero-tag">📦 Platform Update</p>', unsafe_allow_html=True)
st.markdown('<h1 class="hero-title">We\'ve moved to a <span>new home.</span></h1>', unsafe_allow_html=True)
st.markdown("""
    <p class="hero-body">
        This platform has been retired. All features, your data, and everything you love
        are now available at our new address — faster and better than ever.
    </p>
""", unsafe_allow_html=True)

# New link card
st.markdown("""
    <div class="link-card">
        <div>
            <div class="link-label">New Platform</div>
            <div class="link-url">paperport.bolt.host</div>
        </div>
        <span style="color: #333; font-size: 1.4rem;">→</span>
    </div>
""", unsafe_allow_html=True)

# CTA Button
st.markdown("""
    <a class="cta-button" href="https://paperport.bolt.host" target="_blank">
        Visit New Platform ↗
    </a>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# Status indicator + footer note
st.markdown("""
    <p class="footer-note">
        <span class="dot"></span>
        The new platform is live and fully operational.
        Please update any saved bookmarks or links to point to
        <strong style="color: #7DF9C2;">paperport.bolt.host</strong>.
        If you have any questions, reach out to our support team.
    </p>
""", unsafe_allow_html=True)
