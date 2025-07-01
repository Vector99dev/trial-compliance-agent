class JurisdictionAgent:
    RESTRICTED_JURISDICTIONS = [
        "Iran", "North Korea", "Syria", "Crimea", 
        "Donetsk PR", "Luhansk PR", "Cuba"
    ]
    
    def check_jurisdiction(self, entity):
        """Check if entity operates in restricted jurisdictions"""
        # In real implementation, this would query a jurisdiction database
        # Mock implementation for trial:
        operating_in = ["USA", "Germany"]
        flagged_jurisdictions = [j for j in operating_in if j in self.RESTRICTED_JURISDICTIONS]
        
        return {
            "status": "fail" if flagged_jurisdictions else "pass",
            "jurisdictions": operating_in,
            "flagged": flagged_jurisdictions
        }
