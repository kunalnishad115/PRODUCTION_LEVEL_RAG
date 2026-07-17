import hashlib

from langchain_core.documents import Document
def generate_chunk_id(
    document: Document,
    chunk_index: int
) -> str:
    """
    Generate a deterministic unique ID
    for every chunk.
    """

    source = document.metadata.get("source", "")
    page = document.metadata.get("page", 0)
    text = document.page_content.strip()
    unique_string = (
        f"{source}|{page}|{chunk_index}|{text}"
    )

    return hashlib.sha256(
        unique_string.encode("utf-8")
    ).hexdigest()