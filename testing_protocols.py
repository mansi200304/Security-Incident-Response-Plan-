import pytest
from incident_response_plan import IncidentResponsePlan

def test_protocols():
    sirp = IncidentResponsePlan()
    assert sirp.get_protocol("Preparation") == "Establish and train an incident response team."
    assert sirp.get_protocol("Identification") == "Detect and confirm incidents."
    assert sirp.get_protocol("Containment") == "Limit the impact of the incident."
    assert sirp.get_protocol("Eradication") == "Remove the cause of the incident."
    assert sirp.get_protocol("Recovery") == "Restore systems to normal operations."
    assert sirp.get_protocol("Lessons Learned") == "Review and improve response strategies."
    assert sirp.get_protocol("Nonexistent Phase") == "Phase not found."

if __name__ == "__main__":
    pytest.main()
