from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import CollectionStatus
from sentence_transformers import SentenceTransformer
import torch


device = "cuda" if torch.cuda.is_available() else "cpu"

# Initialize retriever with SentenceTransformer model
retriever = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
retriever.to(device)

client = QdrantClient(host="localhost", port=6333)

collection = "gif_search"


def insert_gif(url, description):
    id = 1
    emb = retriever.encode(description.strip()).tolist()
    meta = {
        "url": url,
        "description": description,
        }
    client.upsert(
        collection_name=collection, 
        points=[models.PointStruct(id= id, vector=emb, payload=meta)]
        )
    
    # count after insertion
    print(client.count(collection_name=collection,exact=True,))
    return 

def delete_gif(url):
    client.delete(
        collection_name=collection, \
        points_selector=models.FilterSelector( filter=models.Filter(
            must=[
                models.FieldCondition(
                    key="url",
                    match=models.MatchValue(value=url),
                ),
            ],
        )
    ),
)
    # count after deletion
    print(client.count(collection_name=collection,exact=True,))
    return


def main():
    # count original number of GIFs before modifications
    print(client.count(collection_name=collection,exact=True,))
    # upserting a new GIF
    insert_gif("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGI3aGk2c3ZnZnpwazcyamx1cjIybHBjYXlnbm44dDlsOTB6ZTkybCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/q1CIZgFvnmJEtsNXkK/giphy.gif","Professor Jane You with disco")
    
    # deleting the GIF
    # delete_gif("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGI3aGk2c3ZnZnpwazcyamx1cjIybHBjYXlnbm44dDlsOTB6ZTkybCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/q1CIZgFvnmJEtsNXkK/giphy.gif")



if __name__ == "__main__":
    main()