import unittest
import reporter

class TestReporter(unittest.TestCase):
    def test_report(self):
        # Test with a sample job search result
        report_in_markdown = "# Job Search Report\n\n## Summary\nThis is a summary of the job search results.\n\n## Recommendations\n- Job 1: Software Engineer at Company A\n- Job 2: Data Scientist at Company B"

        report = reporter.save_recomendation_jobs("test_report.md", report_in_markdown)
        
        self.assertIsInstance(report, str)
        self.assertTrue("Report saved successfully to 'test_report.md'.", report)

    def test_report_empty(self):
        # Test with an empty job search result
        job_search_result = {
            "jobs_results": []
        }
        report = reporter.save_recomendation_jobs("test_report_empty.md", job_search_result)
        
        self.assertIsInstance(report, str)
        self.assertTrue("Report content cannot be empty.", report)

    def test_file_name_empty(self):
        # Test with an empty file name
        report_in_markdown = "# Job Search Report\n\n## Summary\nThis is a summary of the job search results.\n\n## Recommendations\n- Job 1: Software Engineer at Company A\n- Job 2: Data Scientist at Company B"
        report = reporter.save_recomendation_jobs("", report_in_markdown)
        
        self.assertIsInstance(report, str)
        self.assertTrue("Filename cannot be empty.", report)
        

if __name__ == '__main__':
    unittest.main()