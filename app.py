import json
import numpy as np
import streamlit as st
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CarCare AI | Smart Service Advisor",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM UI STYLING
# ============================================================

st.markdown("""
<style>

    /* ---------- MAIN APP ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 0%,
                rgba(59, 130, 246, 0.12),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 10%,
                rgba(14, 165, 233, 0.10),
                transparent 25%
            ),
            #080d18;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* ---------- SIDEBAR ---------- */

    [data-testid="stSidebar"] {
        background: #0b1220;
        border-right: 1px solid #1e293b;
    }


    /* ---------- HEADINGS ---------- */

    h1 {
        color: #f8fafc !important;
        font-weight: 800 !important;
        letter-spacing: -1px;
    }

    h2 {
        color: #f1f5f9 !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #e2e8f0 !important;
    }


    /* ---------- TEXT ---------- */

    p, label {
        color: #cbd5e1;
    }


    /* ---------- TEXT AREA ---------- */

    textarea {
        background-color: #111827 !important;
        color: #f8fafc !important;
        border: 1px solid #263244 !important;
        border-radius: 14px !important;
    }

    textarea:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 1px #3b82f6 !important;
    }


    /* ---------- INPUTS ---------- */

    input {
        background-color: #111827 !important;
        color: #f8fafc !important;
        border-radius: 10px !important;
    }


    /* ---------- BUTTON ---------- */

    .stButton > button {
        width: 100%;
        min-height: 50px;
        border-radius: 12px;
        border: 1px solid #3b82f6;
        background: linear-gradient(
            90deg,
            #2563eb,
            #4f46e5
        );
        color: white;
        font-weight: 750;
        font-size: 15px;
        transition: 0.2s;
    }

    .stButton > button:hover {
        border-color: #60a5fa;
        transform: translateY(-1px);
    }


    /* ---------- METRICS ---------- */

    [data-testid="stMetric"] {
        background: #111827;
        border: 1px solid #263244;
        border-radius: 15px;
        padding: 18px;
    }

    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
    }

    [data-testid="stMetricValue"] {
        color: #f8fafc !important;
    }


    /* ---------- ALERTS ---------- */

    [data-testid="stAlert"] {
        border-radius: 12px;
    }


    /* ---------- DIVIDER ---------- */

    hr {
        border-color: #1e293b;
    }


    /* ---------- EXPANDER ---------- */

    [data-testid="stExpander"] {
        border: 1px solid #263244;
        border-radius: 14px;
        background: #0d1422;
    }


    /* ---------- PROGRESS ---------- */

    [data-testid="stProgress"] > div > div > div > div {
        background: linear-gradient(
            90deg,
            #2563eb,
            #06b6d4
        );
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🚗 CarCare AI")

    st.caption(
        "Smart Car Service Recommendation System"
    )

    st.divider()

    st.markdown("### 🧠 Technology")

    st.write("• LangChain")
    st.write("• Groq LLM")
    st.write("• Fuzzy Logic")
    st.write("• Streamlit")

    st.divider()

    st.markdown("### 🔄 System Flow")

    st.write("1. 💬 User describes problem")
    st.write("2. 🧠 AI extracts information")
    st.write("3. 〰️ Fuzzy system evaluates inputs")
    st.write("4. 🔧 Service is recommended")

    st.divider()

    st.caption(
        "AI handles natural-language understanding, "
        "while Fuzzy Logic handles service priority."
    )


# ============================================================
# HEADER
# ============================================================

header_left, header_right = st.columns(
    [5, 1]
)

with header_left:

    st.markdown(
        "# 🚗 CarCare AI"
    )

    st.markdown(
        "### AI-Based Car Service Recommendation System"
    )

    st.caption(
        "Understand your car problem with AI and calculate "
        "service priority using Fuzzy Logic."
    )


with header_right:

    st.metric(
        "AI + Fuzzy",
        "ACTIVE"
    )


st.divider()


# ============================================================
# PROJECT OVERVIEW
# ============================================================

st.markdown("## ⚡ How CarCare AI Works")

flow1, flow2, flow3, flow4 = st.columns(4)


with flow1:

    with st.container(border=True):

        st.markdown("### 💬")

        st.markdown("**Natural Language**")

        st.caption(
            "Describe your car problem in your own words."
        )


with flow2:

    with st.container(border=True):

        st.markdown("### 🧠")

        st.markdown("**AI Extraction**")

        st.caption(
            "LangChain + Groq extracts useful car information."
        )


with flow3:

    with st.container(border=True):

        st.markdown("### 〰️")

        st.markdown("**Fuzzy Inference**")

        st.caption(
            "Membership functions and fuzzy rules calculate priority."
        )


with flow4:

    with st.container(border=True):

        st.markdown("### 🔧")

        st.markdown("**Recommendation**")

        st.caption(
            "The system recommends the required service."
        )


st.write("")


# ============================================================
# AI / LANGCHAIN
# ============================================================

def extract_car_data(user_text):

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0,
        api_key=st.secrets["GROQ_API_KEY"]
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            Extract car service information from the user's message.

            Return ONLY valid JSON with exactly these keys:

            car_age_years
            mileage_km
            severity
            problem

            Rules:

            - car_age_years = car age in years
            - mileage_km = mileage in kilometres
            - severity = number from 0 to 10
            - problem = main car problem
            - If a value is missing, use 0.
            """
        ),
        ("human", "{text}")
    ])

    response = llm.invoke(
        prompt.format_messages(
            text=user_text
        )
    )

    result = response.content.strip()

    result = result.replace(
        "```json",
        ""
    )

    result = result.replace(
        "```",
        ""
    )

    result = result.strip()

    return json.loads(result)


