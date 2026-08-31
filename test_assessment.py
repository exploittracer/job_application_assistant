from types import SimpleNamespace

from analysis.assessor import JobAssessor
from analysis.scorer import (
    classify_score,
    final_recommendation
)


def main():

    job = SimpleNamespace(

        source="Jobstreet",

        title="Technical Support Level 3 (Scripting & Coding / AI Literacy) I US Hybrid",

        company="REALPAGE Phils Inc",

        location="Hybrid - Philippines",

        salary="₱50,000 - ₱60,000",

        date_posted="2026-08-27",

        url="https://ph.jobstreet.com/job/94244829",

        description="""

Make an Impact with RealPage

 Looking for a role where your work directly influences business outcomes and customer success?

 At RealPage, you'll join a global SaaS technology company that is transforming the real estate industry through innovative software, data, and AI-driven solutions. We empower our teams to think big, take ownership, and deliver meaningful results every day.

 Whether you're solving complex challenges, collaborating with global stakeholders, or driving operational excellence, you'll have the opportunity to grow your career while making a real impact.

The Technical Support Level 3 role provides advanced technical and functional support for RealPage software solutions, troubleshooting complex issues, guiding users, and ensuring timely resolution while maintaining high customer satisfaction. This role also supports AI-driven and automation initiatives by leveraging tools and emerging technologies to enhance operational efficiency and customer experience.

What You'll Do

    Provide advanced technical and functional support for RealPage solutions, resolving complex issues such as CRM configurations, product integrations, and software navigation via phone, email, and chat.

    Serve as the primary escalation point for customer support concerns, facilitate MBRs for PMCs, and coordinate with Tier 3, Development, and cross-functional teams to drive issue resolution.

    Document customer interactions, resolutions, and escalations while ensuring clear communication and accurate ticket management.

    Stay current on RealPage product updates, collaborate on support process improvements, and meet established KPIs for response time, resolution rate, and customer satisfaction.

    Report to the Customer Support Performance Coach or Senior Customer Support leadership.

    Leverage AI-powered tools, knowledge assistants, and automation solutions to improve troubleshooting efficiency, accuracy, and overall customer support experience.

    Utilize scripts, queries (e.g., SQL), and automation tools to streamline repetitive support tasks, support issue resolution, and identify opportunities for workflow automation.

    Contribute to AI knowledge bases, solution documentation, and the testing/adoption of new AI-driven support capabilities while ensuring compliance with company AI governance guidelines.

What We're Looking For

    Minimum of 3 years of college education, preferably in Business, IT, or a related field.

    2-4 years of technical customer support experience, preferably in a SaaS environment, with strong problem-solving, communication, and multitasking skills.

    Experience with CRM and support tools (Salesforce, Zendesk, Jira) and troubleshooting in SaaS environments.

    Proficient in Microsoft Office (Word, Excel, PowerPoint).

    Knowledge of SQL and data coding and fixes. Exposure to Python, SQL, automation workflows, and AI-assisted support tools.

Work Schedule & Setup

    Must be willing to work onsite during the first 90 days of training

    Hybrid setup begins on the 4th month, with two onsite days per week

    Supports US business operations - Fixed graveyard shift schedule with night differential pay

What We Offer

    Enjoy complimentary meals while you’re in the office

    Day 1 HMO coverage with up to two FREE dependents

    Retirement savings plan

    Leave conversion program

    Life insurance coverage

    Enjoy paid time off, company holidays


Employer questions
Your application will include the following questions:

    Which of the following statements best describes your right to work in the Philippines?
    What's your expected monthly basic salary?
    How many years' experience do you have in a Technical Support Role?
    Which of the following types of qualifications do you have?
    Are you available to work on a nighshift schedule?
    How many years' experience do you have using SQL queries?
    How many years of AI Engineering experience do you have?
    How many years of experience do you have in the SaaS Industry?
    How many years' experience do you have as a Call Agent?        """
    )

    assessor = JobAssessor()

    print("\nAnalyzing job...\n")

    assessment = assessor.assess(job)

    recommendation = final_recommendation(
        assessment
    )

    match_level = classify_score(
        assessment.fit_score
    )

    print("=" * 70)

    print(
        f"FIT SCORE: {assessment.fit_score}%"
    )

    print(
        f"MATCH LEVEL: {match_level}"
    )

    print(
        f"RECOMMENDATION: {recommendation}"
    )

    print("=" * 70)

    print("\nROLE SUMMARY")
    print(assessment.role_summary)

    print("\nSTRENGTHS")

    for item in assessment.strengths:
        print(f"- {item}")

    print("\nTRANSFERABLE SKILLS")

    for item in assessment.transferable_skills:
        print(f"- {item}")

    print("\nSKILL GAPS")

    for item in assessment.skill_gaps:
        print(f"- {item}")

    print("\nEXPERIENCE GAPS")

    for item in assessment.experience_gaps:
        print(f"- {item}")

    print("\nLEARNING PRIORITIES")

    for item in assessment.learning_priorities:
        print(f"- {item}")

    print("\nMANDATORY FAILURES")

    for item in assessment.mandatory_failures:
        print(f"- {item}")

    print("\nREASONING")
    print(assessment.reasoning)


if __name__ == "__main__":
    main()