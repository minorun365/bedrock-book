from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.embeddings.bedrock import BedrockEmbedding
from llama_index.llms.bedrock import Bedrock
from tokenizers import Tokenizer

llm = Bedrock(
    model="anthropic.claude-3-sonnet-20240229-v1:0",
)

embed_model = BedrockEmbedding(
    model="cohere.embed-multilingual-v3",
)

tokenizer = Tokenizer.from_pretrained("Cohere/Cohere-embed-multilingual-v3.0")

reader = SimpleDirectoryReader("./data/aws/")
documents = reader.load_data()

splitter = SentenceSplitter(tokenizer=tokenizer.encode, chunk_size=512)
nodes = splitter.get_nodes_from_documents(documents)

docstore = SimpleDocumentStore()
docstore.add_documents(nodes)

storage_context = StorageContext.from_defaults(docstore=docstore)
vector_index = VectorStoreIndex(
    nodes, storage_context=storage_context, embed_model=embed_model
)

query_engine = vector_index.as_query_engine(llm=llm)
response = query_engine.query("Guardrails for Amazon Bedrock とはどういう機能ですか？")

print(response)
