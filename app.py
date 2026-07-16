import streamlit as st
from scheme_logic import check_eligibility
from helper import load_scheme_data


st.set_page_config(
    page_title="Government Scheme Finder",
    page_icon="🏛",
    layout="wide"
)

st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

h1{
    color:#0B5394;
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:12px;
    background:#0B5394;
    color:white;
    font-size:18px;
    border:none;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1565C0;
}

div[data-baseweb="select"]{
    border-radius:10px;
}

input{
    border-radius:10px;
}

.scheme-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.1);
    margin-top:15px;
}

.header-box{
    background:linear-gradient(90deg,#0B5394,#1976D2);
    color:white;
    padding:20px;
    border-radius:15px;
    margin-bottom:25px;
}

</style>
""", unsafe_allow_html=True)

   


st.markdown("""
<div class="header-box">

<h1>🏛 Government Scheme Finder</h1>

<p style="font-size:18px;">
Find the government schemes that match your profile.
</p>

</div>
""", unsafe_allow_html=True)

with st.sidebar:

    st.title("📌 Quick Menu")

    st.info("Fill your details and click Find My Schemes.")

    st.markdown("---")

    st.write("### Features")

    st.write("✅ Eligibility Checker")

    st.write("✅ Government Schemes")

    st.write("✅ AI Recommendation (Coming Soon)")

    st.write("✅ PDF Report (Coming Soon)")

st.divider()


with st.container():
    st.subheader("👤 Personal Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=0, max_value=100, step=1)

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    state = st.selectbox(
        "State",
        [
            "Chhattisgarh",
            "Madhya Pradesh",
            "Maharashtra",
            "Delhi",
            "Other"
        ]
    )

    occupation = st.selectbox(
        "Occupation",
        [
            "Student",
            "Farmer",
            "Business",
            "Employee",
            "Unemployed"
        ]
    )

with col2:
    income = st.number_input(
        "Annual Income (₹)",
        min_value=0,
        step=1000
    )

    category = st.selectbox(
        "Category",
        [
            "General",
            "OBC",
            "SC",
            "ST",
            "EWS"
        ]
    )

    student = st.radio(
        "Are you a Student?",
        ["Yes", "No"]
    )

    farmer = st.radio(
        "Are you a Farmer?",
        ["Yes", "No"]
    )

st.divider()


if st.button("🔍 Find My Schemes", use_container_width=True):

    user_data = {
    "age": age,
    "occupation": occupation,
    "income": income,
    "student": student,
    "farmer": farmer
}
    
    schemes = load_scheme_data()

    results = check_eligibility(user_data, schemes)

    st.subheader("📋 Eligible Schemes")

    if len(results) == 0:
        st.warning("No matching schemes found.")
    else:
     st.subheader("🎯 Schemes You Can Apply For")

    for scheme in results:

        with st.container(border=True):

            col1, col2 = st.columns([3,1])

            with col1:

                st.markdown(f"##  {scheme['SchemeName']}")

                st.write(f"** Benefits:** {scheme['Benefits']}")

                st.write(f"** Documents:** {scheme['Documents']}")

            with col2:

                st.link_button(
                    "Apply",
                    scheme["OfficialLink"],
                    use_container_width=True
                )

    st.write("### Your Details")

    st.write(f"Age : {age}")
    st.write(f"Gender : {gender}")
    st.write(f"State : {state}")
    st.write(f"Occupation : {occupation}")
    st.write(f"Income : ₹{income:,.0f}")
    st.write(f"Category : {category}")
    st.write(f"Student : {student}")
    st.write(f"Farmer : {farmer}")
    schemes = load_scheme_data()

    st.write("### Available Schemes")

    st.dataframe(schemes)

    st.markdown("---")
    st.caption("Developed using Python • Streamlit • Pandas")