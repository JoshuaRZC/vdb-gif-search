---
up: [[Database Systems Data Models Vector]]
next:
tags:
  - Node
  - Reference
description:
status: Raw
---

# [[Database Systems Data Models Vector]] Query

- [[Database Systems Data Models]]
- [[Database Systems Data Models Vector]]

We know that traditional (scalar) databases store strings, numbers, and other types of scalar data in rows and columns (tables). On the other hand, a vector database operates on vectors, so the way it is optimized and queried is quite different. In traditional database, we are usually querying for rows (tuples) in the database (relations) where the value usually exactly matches out query.

In Vector Database, we apply a similarity metric to find a vector that is most similar to our query.
 
## Overview

- To perform similarity search and retrieval in a vector database, we need to use a query vector that represents our desired information or criteria.
- Database Systems Data Models Vector Query Vector: The query vector can be either derived from the same type of data as the stored vectors (e.g., using an image as a query for an image database), or from different types of data (e.g., using text as a query for an image database).
- Database Systems Data Models Vector Query Similarity Measure: We need a similarity measure that calculates how close two vectors are in the vector space.
    - The Similarity Measure can be based on various metrics, such as Cosine Similarity, Euclidean Distances, Hamming Distance, Jaccard Index, etc.
- Database Systems Data Models Vector Query Result: The result of the similarity search and retrieval is usually a ranked list of vectors that have the highest similarity scores with the query vector.
    - We can then access the corresponding raw data associated with each vector from the original source or index.

## Database Systems Data Model Vector Query Filtering

- Database Systems Data Model Vector Query Filtering Prelude: Every vector stored in the Vector Database also includes metadata.
    - The vector database usually maintains two indexes: a vector index and a metadata index.
- Database Systems Data Model Vector Query Filtering: In addition to the ability to query for similar vectors, Vector Databases can also filter results based on a metadata query.
    - Vector Databases can perform the metadata filtering either before or after the vector search itself.
    - But in either case, there are difficulties that cause the query process to slow down.
- Database Systems Data Model Vector Query Filtering Pre-Filtering: In the Pre-Filtering Query, the metadata filtering is done before the vector search.
    - While this can help reduce the search space, it may also cause the system to overlook relevant result that do not match the metadata filter criteria.
    - Additionally, extensive metadata filtering may slow down the query process due to the added computational overhead.
- Database Systems Data Model Vector Query Filtering Post-Filtering: In the Post-Filtering Query, the metadata filtering is done after the vector search.
    - This can help ensure that all relevant results are considered, but it may also introduce additional overhead and slow the the query process, as irrelevant results need to be filtered out after the search is complete.
- Database Systems Data Model Vector Query Filtering Remark: To optimize the Query Filtering process, vector databases use various techniques, such as leveraging advanced indexing method for metadata or using parallel processing to speed up the filtering tasks.
    - Balancing the trade-off between search performance and filtering accuracy is essential for providing efficient and relevant query results in vector databases.

# Footnotes
