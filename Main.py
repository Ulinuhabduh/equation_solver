import streamlit as st
from sympy import symbols, Eq, solve, sympify, latex, N


def solve_equation(equation_input, variable_input, convert_numeric):
    try:
        if "=" in equation_input:
            left_expr, right_expr = equation_input.split("=")
        else:
            left_expr, right_expr = equation_input, "0"

        left_expr = sympify(left_expr)
        right_expr = sympify(right_expr)
        equation = Eq(left_expr, right_expr)

        variable = symbols(variable_input)
        solutions = solve(equation, variable)

        if convert_numeric:
            numeric_solutions = [N(sol) for sol in solutions]
            return numeric_solutions
        else:
            return solutions
    except Exception as e:
        return str(e)


def main():
    st.set_page_config(page_title="Equation Solver", page_icon="🔢")

    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #2E3440;
            font-family: 'Arial', sans-serif;
            padding: 20px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.5);
            color: #D8DEE9;
        }
        h1 {
            color: #88C0D0;
            text-align: center;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #5E81AC;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px 2px;
            cursor: pointer;
            transition-duration: 0.4s;
        }
        .stButton>button:hover {
            background-color: white;
            color: black;
            border: 2px solid #5E81AC;
        }
        .stTextInput>div>div>input {
            border-radius: 5px;
            border: 1px solid #4C566A;
            padding: 10px;
            background-color: #434C5E;
            color: #D8DEE9;
        }
        .stTextInput>div>div>input:focus {
            border-color: #81A1C1;
            box-shadow: 0px 0px 5px rgba(129, 161, 193, 0.5);
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

    st.title("Equation Solver 🔢")

    st.info(
        """
    **Selamat datang di Equation Solver!**  
    Aplikasi ini memungkinkan Anda untuk menyelesaikan persamaan matematika apapun dengan mudah. Cukup masukkan persamaan dan variabel yang ingin Anda selesaikan, dan biarkan aplikasi ini melakukan sisanya.
    """
    )

    st.markdown("---")

    persamaan_input = st.text_input(
        "Masukkan persamaan (misal, x**2 - 5*x + 6 = 0):", "x**2 - 5*x + 6 = 0"
    )

    variabel_input = st.text_input(
        "Masukkan variabel yang ingin diselesaikan (misal, x):", "x"
    )

    convert_numeric = st.checkbox("Konversi solusi ke bentuk numerik", False)

    if st.button("Solusi"):
        solusi = solve_equation(persamaan_input, variabel_input, convert_numeric)

        if isinstance(solusi, list):
            st.write("Solusi:")
            for i, sol in enumerate(solusi, start=1):
                st.latex(latex(sol))
        else:
            st.error(f"Error: {solusi}")

    st.markdown("---")

    st.write("Dibuat oleh ***M Ulin Nuha Abduh*** dengan ❤️ menggunakan Streamlit")

# Menjalankan aplikasi
if __name__ == "__main__":
    main()
