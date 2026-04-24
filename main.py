# Raynet Junior Tech Glossary
tech_dictionary = {
 "Python": "A high-level programming language.",
 "Git": "A distributed version control system.",
 "HTML": "The standard markup language for creating web pages.",
 "CSS": "A style sheet language used for describing the presentation of a document.",
 "API": "Application Programming Interface, a set of rules for building software."

}
def list_terms():
 for term, desc in tech_dictionary.items():
    print(f"{term}: {desc}")
list_terms()