# ============================================================
# FUZZY LOGIC
# ============================================================

# ---------- INPUT VARIABLES ----------

age = ctrl.Antecedent(
    np.arange(0, 16, 1),
    "age"
)

mileage = ctrl.Antecedent(
    np.arange(0, 150001, 1000),
    "mileage"
)

severity = ctrl.Antecedent(
    np.arange(0, 11, 1),
    "severity"
)


# ---------- OUTPUT VARIABLE ----------

priority = ctrl.Consequent(
    np.arange(0, 101, 1),
    "priority"
)


# ============================================================
# MEMBERSHIP FUNCTIONS
# ============================================================

# ---------- CAR AGE ----------

age["new"] = fuzz.trimf(
    age.universe,
    [0, 0, 4]
)

age["medium"] = fuzz.trimf(
    age.universe,
    [2, 6, 10]
)

age["old"] = fuzz.trimf(
    age.universe,
    [7, 15, 15]
)


# ---------- MILEAGE ----------

mileage["low"] = fuzz.trimf(
    mileage.universe,
    [0, 0, 40000]
)

mileage["medium"] = fuzz.trimf(
    mileage.universe,
    [25000, 60000, 90000]
)

mileage["high"] = fuzz.trimf(
    mileage.universe,
    [70000, 150000, 150000]
)


# ---------- PROBLEM SEVERITY ----------

severity["low"] = fuzz.trimf(
    severity.universe,
    [0, 0, 4]
)

severity["medium"] = fuzz.trimf(
    severity.universe,
    [2, 5, 8]
)

severity["high"] = fuzz.trimf(
    severity.universe,
    [6, 10, 10]
)


# ---------- SERVICE PRIORITY ----------

priority["low"] = fuzz.trimf(
    priority.universe,
    [0, 0, 40]
)

priority["medium"] = fuzz.trimf(
    priority.universe,
    [25, 50, 75]
)

priority["high"] = fuzz.trimf(
    priority.universe,
    [60, 100, 100]
)


# ============================================================
# FUZZY RULES
# ============================================================

