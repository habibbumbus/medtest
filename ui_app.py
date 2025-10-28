import streamlit as st
import json
import os
from utils.test_runner import run_all_tests

st.set_page_config(page_title="MedTest – Verification & Validation Dashboard")

st.title("🧪 MedTest – Verification & Validation Dashboard")
st.caption("Automated regression-style execution and reporting")

st.subheader("Run automated test suite")

if st.button("▶ Run All Tests"):
    results = run_all_tests()
    st.session_state["last_results"] = results

# Load last known results
results = None
if "last_results" in st.session_state:
    results = st.session_state["last_results"]
elif os.path.exists("last_results.json"):
    with open("last_results.json", "r") as f:
        results = json.load(f)

st.divider()
st.subheader("Latest Execution Summary")

if results:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total", results["total"])
    c2.metric("Passed", results["passed"])
    c3.metric("Failures", results["failures"])
    c4.metric("Errors", results["errors"])
    st.text(f"Timestamp: {results['timestamp']}")
    st.subheader("Execution Log / Defect Signals")
    st.code(results["details"], language="text")
else:
    st.write("No test run yet. Click 'Run All Tests' above.")

st.divider()
st.caption("Iteration: Sprint 1 mock | Built for Agfa HealthCare interview demo")
