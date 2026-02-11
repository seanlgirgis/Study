# 1. Realistic J2EE: From EJB to Spring Boot

## The "Old" J2EE vs. The "Real" World
When people say "J2EE" (Java 2 Platform, Enterprise Edition), they often mean the *enterprise capability* of Java, not necessarily the specific ancient technologies like EJB 2.0 (Entity Java Beans) or heavy XML configuration.

Modern Enterprise Java (now formally **Jakarta EE** but dominated by **Spring Boot**) focuses on:
1.  **Dependency Injection (DI)**: Components don't create their dependencies; they are given to them (e.g., `@Autowired`).
2.  **AOP (Aspect Object Programming)**: Handling cross-cutting concerns like logging and transactions separately from business logic.
3.  **REST APIs**: Stateless communication over HTTP, replacing older SOAP/RMI protocols.
4.  **Microservices / Modular Monoliths**: Breaking down massive "EAR" (Enterprise Archive) files into smaller, deployable JARs.

## Key Components in a Realistic App
In our target application, we will simulate these layers:

| Layer | Responsibility | Annotation/Tech |
| :--- | :--- | :--- |
| **Controller** | Handles HTTP Requests (Input/Output). | `@RestController`, `@GetMapping` |
| **Service** | Contains the Business Logic & Transactions. | `@Service`, `@Transactional` |
| **Repository** | Talks to the Database (DAO pattern). | `@Repository`, `Spring Data JPA` |
| **Entity** | Represents the Database Table. | `@Entity`, `@Table` |

## Why Performance Matters Here?
In "Real" J2EE, performance bottlenecks usually happen in:
-   **Database Connections**: Running out of potential connections in the pool (HikariCP).
-   **Synchronous Blocking**: Waiting for a long 3rd party API call or complex calculation.
-   **Memory Leaks**: Keeping too many objects in the Heap.

We will simulate a **Blocking** scenario in our test app to demonstrate how JMeter can find the "breaking point" of a Thread Pool.
