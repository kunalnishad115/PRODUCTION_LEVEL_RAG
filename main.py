from app.vectorstore.vectorstore_factory import VectorStoreFactory

vectorstore = VectorStoreFactory.get_vectorstore()

documents = vectorstore.get_all_documents()

print(f"Total Documents : {len(documents)}")

for doc in documents[:2]:
    print("-" * 80)
    print(doc.page_content[:200])
    print(doc.metadata)