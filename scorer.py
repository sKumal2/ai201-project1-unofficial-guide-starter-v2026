"""
scorer.py

Scoring helpers for the AI201 Project 1 evaluation.

These checks are intentionally simple and deterministic.
They are based on the five evaluation questions used by run_eval.py.
"""


def normalize(text):
    if text is None:
        return ""
    return str(text).lower().strip()


def retrieved_text(results):
    """
    Convert retrieved chunks/results into one searchable string.
    Works with strings, dictionaries, objects, or lists.
    """
    if results is None:
        return ""

    if not isinstance(results, (list, tuple)):
        results = [results]

    pieces = []

    for result in results:

        if isinstance(result, str):
            pieces.append(result)
            continue

        if isinstance(result, dict):
            for key in [
                "text",
                "content",
                "chunk",
                "document",
                "source",
                "filename",
            ]:
                if key in result:
                    pieces.append(str(result[key]))
            continue

        # fallback for custom result objects
        for attr in [
            "text",
            "content",
            "chunk",
            "document",
            "source",
            "filename",
        ]:
            if hasattr(result, attr):
                pieces.append(str(getattr(result, attr)))

        pieces.append(str(result))

    return normalize(" ".join(pieces))


# ---------------------------------------------------------
# Criterion 1
# Did retrieval contain information needed for the answer?
# ---------------------------------------------------------

def retrieval_contains_answer(question, results):
    question = normalize(question)
    text = retrieved_text(results)

    if not text:
        return False

    # Q1
    if "good dining halls" in question:
        return (
            "pellew" in text
            or "halden" in text
        )

    # Q2
    if "wait times" in question and "commons" in question:
        return (
            "kestrel" in text
            and (
                "20 to 25" in text
                or "20-25" in text
                or "12:15" in text
            )
        )

    # Q3
    if "dining halls close" in question and "weekend" in question:
        return (
            "halden" in text
            and (
                "sunday" in text
                or "weekend" in text
            )
        )

    # Q4
    if "guests" in question and "dorm" in question:
        # Your current retrieved chunks do NOT contain a guest policy.
        return (
            "guest policy" in text
            or "guests may" in text
            or "guest limit" in text
            or "overnight guest" in text
        )

    # Q5
    if "reserve a study room" in question:
        return (
            "study_group_rooms" in text
            or (
                "study room" in text
                and "book" in text
            )
        )

    return False


# ---------------------------------------------------------
# Criterion 2
# Does the answer name a source?
# ---------------------------------------------------------

def answer_names_source(answer):
    text = normalize(answer)

    if not text:
        return False

    source_markers = [
        ".txt",
        ".md",
        ".pdf",
        "source:",
        "sources:",
    ]

    return any(marker in text for marker in source_markers)


# ---------------------------------------------------------
# Criterion 3
# Did the relevance gate reject an out-of-scope question?
# ---------------------------------------------------------

def gate_refused(decision):
    if decision is None:
        return False

    # bool convention:
    # True = accepted, False = refused
    if isinstance(decision, bool):
        return not decision

    if isinstance(decision, dict):

        for key in ["passed", "allowed", "accepted"]:
            if key in decision:
                return not bool(decision[key])

        if "decision" in decision:
            decision = decision["decision"]

    text = normalize(decision)

    return any(
        word in text
        for word in [
            "refused",
            "reject",
            "rejected",
            "blocked",
            "out_of_scope",
            "out-of-scope",
            "out of scope",
        ]
    )


# ---------------------------------------------------------
# Criterion 5
# Is the generated answer grounded?
# ---------------------------------------------------------

def answer_is_grounded(question, answer):
    """
    Lightweight checks for the five fixed evaluation questions.

    This checks whether the generated answer stayed consistent with
    the known evidence. It does NOT attempt to be a universal
    factuality grader.
    """

    q = normalize(question)
    a = normalize(answer)

    if not a:
        return False

    if "good dining halls" in q:
        return (
            ("pellew" in a or "halden" in a)
            and ".txt" in a
        )

    if "wait times" in q and "commons" in q:
        return (
            "20 to 25" in a
            or "20-25" in a
        )

    if "dining halls close" in q and "weekend" in q:
        return "halden" in a and "sunday" in a

    if "guests" in q and "dorm" in q:
        # Correct behavior here is NOT to invent a guest limit.
        return (
            "don't have enough information" in a
            or "do not have enough information" in a
            or "do not mention guest policies" in a
        )

    if "reserve a study room" in q:
        return (
            "library site" in a
            and (
                "two weeks" in a
                or "2 weeks" in a
            )
        )

    return False


# ---------------------------------------------------------
# Main scorer
# ---------------------------------------------------------

def score(question, answer, results, decision=None):
    return {
        "criterion_1": retrieval_contains_answer(question, results),
        "criterion_2": answer_names_source(answer),
        "criterion_3": (
            gate_refused(decision)
            if decision is not None
            else None
        ),
        "criterion_5": answer_is_grounded(question, answer),
    }


# Alias in case run_eval.py expects this name.
def score_answer(question, answer, results, decision=None):
    return score(question, answer, results, decision)

def judge(question, expects, answer, results):
    """
    Main function expected by run_eval.py.

    Returns True if the answer passes the evaluation
    for this question, otherwise False.
    """

    # Criterion 1:
    # retrieval should contain the information needed
    if not retrieval_contains_answer(question, results):
        return False

    # The answer itself should also be grounded/correct
    if not answer_is_grounded(question, answer):
        return False

    return True