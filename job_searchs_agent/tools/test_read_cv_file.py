import os
import unittest
import read_cv_file

current_dir = os.path.dirname(os.path.abspath(__file__))

class TestReadCvFile(unittest.TestCase):
    def test_read_cv_file_txt(self):
        # Test reading a valid TXT CV file
        valid_txt_path = os.path.normpath(os.path.join(current_dir, "..", "test_cv", "test_cv.txt"))

        result = read_cv_file.read_cv_file(valid_txt_path)
        self.assertEqual(result, "This is a test CV content.")

    def test_read_cv_file_pdf(self):
        # Test reading a valid PDF CV file
        valid_pdf_path = os.path.normpath(os.path.join(current_dir, "..", "test_cv", "test_cv.pdf"))

        result = read_cv_file.read_cv_file(valid_pdf_path)
        self.assertIn("This is a test CV content in PDF.", result)

    def test_read_cv_file_docx(self):
        # Test reading a valid DOCX CV file
        valid_docx_path = os.path.normpath(os.path.join(current_dir, "..", "test_cv", "test_cv.docx"))

        result = read_cv_file.read_cv_file(valid_docx_path)
        self.assertIn("This is a test CV content in DOCX.", result)

    def test_read_cv_file_nonexistent(self):
        # Test reading a non-existent CV file
        nonexistent_file_path = 'nonexistent_cv.txt'
        result = read_cv_file.read_cv_file(nonexistent_file_path)
        self.assertEqual(result, f"The file '{nonexistent_file_path}' does not exist.")


if __name__ == '__main__':
    unittest.main()
