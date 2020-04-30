# McQueen Clinic Patient Database

This milestone project was used to build an interactive patient database for the clinic administrator. The application will allow the administrator to view all patients, search through the patients, edit a patient, add a patient, and also manage the doctors at the clinic. This will allow the clinic to store patient information in a secure database to which only they have access to. 

## UX

Boostrap was used to build a mobile friendly responsize app that utilizes clean lines and plenty of whitespace. As this app will be used constantly throughout the day by a clinic administrator, it is important to make it easy to read and use and to stray away from visual gimmicks and items that are there purely for visual appeal. 

### User Stories

The clinic administrator needs to search the contact information about a particular patient. Upon launching the app, the search functionality present in the header can be used to search by first name, last name, or health card number. This is a good way to quicly get the result of the patient in question.

The clinic administrator needs to register a new patient visiting the clinic. Upon launching the app, the add patient button present in the header allows to redirect to an add patient form. The form has validation functionality ensuring that health card numbers, phone numbers, and email addresses are inputted correctly. Upon adding the patient, the administrator is redirected to the all patients view and can scroll or search to confirm entry.

The clinic administrator needs to update the contact information for a patient. Upon launching the app, the administrator can either scroll to or search for the patient. By clicking the view/edit patient button present beside the name of the patient, the administrator is redirected to an update patient form prepopulated with the current entries in the database. At this point changes can be made and update can be submitted. The same form validations are present as the insert patient form.

The clinic administrator needs to delete a patient. Upon launching the app, the administrator can either scroll to or search for the patient. By clicking the view/edit patient button present beside the name of the patient, the administrator is redirected to an update patient form prepopulated with the current entries in the database. At this point changes the delete patient button can be used to delete the patient.

The clinic administrator wants to add a doctor from the clinic database. Upon launching the app the manage doctors button present in the footer can be used to redirect to a page with all the clinic doctors. At this point the add doctor form can be used to input a name and the submitted. The page will refresh and provide instant confirmation of the doctor that has been added to the database.

The clinic administrator wants to remove a doctor from the clinic database. Upon launching the app the manage doctors button present in the footer can be used to redirect to a page with all the clinic doctors. At this point the administraor can use the delete button to remove a doctor from the database.

## Features

### Patients

The patients view is the default view upon launching the app. This is intentionally done as this is a patient database and all the patients should be listed upon launch. The consistent header and footer provide further ways to navigate to other important sections of the app. Each patient also has a view/edit button beside the entry to allow to attain and update further information about the patient.

### Search Patients

The search patients function present in the header allows the administrator quick access to conduct a search. Currently the search functionality is limited to first name, last name, and health card number. However, further search types will be added. The search only allows for exact matches at the moment. Again, a partial match functionality will be implemented in a future update.

### Add Patient

The add patient button is easily accessible from any page as it is available in the header. The add patient page features a simple to use form with all fields deemed required. Validation is implemented wherever neccessary. For example, the health card number is must be 8 numerical characters and a phone number must be 10 numerical characters. Other input type validation is implemented such as for email and tel.

### View/Edit Patient

The view/edit patient view features a form identical to that on the add patient view. However, this form is prepopulated with information stored in the database. This view allows the administrator to attain information about the patient or to update it if they choose to do so. This page also features a delete patient button that allows the entry to be removed from the database. When conducting an update, the form features the same validation features as the insert patient form.

### Manage Doctors

The manage doctors section can be reached by the manage doctors button present in the footer of every page. This page allows the administrator to add or delete doctors that are present at the clinic. The change is automatically updated in the patient form allowing the new or existing patients to be updated with the correct doctor.

### Features Left to Implement

A login fucntionality should be added to keep out users that are not authorized to access the database. Alongside a user authentication fucntion, a last updated by and time will be added to the patient database to store infrormation about who edited the patient last and when the edit was made.

A more robust search functionality should be included that allows for partial match. It would also be wise to an advanced search functionality that allows for multiple filtering options.

## Technologies used

HTML - Used to build basic content of the website
CSS - Used for complete styling of the website 
Bootstrap - Used to apply layout style to the website
Python - Used to create the app
MongoDB - Used as a database to store the data
Flask - To create the connection between Python app and MongoDB
Font Awesome - Used to insert icons on the page

## Testing

The forms were tested thoroughly tested to insert incorrect values but the form performed well and the database was able to handle the information correctly.

The webstie was throuhghly tested in multiple browsers (Firefox, Chrome, Edge, Safari, and IE). The website responsiveness acted correctly in all browsers.

The website was also observed in many different mobile and tablet resolution using Google Developer Tools, again acting as expected. The app is completely responsive. 

The website was tested in W3C HTML & CSS validators and no errors were realized.

## Deployment

The website was pushed to github using gitpod. Once the final version of the website was committed and pushed, the website was hosted using heroku. 

Please find the live website here: https://mcqueen-clinic.herokuapp.com/

Currently the live version and development versions are identical. 

## Credits

### Content

All text content was created by myself. No content was copied from elsewhere.

### Media 

Font Awesome was used to insert icons on to the page.

### Acknowledgements

Code Institute - Learning from the code institute program were applied
W3 Schools - Used as a constant reference for code
