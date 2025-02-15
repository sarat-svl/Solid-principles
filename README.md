### Why Use SOLID?
* Makes code easier to maintain and scale.
* Improves code readability and reusability.
* Encourages loosely coupled and extensible design.
* Helps in writing testable and modular code.

&nbsp;

| Principle | Concept |
| --- | --- |
| **S**ingle Responsibility | A class should have only **one reason to change** |
| **O**pen/Closed | Code should be **open for extension, closed for modification** |
| **L**iskov Substitution | Subclasses should be **replaceable** for their base class |
| **I**nterface Segregation | Don’t force classes to **implement unused methods** |
| **D**ependency Inversion | Depend on **abstractions, not concrete implementations** |

&nbsp;

### 🛒 Problem Statement

We need to design an Order Processing System where:
- Orders can be processed via different payment methods (Credit Card, PayPal, etc.).
- Orders can have different shipping methods (Standard, Express).
- Order notifications (Email, SMS) should be sent to customers.
- The system should be extensible for new payment/shipping/notification methods.
