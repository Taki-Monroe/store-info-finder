import streamlit as st
import json
import random

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

# Function to get a random store information
def get_random_store(store_data):
    return random.choice(store_data)

# Streamlit app setup
def main():
    st.title("Store Information Finder")

    # Load the store data
    store_data = load_store_data()

    # Section for manual store ID input
    st.subheader("Find Store by ID")
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
