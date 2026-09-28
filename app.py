import streamlit as st

st.set_page_config(
    page_title="AI Smart Tutor",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 20% 20%, rgba(0, 180, 255, 0.12), transparent 30%),
        radial-gradient(circle at 80% 70%, rgba(90, 50, 255, 0.12), transparent 30%),
        #050912;
    color: #ffffff;
}

/* Animated background */
.stApp::before {
    content: "";
    position: fixed;
    width: 500px;
    height: 500px;
    background: rgba(0, 174, 255, 0.08);
    border-radius: 50%;
    filter: blur(100px);
    top: -150px;
    left: -150px;
    animation: float 8s infinite alternate;
    pointer-events: none;
}

@keyframes float {
    from {
        transform: translate(0px, 0px);
    }
    to {
        transform: translate(250px, 150px);
    }
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #07111f, #030711);
    border-right: 1px solid rgba(0, 174, 255, 0.25);
}

/* Main title */
.hero {
    padding: 50px 20px;
    text-align: center;
    border-radius: 25px;
    background: linear-gradient(
        135deg,
        rgba(0, 174, 255, 0.12),
        rgba(70, 30, 180, 0.12)
    );
    border: 1px solid rgba(0, 174, 255, 0.25);
    box-shadow: 0 0 40px rgba(0, 174, 255, 0.08);
    animation: appear 1s ease;
}

.hero h1 {
    font-size: 52px;
    background: linear-gradient(90deg, #00c6ff, #7b61ff);
    -webkit-background-clip: text;
    color: transparent;
}

.hero p {
    color: #9ba9bd;
    font-size: 18px;
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Cards */
.card {
    padding: 25px;
    border-radius: 20px;
    background: rgba(12, 23, 40, 0.75);
    border: 1px solid rgba(0, 174, 255, 0.20);
    box-shadow: 0 0 25px rgba(0, 174, 255, 0.06);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-6px);
    border-color: #00b7ff;
    box-shadow: 0 0 30px rgba(0, 183, 255, 0.18);
}

.metric {
    font-size: 32px;
    font-weight: bold;
    color: #00c6ff;
}

.small {
    color: #8998aa;
}

/* Buttons */
.stButton > button {
    border-radius: 12px;
    border: 1px solid #00b7ff;
    background: linear-gradient(90deg, #0077ff, #6236ff);
    color: white;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    box-shadow: 0 0 20px rgba(0, 183, 255, 0.45);
    transform: scale(1.03);
}

/* Inputs */
.stTextInput input,
.stTextArea textarea {
    background: #091321 !important;
    color: white !important;
    border: 1px solid #193451 !important;
    border-radius: 12px !important;
}

</style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:

    st.markdown("""
    <div style="text-align:center;padding:20px">

    <div style="font-size:55px;">🤖</div>

    <h2 style="
        color:#00c6ff;
        margin-bottom:0;
    ">
    AI Smart Tutor
    </h2>

    <p style="color:#718096">
    Intelligent Learning Platform
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("""
    <div class="card">
    <b>🚀 AI Learning System</b>
    <br><br>
    Personalized learning powered by AI.
    </div>
    """, unsafe_allow_html=True)


# Main screen
st.markdown("""
<div class="hero">

<h1>AI Smart Tutor</h1>

<p>
Your intelligent learning companion for
personalized education, quizzes and analytics.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
    <div class="metric">120+</div>
    <div class="small">Lessons</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <div class="metric">85%</div>
    <div class="small">Avg Score</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <div class="metric">24</div>
    <div class="small">Quizzes</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
    <div class="metric">12</div>
    <div class="small">Students</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

st.markdown("""
<div class="card">

<h2 style="color:#00c6ff">
⚡ Welcome to AI Smart Tutor
</h2>

<p style="color:#a5b4c5;font-size:17px">

Use the navigation menu to explore the platform.

</p>

<ul style="color:#a5b4c5;font-size:16px">

<li>📊 View student performance</li>
<li>🤖 Ask the AI Tutor questions</li>
<li>📝 Take interactive quizzes</li>
<li>📈 Analyze learning progress</li>

</ul>

</div>
""", unsafe_allow_html=True)
