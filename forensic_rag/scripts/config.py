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
