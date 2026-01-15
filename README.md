# Numida QA Engineer Assessment -- Ian Michael Kinyanjui 
This repository contains automated UI and API tests for a simplified loan application system, completed as part of the Numida Senior QA Engineer assessment.

---
## Tech Stack
### API Testing
- Python
- pytest
- requests

### UI Testing
- Playwright (TypeScript)


## Setup Instructions
### 1. Start the Application Locally 
Follow the instructions in the provided QUICK_START.md in the initial provision to run the app locally.

---

### 2. UI and API Tests Setup

```bash

cd api-tests
python -m venv venv
source venv/bin/activate
pip install pytest requests

### Run API Tests
pytest -v

---

cd ui-tests
npm install
npx playwright install

### Run UI Tests
npx playwright test

```

## **Test Plan and Design Considerations**

1. **Scope and Objectives**

The objective of the suite was to validate that the application flow/user journey is completed as needed while creating a framework that allows for scalability and maintainability. The items in scope of testing include the happy path for the loan application process while considering key validations are met. 

1. **Automated UI and API Testing Considerations** 

My choice for automation testing of the UI involves the use of Playwright  because of its speed, auto waits, reliable selectors, multi-browser/platform support, and ease of implementation on CI.  Playwright also offers a wide range of debugging tools which reduce flakiness and these tools enable dynamic content to be automated and the system is applicable for large-scale testing because of the stability it provides. 

The choice to use Pytest+requests is because of my comfort using Python and the simplicity of using the testing framework because of its flexibility and its seamless integration with existing development workflows. 

1. **Automation Coverage** 

Automated testing scenarios that were covered include:

- verifying that the landing page loads
- OTP request and verification is successful
- Loan Submission Successful
- Status Screen is visible post application
1. Manual Testing Coverage 

Manual testing efforts involved determining that the happy path was achieved when steps were followed from start to finish.

The process extended to testing other limits of the application such as testing whether it was possible to reapply for a loan with the same application details, and testing the formats expected in the various fields such as the name, email, phone number, and ID structure. 

1. **Bugs, Defects, Gaps**

— **Defects**

- The application does not show on the application page that when the Name, ID, Email Address, or Date have not been input correctly that the loan won’t be processed. One has to inspect the page and check the payload in the network traffic section to determine what the error is. For a regular user, the process could be frustrating since they would not be able to know the reason as to why their loan application is not being processed.
- The phone number format/specification does not have controls allowing one to input numbers and some special characters into the number field
- The loan does not get automatically rejected if the age of the applicant is out of scope/unreasonable range

— **Bugs**

- The 15 days loan option does not seem to be viable despite it being the default option
- The same ID number can be reused

— **Gaps**

- No API Schema Validation
- No retry limit for OTP
- No explicit logout
- No IPRS check on the ID number against other systems to determine viability of the applicant
    
    
Open Questions (Intentionally Left Unanswered)

- What happens if the user abandons the flow halfway?
The application does not receive the request if its not completed/submitted 
- How are retries handled?
The page is cached so a retry does not affect the process 
- Are there rate limits?
Minimum 1000 Max 100000
- What happens if the same National ID is reused?
The Loan is still approved - this is a defect
