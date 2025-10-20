import streamlit as st

# Page configuration
st.set_page_config(page_title="🧮 Calculator App", page_icon="🧮", layout="centered")

# App title
st.title("🧮 Simple Calculator")
st.write("Perform basic arithmetic operations easily!")

# Input fields
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter first number:", value=0.0, format="%.4f")
with col2:
    num2 = st.number_input("Enter second number:", value=0.0, format="%.4f")

# Operation selection
operation = st.selectbox("Select operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculation logic
if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                st.error("❌ Cannot divide by zero.")
                result = None
            else:
                result = num1 / num2
        if result is not None:
            st.success(f"✅ Result: {result:.4f}")
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")

# Footer
st.markdown("---")
st.caption("Created with ❤️ using Streamlit")
