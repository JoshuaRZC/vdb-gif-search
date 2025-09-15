# Vector-Database-Powered Semantic GIF Search

We will use the [Tumblr GIF Description Dataset](http://raingo.github.io/TGIF-Release/), which contains over 100k animated GIFs and 120K sentences describing its visual content. Using this data with a *vector database* and *retriever* we are able to create an NLP-powered GIF search tool.

## Project Setup

```shell
# Pull the Qdrant Docker Image
docker pull qdrant/qdrant
# Create Virtual Environment
poetry install

# Start the Qdrant Server
docker run -p 6333:6333 \
    -v $(pwd)/data/qdrant:/qdrant/storage \
    qdrant/qdrant

# Active the Virtual Python Environment
poetry shell
# Start the Streamlit Web Server
streamlit run vdb3170/app.py

```

## Project Layout

- The `vdb/gif-search.ipynb` demonstrates the data preparation, indexing, and querying steps needed to populate and query the index.
- The `vdb/app.py` is the Streamlit script powering the app itself.
- The `vdb/get_started.ipynb` use faked song examples to illustrate the elementary Qdrant Python Client API.
- The `data/tgit-v1.0.tsv` contains GIF urls and description about these 10k GIFs.
- The `data/qdrant` contains the vector database related files.
- The `models/all-MiniLM-L6-v2` stores a fined Sentence Transformer Model.

## Project Teams

- Database System Teams: All, Gao
    <!-- - Database System Implementation:
    - Database System Testing: -->
- Report Teams: Wu, Ren, Kee, HT
    <!-- - Report Abstract:
    - Report Background:
    - Report Description:
    - Report Implementation:
    - Report Testing:
    - Report Conclusion:
    - Report Reference: -->
- Slides Teams: Ren, Kee, HT
    <!-- - Slides Abstract:
    - Slides Background:
    - Slides Implementation: -->
- Presentation Teams: HT, Ren, Kee
    <!-- - Slides Abstract:
    - Slides Background:
    - Slides Design: -->
