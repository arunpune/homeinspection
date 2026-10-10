# 🏠 AI Home Inspection System

> **Automated residential property inspections powered by AI and building standards.**

Transform your home inspection process with intelligent visual analysis. Upload photos or videos of your property and receive a comprehensive, standards-based inspection report in minutes—without requiring a professional on-site visit.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Getting Started](#getting-started)
- [Detailed Usage Walkthrough](#detailed-usage-walkthrough)
- [Understanding the Inspection Report](#understanding-the-inspection-report)
- [Project Structure](#project-structure)
- [Configuration Options](#configuration-options)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [License & Disclaimer](#license--disclaimer)

---

## 🎯 Overview

The **AI Home Inspection System** is a cutting-edge web application that combines:

- **Visual Analysis**: Upload photos and videos of your home
- **AI-Powered Evaluation**: Google Gemini analyzes media against building standards
- **Standards Compliance**: Checks compliance with Australian building codes and housing standards
- **Structured Reports**: Generates detailed JSON reports with findings, recommendations, and maintenance schedules

This system is ideal for:
- **Homeowners** conducting self-assessments
- **Real estate professionals** performing pre-sale inspections
- **Property managers** maintaining rental properties
- **Building inspectors** augmenting their expertise with AI analysis
- **Insurance companies** assessing property conditions

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| **Multi-Format Support** | Analyze multiple images or single video files (MP4, MOV, AVI) |
| **Automated Frame Extraction** | Automatically extracts key frames from videos (every 5 seconds) |
| **Standards-Based Analysis** | Evaluates properties against official Australian building codes and housing design standards |
| **Executive Summary** | Quick overview of overall condition and critical issues |
| **Detailed Findings** | Room-by-room or area-by-area inspection results with specific issues |
| **Compliance Status** | Clear indicators of code compliance and violations |
| **Maintenance Schedule** | Prioritized maintenance tasks (immediate, monthly, quarterly, annual) |
| **Cost Analysis** | Estimated cost considerations for required repairs |
| **Reference Documentation** | Links findings back to specific building code sections |
| **Export Reports** | Download complete reports as JSON for archival or further processing |
| **Web Interface** | User-friendly Streamlit UI—no CLI required |

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.8+ |
| **Web Framework** | Streamlit |
| **AI Engine** | Google Generative AI (Gemini 1.5 Flash) |
| **Computer Vision** | OpenCV (opencv-python-headless) |
| **Data Processing** | NumPy, Pillow, Pandas |
| **Model Optimization** | Google Gemini Prompt Caching |
| **Standards Database** | PDF documents (ABCB, NCC, Livable Housing Design) |

---

## 💻 System Requirements

Before you begin, ensure you have:

- **Python**: Version 3.8 or higher
- **Virtual Environment Tool**: `venv` (built into Python) or `conda`
- **Disk Space**: ~2 GB for dependencies and datasets
- **Internet Connection**: Required for Google Gemini API calls
- **Google Cloud Account**: Free tier available; requires an API key
- **Operating System**: macOS, Linux, or Windows

Optional but recommended:
- **Git**: For cloning the repository
- **Visual Studio Code** or similar IDE for development

---

## 📦 Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/arunpune/homeinspection.git
cd homeinspection
```

### Step 2: Create a Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

You should see `(.venv)` prefix in your terminal, indicating the virtual environment is active.

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This installs:
- `streamlit` — web application framework
- `google-generativeai` — Google Gemini API client
- `opencv-python-headless` — video processing
- `numpy`, `pillow`, `pandas` — data processing libraries
- And all supporting dependencies

**Expected installation time**: 3–5 minutes on a standard connection.

### Step 4: Obtain a Google Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click **"Create API Key in new project"**
3. Copy your API key to a safe location (you'll need it to run the app)
4. Note: Free tier quotas apply; see [pricing details](https://ai.google.dev/pricing)

### Step 5: Verify Installation

```bash
streamlit --version
python -c "import google.generativeai; print('Google Generative AI installed successfully')"
```

Both commands should run without errors.

---

## 🚀 Getting Started

### Quick Start (5 minutes)

```bash
# Ensure virtual environment is activated
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows

# Run the app
streamlit run app.py
```

Your browser will automatically open to `http://localhost:8501`. If it doesn't, manually navigate to that URL.

---

## 📖 Detailed Usage Walkthrough

### Phase 1: Configuration (Sidebar Setup)

When the app opens, you'll see a **Configuration** panel on the left sidebar.

#### 1.1 Enter Your Gemini API Key

- **Field**: "Enter Gemini API Key"
- **Type**: Password input (masked for security)
- **Action**: Paste your API key from Google AI Studio
- **Note**: This is required; the app will not proceed without it

```
Example (DO NOT share your real key):
AIzaSyA... (your actual key will be much longer)
```

#### 1.2 Specify Building Standards Folder

- **Field**: "Path of Building Standards folder"
- **Default**: `building_standards`
- **Description**: Directory containing PDF documents of building codes and standards
- **Example Paths**:
  - Relative: `Datasets/building_standards` (if running from repo root)
  - Absolute: `/home/user/homeinspection/Datasets/building_standards` (macOS/Linux)
  - Absolute: `C:\Users\user\homeinspection\Datasets\building_standards` (Windows)

**What's inside:**
- `Livable-Housing-Design-Standard-2022-1.3.pdf` — Design accessibility standards
- `abcb-housing-provisions-2022-*.pdf` (parts 1–3) — Detailed building code requirements
- `ncc2022-volume-two-20230501b.pdf` — National Construction Code

#### 1.3 Specify Sample Examples Folder

- **Field**: "Path of Sample Examples folder"
- **Default**: `examples`
- **Description**: Directory with subdirectories `example1` and `example2` containing sample reference documents
- **Purpose**: Helps the AI model learn the expected inspection format by example
- **Example Paths**:
  - Relative: `Datasets/examples`
  - Absolute: `/home/user/homeinspection/Datasets/examples`

#### 1.4 Initialize the Inspector

- **Button**: "Initialize Inspector"
- **Action**: Uploads standards and examples to Google Gemini's servers and creates a cached content session
- **Duration**: 30–60 seconds (one-time per session)
- **Success Message**: Green checkmark with "Inspector initialized successfully!"
- **Error Handling**: Red error message if paths are invalid or API key is incorrect

### Phase 2: Media Upload

Once the inspector is initialized, the main panel appears.

#### 2.1 Choose Media Type

- **Radio Buttons**: "Image" or "Video"
- **Default**: "Image"
- **Purpose**: Tells the app which file types to expect and how to process them

#### 2.2 Upload Image(s)

**If you selected "Image":**
- **Accepted Formats**: JPG, JPEG, PNG
- **Multiple Files**: Yes, you can upload multiple images at once
- **Recommended**: 5–15 high-quality photos covering all rooms and exterior areas
- **Action**: Click "Browse files" or drag and drop

**Best Practices:**
- Ensure good lighting (natural light preferred)
- Include wide shots (full room views) and close-ups (potential issues)
- Capture condition of walls, ceilings, floors, fixtures, and systems
- Include timestamps (EXIF data) if possible

#### 2.3 Upload Video

**If you selected "Video":**
- **Accepted Formats**: MP4, MOV, AVI
- **Multiple Files**: No, single video only
- **Duration**: Typically 5–15 minutes (walkthrough tour)
- **Resolution**: 1080p or higher recommended
- **Action**: Click "Browse files"

**Best Practices:**
- Record a steady walkthrough of the property
- Include narration of areas and issues being filmed
- Avoid rapid camera movement; pan slowly
- Ensure adequate lighting throughout

**What Happens:**
- The app extracts frames every 5 seconds automatically
- Extracted frames are saved in the `extracted_frames/` directory
- Frames are sent to Gemini for analysis

#### 2.4 Processing Confirmation

After upload completes:
- **Status**: Green checkmark "Media processed successfully!"
- **Next Step**: Click "Generate Inspection Report" button

---

### Phase 3: Report Generation

#### 3.1 Generate Report

- **Button**: "Generate Inspection Report"
- **Duration**: 2–5 minutes (depending on media volume and Gemini API response time)
- **Status**: Blue spinner with "Generating report (this may take a few minutes)..."
- **Success**: Green checkmark "Report generated successfully!"

**Behind the Scenes:**
1. The AI model receives the uploaded media and all building standards
2. Gemini analyzes each image/frame against the standards
3. A JSON report is generated following a strict schema
4. The report is displayed in the UI and saved to `inspection_report.json`

#### 3.2 View the Inspection Report

Once generated, the report appears with several sections:

##### Executive Summary (Expanded by Default)

**Overall Condition:**
- Text description: "Poor", "Fair", "Good", "Excellent"
- Example: "The property shows signs of age and deferred maintenance, particularly in plumbing and exterior finishes."

**Critical Issues:**
- High-priority items in red (⚠️)
- Example: "Foundation cracks exceeding 3mm width"
- These require immediate attention

**Recommended Actions:**
- Action items in blue info boxes (🔧)
- Example: "Schedule immediate repair of roof leaks in attic"
- Prioritized list of next steps

##### Detailed Inspection Findings

Each finding is collapsible and includes:

**Header Format:**
`{Area} - {Condition}`

Example: `Kitchen - Fair`

**When Clicked, Shows:**

- **Media Reference**: Frame from video (if applicable) with timestamp
  - Displayed on the left side as a thumbnail
  
- **Compliance Status**:
  - ✅ Compliant
  - ⚠️ Non-compliant
  - 🔄 Partial compliance
  
- **Issues Found** (bulleted list):
  - "Cabinet hardware shows corrosion"
  - "Countertop caulking missing in corners"
  
- **Standard Reference**:
  - Links to specific building code sections
  - Example: "NCC 2022 Volume Two - Part 3.5.2"
  
- **Recommendation**:
  - Specific action to address the issue
  - Example: "Re-caulk all seams with waterproof silicone; replace corroded hardware"

**Typical Areas Covered:**
- Kitchen, Bathrooms, Bedrooms
- Living Areas, Hallways
- Roof, Exterior Walls, Foundation
- HVAC, Electrical, Plumbing
- Flooring, Windows, Doors
- Structural Elements

##### Maintenance Schedule (Collapsed by Default)

Organized by frequency:

**Immediate Tasks** (Next 7 days):
- Address critical safety issues
- Example: "Repair loose electrical outlet"

**Monthly Tasks:**
- Routine inspection activities
- Example: "Inspect basement for moisture"

**Quarterly Tasks:**
- Seasonal maintenance
- Example: "Clean gutters and downspouts"

**Annual Tasks:**
- Yearly upkeep
- Example: "Test HVAC systems"

**Cost Considerations:**
- Rough estimates for repairs
- Example: "$200–500 for gutter cleaning"
- "Cost considerations" section if repair budgets are mentioned

#### 3.3 Download Full Report

- **Button**: "Download Full Report"
- **Format**: JSON file named `home_inspection_report_{timestamp}.json`
- **Contents**: Complete structured report with all findings
- **Use Cases**:
  - Archive in home maintenance records
  - Share with contractors for quotes
  - Submit to insurance companies
  - Import into property management software

---

## 📊 Understanding the Inspection Report

### Report JSON Structure

The generated report follows this schema:

```json
{
  "executiveSummary": {
    "overallCondition": "string",
    "criticalIssues": ["string array"],
    "recommendedActions": ["string array"]
  },
  "detailedInspection": [
    {
      "area": "string",
      "mediaReference": "string (frame_timestamp.jpg)",
      "timestamp": "string",
      "condition": "string (Poor/Fair/Good/Excellent)",
      "complianceStatus": "string",
      "issuesFound": ["string array"],
      "referenceDoc": "string (e.g., NCC 2022)",
      "referenceSection": "string",
      "recommendation": "string"
    }
  ],
  "maintenanceNotes": {
    "recurringIssues": ["string array"],
    "preventiveRecommendations": ["string array"],
    "maintenanceSchedule": [
      {
        "frequency": "string",
        "tasks": ["string array"]
      }
    ],
    "costConsiderations": ["string array"]
  }
}
```

### Interpreting Compliance Status

- **Compliant**: Meets all applicable building codes and standards
- **Non-compliant**: Violates one or more building code requirements (may require permits to fix)
- **Partial Compliance**: Meets some but not all requirements (review details for specifics)

### Understanding Cost Tiers

- **Under $500**: Minor repairs (caulking, hardware replacement)
- **$500–2,000**: Moderate repairs (fixture replacement, small system repairs)
- **$2,000–10,000**: Major repairs (structural, major system overhaul)
- **$10,000+**: Extensive work (foundation repair, full HVAC replacement)

---

## 📁 Project Structure

```
homeinspection/
├── README.md                           # This file
├── app.py                              # Streamlit web app (main entry point)
├── logic.py                            # Core inspection logic & Gemini integration
├── requirements.txt                    # Python dependencies
├── requirements1.txt                   # Alternate dependency list
├── inspection_report.json              # Example generated report
│
├── Datasets/                           # Reference data and test media
│   ├── building_standards/
│   │   ├── Livable-Housing-Design-Standard-2022-1.3.pdf
│   │   ├── abcb-housing-provisions-2022-20230501b_p1.pdf
│   │   ├── abcb-housing-provisions-2022-20230501b_p2.pdf
│   │   ├── abcb-housing-provisions-2022-20230501b_p3.pdf
│   │   └── ncc2022-volume-two-20230501b.pdf
│   │
│   ├── examples/
│   │   ├── example1/                  # Sample reference materials
│   │   └── example2/                  # Sample reference materials
│   │
│   └── user_data/                     # Test images and video for demo
│       ├── IMG_4436 Large.jpeg
│       ├── IMG_4438 Large.jpeg
│       ├── ...
│       └── home_inspection.mp4
│
├── extracted_frames/                  # Auto-generated during video processing
│   ├── frame_0.jpg
│   ├── frame_5.jpg
│   └── frame_10.jpg
│
├── .devcontainer/                     # Docker dev environment config
│
└── .github/                           # GitHub workflows and configuration
```

### Key Files Explained

| File | Purpose |
|------|---------|
| `app.py` | Streamlit UI; handles user input, displays reports |
| `logic.py` | `HomeInspector` class; loads standards, uploads media, generates reports |
| `requirements.txt` | All Python packages needed (main list) |
| `Datasets/building_standards/` | PDF reference documents for Gemini model |
| `Datasets/user_data/` | Sample media files for testing |
| `extracted_frames/` | Generated during app runtime; contains video frames |

---

## ⚙️ Configuration Options

### Environment Variables (Optional)

You can set environment variables to avoid entering credentials each time:

**Create a `.env` file in the repository root:**

```env
GEMINI_API_KEY=your_actual_api_key_here
STANDARDS_DIR=Datasets/building_standards
EXAMPLES_DIR=Datasets/examples
```

**Then modify `app.py` to use:**

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "")
standards_dir = os.getenv("STANDARDS_DIR", "building_standards")
examples_dir = os.getenv("EXAMPLES_DIR", "examples")
```

### Customizing Building Standards

**To use different standards documents:**

1. Create a new folder: `Datasets/my_standards/`
2. Add your PDF documents (e.g., local building codes, custom checklists)
3. In the app sidebar, enter the path: `Datasets/my_standards`
4. Re-initialize the inspector

**Supported File Types:** `.pdf`, `.txt`, `.doc`, `.docx`, `.jpg`, `.jpeg`, `.png`

### Adjusting Model Parameters

Edit `logic.py` to customize Gemini behavior:

```python
generation_config = {
    "temperature": 0.1,           # Lower = more deterministic
    "max_output_tokens": 8192,    # Max response length
    "response_mime_type": "application/json",
}
```

**Temperature tuning:**
- `0.0–0.3`: More consistent, deterministic results
- `0.5–0.7`: Balanced creativity and consistency
- `0.8–1.0`: More creative, varied responses

---

## 🔧 Troubleshooting

### Issue: "Please initialize the inspector in the sidebar first"

**Cause:** Inspector wasn't successfully initialized.

**Solution:**
1. Check that your API key is correct (copy-paste from Google AI Studio)
2. Verify internet connectivity
3. Ensure `Datasets/building_standards/` and `Datasets/examples/` paths are correct
4. Check Streamlit console for error messages
5. Try re-entering credentials and clicking "Initialize Inspector" again

### Issue: "Could not open video file"

**Cause:** Video format not supported or file corrupted.

**Solution:**
1. Verify file is actually an MP4, MOV, or AVI file
2. Try re-encoding with FFmpeg:
   ```bash
   ffmpeg -i input.mov -c:v libx264 -preset medium -crf 23 output.mp4
   ```
3. Ensure video is not larger than 500 MB

### Issue: "Error loading standard [filename]"

**Cause:** PDF file is corrupted or unsupported format.

**Solution:**
1. Verify PDF is not password-protected
2. Try opening the PDF in a reader to confirm it's valid
3. Consider re-downloading or converting the document
4. Remove problematic files and reload

### Issue: Streamlit app crashes or is slow

**Cause:** Heavy media or insufficient system resources.

**Solution:**
1. Reduce image resolution before uploading (target: 1920×1440 or smaller)
2. Limit video to 10 minutes or less
3. Close other applications to free RAM
4. Increase Streamlit's cache timeout:
   ```bash
   streamlit run app.py --client.caching.maxMessageSize=200
   ```

### Issue: "Quota exceeded" from Google Gemini API

**Cause:** Exceeded free tier request limits.

**Solution:**
1. Upgrade your Google Cloud account to a paid plan
2. Set up billing: https://console.cloud.google.com/billing
3. Wait for quota to reset (typically daily or monthly)
4. Use smaller files or fewer consecutive requests

### Issue: Permission denied when accessing `Datasets/` folder

**Cause:** File permissions issue on Windows or Unix systems.

**Solution:**
1. **Windows**: Run command prompt as Administrator
2. **macOS/Linux**: 
   ```bash
   chmod -R 755 Datasets/
   ```

---

## 🔮 Future Enhancements

### Short Term (Next Release)

- [ ] **Batch Processing**: Upload and inspect multiple homes in sequence
- [ ] **PDF Export**: Generate reports in PDF format for printing
- [ ] **Image Comparison**: Before/after image pairs for repairs
- [ ] **Custom Checklists**: User-defined inspection criteria
- [ ] **Multi-language Support**: Reports in Spanish, French, etc.

### Medium Term

- [ ] **Database Backend**: Store reports in PostgreSQL or MongoDB
- [ ] **User Accounts**: Save inspection history and profiles
- [ ] **Cost Estimation**: Integration with contractor pricing databases
- [ ] **Computer Vision**: Local image processing for faster pre-analysis
- [ ] **Mobile App**: React Native version for on-site inspections

### Long Term

- [ ] **Machine Learning**: Train custom models on historical inspection data
- [ ] **AR Visualization**: Augmented reality overlay of issues on live video
- [ ] **Marketplace Integration**: Connect inspectors with contractors
- [ ] **Regulatory Compliance**: Support for multiple jurisdictions and building codes
- [ ] **Predictive Maintenance**: AI-powered failure prediction based on property age/condition

---

## 📝 License & Disclaimer

### Usage Disclaimer

**This tool is for informational and reference purposes only.** It does not replace:
- Professional home inspections by licensed inspectors
- Structural engineering assessments
- Specialized system inspections (electrical, plumbing, HVAC)
- Legal or compliance reviews by qualified professionals

**Limitations:**
- AI analysis may miss subtle defects visible only in person
- Photo quality, angle, and lighting affect accuracy
- This tool cannot diagnose hidden structural or system issues
- Always consult licensed professionals for critical repairs

### Data Privacy

- Your media files are uploaded to Google Gemini's servers
- Google may retain metadata per their privacy policy
- API key should never be committed to version control
- Consider masking personal information in photos before upload

### Liability

The developers assume no liability for:
- Inaccurate inspections or missed issues
- Financial losses from incomplete assessments
- Injuries or property damage resulting from reliance on this tool
- Unauthorized use of your API key or personal data

---

## 🤝 Contributing

Found a bug or have a feature request?

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-idea`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to your fork: `git push origin feature/your-idea`
5. Open a Pull Request

---

## 📞 Support & Feedback

- **Issues**: Report bugs on [GitHub Issues](https://github.com/arunpune/homeinspection/issues)
- **Discussions**: Share ideas on [GitHub Discussions](https://github.com/arunpune/homeinspection/discussions)
- **Email**: Contact the maintainer directly

---

## 🎓 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Generative AI API Guide](https://ai.google.dev/docs)
- [OpenCV Video Processing](https://docs.opencv.org/master/index.html)
- [Australian Building Codes](https://www.building.gov.au/)
- [National Construction Code](https://www.ncc.abcb.gov.au/)

---

**Happy inspecting! 🔍🏠**

*Last updated: October 2026*
