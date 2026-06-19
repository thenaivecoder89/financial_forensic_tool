# File_name: config.py
# Purpose: To store all common paths, database settings, model settings,
# and project-level constants used by the RAG pipeline

from pathlib import Path
import os
from dotenv import load_dotenv

# Project paths
project_root = Path(__file__).resolve().parents[1]
corpus_dir =  project_root / "corpus"
client_data_dir = project_root / "client_data"
output_dir = project_root / "output"
draft_report_dir = output_dir / "draft_report"
exceptions_dir = output_dir / "exceptions"
extracted_tables_dir = output_dir / "extracted_tables"
extracted_text_dir = output_dir / "extracted_text"
findings_register_dir = output_dir / "findings_register"

# Database
load_dotenv()
db_url = os.getenv("VECTOR_DB")
if not db_url:
    raise RuntimeError(
        "Database URL variable is not set. Please set to railway DB using public connection string."
    )
db_schema = "forensic_rag"

# LLM
openai_api_key = os.getenv("OPENAI_API_KEY")
llm_provider = "openai"
llm_model = "gpt-5.5" 

# Embeddings
embedding_provider = "openai"
embedding_model = "text-embedding-3-small"
embedding_dimension = 1536

# Chunking
chunk_size_tokens = 1000
chunk_overlap_tokens = 150

# Corpus packs
corpus_packs = {
    "aml_sanctions": corpus_dir / "aml_sanctions_04",
    "bahrain_context": corpus_dir / "bahrain_context_03",
    "forensic_methodology": corpus_dir / "forensic_methodology_01",
    "internal_controls": corpus_dir / "internal_controls_02",
    "report_structure": corpus_dir / "report_structure_05"
}

# Client data packs
client_data_packs = {
    "ap_ar": client_data_dir / "ap_ar",
    "bank": client_data_dir / "bank",
    "contracts": client_data_dir / "contracts",
    "financials": client_data_dir / "financials",
    "legal_regulatory": client_data_dir / "legal_regulatory",
    "ownership": client_data_dir / "ownership"
}

# File handling
supported_text_extensions = {".pdf", ".docx", ".txt", ".md"}
supported_table_extensions = {".csv", ".xlsx", ".xls"}
supported_archive_extensions = {".zip"}
exclude_from_rag = {
    "validation_ground_truth_findings.csv",
    ".DS_Store",
    "Thumbs.db"
}
store_raw_files_in_db = False # To avoid storing large files like the ACFE Manual as raw binary in DB

# Runtime
default_currency = "BHD"
default_jurisdiction = "Bahrain"
project_name = "Financial Forensic RAG"