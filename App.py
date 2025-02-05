import streamlit as st
import pandas as pd

# Initialize session state for multi-step navigation and contract data persistence
if "current_tcode" not in st.session_state:
    st.session_state.current_tcode = None
if "step" not in st.session_state:
    st.session_state.step = 1
if "contracts" not in st.session_state:
    st.session_state.contracts = pd.DataFrame({
        "Contract ID": ["C-1001", "C-1002", "C-1003"],
        "Customer": ["Air Force", "NASA", "Boeing"],
        "Type": ["Fixed Rate", "Time & Materials", "Cost-Based"],
        "Status": ["Active", "Pending", "Completed"],
        "Billing Amount": [500000, 200000, 750000]
    })

# SAP GUI Layout - Enhanced UI with SAP Theme
st.set_page_config(layout="wide", page_title="SAP GUI Full Simulator")
st.markdown("""
    <style>
        body {
            background-color: #f0f2f5;
            font-family: Arial, sans-serif;
        }
        .toolbar {
            background-color: #0a3d62; 
            color: white; 
            padding: 10px; 
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
        }
        .search-bar {
            padding: 5px;
            width: 200px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        .sap-table {
            background-color: white;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
    </style>
""", unsafe_allow_html=True)

# Toolbar with search and navigation buttons
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    if st.button("⬅ Go Back"):
        if st.session_state.step > 1:
            st.session_state.step -= 1
with col2:
    if st.button("➡ Go Forward"):
        st.session_state.step += 1
with col3:
    if st.button("🔄 Refresh"):
        st.session_state.current_tcode = None
        st.session_state.step = 1
with col4:
    st.text_input("🔍 Search", placeholder="Enter T-Code or Description")
with col5:
    st.button("Extras")

# SAP Navigation with detailed T-Code list
st.sidebar.header("SAP T-Code Navigation")
tcode = st.sidebar.selectbox("Select T-Code", [
    "VA01 - Create Sales Order", "VA41 - Create Contract", "VF01 - Billing Document",
    "ME21N - Create Purchase Order", "SE16N - Table Data Viewer", "F-47 - Vendor Down-Payment",
    "F-48 - Vendor Payment", "F-54 - Down Payment Clearing", "MIGO - Goods Movement",
    "MIRO - Invoice Verification", "FB50 - General Ledger Posting", "CO01 - Create Production Order", 
    "MM01 - Create Material Master", "XD01 - Create Customer", "XK01 - Create Vendor"])

if st.sidebar.button("Execute T-Code"):
    st.session_state.current_tcode = tcode
    st.session_state.step = 1

# Multi-Step Processes - Full SAP Functionality
if st.session_state.current_tcode:
    st.title(f"{st.session_state.current_tcode} - SAP GUI Full Simulation")
    
    if st.session_state.current_tcode == "VA41 - Create Contract":
        if st.session_state.step == 1:
            st.subheader("Step 1: Enter Customer Information")
            customer = st.text_input("Customer Name")
            sales_org = st.text_input("Sales Organization")
            distribution_channel = st.text_input("Distribution Channel")
            if st.button("Next Step"):
                if customer.strip() and sales_org.strip() and distribution_channel.strip():
                    st.session_state.step = 2
                else:
                    st.error("All fields must be filled.")
        elif st.session_state.step == 2:
            st.subheader("Step 2: Enter Contract Details")
            contract_type = st.selectbox("Contract Type", ["Fixed Rate", "Time & Materials", "Cost-Based"])
            billing_amount = st.number_input("Billing Amount", min_value=0)
            validity_start = st.date_input("Validity Start Date")
            validity_end = st.date_input("Validity End Date")
            if st.button("Next Step"):
                st.session_state.step = 3
        elif st.session_state.step == 3:
            st.subheader("Step 3: Confirm and Save Contract")
            st.success("Contract Created Successfully!")
            st.session_state.current_tcode = None

    elif st.session_state.current_tcode == "VF01 - Billing Document":
        if st.session_state.step == 1:
            st.subheader("Step 1: Select Contract for Billing")
            contract_id = st.selectbox("Select Contract", st.session_state.contracts["Contract ID"])
            billing_date = st.date_input("Billing Date")
            if st.button("Next Step"):
                st.session_state.step = 2
        elif st.session_state.step == 2:
            st.subheader("Step 2: Generate and Confirm Billing Document")
            st.success(f"Billing document created for Contract {contract_id} on {billing_date}!")
            st.session_state.current_tcode = None

    elif st.session_state.current_tcode == "ME21N - Create Purchase Order":
        if st.session_state.step == 1:
            st.subheader("Step 1: Enter Vendor and Material Information")
            vendor = st.text_input("Vendor Name")
            material = st.text_input("Material/Service")
            if st.button("Next Step"):
                if vendor.strip() and material.strip():
                    st.session_state.step = 2
                else:
                    st.error("Vendor and Material cannot be empty.")
        elif st.session_state.step == 2:
            st.subheader("Step 2: Enter Pricing and Quantity")
            quantity = st.number_input("Quantity", min_value=1)
            price = st.number_input("Unit Price", min_value=0)
            delivery_date = st.date_input("Delivery Date")
            if st.button("Confirm Purchase Order"):
                st.success(f"Purchase Order Created: Vendor - {vendor}, Material - {material}, Qty - {quantity}, Price - {price}, Delivery - {delivery_date}")
                st.session_state.current_tcode = None

    elif st.session_state.current_tcode == "SE16N - Table Data Viewer":
        st.subheader("SAP Table Data Viewer")
        st.dataframe(st.session_state.contracts)
        if st.button("Exit Viewer"):
            st.session_state.current_tcode = None
