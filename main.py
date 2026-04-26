# Raynet Junior Tech Glossary
tech_dictionary = {
 "Python": "A high-level programming language.",
 "Git": "A distributed version control system.",
 "Firewall": "A network security system that monitors and controls incoming and outgoing network traffic.",
 "Docker": "A platform for developing, shipping, and running applications in containers.",
 "Subnet": "A segmented piece of a larger network.",
}
def list_terms():
 for term, desc in tech_dictionary.items():
    print(f"{term}: {desc}")
list_terms()