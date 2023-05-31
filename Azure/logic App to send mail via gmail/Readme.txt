
Challenges faced:
I first created standard azure logic app and i was getting the Internal Server error 

Found solution :
https://learn.microsoft.com/en-us/answers/questions/524626/gmail-connector-does-not-work-in-logic-apps-design

#####################################################################
Other issue faced::
Gmail connector does not work in Logic apps designer: The managed API reference '/subscriptions/..' for V2 API connection 'gmail' is not supported.
Gmail connector does not work in Logic apps designer: The managed API reference '/subscriptions/..' for V2 API connection 'gmail' is not supported.

Tomáš S
26Reputation points
Aug 23, 2021, 10:25 PM
I have tried to connect to Gmail from Azure based on https://learn.microsoft.com/en-us/connectors/gmail/ but azure portal return the error (see below).

Error message:
Failed to create connection for connection id '/subscriptions/....../resourceGroups/P....Email/providers/Microsoft.Web/connections/gmail'. The managed API reference '/subscriptions/............../providers/Microsoft.Web/locations/uksouth/managedApis/gmail' for V2 API connection 'gmail' is not supported.

I can connect with same credential from .net core console application (using google.apis.gmail.v1)

Error on azure:
125650-loggicapp.png
______
Solution::
Works fine with Logic App (Type == Consumption)

127806-capture.jpg

#######
problem:
https://learn.microsoft.com/en-us/answers/questions/828443/internal-server-error-while-invoking-a-functionapp
when I was not able to do in standard logic app, i did it in consumption logic app. 
For internal server error 
https://learn.microsoft.com/en-us/answers/questions/246658/internal-error-in-logic-app
https://learn.microsoft.com/en-us/answers/questions/828443/internal-server-error-while-invoking-a-functionapp
https://learn.microsoft.com/en-us/answers/questions/178612/azure-logic-app-internal-server-error-status-500


######
At first, i was not able to see the inputs , output and errors also 
error-
Inputs and outputs are not loading due to the CORS policy
Add https://portal.azure.com to the allowed origins list in the API CORS settings
Just added https://portal.azure.com in cors setting at left in logic app n i was able to see error. 
Error message:

###########
error code : DomainNotLinked
message: The specified sender domain has not been linked." azure communication
https://stackoverflow.com/questions/75131928/azure-communication-service-email-sending-error
