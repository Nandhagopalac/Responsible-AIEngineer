# Placeholder for hallucination detection logic
import re

def detect_hallucination(output_text, knowledge_base=None):
    """
    Simple heuristic-based hallucination detector.
    - Flags unverifiable citations, unknown sources, or suspicious patterns.
    - Optionally cross-checks against a provided knowledge base (list of trusted facts).
    """

    issues = []

    # 1. Check for fake citations (e.g., "Source: XYZ123")
    if re.search(r"Source: [A-Za-z0-9]+", output_text):
        issues.append("Suspicious citation format detected.")

    # 2. Check for unverifiable claims (e.g., "according to secret data")
    if "secret data" in output_text.lower() or "hidden rules" in output_text.lower():
        issues.append("Unverifiable claim detected.")

    # 3. Check for hallucinated URLs
    if re.search(r"http[s]?://[^\s]+", output_text):
        issues.append("Potential hallucinated URL detected.")

    # 4. Optional: cross-check against knowledge base
    if knowledge_base:
        for fact in knowledge_base:
            if fact.lower() not in output_text.lower():
                issues.append(f"Output missing expected fact: {fact}")

    return issues


if __name__ == "__main__":
    # Example test
    sample_output = "According to secret data, the moon is made of cheese. Source: XYZ123"
    findings = detect_hallucination(sample_output, knowledge_base=["moon is rocky"])
    if findings:
        print("Hallucination Detected:")
        for issue in findings:
            print(f"- {issue}")
    else:
        print("No hallucination detected.")
