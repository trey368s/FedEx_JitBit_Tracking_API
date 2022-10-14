# FedEx JitBit Tracking API
This program is made to track and provide shipping updates on packages that have been sent though the JitBit helpdesk. It gets a list of assigned tickets, goes through there tags looking for tracking numbers, finds the status of the tracking number, and then goes back and comments an update on the ticket. It then checks for items that are delivered and asks if the package has been received, it then checks for a response and either closes the ticket if they have received it or alerts the technician if they have not. You can provide tracking updates to a ticket simply by putting the FedEx tracking number in the tag of a ticket that is assigned to you.
## Documentation
FedEx Developer Portal - https://developer.fedex.com/api/en-us/home.html  
FedEx Authorization API Documentation - https://developer.fedex.com/api/en-us/catalog/authorization/v1/docs.html  
FedEx Track API Documentation - https://developer.fedex.com/api/en-us/catalog/track/docs.html  
JitBit Helpdesk API Documentation - https://www.jitbit.com/helpdesk/helpdesk-api/#/  
## Example
![ergerg](https://user-images.githubusercontent.com/84042739/176241633-90c03885-facb-41f0-981f-4a288d7f4761.PNG)
