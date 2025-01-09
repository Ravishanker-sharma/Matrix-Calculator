# Matrix-Calculator
This project is a GUI-based Matrix Calculator built using Python and the CustomTkinter library. It allows users to input multiple matrices and perform various matrix operations with a user-friendly interface. The application is designed to handle mathematical matrix operations efficiently while providing detailed results, including flattened arrays and matrix shapes.

## Features
* **Matrix Addition:** Adds multiple matrices of the same dimensions.
* **Matrix Subtraction:** Subtracts one matrix from another.
* **Matrix Multiplication:** Element-wise multiplication of matrices.
* **Determinant Calculation:** Computes the determinant of square matrices.
* **Matrix Inversion:** Calculates the inverse of square matrices (if possible).
* **Matrix Transposition:** Computes the transpose of matrices.
* **Adjoint Calculation:** Computes the adjoint (adjugate) of square matrices.
* **Matrix Square:** Calculates the square of matrices.
* **Input Parsing:** Accepts matrix data in a structured format and dynamically processes it.
## How It Works
1. Enter the number of matrices, their dimensions, and their flattened data into the input field following the placeholder example format.
2. Click "Process Input" to parse and store the matrices.
3. Use the operation buttons to perform calculations such as addition, subtraction, multiplication, determinant, and more.
4. Results are displayed in a dedicated read-only output field.
## Example Input
```
2
2 2
1 2 3 4
2 2
9 8 7 6
```
## Technologies Used
* **Python:** Core language for the application.
* **NumPy:** For matrix operations and numerical computations.
* **CustomTkinter:** For creating the modern and responsive GUI.
