from docx import Document


def read_job_description(file_path):
    """
    Reads the job description from a .docx file
    and returns it as a single string.
    """

    doc = Document(file_path)

    text = []

    for para in doc.paragraphs:
        if para.text.strip():
            text.append(para.text)

    return "\n".join(text)


if __name__ == "__main__":
    jd = read_job_description("data/job_description.docx")

    print("=" * 80)
    print(jd)
    print("=" * 80)