rules = [

    ctrl.Rule(
        age["new"] &
        mileage["low"] &
        severity["low"],
        priority["low"]
    ),

    ctrl.Rule(
        age["medium"] &
        mileage["medium"] &
        severity["medium"],
        priority["medium"]
    ),

    ctrl.Rule(
        age["old"] &
        mileage["high"] &
        severity["high"],
        priority["high"]
    ),

    ctrl.Rule(
        severity["high"],
        priority["high"]
    ),

    ctrl.Rule(
        age["old"] &
        mileage["high"],
        priority["high"]
    ),

    ctrl.Rule(
        severity["medium"] &
        (
            age["medium"] |
            mileage["medium"]
        ),
        priority["medium"]
    ),

    ctrl.Rule(
        severity["low"] &
        age["new"] &
        mileage["low"],
        priority["low"]
    )

]


fuzzy_system = ctrl.ControlSystem(
    rules
)


# ============================================================
# FUZZY CALCULATION
# ============================================================

def fuzzy_recommendation(
    car_age,
    km,
    sev,
    problem
):

    simulation = ctrl.ControlSystemSimulation(
        fuzzy_system
    )

    simulation.input["age"] = float(
        np.clip(
            car_age,
            0,
            15
        )
    )

    simulation.input["mileage"] = float(
        np.clip(
            km,
            0,
            150000
        )
    )

    simulation.input["severity"] = float(
        np.clip(
            sev,
            0,
            10
        )
    )

    # Fuzzy inference + defuzzification

    simulation.compute()

    score = float(
        simulation.output["priority"]
    )


    # ========================================================
    # SERVICE DETECTION
    # ========================================================

    problem_lower = problem.lower()

    services = []


    if (
        "ac" in problem_lower
        or
        "air condition" in problem_lower
        or
        "cooling" in problem_lower
    ):

        services.append(
            "AC Service"
        )


    if "oil" in problem_lower:

        services.append(
            "Oil Change"
        )


    if "brake" in problem_lower:

        services.append(
            "Brake Inspection"
        )


    if "engine" in problem_lower:

        services.append(
            "Engine Inspection"
        )


    if (
        "tyre" in problem_lower
        or
        "tire" in problem_lower
    ):

        services.append(
            "Tyre Inspection"
        )


    if not services:

        services.append(
            "General Service"
        )


    # ========================================================
    # PRIORITY LEVEL
    # ========================================================

    if score >= 70:

        level = "High"

    elif score >= 40:

        level = "Medium"

    else:

        level = "Low"


    return (
        score,
        level,
        services
    )


# ============================================================
# USER INPUT
# ============================================================

st.markdown("## 📝 Describe Your Car Problem")

st.caption(
    "Tell the AI what is happening with your car. "
    "You can write normally — no special format is required."
)


user_text = st.text_area(
    "Problem description",
    placeholder=(
        "Example: My car is 5 years old, "
        "has driven 50000 km and AC cooling is very low."
    ),
    height=130,
    label_visibility="collapsed"
)


st.write("")


# ============================================================
# CAR INFORMATION
# ============================================================

st.markdown("## 🚘 Car Information")

st.caption(
    "These values provide additional information for the fuzzy system."
)


col1, col2, col3 = st.columns(3)


with col1:

    car_age = st.number_input(
        "🚗 Car Age (Years)",
        min_value=0,
        max_value=15,
        value=5
    )


with col2:

    mileage = st.number_input(
        "🛣️ Mileage (KM)",
        min_value=0,
        max_value=150000,
        value=50000,
        step=1000
    )


with col3:

    severity_value = st.slider(
        "⚠️ Problem Severity",
        min_value=0,
        max_value=10,
        value=5
    )


st.write("")


# ============================================================
# ANALYZE BUTTON
# ============================================================

