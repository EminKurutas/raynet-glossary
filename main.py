# Raynet Junior Tech Glossary
tech_dictionary = {
 "Python": "A high-level programming language.",
 "Git": "A distributed version control system.",
 "API": "Application Programming Interface, a set of rules for building software applications.",
 "Cloud Computing": "The delivery of computing services over the internet.",
 "Machine Learning": "A subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed."
}
def list_terms():
 for term, desc in tech_dictionary.items():
    print(f"{term}: {desc}")
list_terms()