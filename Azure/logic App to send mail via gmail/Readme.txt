
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
