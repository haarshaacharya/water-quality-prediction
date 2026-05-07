def generate_suggestion(result):

    if result == "GOOD":
        return "Water is safe for drinking."

    elif result == "MODERATE":
        return "Use filtration before drinking."

    else:
        return "Water is polluted. Treatment required."