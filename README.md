a POC service called user service to test agentic SDLC 

This service provides a REST API for managing users. The existing /api/users endpoint returns a list of users, and the new /api/version endpoint returns the version information as "1.0.0".

To run the application:

* Start the MySQL server
* Run the command `mvn spring-boot:run` in the project root directory
* Access the API at http://localhost:8080/api/users or http://localhost:8080/api/version
