#!/bin/bash
# ---------------------------------------------------------------------------
# SETUP SCRIPT for the cloud environment used by the JEE routine.
# Paste this whole file into: Environment settings -> "Setup script".
# It runs once as root on Ubuntu before Claude starts, and the result is cached.
# Every line ends with "|| true" so a temporary download problem never stops a run;
# the routine prompt re-checks the libraries and repairs anything missing.
# ---------------------------------------------------------------------------

# 1. PDF tools (pdftotext, pdftoppm) so the paper PDFs can be read and page images made
apt-get update -y >/dev/null 2>&1 || true
apt-get install -y poppler-utils >/dev/null 2>&1 || true

# 2. Python libraries used by the two skills' scripts
#    python-pptx    -> builds the PowerPoint
#    pypandoc_binary-> converts LaTeX to real PowerPoint equations (bundles pandoc)
#    openpyxl       -> builds the difficulty Excel report
#    lxml           -> equation XML handling
python3 -m pip install --quiet --break-system-packages python-pptx pypandoc_binary openpyxl lxml >/dev/null 2>&1 \
  || python3 -m pip install --quiet python-pptx pypandoc_binary openpyxl lxml >/dev/null 2>&1 \
  || true

exit 0
