from sentence_transformers import SentenceTransformer

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======

>>>>>>> d41cf62 (first commit)
>>>>>>> bbfdd13 (first commit)
>>>>>>> 6446644 (first commit)
class MyEmbeddingFunction():

  def embed_documents(data):
    model = SentenceTransformer('sentence-transformers/paraphrase-albert-small-v2')
    embeddings = model.encode(data)
    return embeddings.tolist()

  def embed_query(query):
    model = SentenceTransformer('sentence-transformers/paraphrase-albert-small-v2')
    embeddings = model.encode(query)
    return embeddings.tolist()
