# AI Home Inspection System

A Python-based Streamlit application that analyzes home photos and videos against building standards and manufacturer guidance, then produces a structured inspection report powered by Google Gemini. The project is designed for property inspections, condition assessments, and maintenance recommendations based on uploaded media and reference standards.

## What this project does

The app allows a user to:

- enter a Gemini API key in the sidebar,
- point to a folder of building standards and a folder of sample reference examples,
- upload multiple images or a single video of a property,
- extract frames from video footage when needed,
- send the media and standards to Gemini for evaluation,
- receive a structured JSON inspection report with:
  - executive summary,
  - detailed inspection findings by area,
  - compliance status,
  - issues found,
  - standard references,
  - recommendations,
  - maintenance schedule and cost considerations.

This is effectively a demo/prototype for AI-assisted residential inspection reporting.

## Stack

- Language: Python 3
- UI framework: Streamlit
- AI model: Google Generative AI (Gemini)
- Computer vision: OpenCV
- Data handling: JSON, file uploads, local temporary directories
- Standards dataset: PDF documents in `Datasets/building_standards`
- Example dataset: folders under `Datasets/examples`

Notable dependencies include:

- `streamlit`
- `google-generativeai`
- `opencv-python-headless`
- `numpy`
- `pillow`
- `pandas`

## Repository structure

```text
.
├── .devcontainer/                  # Dev container configuration
├── .github/                        # GitHub automation/configuration
├── .gitignore                     # Git ignore rules
├── Datasets/                       # inspection reference datasets
│   ├── building_standards/        # PDF standards and code documents
│   ├── examples/                  # sample reference examples
│   └── user_data/                 # sample or user-supplied media
├── extracted_frames/               # video frames generated during processing
├── app.py                          # Streamlit user interface
├── logic.py                        # core inspection logic and Gemini integration
├── inspection_report.json          # generated report output example
├── requirements.txt                # primary Python install list
├── requirements1.txt               # additional or duplicate dependency list
└── README.md                      # project overview (this file)
```

## How it fits together

The application is split into two main components:

- `app.py` handles the user interface and media upload workflow. It asks the user for their Gemini API key and paths to the standards/examples folders, then processes uploaded images or a video.
- `logic.py` is the engine behind the system. It configures the Gemini model, uploads standards and examples as documents, extracts frames from videos with OpenCV, uploads user media, and generates the inspection JSON result.

The overall flow is:

1. User enters API information in the Streamlit sidebar.
2. The app initializes a `HomeInspector` object.
3. The inspector loads standards and sample examples from the dataset folders.
4. The user uploads one or more images or a video.
5. Video files are decomposed into frames at 5-second intervals.
6. Gemini is asked to evaluate the uploaded media against the supplied standard documents.
7. The model returns a structured JSON report summarizing condition, issues, and recommendations.

## Key implementation details

### `app.py`

The Streamlit app includes:

- a sidebar configuration step,
- API key input,
- standards and examples folder input,
- media type choice (`Image` or `Video`),
- upload controls,
- report generation button,
- rendering of the generated JSON in the UI,
- download link for the final JSON report.

### `logic.py`

The main logic class is `HomeInspector`. It does the following:

- initializes the Gemini model using `genai.configure(api_key=...)`,
- loads building standards recursively from the configured folder,
- loads examples from `example1` and `example2` folders,
- creates a cached Gemini content object,
- uploads user media files,
- extracts frames from a user video,
- generates a detailed inspection report using a strict JSON schema.

It returns the report as a Python dictionary by parsing `response.text` with `json.loads(...)`.

## Dataset contents

The repository includes reference legal and technical documents under `Datasets/building_standards`, including PDFs such as:

- `Livable-Housing-Design-Standard-2022-1.3.pdf`
- `abcb-housing-provisions-2022-20230501b_p1.pdf`
- `abcb-housing-provisions-2022-20230501b_p2.pdf`
- `abcb-housing-provisions-2022-20230501b_p3.pdf`
- `ncc2022-volume-two-20230501b.pdf`

The `Datasets/examples` folder contains sample reference folders for example 1 and example 2, which are used to help ground the model to expected inspection outputs.

## How to run

1. Clone the repository.
2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Start the app:

```bash
streamlit run app.py
```

4. In the app sidebar:
   - enter your Gemini API key,
   - keep the default standards path as `Datasets/building_standards` or change it as needed,
   - keep the default examples path as `Datasets/examples` or change it as needed,
   - click `Initialize Inspector`.

5. Upload images or a video and generate the inspection report.

## Notes and caveats

- This repository is a demonstration/prototype and depends on a valid Gemini API key to function.
- The app expects local folder paths for building standards and examples; these are supplied through the UI rather than environment variables in this version.
- Video processing uses OpenCV and extracts frames at five-second intervals.
- The output is a JSON object that follows a strict schema defined in `logic.py`.
- The repo includes a generated sample file, `inspection_report.json`, which shows a typical output structure.

## Potential next improvements

- add environment-variable support for API key and dataset folders,
- improve file validation and error handling,
- add better multi-image/video support for larger inspection jobs,
- store reports in a database or export to PDF/Word,
- add a real backend and authentication layer,
- support images from remote storage or cloud uploads,
- add OCR or structured defect classification.

## Summary

This repository is a proof-of-concept AI home inspection tool that combines Streamlit, OpenCV, and Gemini to automate visual property assessments using building codes and reference standards. It is best understood as an AI-assisted inspection workflow that takes user media as input and produces a structured, actionable inspection report as output.
