# Activity 1: Inheritance Basics

## 1. Parent Class of the Programmer Class
The parent class of the `Programmer` class is the `Employee` class. 

### Explanation:
In programming, inheritance follows real-world relationships. A programmer is a specific type of worker, so it makes sense for it to inherit from a broader class that covers all types of workers, which is the `Employee` class.

---

## 2. Where to Place the `Intern` Class
The `Intern` class should be placed directly under the `Employee` class, making it a sibling to the `Programmer` class.

### Why?
* An Intern is an Employee: Interns share common employee traits like having a department, a supervisor, and a daily schedule. 
* Not all Interns are Programmers: If you place `Intern` under `Programmer`, it means every single intern in the company has to be a coder. By placing it under `Employee`, you can have different types of interns, such as a Marketing Intern, an HR Intern, or a Programming Intern.
