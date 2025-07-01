# Compliance Agent Trial

## Setup
1. Create virtual environment:

		python -m venv venv  
		source venv/bin/activate # Linux/Mac  
		venv\Scripts\activate # Windows

2. Install dependencies:

		pip install requests python-dotenv


## Running the Trial
	python run_trial.py

## Configuration
1. **Real API Integration**: 
   - Create `.env` file with:
     ```
     OCTAGON_API_KEY=your_api_key_here
     ```
   - Modify `run_trial.py`:
     ```
     octagon = OctagonClient(sandbox=False)  # Use real API
     ```

## Architecture
| Component | Purpose | Implementation |
|-----------|---------|----------------|
| `OctagonClient` | Handles sanctions/PEP checks | Mock/real API calls |
| `JurisdictionAgent` | Checks restricted jurisdictions | Rule-based logic |
| `run_trial.py` | Orchestration | Sequential execution |
| `fetch_sanctions.py` | fetch sanction and pep list | fetch from the url |
| `sanctions_loader.py` | return santion result | check from local data |

## Deliverables Checklist

-   `OctagonClient.py`  - Clean class with mock/real API support
-   `JurisdictionAgent.py`  - Rule-based jurisdiction checker
-   `run_trial.py`  - Orchestration script  
-   `compliance_status.json`  - Sample output
-  `fetch_sanctions.py` - Fetches sanction and pep list from OFAC
-   `sanctions_loader.py` - Returns sanction result of selected name.
-   `README.md`  - Clear documentation

## To run
1.  Save all files in  `trial_compliance_agent`  directory
    
2.  Execute: 
	```
	cd trial_compliance_agent
	python run_trial.py
	```
## Acceptance criteria
-   Uses mock Octagon calls by default
    
-   Modular design for easy orchestrator integration
    
-   Lightweight Python implementation
    
-   Comprehensive documentation
    
-   Clear JSON output format

## For production use
1.  Replace jurisdiction mock logic with real data source
    
2.  Implement error handling in API calls
    
3.  Add timeout/retry logic
    
4.  Implement unit tests for each component
