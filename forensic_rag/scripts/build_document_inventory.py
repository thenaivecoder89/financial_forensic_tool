# File_name: build_document_inventory.py
# Purpose: To scan the client data and corpus
# folders to create a master document inventory
# This inventory becomes the control file for the
# rest of the pipeline:
# - extraction
# - database loading
# - chunking
# - embedding
# - evidence traceability

from pathlib import Path
import csv
import hashlib
from datetime import datetime

# Import paths and settings from the config file
import config

# Define where the inventory file will be saved
document_inventory = config.output_dir / "document_inventory.csv"

# Define which root files to scan
# We only scan corpus and client_data
# not output and scripts since these do not contain evidence data
folders_to_scan = [
    config.client_data_dir,
    config.corpus_dir
]

# Define files and folders to ignore when scanning
ignore_file_names = config.exclude_from_rag
ignore_file_prefixes = [
    "$", # Temporary office files
    "." # Hidden files
]
ignore_folder_names = [
    "__pycache__",
    ".git"
]

# Define inventory output columns
inventory_columns = [
    "document_id",
    "source_group",
    "corpus_pack",
    "file_name",
    "file_extension",
    "relative_path",
    "absolute_path",
    "file_size_bytes",
    "last_modified_datetime",
    "sha256_checksum",
    "supported_file_type",
    "extraction_method_hint",
    "index_in_rag",
    "ingest_status",
    "notes",
]

# Scan files and build inventory for RAG
inventory_rows = []
document_counter = 1

for scan_root in folders_to_scan:

    # Skip if folder does not exist
    if not scan_root.exists():
        print(f"WARNING: Folder does not exist and will be skipped: {scan_root}")
        continue

    # Recursively scan all files in the folder
    for file_path in scan_root.rglob("*"):

        # Skip folders
        if file_path.is_dir():
            continue

        # Skip files inside ignored folders
        if any(part in ignore_folder_names for part in file_path.parts):
            continue

        # Skip ignored filenames
        if file_path.name in ignore_file_names:
            continue

        # Skip hidden/ temporary files
        if any(file_path.name.startswith(prefix) for prefix in ignore_file_prefixes):
            continue

        # Get  file extension in lowercase
        file_ext = file_path.suffix.lower()

        # Determine if this is a supported file type
        supported_file_type = "Yes" if file_ext in config.supported_file_types else "No"

        # Section A: Classify source group - tells us whether the document is a client evidence or methodology/ context corpus