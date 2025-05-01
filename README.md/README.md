1. Task Instructions

Access the North Dakota Secretary of State Business Search page.

Search for all active companies starting with the letter "X."

For each company, collect the following:

Commercial Registered Agent

Registered Agent

Owner Name (if available)

Save the collected data into a file (CSV or JSON).

Build a simple graph connecting companies, agents, and owners.

2. Development Journey
First Attempt (nd_scraper.py)
My initial scraper was built using Scrapy (nd_scraper.py).
This first version:

Correctly performed the advanced search for "X" companies.

Scraped basic company names and IDs.

However, it did not successfully pull the Commercial Registered Agent, Registered Agent, or Owner Name fields.

Additionally, website complexities like asynchronous page loading and hidden drawers made Selenium or standard Scrapy approaches unreliable.

Lessons Learned:
Modern web apps often load content dynamically through APIs.

Clicking drawers and scraping visual elements was slow, prone to Selenium timeout errors, and inefficient.

Second and Final Attempt (nd_fetch_details_api.py)
I taught myself how to use the North Dakota site's underlying API instead of interacting with the front-end.

The final scraper (nd_fetch_details_api.py):

Sent POST requests to the hidden business search API to retrieve all companies starting with "X."

Then, for each company, sent a second API call to the filing detail endpoint.

Parsed through the filing detail data to successfully find:

Commercial Registered Agent

Registered Agent

Owner Name

➡️ After collecting the correct data, I added new logic to ensure only the correct field was recorded if multiple types were present.

✅ This dramatically increased reliability, speed, and accuracy compared to the Selenium attempts.

✅ The final result was a complete, clean dataset in both CSV and JSON formats, meeting all Sayari task instructions.

3. How the Scraper Solves the Task
Using nd_fetch_details_api.py:

Queries all active companies whose names start with "X."

For each company:

Searches for a Commercial Registered Agent.

If missing, looks for a Registered Agent.

If still missing, looks for an Owner Name.

Compiles this into structured rows.

Saves everything into:

companies_details_api.csv

companies_details_api.json

Properly includes the Company Name, ID, Type (which of the 3 types it was), and the associated Name.

4. Graphing Solution
A separate script uses NetworkX to:

Create a graph where each company and agent/owner is a node.

Draws an edge between a company and its agent or owner.

Visualizes entity relationships, showing how companies and individuals/organizations are connected.

This serves as a basic entity resolution system — matching names across multiple records to uncover links.

6. Summary
✅ Successfully collected public business data.
✅ Correctly pulled agent/owner names for active companies starting with "X."
✅ Saved the data in structured formats.
✅ Visualized the data through a relationship graph.
✅ Iteratively improved by moving from a brittle Selenium solution to a robust API scraping strategy.
