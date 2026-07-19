import streamlit as st

# 1. Page Configuration (No sidebar, sleek top-tabs layout)
st.set_page_config(
    page_title="Sakshi Kumari | Corporate Finance & Tech-Enabled Analytics",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Premium Styling Engine & Micro-Animations
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <style>
        /* Base page theme & Global Animation */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(18px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #080C14 !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        /* Smooth page rendering */
        [data-testid="stVerticalBlock"] {
            animation: fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) both;
        }

        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 3rem !important;
        }

        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Premium Corporate Typography */
        h1, h2, h3 {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 700 !important;
            color: #F8FAFC !important;
            letter-spacing: -0.02em !important;
        }
        
        p, li, span, div {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #94A3B8 !important;
        }
        
        /* Interactive Glowing Cards */
        .content-card {
            background-color: #0F172A;
            padding: 28px;
            border-radius: 14px;
            border: 1px solid #1E293B;
            margin-bottom: 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }
        
        .content-card:hover {
            transform: translateY(-5px);
            border-color: #10B981 !important;
            box-shadow: 0 10px 25px rgba(16, 185, 129, 0.12);
        }
        
        /* Tech/Finance Pill Badges */
        .badge {
            background-color: #1E293B;
            color: #10B981;
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            font-weight: 500;
            padding: 4px 10px;
            border-radius: 6px;
            border: 1px solid rgba(16, 185, 129, 0.2);
            margin-right: 6px;
            margin-top: 6px;
            display: inline-block;
        }

        .timeline-date {
            font-family: 'JetBrains Mono', monospace;
            font-size: 13px;
            color: #10B981 !important;
            font-weight: 600;
        }
        
        /* Actionable Contact Items */
        .info-box {
            background-color: #0F172A;
            padding: 22px;
            border-radius: 12px;
            border-left: 4px solid #10B981;
            border-right: 1px solid #1E293B;
            border-top: 1px solid #1E293B;
            border-bottom: 1px solid #1E293B;
            margin-bottom: 16px;
            transition: all 0.3s ease;
        }
        
        .info-box:hover {
            transform: translateX(6px);
            background-color: #1E293B;
            border-left-color: #34D399;
        }
        
        .accent-color {
            color: #10B981 !important;
            font-weight: 800;
            letter-spacing: -0.03em;
        }
        
        /* Elevated Top Navigation Tab Bar styling */
        button[data-baseweb="tab"] {
            font-size: 15px !important;
            font-weight: 600 !important;
            color: #64748B !important;
            border-bottom-width: 2px !important;
            transition: all 0.2s ease !important;
            padding: 12px 18px !important;
        }
        
        button[aria-selected="true"] {
            color: #10B981 !important;
            border-bottom-color: #10B981 !important;
        }
        
        button[data-baseweb="tab"]:hover {
            color: #34D399 !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER BLOCK ---
st.markdown("# <span class='accent-color'>SAKSHI KUMARI</span>", unsafe_allow_html=True)
st.markdown("#### BBA Finance Undergraduate | Tech-Enhanced Financial Analyst")
st.write("---")

# --- INTERACTIVE DASHBOARD SECTIONS ---
tab_about, tab_projects, tab_skills, tab_experience, tab_certs, tab_education, tab_contact = st.tabs([
    "👤 About Me", 
    "🛠️ Selected Projects", 
    "🧠 Skills", 
    "💼 Experience",
    "📜 Certifications",
    "🎓 Education",
    "📬 Let's Connect"
])

# --- TAB 1: ABOUT ME ---
with tab_about:
    st.markdown("## 👤 Professional Profile")
    st.markdown(
        """
        <div class="content-card">
            <h3 style="color: #F8FAFC; margin-bottom: 15px;">Bridging Corporate Finance & Modern Analytical Tools</h3>
            <p style="font-size: 16px; line-height: 1.7; color: #CBD5E1; margin-bottom: 18px;">
                I am a Finance undergraduate student currently in my 3rd semester of BBA. 
                My core interest lies in corporate valuation, accounting analysis, and corporate structures. 
                Rather than sticking only to static spreadsheets, I challenge myself to learn modern presentation tools 
                and web dashboards to make financial metrics and trends interactive and easier for corporate teams to digest.
            </p>
            <p style="font-size: 16px; line-height: 1.7; color: #CBD5E1;">
                As a business student, I believe that having a basic grasp of tech systems is a massive career superpower. 
                My goal is to bring modern analytical thinking into financial services, utilizing technology to turn complex datasets into clean visual narratives.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

# --- TAB 2: PROJECTS ---
with tab_projects:
    st.markdown("## 🛠️ Portfolio Projects")
    st.write("Hover over the cards below to observe the interactive highlight features:")
    st.write("")
    
    # Project 1: FP&A Dashboard
    st.markdown(
        """
        <div class="content-card">
            <h3 style="color: #F8FAFC;"><i class="fa-solid fa-chart-line" style="color: #10B981; margin-right: 12px;"></i>Real-Time FP&A Market Intelligence Dashboard</h3>
            <p style="color: #CBD5E1; margin-top: 8px;">
                An interactive web app modeled to track market sector indexes and explain corporate profitability ratios. 
                Built to show how web technologies can make raw stock indicators and analytical ratios accessible at a glance.
            </p>
            <div style="margin-top: 16px;">
                <span class="badge">Analytical UI Layout</span>
                <span class="badge">Financial Metrics</span>
                <span class="badge">Data Presentation</span>
                <span class="badge">Streamlit Prototype</span>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
    st.link_button("🌐 Launch Live Dashboard", "https://fpa-dashboard-ahichqnacyjsrvk9hkto9a.streamlit.app")
    st.write("")
    
    # Project 2: Industry Valuation Matrix
    st.markdown(
        """
        <div class="content-card">
            <h3 style="color: #F8FAFC;"><i class="fa-solid fa-table" style="color: #10B981; margin-right: 12px;"></i>Multi-Sector Corporate Valuation Matrix</h3>
            <p style="color: #CBD5E1; margin-top: 8px;">
                A comprehensive comparative study mapping valuation multiples (P/E, EV/Sales, and Debt/Equity) across five major companies in different sectors. Tracks trendlines over multiple quarters to isolate market valuation anomalies.
            </p>
            <div style="margin-top: 16px;">
                <span class="badge">MS Excel Modeling</span>
                <span class="badge">Ratio Analysis</span>
                <span class="badge">Relative Valuation</span>
                <span class="badge">Competitive Benchmarking</span>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Project 3: Portfolio Beta & Risk Tracker
    st.markdown(
        """
        <div class="content-card">
            <h3 style="color: #F8FAFC;"><i class="fa-solid fa-shield-halved" style="color: #10B981; margin-right: 12px;"></i>Portfolio Beta & Investment Risk Tracker</h3>
            <p style="color: #CBD5E1; margin-top: 8px;">
                An analytical tracking framework modeled to map capital asset behaviors, volatility shifts, and historical covariance matrices. Calculates expected asset returns using CAPM models to identify and reduce stock volatility.
            </p>
            <div style="margin-top: 16px;">
                <span class="badge">Financial Modeling Basics</span>
                <span class="badge">CAPM Principles</span>
                <span class="badge">Beta Calculations</span>
                <span class="badge">Risk Assessment</span>
            </div>
        </div>
        """, unsafe_allow_html=True
    )

# --- TAB 3: SKILLS ---
with tab_skills:
    st.markdown("## 🧠 Core Competencies")
    
    col_fin, col_tech = st.columns(2, gap="large")
    
    with col_fin:
        st.markdown(
            """
            <div class="content-card" style="height: 100%;">
                <h3 style="color: #F8FAFC;"><i class="fa-solid fa-wallet" style="color: #10B981; margin-right: 12px;"></i>Financial & Business Foundations</h3>
                <p style="color: #CBD5E1; margin-bottom: 20px;">Fundamental principles of business administration and corporate accounting:</p>
                <ul style="color: #94A3B8; line-height: 2; font-size: 15px; padding-left: 20px;">
                    <li><strong>Corporate Valuation Basics:</strong> Understanding peer group multiples and market tracking.</li>
                    <li><strong>Fundamental Accounting:</strong> Tracking profitability, liquidity, and leverage metrics (ROE, margins).</li>
                    <li><strong>Capital Structure:</strong> Understanding the relationships between debt, equity, and company growth.</li>
                    <li><strong>Banking & Insurance Principles:</strong> Familiarity with retail banking workflows and insurance underwriting.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True
        )
        
    with col_tech:
        st.markdown(
            """
            <div class="content-card" style="height: 100%;">
                <h3 style="color: #F8FAFC;"><i class="fa-solid fa-graduation-cap" style="color: #10B981; margin-right: 12px;"></i>Tech-Enabled Capabilities (Learning Journey)</h3>
                <p style="color: #CBD5E1; margin-bottom: 20px;">Applying modern digital tooling to enhance traditional business workflows:</p>
                <ul style="color: #94A3B8; line-height: 2; font-size: 15px; padding-left: 20px;">
                    <li><strong>Excel Data Analysis:</strong> Crafting formulas, data validation, and clean formatting models.</li>
                    <li><strong>Interactive Dashboards:</strong> Building clean web app interfaces using Streamlit framework.</li>
                    <li><strong>Basic Scripting Foundations:</strong> Learning core Python syntax, libraries (Pandas), and plotting tools.</li>
                    <li><strong>Visual Presentation:</strong> Designing modern dashboards with streamlined user experiences.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True
        )

# --- TAB 4: EXPERIENCE ---
with tab_experience:
    st.markdown("## 💼 Professional Experience")
    
    # Experience Item 1: FinSckool Equity Research Internship
    st.markdown(
        """
        <div class="content-card">
            <span class="timeline-date">Aug 2025 - Sept 2025 | Virtual Intern</span>
            <h3 style="color: #F8FAFC; margin-top: 6px;">📈 Equity Research Virtual Internship</h3>
            <p style="color: #10B981; font-weight: 600; font-size: 15px;">FinSckool</p>
            <p style="color: #CBD5E1; font-size: 15px; margin-top: 8px; line-height: 1.6;">
                Participated in an intensive, virtual corporate research project focusing on the systematic evaluation and profiling of publicly traded enterprises:
            </p>
            <ul style="color: #94A3B8; line-height: 1.8; margin-top: 10px; padding-left: 20px;">
                <li>Conducted detailed corporate profile studies, mapping competitor landscape segments and industry trend drivers.</li>
                <li>Analyzed key operating metrics and capital structure compositions of target companies.</li>
                <li>Synthesized multi-quarter relative valuation metrics, assessing baseline risk-reward paradigms.</li>
                <li>Gained practical exposure to financial reporting frameworks and structured investment thesis design.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Experience Item 2: Goldman Sachs Simulation
    st.markdown(
        """
        <div class="content-card">
            <span class="timeline-date">Job Simulation | Virtual Participant</span>
            <h3 style="color: #F8FAFC; margin-top: 6px;">🏆 Goldman Sachs Excel Skills Simulation</h3>
            <p style="color: #10B981; font-weight: 600; font-size: 15px;">Forage</p>
            <p style="color: #CBD5E1; font-size: 15px; margin-top: 8px; line-height: 1.6;">
                Completed a highly structured corporate job simulation focused on core analyst workflows, forecasting processes, and financial modeling:
            </p>
            <ul style="color: #94A3B8; line-height: 1.8; margin-top: 10px; padding-left: 20px;">
                <li>Designed a 5-year operational assumption and forecast model, avoiding hardcoded cells.</li>
                <li>Constructed linked Profit & Loss models to dynamically recalculate Gross Profit, EBITDA, and Net Profit.</li>
                <li>Calculated net cash flow profiles and integrated logical repayment schedules to pay down debt using surplus cash flow.</li>
                <li>Generated clean analytical outputs and data visualizations to help clients digest results quickly.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )

# --- TAB 5: CERTIFICATIONS ---
with tab_certs:
    st.markdown("## 📜 Professional Certifications & Training")
    st.write("Review my specialized industry training achievements and credentials below:")
    st.write("")
    
    # Certification Item 1: CBPFI Training
    st.markdown(
        """
        <div class="content-card">
            <span class="timeline-date">Mar 2026 - May 2026 | 120-Hour Program</span>
            <h3 style="color: #F8FAFC; margin-top: 6px;">🏛️ Certificate Programme in Banking, Finance & Insurance (CPBFI)</h3>
            <p style="color: #10B981; font-weight: 600; font-size: 15px;">Bajaj Finserv</p>
            <p style="color: #CBD5E1; font-size: 15px; margin-top: 8px; line-height: 1.6;">
                Completed an intensive, highly competitive 120-hour professional training curriculum designed to bridge academic business learning with actual financial service industries:
            </p>
            <ul style="color: #94A3B8; line-height: 1.8; margin-top: 10px; padding-left: 20px;">
                <li><strong>Core Banking & Financial Services:</strong> Mastered retail banking principles, KYC procedures, underwriting structures, asset/liability products, and key regulatory functions of the RBI.</li>
                <li><strong>Insurance Operations & Management:</strong> Gained deep coverage of life and general insurance mechanisms, underwriting risk variables, distribution strategies, and IRDA directives.</li>
                <li><strong>Communication & Work Skills:</strong> Developed critical corporate soft skills, customer negotiation methodologies, advisory-oriented communication, and advanced interview readiness.</li>
            </ul>
            <div style="margin-top: 16px;">
                <span class="badge">BFSI Ready</span>
                <span class="badge">Banking Operations</span>
                <span class="badge">Insurance Underwriting</span>
                <span class="badge">Professional Soft Skills</span>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
    
    col_cert1, col_cert2 = st.columns(2, gap="large")
    
    with col_cert1:
        st.markdown(
            """
            <div class="content-card">
                <span class="timeline-date">Infosys Springboard</span>
                <h3 style="color: #F8FAFC; margin-top: 6px;">🎓 Professional Upskilling Track</h3>
                <p style="color: #CBD5E1; font-size: 15px; margin-top: 8px; line-height: 1.6;">
                    Completed interactive learning curriculum centered on foundational business concepts, modern work processes, and technology-driven operations.
                </p>
                <div style="margin-top: 16px;">
                    <span class="badge">Business Fundamentals</span>
                    <span class="badge">Infosys Verified</span>
                </div>
            </div>
            """, unsafe_allow_html=True
        )
        
    with col_cert2:
        st.markdown(
            """
            <div class="content-card">
                <span class="timeline-date">Professional Learning Track</span>
                <h3 style="color: #F8FAFC; margin-top: 6px;">📜 Spreadsheet Data Modeling</h3>
                <p style="color: #CBD5E1; font-size: 15px; margin-top: 8px; line-height: 1.6;">
                    Acquired skills in digital spreadsheets, data visualization dashboards, or introductory financial reporting workflows.
                </p>
                <div style="margin-top: 16px;">
                    <span class="badge">Analytical Tools</span>
                    <span class="badge">Digital Upskilling</span>
                </div>
            </div>
            """, unsafe_allow_html=True
        )

# --- TAB 6: EDUCATION ---
with tab_education:
    st.markdown("## 🎓 Academic Background")
    
    st.markdown(
        """
        <div class="content-card">
            <div style="display: flex; justify-content: space-between; align-items: start; flex-wrap: wrap;">
                <div>
                    <span class="timeline-date">Undergraduate Degree | 2024 - Present</span>
                    <h3 style="color: #F8FAFC; margin-top: 4px;">Bachelor of Business Administration (BBA)</h3>
                    <p style="font-size: 16px; font-weight: 500; color: #10B981; margin-top: 2px;">Specialization in Corporate Finance & Accounting Metrics</p>
                </div>
            </div>
            <hr style="border-color: #1E293B; margin: 20px 0;">
            <h4 style="color: #F8FAFC; margin-bottom: 12px; font-size: 16px; font-weight: 600;">📚 Core Academic Coursework:</h4>
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                <span class="badge">Financial Accounting</span>
                <span class="badge">Cost & Management Accounting</span>
                <span class="badge">Quantitative Methods for Finance</span>
                <span class="badge">Financial Management Theory</span>
                <span class="badge">Strategic Management Systems</span>
            </div>
        </div>
        """, unsafe_allow_html=True
    )

# --- TAB 7: CONTACT ---
with tab_contact:
    st.markdown("## 📬 Reach Out")
    st.write("If you're looking for an analytical, tech-enabled finance undergraduate for internship cycles or collaborative projects, let's talk.")
    st.write("")
    
    col_info, col_hire = st.columns([1, 1], gap="large")
    
    with col_info:
        st.markdown(
            """
            <div class="info-box">
                <small style="text-transform: uppercase; letter-spacing: 1.5px; font-family: 'JetBrains Mono'; font-weight: 500; color: #10B981;">Email Address</small>
                <h4 style="margin: 6px 0 0 0; font-weight: 600;"><a href="mailto:roshnirajesh2006@gmail.com" style="color: #F8FAFC; text-decoration: none;">roshnirajesh2006@gmail.com</a></h4>
            </div>
            
            <div class="info-box">
                <small style="text-transform: uppercase; letter-spacing: 1.5px; font-family: 'JetBrains Mono'; font-weight: 500; color: #10B981;">Professional LinkedIn</small>
                <h4 style="margin: 6px 0 0 0; font-weight: 600;"><a href="https://www.linkedin.com/" target="_blank" style="color: #F8FAFC; text-decoration: none;">Connect on LinkedIn ↗</a></h4>
            </div>
            
            <div class="info-box">
                <small style="text-transform: uppercase; letter-spacing: 1.5px; font-family: 'JetBrains Mono'; font-weight: 500; color: #10B981;">Source Repositories</small>
                <h4 style="margin: 6px 0 0 0; font-weight: 600;"><a href="https://github.com/" target="_blank" style="color: #F8FAFC; text-decoration: none;">Explore My Code on GitHub ↗</a></h4>
            </div>
            """, unsafe_allow_html=True
        )
        
    with col_hire:
        st.markdown(
            """
            <div class="content-card" style="text-align: center; padding: 50px 30px; display: flex; flex-direction: column; justify-content: center; height: 100%;">
                <h3 style="color: #10B981; margin-bottom: 12px;"><i class="fa-solid fa-paper-plane" style="margin-right: 10px;"></i>Active Candidate</h3>
                <p style="color: #94A3B8; margin-bottom: 30px; font-size: 15px;">
                    Currently seeking finance, analytical, or banking/insurance internship opportunities.
                </p>
                <div style="margin-top: 10px;">
                    <a href="mailto:roshnirajesh2006@gmail.com" style="background-color: #10B981; color: #080C14; padding: 14px 28px; border-radius: 8px; text-decoration: none; font-weight: 700; font-size: 15px; box-shadow: 0 4px 14px rgba(16, 185, 129, 0.3); transition: all 0.3s ease;">Send Direct Inquiry 📧</a>
                </div>
            </div>
            """, unsafe_allow_html=True
        )
