import chromadb

client = chromadb.PersistentClient(
    path="./rag_db"
)

collection = client.get_collection(
    "schema"
)

data = collection.get()

print("IDs:")
print(data["ids"])

print("\nDocuments:")
for doc in data["documents"]:
    print("\n" + "="*50)
    print(doc)