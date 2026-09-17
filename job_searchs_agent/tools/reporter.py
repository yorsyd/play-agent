def save_recomendation_jobs(filename: str, report_markdown: str) -> str:
    """
    Saves the summary and recommendation report to a Markdown file.

    Args:
        filename (str): The name of the file to save the report.
        report_markdown (str): The content of the report in Markdown format.

    Returns:
        str: A message indicating the success or failure of the operation.
    """
    try:
        if not filename:
            return "Filename cannot be empty."

        if not report_markdown:
            return "Report content cannot be empty."

        if not filename.lower().endswith('.md'):
            filename += '.md'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(report_markdown)
        return f"Report saved successfully to '{filename}'."
    except Exception as e:
        return f"An error occurred while saving the report: {e}"

test = save_recomendation_jobs("test_report.md", "# Test Report\nThis is a test report.")
print(test)  # Output: Report saved successfully to 'test_report.md'.