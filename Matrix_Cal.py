import customtkinter as ctk
import numpy as np


class MatrixCalculatorApp(ctk.CTk):

    def add_matrices(self):
        try:
            result = 0
            for i in range(len(self.matrices)):
                if self.matrices[0].shape != self.matrices[i].shape:
                    raise ValueError("Matrices must have the same dimensions for addition.")

            # Perform the addition
            for i in range(len(self.matrices)):
                result = np.add(result,self.matrices[i])

            # Display the result
            self.display_result(f"Matrix Addition Result:\n{result}\n\nFlattened Matrix : {result.flatten()}\nShape Of Matrix : {result.shape}")
        except Exception as e:
            self.display_result(f"Error: {e}")

    def subtract_matrices(self):
        try:
            for i in range(len(self.matrices)):
                if self.matrices[0].shape != self.matrices[i].shape:
                    raise ValueError("Matrices must have the same dimensions for subtraction.")

            # Perform the subtraction
            for i in range(len(self.matrices) - 1):
                result = np.subtract(self.matrices[0], self.matrices[i+1])

            # Display the result
            self.display_result(
                f"Matrix Subtraction Result:\n{result}\n\nFlattened Matrix : {result.flatten()}\nShape Of Matrix : {result.shape}")
        except Exception as e:
            self.display_result(f"Error: {e}")

    def multiply_matrices(self):
        try:
            # Perform multiplication
            for i in range(len(self.matrices) - 1):
                result = np.multiply(self.matrices[0], self.matrices[i+1])

            # Display the result
            self.display_result(
                f"Matrix Subtraction Result:\n{result}\n\nFlattened Matrix : {result.flatten()}\nShape Of Matrix : {result.shape}")
        except Exception as e:
            self.display_result(f"Error: {e}")

    def determinant_matrix(self):
        try:
            answers = """ """
            for i in range(len(self.matrices)):
                if (self.matrices[i].shape)[0] != (self.matrices[i].shape)[1]:
                    raise ValueError("Matrices must be square matrices for determinant.")

            # Perform the determinant calculation
            for i in range(len(self.matrices)):
                result = np.linalg.det(self.matrices[i])

                # Round the result to an integer if it's very close
                if np.isclose(result, round(result)):
                    result = int(round(result))

                answers += f"{i + 1}. Matrix determinant Result: {result}\n{"-"*200}\n"

            # Display the result
            self.display_result(answers)
        except Exception as e:
            self.display_result(f"Error: {e}")

    def inverse_matrix(self):
        try:
            answers = """ """

            for i in range(len(self.matrices)):
                if self.matrices[i].shape[0] != self.matrices[i].shape[1]:
                    result = "Matrices must be square matrices for Inverse."
                else:
                    dete = np.linalg.det(self.matrices[i])
                    if np.isclose(dete, round(dete)):
                        dete = int(round(dete))
                    if dete != 0:
                        result = np.linalg.inv(self.matrices[i])
                    else:
                        result = "Inverse not possible !"

                answers += f"{i + 1}.Matrix Inverse Result:\n{result}\n\nFlattened Matrix : {result.flatten()}\nShape Of Matrix : {result.shape}\n{"-"*200}\n"

            # Display the result
            self.display_result(answers)
        except Exception as e:
            self.display_result(f"Error: {e}")

    def transpose_matrix(self):
        try:
            answers = """ """
            for i in range(len(self.matrices)):
                result = np.linalg.matrix_transpose(self.matrices[i])

                answers += f"{i + 1}.Matrix Transpose Result:\n{result}\n\nFlattened Matrix : {result.flatten()}\nShape Of Matrix : {result.shape}\n{"-"*200}\n"

            # Display the result
            self.display_result(answers)
        except Exception as e:
            self.display_result(f"Error: {e}")

    def adjoint(self):
        answers = """ """
        for k in range(len(self.matrices)):
            try:
                if self.matrices[k].shape[0] != self.matrices[k].shape[1]:
                    result = "Matrix must be square to compute its adjoint."
                else:
                    cofactor_matrix = np.zeros_like(self.matrices[k], dtype=float)
                    n = self.matrices[k].shape[0]

                    for i in range(n):
                        for j in range(n):
                            # Minor matrix (excluding row i and column j)
                            minor = np.delete(np.delete(self.matrices[k], i, axis=0), j, axis=1)
                            # Cofactor value
                            cofactor_matrix[i, j] = ((-1) ** (i + j)) * np.linalg.det(minor)

                    result = cofactor_matrix.T
                answers += f"{k + 1}.Matrix Adjoint Result:\n{result}\n\nFlattened Matrix : {result.flatten()}\nShape Of Matrix : {result.shape}\n{"-" * 200}\n"

            except Exception as e:
                self.display_result(f"Error: {e}")
        self.display_result(answers)

    def sqaure(self):
        answers = """"""
        try:
            for i in range(len(self.matrices)):
                result = np.linalg.matrix_power(self.matrices[i],2)
                answers += f"{i+ 1}.Matrix Square Result:\n{result}\n\nFlattened Matrix : {result.flatten()}\nShape Of Matrix : {result.shape}\n{"-" * 200}\n"
            self.display_result(answers)
        except Exception as e:
            self.display_result(e)

    def add_placeholder(self, placeholder_text):
        def on_focus_in(event):
            if self.matrix_input_text.get("1.0", "end-1c") == placeholder_text:
                self.matrix_input_text.delete("1.0", "end")
                self.matrix_input_text.configure(fg_color="black")  # Change text color for user input

        def on_focus_out(event):
            if self.matrix_input_text.get("1.0", "end-1c") == "":
                self.matrix_input_text.insert("1.0", placeholder_text)
                self.matrix_input_text.configure(fg_color="gray")  # Change text color for placeholder

        # Set initial placeholder text
        self.matrix_input_text.insert("1.0", placeholder_text)
        self.matrix_input_text.configure(fg_color="gray")  # Change text color for placeholder

        # Bind events
        self.matrix_input_text.bind("<FocusIn>", on_focus_in)
        self.matrix_input_text.bind("<FocusOut>", on_focus_out)

    def __init__(self):
        super().__init__()
        self.title("Matrix Calculator")
        self.geometry("700x620")

        # Input Section
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(pady=10, fill="both", expand=True)

        self.matrix_input_label = ctk.CTkLabel(self.input_frame, text="Enter Matrix Data (Format: see example below):")
        self.matrix_input_label.pack(anchor="w", padx=10)

        # Textarea for matrix input
        self.matrix_input_text = ctk.CTkTextbox(self.input_frame, width=600, height=150)
        self.matrix_input_text.pack(pady=10, padx=10, fill="x")

        self.submit_button = ctk.CTkButton(self.input_frame, text="Process Input", command=self.process_input)
        self.submit_button.pack(pady=10)

        # Operations Section
        self.operations_frame = ctk.CTkFrame(self)
        self.operations_frame.pack(pady=10)

        self.add_button = ctk.CTkButton(self.operations_frame, text="Add", command=self.add_matrices)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.subtract_button = ctk.CTkButton(self.operations_frame, text="Subtract", command=self.subtract_matrices)
        self.subtract_button.grid(row=0, column=1, padx=5, pady=5)

        self.multiply_button = ctk.CTkButton(self.operations_frame, text="Multiply", command=self.multiply_matrices)
        self.multiply_button.grid(row=0, column=2, padx=5, pady=5)

        self.determinant_button = ctk.CTkButton(self.operations_frame, text="Determinant", command=self.determinant_matrix)
        self.determinant_button.grid(row=0, column=3, padx=5, pady=5)

        self.inverse_button = ctk.CTkButton(self.operations_frame, text="Inverse", command=self.inverse_matrix)
        self.inverse_button.grid(row=1, column=0, padx=5, pady=5)

        self.transpose_button = ctk.CTkButton(self.operations_frame, text="Transpose", command=self.transpose_matrix)
        self.transpose_button.grid(row=1, column=1, padx=5, pady=5)

        self.adjoint_button = ctk.CTkButton(self.operations_frame, text="Adjoint", command=self.adjoint)
        self.adjoint_button.grid(row=1, column=2, padx=5, pady=5)

        self.square_button = ctk.CTkButton(self.operations_frame, text="Square", command=self.sqaure)
        self.square_button.grid(row=1, column=3, padx=5, pady=5)

        # Output Section
        self.output_frame = ctk.CTkFrame(self)
        self.output_frame.pack(pady=10, fill="both", expand=True)

        self.result_label = ctk.CTkLabel(self.output_frame, text="Result:")
        self.result_label.pack(anchor="w", padx=10)

        self.result_display = ctk.CTkTextbox(self.output_frame, width=600, height=150)
        self.result_display.pack(pady=10, padx=10, fill="x")
        self.result_display.configure(state="disabled")  # Make result display read-only

    def process_input(self):
        # Get the input from the textarea
        input_data = self.matrix_input_text.get("1.0", "end").strip()

        try:
            # Parse and process the input data
            lines = input_data.splitlines()
            num_matrices = int(lines[0])
            matrices = []
            idx = 1

            for _ in range(num_matrices):
                dimensions = list(map(int, lines[idx].split()))
                rows, cols = dimensions
                idx += 1
                flat_data = list(map(int, lines[idx].split()))
                matrix = np.array(flat_data).reshape(rows, cols)
                matrices.append(matrix)
                idx += 1

            # Store matrices for later operations
            self.matrices = matrices

            # Display matrices (for testing or debugging)
            result = "Matrices Processed:\n"
            for i, mat in enumerate(matrices, 1):
                result += f"Matrix {i}:\n{mat}\n"

            self.display_result(result)
        except Exception as e:
            self.display_result(f"Error in input: {e}")

    def display_result(self, result):
        self.result_display.configure(state="normal")
        self.result_display.delete("1.0", "end")
        self.result_display.insert("1.0", result)
        self.result_display.configure(state="disabled")


# Run the app
if __name__ == "__main__":
    placetext = '''Example Input:\n2 - Number of matrix\n2 2 - Shape of matrix\n1 2 3 4 - Flattened Matrix\n2 2 - Shape of matrix\n9 8 7 6 - Flattened Matrix\n'''
    app = MatrixCalculatorApp()
    app.add_placeholder(placetext)
    app.mainloop()
