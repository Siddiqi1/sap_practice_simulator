import streamlit as st
import pandas as pd

# Initialize session state for contract data persistence
if "contracts" not in st.session_state:
    st.session_state.contracts = pd.DataFrame({
        "Contract ID": ["C-1001", "C-1002", "C-1003"],
        "Customer": ["Air Force", "NASA", "Boeing"],
        "Type": ["Fixed Rate", "Time & Materials", "Cost-Based"],
        "Status": ["Active", "Pending", "Completed"],
        "Billing Amount": [500000, 200000, 750000]
    })

# Streamlit UI - Make it look more like SAP GUI
st.set_page_config(layout="wide", page_title="SAP-Like GUI Simulator")
st.markdown("""
    <style>
        .main {background-color: #f4f4f4; padding: 20px; border-radius: 10px;}
        .sidebar .sidebar-content {background-color: #0a3d62; color: white;}
        .css-1d391kg {background-color: #f4f4f4;}
        .stButton>button {background-color: #0a3d62; color: white; border-radius: 5px;}
    </style>
""", unsafe_allow_html=True)

st.sidebar.header("SAP-Like Navigation")
option = st.sidebar.selectbox("Select T-Code", [
    "VA01 - Create Sales Order", "VA41 - Create Contract", "VF01 - Billing Document",
    "ME21N - Create Purchase Order", "SE16N - Table Data Viewer", "F-47 - Vendor Down-Payment",
    "F-48 - Vendor Payment", "F-54 - Down Payment Clearing", "MIGO - Goods Movement",
    "MIRO - Invoice Verification"])

if option == "VA41 - Create Contract":
    st.title("VA41 - Create Contract")
    customer = st.text_input("Customer Name")
    contract_type = st.selectbox("Contract Type", ["Fixed Rate", "Time & Materials", "Cost-Based"])
    billing_amount = st.number_input("Billing Amount", min_value=0)
    if st.button("Create Contract"):
        if customer.strip() == "":
            st.error("Customer name cannot be empty.")
        else:
            new_contract = pd.DataFrame({
                "Contract ID": [f"C-{len(st.session_state.contracts) + 1001}"],
                "Customer": [customer],
                "Type": [contract_type],
                "Status": ["Pending"],
                "Billing Amount": [billing_amount]
            })
            st.session_state.contracts = pd.concat([st.session_state.contracts, new_contract], ignore_index=True)
            st.success("Contract Created Successfully!")

elif option == "VF01 - Billing Document":
    st.title("VF01 - Billing Document Processing")
    if not st.session_state.contracts.empty:
        contract_id = st.selectbox("Select Contract", st.session_state.contracts["Contract ID"])
        if st.button("Generate Billing Document"):
            st.success(f"Billing document created for Contract {contract_id}!")
    else:
        st.warning("No contracts available for billing.")

elif option == "ME21N - Create Purchase Order":
    st.title("ME21N - Create Purchase Order")
    vendor = st.text_input("Vendor Name")
    material = st.text_input("Material/Service")
    quantity = st.number_input("Quantity", min_value=1)
    price = st.number_input("Unit Price", min_value=0)
    if st.button("Create Purchase Order"):
        st.success(f"Purchase Order created for {vendor}, Material: {material}, Quantity: {quantity}, Price: {price}")

elif option == "SE16N - Table Data Viewer":
    st.title("SE16N - Table Data Viewer")
    st.dataframe(st.session_state.contracts)

elif option == "F-47 - Vendor Down-Payment":
    st.title("F-47 - Vendor Down-Payment")
    vendor = st.text_input("Vendor Name")
    amount = st.number_input("Down Payment Amount", min_value=0)
    if st.button("Process Down Payment"):
        st.success(f"Down payment of ${amount} recorded for vendor {vendor}.")

elif option == "F-48 - Vendor Payment":
    st.title("F-48 - Vendor Payment Processing")
    vendor = st.text_input("Vendor Name")
    amount = st.number_input("Payment Amount", min_value=0)
    if st.button("Process Payment"):
        st.success(f"Payment of ${amount} processed for vendor {vendor}.")

elif option == "MIGO - Goods Movement":
    st.title("MIGO - Goods Movement")
    material = st.text_input("Material Code")
    quantity = st.number_input("Quantity", min_value=1)
    location = st.text_input("Storage Location")
    if st.button("Confirm Goods Movement"):
        st.success(f"Goods movement for Material {material}, Quantity {quantity} to {location} recorded.")

elif option == "MIRO - Invoice Verification":
    st.title("MIRO - Invoice Verification")
    vendor = st.text_input("Vendor Name")
    invoice_amount = st.number_input("Invoice Amount", min_value=0)
    if st.button("Verify Invoice"):
        st.success(f"Invoice of ${invoice_amount} verified for vendor {vendor}.")
