import json
from authenticate_api import start_bloomberg_session

def query_esg_data(session, companies, fields):
    """
    Query ESG data for multiple companies.

    Args:
        session: Active Bloomberg session.
        companies: List of tickers (e.g., ["AAPL US Equity"]).
        fields: List of ESG metrics.

    Returns:
        list: Retrieved ESG data.
    """
    ref_data_service = session.getService("//blp/refdata")
    request = ref_data_service.createRequest("ReferenceDataRequest")

    for company in companies:
        request.getElement("securities").appendValue(company)
    for field in fields:
        request.getElement("fields").appendValue(field)

    session.sendRequest(request)
    results = []

    while True:
        event = session.nextEvent()
        for msg in event:
            if event.eventType() in (blpapi.Event.RESPONSE, blpapi.Event.PARTIAL_RESPONSE):
                for security in msg.getElement("securityData").values():
                    company = security.getElementAsString("security")
                    data = {field: security.getElement("fieldData").getElementAsString(field) 
                            if security.getElement("fieldData").hasElement(field) else "N/A" for field in fields}
                    data["Company"] = company
                    results.append(data)
        if event.eventType() == blpapi.Event.RESPONSE:
            break
    return results

if __name__ == "__main__":
    session = start_bloomberg_session()
    companies = ["AAPL US Equity", "MSFT US Equity", "TSLA US Equity"]
    fields = ["ESG_DISCLOSURE_SCORE", "CARBON_EMISSIONS_TOTAL", "GENDER_DIVERSITY"]

    esg_data = query_esg_data(session, companies, fields)
    with open("examples/sample_response.json", "w") as f:
        json.dump(esg_data, f, indent=4)
    print("ESG data saved to JSON.")
