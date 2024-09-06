import os
import pdfplumber
import streamlit as st
from groq import Groq

# Set your API key here directly for testing
# os.environ["GROQ_API_KEY"] = "GROQ_API_KEY"

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

# Function to upload and index the content (mocked for simplicity)
def index_pdf_content(text):
    # This is a mock function. In practice, you would use Groq's API to upload and index the text.
    st.write("Indexing content (mocked)...")
    # You would replace this with actual code to index the text

# Create a function to query the indexed content
def query_indexed_content(query):
    st.write("Querying indexed content...")
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query
            }
        ],
        model="llama-3.1-70b-versatile"
    )
    st.write("API Response:", response)  # Debugging: show full API response
    return response.choices[0].message.content if response.choices else "No response content"

# Streamlit App
def main():
    st.title("PDF Query Application")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file is not None:
        st.write("PDF uploaded successfully!")
        
        # Extract text from the uploaded PDF
        pdf_text = extract_text_from_pdf(uploaded_file)
        
        # Show a preview of the extracted text
        st.write("Extracted Text Preview:", pdf_text[:1000])  # Show first 1000 characters
        
        # Index the PDF content (mocked)
        index_pdf_content(pdf_text)
        
        st.write("PDF content indexed. You can now ask questions about the PDF.")
        
        user_query = st.text_input("Enter your query:")
        
        if user_query:
            # Query the indexed content
            response = query_indexed_content(user_query)
            st.write("Response:", response)

if __name__ == "__main__":
    main()
