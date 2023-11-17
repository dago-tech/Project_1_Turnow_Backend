# Use cases

There are two types of application users

1. End client user: from now on will only be called __client__. This client refers to the clients of the institutions that use the application.

2. Institutional client user: from now on it will be called __user__. It makes references to the users registered by the institution that acquired the __TurNow__ application, which have different types of access and roles within it.

***
## Client => Use cases

- The client can request a turn in person to be served according to their needs and according to the turn structure established by the institution.

- The client can view on a screen which turns are being served at the moment and which service desk they are in. On the same screen you can see when your turn is assigned to a service desk.


### Use cases not supported

- The client will not be able to request a turn outside the physical offices or virtually.

- The client will not be able to request to reschedule their turn if they are not present at the time of their assignment.


***
## User => Use cases

__Administrator role__:

- Can create users, this new user can have an administrator role or a service desk role, also can modify any user's information. 
- Can create categories for the different types of services provided and clients.
- Can define the priority of clients (elderly, disability, etc., registered or unregistered clients)
- Can configure the different service desks and assign them the different service categories with their respective service priorities.
- Can add new service desks
- Can see daily, weekly and/or monthly statistics of the number of turns attended, categories of turns, waiting times, service priorities, service time in service desk, among others. The statistics are not in real time and are generated daily once the workday has ended. (Future feature)

__Service desk role__:

- The service desk user can see on a screen the first turn to serve and after attention he will mark it as served once he has done it.
- The service desk user can also reassign a turn to another service desk if necessary, for example if the service the user needs cannot be provided in that specific service desk.(Future feature)


### Use cases not supported

- Service desk users cannot create new users, neither they can modify any user's information
