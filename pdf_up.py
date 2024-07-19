import streamlit as st
import os
from pypdf import PdfMerger
from ingest1 import create_vector_database
import nest_asyncio  # noqa: E402
nest_asyncio.apply()

# bring in our LLAMA_CLOUD_API_KEY
from dotenv import load_dotenv
load_dotenv()

##### LLAMAPARSE #####
#from langchain_chroma import Chroma
import os
from pypdf import PdfMerger
import streamlit as st

def process_uploaded_file():
    st.title("Upload File to Chat")
    uploaded_files = st.file_uploader("File upload",accept_multiple_files=True, type="pdf")
    if uploaded_files:
        merger = PdfMerger()

        for pdf in uploaded_files:
            merger.append(pdf)
    
        output_path = "merged.pdf"
        with open(output_path, "wb") as f:
            merger.write(f)
        path = os.path.abspath(output_path)

    #with open(path, "wb") as f:
    #    f.write(uploaded_file.getvalue())   
        st.write("Document uploaded successfully!")
        #st.write(path)
        # Display the uploaded document
        st.write("Preview of the document:")
        # Button to start parsing and vector database creation
        if st.button("Start Processing"):
            # Placeholder for processing logic
            st.write("Processing...")

            # Placeholder for progress bar
            with st.spinner('Processing...'):
                # Call your function to parse data and create vector database
                create_vector_database(path)

            st.success("Processing completed!")

            # Display success message
            st.write("Vector database created successfully!")

            # Show success image
            #success_image = Image.open("success_image.jpg")
            #st.image(success_image, caption="Success!", use_column_width=True)


    # Add a footer
    #st.text("Built with Streamlit")

