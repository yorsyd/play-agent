import unittest
import job_researcher

class TestSearchJobPostings(unittest.TestCase):
    def test_search_job_postings_valid(self):
        # Test with valid job and location preferences
        job_preference = "Software Engineer"
        location_preference = "San Francisco, CA"
        result = job_researcher.search_job_postings(job_preference, location_preference)
        
        self.assertIsInstance(result, dict)
        if len(result["jobs_results"]) > 0:
            job_posting = result["jobs_results"][0]
            self.assertIn("title", job_posting)
            self.assertIn("location", job_posting)
            self.assertIn("company_name", job_posting)
            self.assertIn("description", job_posting)
            self.assertIn("job_highlights", job_posting)
            self.assertIn("source_link", job_posting)

    def test_search_job_postings_empty_preferences(self):
        # Test with empty job and location preferences
        job_preference = ""
        location_preference = ""
        result = job_researcher.search_job_postings(job_preference, location_preference)
        
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("An error occurred while searching for job postings:"))

        self.assertIn("An error occurred while searching for job postings:", result)

if __name__ == '__main__':
    unittest.main()