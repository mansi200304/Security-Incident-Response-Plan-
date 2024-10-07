class IncidentResponsePlan:
    def __init__(self):
        self.protocols = {
            "Preparation": "Establish and train an incident response team.",
            "Identification": "Detect and confirm incidents.",
            "Containment": "Limit the impact of the incident.",
            "Eradication": "Remove the cause of the incident.",
            "Recovery": "Restore systems to normal operations.",
            "Lessons Learned": "Review and improve response strategies."
        }

    def get_protocol(self, phase):
        return self.protocols.get(phase, "Phase not found.")

# Example usage:
if __name__ == "__main__":
    sirp = IncidentResponsePlan()
    print(sirp.get_protocol("Preparation"))
