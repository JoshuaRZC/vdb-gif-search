"""
app.py: Main Interface using streamlit

Author: Zayn Yuan
Time: Dec 03, 2023
Version: 0.0.1
Commentary:

# Scratch
"""

## Code:
import streamlit as st
from pathlib import Path
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer


def card(urls):
    figures = [
        f"""
        <figure style="margin-top: 5px; margin-bottom: 5px; !important;">
            <img src="{url}" style="width: 130px; height: 100px; padding-left: 5px; padding-right: 5px" >
        </figure>
    """
        for url in urls
    ]
    return st.markdown(
        f"""
        <div style="display: flex; flex-flow: row wrap; text-align: center; justify-content: center;">
        {''.join(figures)}
        </div>
    """,
        unsafe_allow_html=True,
    )


def main():
    client = QdrantClient(host="localhost", port=6333)
    collection = "gif_search"
    path = str(Path(__file__).parent.parent / "models/all-MiniLM-L6-v2")
    retriever = SentenceTransformer(path)
    # retriever = SentenceTransformer("../models/all-MiniLM-L6-v2")

    st.write(
        """
    ## ⚡️ Vector-Database-Powered Semantic GIF Search ⚡️
    """
    )

    query = st.text_input("What are you looking for?", "")

    if st.button("Search"):
        if query != "":
            with st.spinner(text="Similarity Searching..."):
                results = client.search(
                    collection_name=collection,
                    query_vector=retriever.encode(query).tolist(),
                    limit=10,
                )

                urls = []
                for vector in results:
                    url = vector.payload["url"]
                    urls.append(url)

            with st.spinner(text="Fetching GIFs 🚀🚀🚀"):
                card(urls)


if __name__ == "__main__":
    main()
