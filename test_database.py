from database.db import get_session
from database.models import Job


def main():

    session = get_session()

    job = Job(
        source="TEST",
        title="IT Support Specialist",
        company="Example Company",
        location="Remote",
        salary="₱40,000 - ₱50,000",
        url="https://example.com/test-job",
        description="""
        We are looking for an IT Support Specialist with experience
        in troubleshooting Windows computers, networking,
        Google Workspace and technical support.
        """
    )

    session.add(job)
    session.commit()

    print(f"Job inserted with ID: {job.id}")

    session.close()


if __name__ == "__main__":
    main()