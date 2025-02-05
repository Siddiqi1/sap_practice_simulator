import streamlit as st
import pandas as pd

# Simulated contract database
data = {
    "Contract ID": ["C-1001", "C-1002", "C-1003"],
    "Customer": ["Air Force", "NASA", "Boeing"],
    "Type": ["Fixed Rate", "Time & Materials", "Cost-Based"],
    "Status": ["Active", "Pending", "Completed"],
    "Billing Amount": [500000, 200000, 750000]
}

# Convert to DataFrame
contracts_df = pd.DataFrame(data)

# Streamlit UI
st.title("SAP-Like Contract Management Simulator")
st.sidebar.header("Navigation")
option = st.sidebar.selectbox("Select Operation", ["View Contracts", "Create Contract", "Billing", "Vendor Payments", "Execute T-Code"])

if option == "View Contracts":
    st.subheader("Contract Database")
    st.dataframe(contracts_df)

elif option == "Create Contract":
    st.subheader("Create New Contract")
    customer = st.text_input("Customer Name")
    contract_type = st.selectbox("Contract Type", ["Fixed Rate", "Time & Materials", "Cost-Based"])
    billing_amount = st.number_input("Billing Amount", min_value=0)
    if st.button("Save Contract"):
        new_contract = pd.DataFrame({
            "Contract ID": [f"C-{len(contracts_df) + 1001}"],
            "Customer": [customer],
            "Type": [contract_type],
            "Status": ["Pending"],
            "Billing Amount": [billing_amount]
        })
        contracts_df = pd.concat([contracts_df, new_contract], ignore_index=True)
        st.success("Contract Created Successfully!")

elif option == "Billing":
    st.subheader("Process Billing Document")
    contract_id = st.selectbox("Select Contract", contracts_df["Contract ID"])
    if st.button("Generate Billing Document"):
        st.success(f"Billing document created for Contract {contract_id}!")

elif option == "Vendor Payments":
    st.subheader("Vendor Down-Payment Processing")
    vendor = st.text_input("Vendor Name")
    amount = st.number_input("Payment Amount", min_value=0)
    if st.button("Process Payment"):
        st.success(f"Payment of ${amount} processed for {vendor}!")

elif option == "Execute T-Code":
    st.subheader("SAP-Like T-Code Execution")
    tcode = st.text_input("Enter T-Code (e.g., VA41, VF01, SE16N)")
    if st.button("Execute"):
        if tcode in ["VA41", "VF01", "SE16N", "ME21N"]:
            st.success(f"Simulated execution of transaction: {tcode}")
        else:
            st.error("Invalid T-Code or feature not yet implemented.")
