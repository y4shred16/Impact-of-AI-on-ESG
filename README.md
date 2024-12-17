# Impact-of-AI-on-ESG

## **Overview**
This project provides tools to retrieve and analyze ESG (Environmental, Social, Governance) data using Bloomberg's API. It includes Python scripts to:
- Authenticate with the Bloomberg API.
- Query ESG metrics for multiple companies.
- Save the retrieved data in structured formats (JSON and CSV).
- Visualize key ESG metrics for better insights.

---

## **Features**
- Retrieve key ESG metrics, such as:
  - ESG Disclosure Score
  - Carbon Emissions (Scope 1, 2, and 3)
  - Workforce Diversity
- Process and save data into CSV format.
- Visualize ESG scores for analysis.

---

## **Prerequisites**
Ensure the following requirements are met before running the project:
1. **Bloomberg Terminal Subscription**:
   - Active Bloomberg Terminal with API access.
   - ESG API entitlements enabled (`API<GO>`).

2. **Software and Libraries**:
   - **Python 3.8+**
   - **Libraries**: Install required packages using:
     ```bash
     pip install -r requirements.txt
     ```

3. **Bloomberg API Software**:
   - Download and install Bloomberg API software (`blpapi`).
   - Ensure `BLPAPI_ROOT` is correctly configured:
     - **Windows**:
       ```bash
       set BLPAPI_ROOT=C:\blp\API
       ```
     - **Linux/Mac**:
       ```bash
       export BLPAPI_ROOT=/opt/blpapi
       ```

---

## **Setup Instructions**

### Step 1: Clone the Repository
Clone this project from GitHub to your local system:
```bash
git clone https://github.com/y4shred16/Impact-of-AI-on-ESG.git
cd bloomberg-esg-data-retrieval
