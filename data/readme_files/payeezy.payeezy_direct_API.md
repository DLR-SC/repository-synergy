# Payeezy Direct API

User Action: Buyer does a checkout on the merchant hosted site by clicking on buy/submit button. This needs to be a secure page.

1. Upon Submit the form gets posted to the Merchant server
2. Merchant’s backend server invokes the Payeezy API over a SSL connection and submits the order information securely. The call 
   requires providing an authorization header with a HMAC hash. Refer to API docs section for more information on this.
3. Payeezy process the transactions (such as authorize, purchase) with the provided transaction details and sends back the response
4. Success/failure message needs to be handled accordingly by the merchants server.

NOTE: The merchant/third party is responsible for PCI compliance and may be required to provide First Data with additional documentation and/or their attestation of compliance

# Payeezy supported language
Java, PHP, Python,Ruby, nodeJS and Curl. 

# Release notes:
* Tokenised Transactions - Token is generated for the card and the transactions are made using the token.US merchants will receive Transarmor multi-use tokens and EU merchants will receive Data Vault tokens.
* AVS,CVV, SoftDescriptor and 3DS Card Transactions - This feature is used to make credit card transactions [Non-Tokenised].<US merchants/EU Merchant
* Dynamic Currency Conversion and Dynamic Pricing - <US merchants/EU Merchant>
* TimeOutReversal - US merchants/EU Merchants> Any transaction can be reversed except for VOID.
We will have to send an additional attribute "reversal_id" in the request payload. This method is applicable only to merchants domiciled in US and Europe.
* GermanDirectDebit - <EU Merchants> This method is applicable only to merchants domiciled in Germany.

# Getting Started with Payeezy
Using below listed steps, you can easily integrate your mobile/web payment application with Payeezy APIs and go LIVE!
*	LITE  - REGISTRATION  
*	GET CERTIFIED
*	ADD MERCHANTS 
*	LIVE!

![alt tag](https://github.com/payeezy/get_started_with_payeezy/raw/master/payeezy_flow_diagram.png)

For more information on getting started, visit  [get_start_with_payeezy guide] (https://github.com/payeezy/get_started_with_payeezy/blob/master/get_started_with_payeezy042015.pdf) or [download](https://github.com/payeezy/get_started_with_payeezy/raw/master/get_started_with_payeezy042015.pdf)

# Testing - Payeezy {SANDBOX region}
For test credit card,eCheck,GiftCard please refer to [test data ](https://github.com/payeezy/testing_payeezy/blob/master/payeezy_testdata042015.pdf) or [download] (https://github.com/payeezy/testing_payeezy/raw/master/payeezy_testdata042015.pdf)

# Error code/response - Payeezy {SANDBOX/PROD region}
For HTTP status code, API Error codes and error description please refer to [API error code ](https://developer.payeezy.com/payeezy_new_docs/apis) and select your API

#Questions?
We're always happy to help with code or other questions you might have! Check out [FAQ page](https://developer.payeezy.com/faq-page) or call us. 

## Contributing
1. Fork it 
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request  

## Feedback
We appreciate the time you take to try out our sample code and welcome your feedback. Here are a few ways to get in touch:
* For generally applicable issues and feedback, create an issue in this repository.
* support@payeezy.com - for personal support at any phase of integration
* [1.855.799.0790](tel:+18557990790)  - for personal support in real time 

## Terms of Use
Terms and conditions for using Payeezy Direct API: Please see [Payeezy Terms & conditions](https://developer.payeezy.com/terms-use)
 
### License
The Payeezy Direct API is open source and available under the MIT license. See the LICENSE file for more info.
