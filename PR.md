Challenge: perform the Coding challenge using django and integrating with Circleci deployed to Heroku

feature: "Give to the notification model a notification_type that has two types - WELCOME and ALERT
- Retrieve this notification feed from the backend and populate the page"

changelog: 
- A new attribute was created in the Notification model which includes a 'Welcome' and 'Alert'. Views were created with rest_framework with the information of the notification model, so the frontend receive the information and display one of the two possible notifications as soon as they determine if the user is authenticated for the first time or are login as a regular user. and can show the corresponding notification.


extra comments:

- Although I corrected and managed to pass 15 tests, it was impossible for me to correct "test_list_notifications()" on time, so I left it commented. I understand that it is not the right thing to do, but I made that decision in order to make the delivery on time and hoping that everything works correctly.

- I was able to create the access to Circleci, but since it was my first time working with this technology, I spent a lot of time trying to understand the deployment, so I didn't have time to do it correctly.
