import streamlit as st
import json
import random

# Load the store data from the Streamlit secrets
def load_store_data():
    # Fetch the JSON string from the Streamlit secrets
    store_data_json = st.secrets.get("general", {}).get("store_db", None)

    if store_data_json is None:
        st.error("Store data not found in the secrets. Please check your secrets.toml.")
        return []

    # Try to load the JSON and check if it's valid
    try:
        return json.loads(store_data_json)
    except json.JSONDecodeError:
        st.error("Failed to decode the JSON data. Please check the secrets.toml format.")
        return []

# Function to get store information by store ID
def get_store_info(store_id, store_data):
    for store in store_data:
        if str(store['storeId']) == str(store_id):  # Ensuring the ID comparison is consistent
            return store
    return None

# Function to get a random store information
def get_random_store(store_data):
    return random.choice(store_data)

# Streamlit app setup
def main():
    st.title("Store Information Finder")

    # Load the store data from secrets
    store_data = load_store_data()

    if not store_data:
        return  # Stop the app if there was an error in loading data

    # Section for manual store ID input
    st.subheader("Find Store by ID")
    
    # Using number_input for store_id instead of text_input
    store_id = st.number_input("Enter Store ID:", min_value=1, step=1)

    if store_id:
        # Retrieve the store info based on the entered store ID
        store_info = get_store_info(store_id, store_data)
        
        if store_info:
            # Display store information
            st.write(f"**Store ID**: {store_info['storeId']}")
            st.write(f"**Address**: {store_info['address']}")
            st.write(f"**Zip Code**: {store_info['zipCode']}")
            st.write(f"**Phone Number**: {store_info['phoneNumber']}")
            st.write(f"[Dialer URL]({store_info['dialer_url']})")
        else:
            st.error("Store ID not found.")

    # Section for random store generator
    st.subheader("Random Store Generator")
    if st.button("Generate Random Store"):
        random_store = get_random_store(store_data)
        # Display random store information
        st.write(f"**Store ID**: {random_store['storeId']}")
        st.write(f"**Address**: {random_store['address']}")
        st.write(f"**Zip Code**: {random_store['zipCode']}")
        st.write(f"**Phone Number**: {random_store['phoneNumber']}")
        st.write(f"[Dialer URL]({random_store['dialer_url']})")

if __name__ == "__main__":
    main()
