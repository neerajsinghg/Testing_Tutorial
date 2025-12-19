/**
 * Here’s a list of Java programs related to **Identifiers**:

### **Basic Identifier Usage**
1. **Valid and Invalid Identifiers** – Demonstrate valid and invalid identifier names.
2. **Case Sensitivity of Identifiers** – Show how Java treats `Var`, `var`, and `VAR` as different identifiers.
3. **Usage of Identifiers in Variables** – Declare and use variables with different types of valid identifiers.
4. **Identifiers in Methods** – Create methods using meaningful identifiers.
5. **Class and Object Identifiers** – Define a class and create objects with proper naming conventions.
6. **Constant Identifiers** – Use `final` keyword to define constant identifiers (e.g., `final int MAX_VALUE = 100;`).

### **Identifier Scope and Access Modifiers**
7. **Local and Global Identifiers** – Demonstrate variable scope with different identifiers.
8. **Static Identifiers** – Show the use of static variables and methods.
9. **Private vs Public Identifiers** – Use different access modifiers to define class variables and methods.

### **Identifiers in OOP Concepts**
10. **Class and Method Identifiers in Inheritance** – Use identifiers in base and derived classes.
11. **Identifiers in Polymorphism** – Use method overloading and overriding with different method identifiers.
12. **Identifiers in Interfaces** – Define an interface and implement it in a class.
13. **Identifiers in Abstract Classes** – Use abstract method identifiers.

### **Identifiers in Java Best Practices**
14. **Camel Case and Naming Conventions** – Follow best practices in naming variables, classes, and methods.
15. **Identifiers in Packages** – Define a custom package and use meaningful package names.
16. **Identifiers in Exception Handling** – Use descriptive identifiers in `try-catch-finally` blocks.

Would you like me to provide a sample program for any of these topics? 🚀
 */
package java_question;

//Package Identifier
//package com.example.identifiers;

//Class Identifier
public class IdentifierExample {

 // Constant Identifier (final keyword used for constants)
 private static final int MAX_COUNT = 5;

 // Instance Variable Identifiers
 private String studentName;
 private int studentAge;

 // Constructor Identifier (same as class name)
 public IdentifierExample(String name, int age) {
     this.studentName = name;
     this.studentAge = age;
 }

 // Static Method Identifier
 public static void displayMaxCount() {
     System.out.println("Max count allowed: " + MAX_COUNT);
 }

 // Instance Method Identifier
 public void displayStudentInfo() {
     System.out.println("Student Name: " + studentName);
     System.out.println("Student Age: " + studentAge);
 }

 // Method Overloading (Polymorphism - same method name but different parameters)
 public void displayStudentInfo(String extraInfo) {
     System.out.println("Student Name: " + studentName + ", " + extraInfo);
 }

 // Inner Class Identifier
 class InnerClass {
     void showMessage() {
         System.out.println("This is an inner class example.");
     }
 }

 public static void main(String[] args) {
     // Object Identifiers
     IdentifierExample student1 = new IdentifierExample("John Doe", 20);
     IdentifierExample student2 = new IdentifierExample("Jane Doe", 22);

     // Calling Static Method
     displayMaxCount();

     // Calling Instance Methods
     student1.displayStudentInfo();
     student2.displayStudentInfo("Excellent Performer");

     // Working with Inner Class
     IdentifierExample.InnerClass innerObj = student1.new InnerClass();
     innerObj.showMessage();
 }
}