if st.button(
    "🔍 Analyze Car & Get Service Recommendation",
    use_container_width=True
):

    if not user_text.strip():

        st.warning(
            "⚠️ Please describe your car problem first."
        )

    else:

        try:

            # =================================================
            # AI EXTRACTION
            # =================================================

            with st.spinner(
                "🧠 AI is understanding your car problem..."
            ):

                data = extract_car_data(
                    user_text
                )


            extracted_age = float(
                data.get(
                    "car_age_years",
                    car_age
                ) or car_age
            )


            extracted_mileage = float(
                data.get(
                    "mileage_km",
                    mileage
                ) or mileage
            )


            extracted_severity = float(
                data.get(
                    "severity",
                    severity_value
                ) or severity_value
            )


            extracted_problem = data.get(
                "problem",
                user_text
            )


            # =================================================
            # AI RESULT
            # =================================================

            st.divider()

            st.markdown(
                "## 🧠 AI Analysis"
            )

            st.caption(
                "LangChain + Groq converted your natural-language "
                "description into structured information."
            )


            info1, info2, info3, info4 = st.columns(4)


            with info1:

                st.metric(
                    "🚗 Car Age",
                    f"{extracted_age:g} Years"
                )


            with info2:

                st.metric(
                    "🛣️ Mileage",
                    f"{extracted_mileage:,.0f} KM"
                )


            with info3:

                st.metric(
                    "⚠️ Severity",
                    f"{extracted_severity:g}/10"
                )


            with info4:

                st.metric(
                    "🔧 Problem",
                    extracted_problem
                )


            # =================================================
            # FUZZY INFERENCE
            # =================================================

            with st.spinner(
                "〰️ Fuzzy Logic is calculating service priority..."
            ):

                score, level, services = (
                    fuzzy_recommendation(
                        extracted_age,
                        extracted_mileage,
                        extracted_severity,
                        extracted_problem
                    )
                )


            # =================================================
            # FINAL RESULT
            # =================================================

            st.divider()

            st.markdown(
                "## 🎯 Service Recommendation"
            )


            result_col1, result_col2 = st.columns(
                [1, 1.7]
            )


            # -------------------------------------------------
            # SCORE CARD
            # -------------------------------------------------

            with result_col1:

                with st.container(border=True):

                    st.markdown(
                        "### 〰️ Fuzzy Priority"
                    )

                    st.metric(
                        "Service Priority Score",
                        f"{score:.1f}/100"
                    )


                    st.progress(
                        min(
                            max(score / 100, 0.0),
                            1.0
                        )
                    )


                    if level == "High":

                        st.error(
                            "🔴 HIGH PRIORITY"
                        )

                    elif level == "Medium":

                        st.warning(
                            "🟡 MEDIUM PRIORITY"
                        )

                    else:

                        st.success(
                            "🟢 LOW PRIORITY"
                        )


            # -------------------------------------------------
            # SERVICE CARD
            # -------------------------------------------------

            with result_col2:

                with st.container(border=True):

                    st.markdown(
                        "### 🔧 Recommended Service"
                    )

                    st.caption(
                        "Based on the detected car problem:"
                    )


                    for service in services:

                        st.success(
                            f"🔧 {service}"
                        )


                    st.info(
                        "The final recommendation combines "
                        "AI-based information extraction with "
                        "fuzzy inference."
                    )


            # =================================================
            # DECISION PIPELINE
            # =================================================

            st.write("")

            st.markdown(
                "### 🔄 Decision Pipeline"
            )


            pipe1, pipe2, pipe3, pipe4 = st.columns(4)


            with pipe1:

                with st.container(border=True):

                    st.markdown(
                        "### 1️⃣"
                    )

                    st.markdown(
                        "**User Input**"
                    )

                    st.caption(
                        "Natural-language problem"
                    )


            with pipe2:

                with st.container(border=True):

                    st.markdown(
                        "### 2️⃣"
                    )

                    st.markdown(
                        "**AI Extraction**"
                    )

                    st.caption(
                        "LLM extracts car details"
                    )


            with pipe3:

                with st.container(border=True):

                    st.markdown(
                        "### 3️⃣"
                    )

                    st.markdown(
                        "**Fuzzy Inference**"
                    )

                    st.caption(
                        "Rules calculate priority"
                    )


            with pipe4:

                with st.container(border=True):

                    st.markdown(
                        "### 4️⃣"
                    )

                    st.markdown(
                        "**Recommendation**"
                    )

                    st.caption(
                        "Service + priority"
                    )


        except Exception as e:

            st.error(
                f"❌ Error: {e}"
            )


