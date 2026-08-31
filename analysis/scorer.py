def classify_score(score):

    if score >= 90:
        return "Excellent Match"

    if score >= 80:
        return "Strong Match"

    if score >= 75:
        return "Good Match"

    if score >= 65:
        return "Borderline"

    return "Poor Match"


def final_recommendation(
    assessment,
    threshold=75
):

    if assessment.mandatory_failures:
        return "SKIP"

    if assessment.fit_score >= threshold:
        return "APPLY"

    if assessment.fit_score >= 65:
        return "CONSIDER"

    return "SKIP"