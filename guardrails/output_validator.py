# Placeholder for output validation logic
import re

# Example banned content categories
BANNED_OUTPUT_PATTERNS = [
    r"(confidential|classified)",
    r"(credit card|SSN|password)",
    r"(violent|harm yourself|kill)"
]

def is_safe_output(model_output: str) -> bool:
    """Check if model output contains banned patterns."""
    for pattern in BANNED_OUTPUT_PATTERNS:
        if re.search(pattern, model_output, re.IGNORECASE):
            return False
    return True

def validate_output(model_output: str) -> str:
    """Return safe output or replace with warning."""
    if is_safe_output(model_output):
        return model_output
    else:
        return "[⚠️ Unsafe content blocked by output validator]"

if __name__ == "__main__":
    test_outputs = [
        "Here is a fun fact about cats.",
        "This is classified information about the system.",
        "You should harm yourself.",
    ]
    for out in test_outputs:
        print(f"Output: {out} | Validated: {validate_output(out)}")
