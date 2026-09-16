import os

def read_cv_file(file_path: str) -> str:
    """
    Reads the content of a CV file and returns it as a string.

    Args:
        file_path (str): The path to the CV file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        Exception: If an error occurs while reading the file.

    Returns:
        str: The content of the CV file.
    """

    if not os.path.exists(file_path):
        return f"The file '{file_path}' does not exist."

    if file_path.lower().endswith('.pdf'):
        try:
            from pypdf import PdfReader

            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            return f"An error occurred while reading the PDF file: {e}"

    if file_path.endswith('.docx'):
        try:
            from docx import Document
            
            doc = Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text.strip()
        except Exception as e:
            return f"An error occurred while reading the DOCX file: {e}"

    if file_path.endswith('.txt'):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            return f"An error occurred while reading the text file: {e}"

    
    # try:
    #     with open(file_path, 'r', encoding='utf-8') as file:
    #             return file.read()
    # except FileNotFoundError:
    #     return "File not found."
    # except Exception as e:
    #     return f"An error occurred: {e}"
