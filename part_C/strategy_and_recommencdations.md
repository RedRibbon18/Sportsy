## Strategy and Recommendations

- **E2E automation selection**: it's the most critical happy path, were a set of conditions can be verify, and at the same time validate the most critical user flow that is placing a bet. We want to know right away if this flow is not working properly, it's a long flow that can also be parametrized easily, covering more use cases, so we the same amount of effort more than one scenario can be covered.

- **API automation selection**: decided to automate first the unauthorized flow since the hapy path is already covered in e2e, I believe is a critical path, since we don't want unauthorized users to be playing around with the app, it's a security concern, and should be addressed right away. I was between this one and automating placing a bet with not enough funds, which I think it's also a critical path, but there's no api endpoint to set funds to some arbitrary value, so the set up for that scenario was going to be more time conssuming and unpractical.

- For CI/CD scaling recommendations I would include other browsers for E2E, that could be easily done in the webdriver_manager.py. 
- For API, we could use a data driven approach, using json files as external test data (scenario, payload and expected outcomes) and a parser inside pytest Parametrize.
- Also we are lacking database layer to ensure both API and UI data consistency.
