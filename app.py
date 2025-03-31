import streamlit as st
from logic import HomeInspector
import os
from pathlib import Path
import tempfile
import json

# Page config
st.set_page_config(
    page_title="Home Inspection AI",
    page_icon="🏠",
    layout="wide"
)

# Sidebar for API key input
with st.sidebar:
    st.title("Step 1: Configuration")
    st.markdown("Please enter your Gemini API key and the paths of the building standards folder and sample examples folder.")
    st.title("Configuration")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    standards_dir = st.text_input("Path of Building Standards folder", value="building_standards")
    examples_dir = st.text_input("Path of Sample Examples folder", value="examples")

    if st.button("Initialize Inspector"):
        if not api_key:
            st.error("Please enter a valid Gemini API key")
        else:
            try:
                inspector = HomeInspector(api_key, standards_dir, examples_dir)
                st.session_state.inspector = inspector
                st.session_state.processed = False
                st.success("Inspector initialized successfully!")
            except Exception as e:
                st.error(f"Error initializing inspector: {str(e)}")

# Main app
st.title("🏠 AI Home Inspection System")

st.markdown("Upload an image or a video of your home for a detailed inspection report")

if 'inspector' not in st.session_state:
    st.warning("Please initialize the inspector in the sidebar first")
    st.stop()

inspector = st.session_state.inspector

# Choose Image or Video
st.title("Step 2: Upload Media")
st.markdown("Upload an image or a video of your home for a detailed inspection report")
choice = st.radio("Choose media type:", ("Image", "Video"))

# File upload for multiple images
if choice == "Image":
    uploaded_files = st.file_uploader("Upload images of your home", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
else:
    uploaded_files = st.file_uploader("Upload a video of your home", type=["mp4", "mov", "avi"])

if uploaded_files and not st.session_state.get("processed", False):
    with st.spinner("Processing media..."):
        try:
            temp_dir = tempfile.mkdtemp()

            # Handle multiple images
            if choice == "Image":
                image_paths = []
                for uploaded_file in uploaded_files:
                    image_path = os.path.join(temp_dir, uploaded_file.name)
                    with open(image_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    image_paths.append(image_path)
                
                inspector.upload_user_media(image_paths)
            
            # Process video (single file)
            elif choice == "Video" and uploaded_files is not None:
                media_path = os.path.join(temp_dir, uploaded_files.name)
                with open(media_path, "wb") as f:
                    f.write(uploaded_files.getbuffer())
                
                inspector.process_video(media_path)
            
            st.session_state.processed = True
            st.success("Media processed successfully!")
        except Exception as e:
            st.error(f"Error processing media: {str(e)}")


# Generate Report
if st.session_state.get("processed", False):
    if st.button("Generate Inspection Report"):
        with st.spinner("Generating report (this may take a few minutes)..."):
            try:
                report = inspector.generate_report()
                st.session_state.report = report
                
                with open("inspection_report.json", "w") as f:
                    json.dump(report, f, indent=4)
                
                st.session_state.report_ready = True
                st.success("Report generated successfully!")
            except Exception as e:
                st.error(f"Error generating report: {str(e)}")

# Display report
if st.session_state.get("report_ready", False):
    report = st.session_state.report
    st.header("Inspection Report")

    with st.expander("Executive Summary", expanded=True):
        st.subheader("Overall Condition")
        st.write(report['executiveSummary']['overallCondition'])
        
        st.subheader("Critical Issues")
        for issue in report['executiveSummary']['criticalIssues']:
            st.error(f"⚠️ {issue}")
            
        st.subheader("Recommended Actions")
        for action in report['executiveSummary']['recommendedActions']:
            st.info(f"🔧 {action}")

    st.header("Detailed Inspection Findings")
    for finding in report['detailedInspection']:
        with st.expander(f"{finding['area']} - {finding['condition']}", expanded=False):
            cols = st.columns([1, 3])
            
            if finding.get('mediaReference') and finding['mediaReference'].startswith('frame_'):
                frame_path = os.path.join("extracted_frames", finding['mediaReference'])
                if os.path.exists(frame_path):
                    cols[0].image(frame_path, caption=f"Frame at {finding.get('timestamp', 'N/A')}")
            
            with cols[1]:
                st.markdown(f"**Compliance Status:** `{finding['complianceStatus']}`")
                
                if finding.get('issuesFound'):
                    st.markdown("**Issues Found:**")
                    for issue in finding['issuesFound']:
                        st.markdown(f"- {issue}")
                
                if finding.get('referenceDoc') and finding.get('referenceSection'):
                    st.markdown(f"**Standard Reference:** {finding['referenceDoc']} - {finding['referenceSection']}")
                
                if finding.get('recommendation'):
                    st.markdown(f"**Recommendation:** {finding['recommendation']}")

    with st.expander("Maintenance Schedule", expanded=False):
        for schedule in report['maintenanceNotes']['maintenanceSchedule']:
            st.subheader(f"{schedule['frequency']} Tasks")
            for task in schedule['tasks']:
                st.markdown(f"- {task}")
        
        if report['maintenanceNotes'].get('costConsiderations'):
            st.subheader("Cost Considerations")
            for cost in report['maintenanceNotes']['costConsiderations']:
                st.markdown(f"- {cost}")
    
    st.download_button(
        label="Download Full Report",
        data=json.dumps(report, indent=4),
        file_name="home_inspection_report.json",
        mime="application/json"
    )
