#Developer: Emin
# Raynet Junior Tech Glossary
# Contributor: Kerem
tech_dictionary = {
 "Python": "A high-level programming language.",
 "Git": "A distributed version control system.",
 "Firewall": "A network security system that monitors and controls incoming and outgoing network traffic.",
 "Docker": "A platform designed to help developers create, deploy, and run applications by using containers.",
 "Subnet": "A logical subdivision of an IP network."
}
def list_terms():
 for term, desc in tech_dictionary.items():
    print(f"{term}: {desc}")
list_terms()