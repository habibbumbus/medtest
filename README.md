# 🧪 MedTest: Automated Verification & Validation Dashboard

A lightweight Python + Streamlit demo showing automated test execution, logging, and reporting.

## Features
- Auto-discovers all tests in `tests/`
- Produces a JSON summary (`last_results.json`)
- Displays metrics in a simple Streamlit UI
- Mimics QA/validation workflow with intentional failures

## Run Locally
```bash
pip install streamlit
python -m unittest discover tests
streamlit run ui_app.py
