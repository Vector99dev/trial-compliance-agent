import os
import requests
from sanctions_loader import SanctionsDataLoader

class OctagonClient:
    BASE_URL = "https://api-gateway.octagonagents.com/v1"
    
    def __init__(self, api_key=None, sandbox=True):
        self.api_key = api_key or os.getenv("OCTAGON_API_KEY")
        self.sandbox = sandbox
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def _mock_response(self, endpoint):
        """Generate mock responses for sandbox mode"""
        if "sanctions" in endpoint:
            return {"flagged": False, "match_score": 0.1}
        elif "pep" in endpoint:
            return {"flagged": True, "position": "Former Minister"}
        return {"error": "Invalid endpoint"}
    
    def _call_api(self, endpoint, payload):
        if self.sandbox or not self.api_key:
            return self._mock_response(endpoint)
        
        response = requests.post(
            f"{self.BASE_URL}/{endpoint}",
            headers=self.headers,
            json=payload,
            timeout=10
        )
        return response.json()
    
    def check_sanctions(self, name):
        loader = SanctionsDataLoader()
        return loader.is_sanctioned(name)
        # payload = {"input": f"Is {name} on any sanctions lists?"}
        # return self._call_api("responses?model=octagon-sanctions-agent", payload)
    
    def check_pep(self, name):
        payload = {"input": f"Is {name} a Politically Exposed Person?"}
        return self._call_api("responses?model=octagon-pep-agent", payload)
