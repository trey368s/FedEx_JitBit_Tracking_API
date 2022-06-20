# FedEx JitBit Tracking API
FedEx Developer Portal Project- https://developer.fedex.com/api/en-us/project/overview.html#/projectoverview/testkey/77581efd-64d2-4439-a3cf-336d9662186f  
FedEx Authorization API Documentation - https://developer.fedex.com/api/en-us/catalog/track/docs.html  
FedEx Track API Documentation - https://developer.fedex.com/api/en-us/catalog/track/docs.html  
JitBit Helpdesk API Documentation - https://www.jitbit.com/helpdesk/helpdesk-api/#/  

This program is made to track and provide shipping updates on packages that have been sent though the JitBit helpdesk. It gets a list of assigned tickets, goes through there tags looking for tracking numbers, finds the status of the tracking number, and then goes back and comments an update on the ticket. It then checks for items that are delivered and asks if the package has been received, it then checks for a response and either closes the ticket if they have received it or alerts the technician if they have not. 
