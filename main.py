#Contributor:Kerem
#Developer: Emin
# Raynet Junior Tech Glossary
tech_dictionary = {
 "Python": "A high-level programming language.",
 "Git": "A distributed version control system.",
 "Firewall": "A network security system that monitors and controls incoming and outgoing network traffic.",
 "Subnet": "A segmented piece of a larger network.",
 "Docker": "A platform for developing, shipping, and running applications in containers."
}
def list_terms():
 for term, desc in tech_dictionary.items():
    print(f"{term}: {desc}")
list_terms()