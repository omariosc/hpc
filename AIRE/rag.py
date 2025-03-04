import os
import streamlit as st
from langchain_community.document_loaders import PDFPlumberLoader  # For PDFs
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings  # Updated import
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document

# -- Custom CSS for Streamlit UI --
primary_color = "#1E90FF"
secondary_color = "#FF6347"
background_color = "#F5F5F5"
text_color = "#4561e9"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {background_color};
        color: {text_color};
    }}
    .stButton>button {{
        background-color: {primary_color};
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
    }}
    .stTextInput>div>div>input {{
        border: 2px solid {primary_color};
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }}
    .stFileUploader>div>div>div>button {{
        background-color: {secondary_color};
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
    }}
    </style>
""",
    unsafe_allow_html=True,
)


# -- Function to recursively load documents from a directory --
def load_documents_from_directory(directory):
    docs = []
    st.write(f"Checking directory: {directory}")
    for root, dirs, files in os.walk(directory):
        st.write(f"Found {len(files)} files in {root}")
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith(".pdf"):
                try:
                    loader = PDFPlumberLoader(file_path)
                    loaded_docs = loader.load()
                    docs.extend(loaded_docs)
                    st.write(f"Loaded {len(loaded_docs)} pages from {file}")
                except Exception as e:
                    st.error(f"Error loading PDF {file_path}: {e}")
            elif file.lower().endswith(".txt") or file.lower().endswith(".md") or file.lower().endswith(".qmd") or file.lower().endswith(".yml"):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    docs.append(
                        Document(page_content=content, metadata={"source": file_path})
                    )
                    st.write(f"Loaded text file: {file}")
                except Exception as e:
                    st.error(f"Error loading text file {file_path}: {e}")

    # Debug the loaded documents
    st.write(f"Total documents loaded: {len(docs)}")
    if len(docs) > 0:
        st.write("First document preview:")
        preview = (
            docs[0].page_content[:100] + "..."
            if len(docs[0].page_content) > 100
            else docs[0].page_content
        )
        st.write(preview)

    return docs


# -- Streamlit App Title and Directory Input --
st.title("AIRE RAG Assistant")
directory = st.text_input(
    "Enter the repository directory path:",
    value="/Users/scsoc/Downloads/aire-main/docs/",
)

if directory:
    if os.path.exists(directory):
        st.write(f"Loading documents from: {directory}")
        docs = load_documents_from_directory(directory)
        st.write(f"Loaded {len(docs)} document(s).")

        if len(docs) > 0:
            try:
                # -- Split Documents into Chunks --
                model_name = "sentence-transformers/all-mpnet-base-v2"
                embeddings_model = HuggingFaceEmbeddings(model_name=model_name)

                # Test if embedding works
                test_text = "This is a test sentence to verify embeddings work."
                test_embedding = embeddings_model.embed_query(test_text)
                st.write(
                    f"✓ Test embedding successful, dimension: {len(test_embedding)}"
                )

                # Now use SemanticChunker
                text_splitter = SemanticChunker(embeddings_model)
                documents = text_splitter.split_documents(docs)
                st.write(f"Documents after splitting: {len(documents)}")

                if len(documents) > 0:
                    # -- Create the Vector Store --
                    vector = FAISS.from_documents(documents, embeddings_model)
                    retriever = vector.as_retriever(
                        search_type="similarity", search_kwargs={"k": 3}
                    )

                    # -- Define the LLM and QA Chain --
                    llm = Ollama(model="deepseek-r1:1.5B")
                    prompt_template = """
                    1. Use the following pieces of context to answer the question.
                    2. If you don't know the answer, say "I don't know" without fabricating details.
                    3. Provide a detailed answer, with a series of bullet points outlining each step.
                    Context: {context}
                    Question: {question}
                    Helpful Answer:"""
                    QA_CHAIN_PROMPT = PromptTemplate.from_template(prompt_template)
                    llm_chain = LLMChain(llm=llm, prompt=QA_CHAIN_PROMPT, verbose=True)

                    document_prompt = PromptTemplate(
                        input_variables=["page_content", "source"],
                        template="Context:\n{page_content}\nSource: {source}",
                    )

                    combine_documents_chain = StuffDocumentsChain(
                        llm_chain=llm_chain,
                        document_variable_name="context",
                        document_prompt=document_prompt,
                        verbose=True,
                    )

                    qa = RetrievalQA(
                        combine_documents_chain=combine_documents_chain,
                        verbose=True,
                        retriever=retriever,
                        return_source_documents=True,
                    )

                    # -- User Query Input --
                    user_query = st.text_input("Ask a question about the repository:")
                    if user_query:
                        with st.spinner("Processing query..."):
                            result = qa(user_query)
                            st.write("**Response:**")
                            st.write(result["result"])
                            st.write("**Source Documents:**")
                            for doc in result["source_documents"]:
                                st.write(doc.metadata.get("source", "Unknown"))
                else:
                    st.error(
                        "No documents generated after splitting. SemanticChunker may not be working properly."
                    )
            except Exception as e:
                st.error(f"Error: {str(e)}")
                import traceback

                st.code(traceback.format_exc())
        else:
            st.error(
                "No documents found in the directory. Please add PDF or TXT files to the directory."
            )
    else:
        st.error(
            "The provided directory path does not exist. Please check and try again. Make sure there is a / at the end of the path."
        )
else:
    st.write("Please enter a directory path to load documents from the repository.")
