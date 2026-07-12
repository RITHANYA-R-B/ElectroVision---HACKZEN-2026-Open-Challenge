import streamlit as st
from PIL import Image
import json
import os
from detect import detect

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="ElectroVision",
    page_icon="🔌",
    layout="wide"
)

# ==========================================
# FUNCTION TO LOAD JSON FILES
# ==========================================

def load_component(component):

    filename = component.lower().replace(" ", "_") + ".json"

    if component == "Crystal Oscillator":
        filename = "crystal.json"

    filepath = os.path.join("tutor", filename)

    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            return json.load(file)

    return None


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🔌 ElectroVision")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📖 About Project",
        "ℹ Version"
    ]
)

st.sidebar.markdown("---")
st.sidebar.success("Version 1.0")

# ==========================================
# ABOUT PAGE
# ==========================================

if page == "📖 About Project":

    st.title("📖 About Project")

    st.markdown("""
## 🔌 ElectroVision

ElectroVision is an AI-powered **Component Detector and Interactive Tutor**.

It uses Computer Vision to identify electronic components and provides educational information for each detected component.

### 🚀 Features

- 📷 Component Image Upload
- 🤖 AI Component Detection
- 📚 Interactive AI Tutor
- 📊 Detection Summary
- 📄 Analysis Report
- 🎯 Beginner-friendly learning interface

### 🎯 Objective

To simplify Electronic Component understanding by combining AI-based detection with educational content.
""")

    st.stop()

# ==========================================
# VERSION PAGE
# ==========================================

if page == "ℹ Version":

    st.title("ℹ Version")

    st.info("""
ElectroVision

Version : 1.0

Developed for Computer Vision Open Challenge Hackathon 2026
""")

    st.stop()

# ==========================================
# HOME PAGE
# ==========================================

st.title("🔌 ElectroVision")

st.subheader("AI Electronic Component Analyzer & Interactive Tutor")

st.write("""
Upload an image to:

- Detect electronic components
- Learn about detected components
- View AI analysis
- Generate a report
""")

uploaded_file = st.file_uploader(
    "📤 Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    temp_path = "temp_image.jpg"
    image.save(temp_path)
    
    processed_image, detected_components = detect(temp_path)
    
    col1, col2 = st.columns([2, 1])

    with col1:

        st.subheader("📷 Uploaded Image")

        st.image(
            image,
            use_container_width=True
        )

    with col2:

        st.subheader("📊 Detection Summary")

        total_components = sum(item["Count"] for item in detected_components)

        total_classes = len(detected_components)

        confidence_sum = sum(item["Confidence"] for item in detected_components)

        average_confidence = round(
            confidence_sum / total_classes,
            2
        ) if total_classes else 0

        st.metric("Total Components", total_components)
        st.metric("Detected Classes", total_classes)
        st.metric("Average Confidence", f"{average_confidence}%")

        average_confidence = 0

        if total_components > 0:
            average_confidence = round(confidence_sum / total_components, 2)

        st.metric("Total Components", total_components)

        st.metric("Detected Classes", total_classes)

        st.metric("Average Confidence", f"{average_confidence}%")

    st.divider()

    # ==========================================
    # DETECTED COMPONENTS
    # ==========================================

    st.subheader("🔍 Detected Components")

    st.table(detected_components)

    st.divider()

    # ==========================================
    # AI TUTOR
    # ==========================================

    st.subheader("📚 AI Tutor")

    component_names = sorted(
        {item["Component"] for item in detected_components}
    )

    component = st.selectbox(
        "Select a Detected Component",
        component_names
    )

    data = load_component(component)

    if data:

        st.subheader("📘 Component Information")

        with st.expander("🟦 Name", expanded=True):
            st.write(data["name"])

        with st.expander("🟩 Function", expanded=True):
            st.write(data["function"])

        with st.expander("📋 Applications"):
            for item in data["applications"]:
                st.write("• " + item)

        with st.expander("⚡ Common Values"):
            for value in data["common_values"]:
                st.write("• " + value)

        with st.expander("⚠️ Failure Symptoms"):
            for item in data["failure_symptoms"]:
                st.write("• " + item)

        with st.expander("💡 Interesting Fact", expanded=True):
            st.success(data["interesting_fact"])

    else:

        st.warning(
            f"No information available for **{component}**."
        )

    st.divider()

        # ==========================================
    # DETECTION RESULT
    # ==========================================

    st.subheader("🖼️ Detection Result")

    st.image(
        processed_image,
        caption="Detected Components",
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # ANALYSIS REPORT
    # ==========================================

    st.subheader("📄 Analysis Report")

    # Create detected component list
    component_list = ""

    for item in detected_components:
        component_list += (
            f"• {item['Component']} "
            f"(Count: {item['Count']}, "
            f"Confidence: {item['Confidence']}%)\n"
        )

    report = f"""
    ElectroVision Analysis Report

    --------------------------------------------

    Detected Components
    -------------------
    {component_list}

    Detection Summary
    -----------------
    Total Components : {total_components}

    Detected Classes : {total_classes}

    Average Confidence : {average_confidence}%

    Note:
    This report is generated using Computer Vision analysis.
    Electrical testing is recommended for complete verification.
    """

    st.text_area(
        "Generated Report",
        value=report,
        height=300
    )

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="PCB_Analysis_Report.txt",
        mime="text/plain"
    )

else:

    st.info("👆 Please upload an image to begin analysis.")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "🔌 ElectroVision v1.0 | AI Electronic Component Analyzer & Interactive Tutor | Computer Vision Open Challenge 2026"
)