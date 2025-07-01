from OctagonClient import OctagonClient
from JurisdictionAgent import JurisdictionAgent
from fetch_sanctions import fetch_files
import json

def run_compliance_check(entity_name):
    # Initialize agents
    octagon = OctagonClient(sandbox=True)  # Use sandbox mode for trial
    jurisdiction_agent = JurisdictionAgent()
    
    # Execute checks
    sanctions_status = octagon.check_sanctions(entity_name)
    pep_status = octagon.check_pep(entity_name)
    jurisdiction_status = jurisdiction_agent.check_jurisdiction(entity_name)
    
    # Prepare unified output
    return {
        "entity": entity_name,
        "sanctions": {"flagged": sanctions_status.get("flagged", False)},
        "pep": {"flagged": pep_status.get("flagged", False)},
        "jurisdiction": {
            "status": jurisdiction_status["status"],
            "flagged_jurisdictions": jurisdiction_status["flagged"]
        }
    }

def daily_sanctions_update():
    print("Downloading fresh sanctions data...")
    fetch_files()
    print("Sanctions data updated!")

if __name__ == "__main__":
    # Runs first to fetch the data.
    daily_sanctions_update()
    result = run_compliance_check("Acme Corp")
    
    with open("compliance_status.json", "w") as f:
        json.dump(result, f, indent=2)
    
    print("Compliance check completed. Results saved to compliance_status.json")
