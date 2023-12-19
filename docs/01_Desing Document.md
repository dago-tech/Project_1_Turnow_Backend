# Turnow Application


## Summary
This document sets out the initial guidelines for developing a turn management software application. It is proposed to make its backend in Django RestFramework and its frontend in React JS.
...

## General objective

Design a generic turn management application to ease and optimize the attention and/or provision of services in different types of organizations or companies, allowing better organization, control and attention to users or clients.

***
## Expectations

- Enable greater control: The application will provide better visibility and control of turn scheduling, which can help organizations better plan their resources and optimize care.

- Enhance efficiency in customer service: The application can allow better management of turns, helping organizations provide services more efficiently.

- Deliver an improved user experience: A well-designed app can provide an engaging and easy-to-use user experience, which can increase app adoption and usage.

- Increase user satisfaction: By improving service efficiency and assigning turns more easily and quickly, end-user satisfaction can increase.

***
## Scope

**Turn management**: The application must allow users to obtain a turn in person and also allow employees or managers of the organization to manage turns, modify them or cancel them if necessary.

**Notifications**: The application must send notifications on a screen to clients.

**Customization**: The application must allow each organization to customize its configuration, for example, defining the hours of operation, the services available, the number of turns that can be issued per day, number of modules.

**Monitoring**: The application must allow employees or managers of the organization to monitor the status of turns, in order to anticipate possible problems and improve customer service.

**Data analysis**: The application must allow the collection and analysis of data on customer service, such as average waiting time, number of shifts attended per day, customer satisfaction, among others.

**Security**: It is important to guarantee the security of users' personal data and the organization's sensitive information. Security measures, such as user authentication and data encryption, should be implemented to prevent potential security threats.

**User Interface**: The user interface should be intuitive, easy to use, and visually appealing. Users should be able to quickly understand how to use the app and perform actions seamlessly.
***

## Proposed and alternative solution

To achieve this, it is necessary to develop an intuitive and easy-to-use user interface so that users can request their turn and receive notifications about the status of their turn. In addition, a screen must be developed to display the current turns and the address of the corresponding service desk.

On the other hand, a screen must be developed for the administration of turns, where employees or managers of the organization can manage the turns, modify them or cancel them if necessary. It is also important to have a screen for attending turns in the corresponding specific service desk.

Regarding the categorization of shifts, a system must be implemented that allows different categories of turns to be assigned depending on the type of service to be requested or the priority given by the organization. In this way, efficiency in customer service can be improved and waiting time reduced.
 
***
   

## Boundaries

- The database will save a limited number of records over time.
- Only one user can register at a time.
- Reports will be generated daily, weekly and monthly. However, they will only be stored for a period of one month, since they will be sent to the email assigned as a management role.

