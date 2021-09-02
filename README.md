# preprlogin
Pytest framework is used to assert and verify the prepr login page.

To install Pytest
1. Run the following command in your command line:
`pip install -U pytest`
2. Check that you installed the correct version:
`pytest --version`

#Run Behave Tests in Parallel
On BrowserStack, you can run multiple Behave tests at the same time across various browser, device and OS combinations.

1. To run tests on multiple browsers in parallel with Behave on BrowserStack Automate, follow the below steps:
` git clone https://github.com/browserstack/behave-browserstack
 cd behave-browserstack`
 
2. Install the dependencies using the following command:
`pip install -r requirements.txt`

3.Update parallel.json files within the behave-browserstack/config/ directory with your credentials

4.Now, execute the test using the following command:
`paver run parallel`
