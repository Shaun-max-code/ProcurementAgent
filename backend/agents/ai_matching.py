from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def find_ai_matches(
    request_text,
    suppliers_df
):

    supplier_texts = []

    for _, row in suppliers_df.iterrows():

        supplier_texts.append(
            f"{row['Supplier']} "
            f"{row['Category']} "
            f"{row['Country']}"
        )

    request_embedding = model.encode(
        [request_text]
    )

    supplier_embeddings = model.encode(
        supplier_texts
    )

    similarities = cosine_similarity(
        request_embedding,
        supplier_embeddings
    )[0]

    suppliers_df["Score"] = similarities

    return suppliers_df.sort_values(
        by="Score",
        ascending=False
    )