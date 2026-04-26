# Raynet Junior Tech Glossary
tech_dictionary = {
 "Python": "A high-level programming language.",
 "Git": "A distributed version control system.",
 "API": "Application Programming Interface, a set of rules for building software applications.",
 "HTML": "HyperText Markup Language, the standard language for creating web pages.",
 "CSS": "Cascading Style Sheets, used for describing the presentation of a document"
}
def list_terms():
 for term, desc in tech_dictionary.items():
    print(f"{term}: {desc}")
list_terms()