# ============================================================
# FUZZY LOGIC EXPLANATION
# ============================================================

st.divider()

st.markdown(
    "## 🧠 Understand the Fuzzy Logic"
)

tab1, tab2 = st.tabs(
    [
        "📋 Fuzzy Rules",
        "📊 Membership Functions"
    ]
)


# ============================================================
# TAB 1 - RULES
# ============================================================

with tab1:

    st.markdown(
        "### Fuzzy Rules Used"
    )

    st.write(
        "1️⃣ **New car + Low mileage + Low severity → Low priority**"
    )

    st.write(
        "2️⃣ **Medium age + Medium mileage + Medium severity → Medium priority**"
    )

    st.write(
        "3️⃣ **Old car + High mileage + High severity → High priority**"
    )

    st.write(
        "4️⃣ **High problem severity → High priority**"
    )

    st.write(
        "5️⃣ **Old car + High mileage → High priority**"
    )

    st.write(
        "6️⃣ **Medium severity + Medium age/mileage → Medium priority**"
    )

    st.write(
        "7️⃣ **Low severity + New car + Low mileage → Low priority**"
    )


# ============================================================
# TAB 2 - MEMBERSHIP FUNCTIONS
# ============================================================

with tab2:

    st.markdown(
        "### Input Membership Categories"
    )


    membership1, membership2, membership3 = st.columns(3)


    with membership1:

        st.markdown(
            "#### 🚗 Car Age"
        )

        st.write(
            "• New"
        )

        st.write(
            "• Medium"
        )

        st.write(
            "• Old"
        )


    with membership2:

        st.markdown(
            "#### 🛣️ Mileage"
        )

        st.write(
            "• Low"
        )

        st.write(
            "• Medium"
        )

        st.write(
            "• High"
        )


    with membership3:

        st.markdown(
            "#### ⚠️ Severity"
        )

        st.write(
            "• Low"
        )

        st.write(
            "• Medium"
        )

        st.write(
            "• High"
        )


    st.divider()


    st.markdown(
        "### Output Membership"
    )

    st.write(
        "The fuzzy system produces a **Service Priority Score "
        "from 0 to 100**."
    )

    st.write(
        "🟢 Low Priority → 0–39"
    )

    st.write(
        "🟡 Medium Priority → 40–69"
    )

    st.write(
        "🔴 High Priority → 70–100"
    )


# ============================================================
# ABOUT PROJECT
# ============================================================

with st.expander(
    "ℹ️ About This Mini Project"
):

    st.markdown(
        """
        **AI-Based Car Service Recommendation System**

        This mini project combines two important AI concepts:

        **1. AI / LLM Component**

        LangChain and the Groq LLM understand a user's
        natural-language car problem and extract structured
        information such as car age, mileage, severity and
        the main problem.

        **2. Fuzzy Logic Component**

        The extracted information is passed into a genuine
        fuzzy inference system. Membership functions represent
        linguistic values such as New, Medium, Old, Low, Medium
        and High.

        Fuzzy rules are evaluated and the final service priority
        is obtained through fuzzy inference and defuzzification.

        **Final Output**

        The system provides:

        - Fuzzy service priority score
        - Priority level
        - Recommended car service
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🚗 CarCare AI • LangChain + Groq LLM + Fuzzy Logic • "
    "AI-Based Car Service Recommendation System"
)