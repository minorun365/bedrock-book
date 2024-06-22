# Pyhton外部モジュールのインポート
from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.embeddings.bedrock import BedrockEmbedding
from llama_index.llms.bedrock_converse import BedrockConverse
from tokenizers import Tokenizer

# Bedrockを生成
llm = BedrockConverse(
    model="anthropic.claude-3-sonnet-20240229-v1:0",
)

# BedrockEmbeddingを生成
embed_model = BedrockEmbedding(
    model="cohere.embed-multilingual-v3",
)

# Tokenizerを生成
tokenizer = Tokenizer.from_pretrained("Cohere/Cohere-embed-multilingual-v3.0")

# ファイルの読み込み
reader = SimpleDirectoryReader("./data/aws/")
documents = reader.load_data()

# ファイルを分割し、ノードに変換
splitter = SentenceSplitter(tokenizer=tokenizer.encode, chunk_size=512)
nodes = splitter.get_nodes_from_documents(documents)

# SimpleDocumentStoreの生成とノードの登録
docstore = SimpleDocumentStore()
docstore.add_documents(nodes)

# ベクトルDBを定義しノードのベクトル
storage_context = StorageContext.from_defaults(docstore=docstore)
vector_index = VectorStoreIndex(
    nodes, storage_context=storage_context, embed_model=embed_model
)

# ベクトルDBから検索し、生成AIで回答生成
query_engine = vector_index.as_query_engine(llm=llm)
response = query_engine.query("Guardrails for Amazon Bedrock とはどういう機能ですか？")

print(response)
