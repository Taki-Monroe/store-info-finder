import streamlit as st
import json

# Load the store data from the store_db.json file
def load_store_data():
    with open('store_db.json', 'r') as file:
        return json.load(file)

# Function to get store information by store ID
def get_store_info(store_id, store_data):
    for store in store_data:
        if str(store['storeId']) == str(store_id):  # Ensuring the ID comparison is consistent
            return store
    return None

# Streamlit app setup
def main():
    st.title("Store Information Finder")

    # Load the store data
    store_data = load_store_data()

    # User input for store ID (as a text field)
    store_id = st.text_input("Enter Store ID:")

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

if __name__ == "__main__":
    main()
