import streamlit as st
import os

# Path to the text file database
DATABASE_PATH = os.path.join('data', 'database.txt')

# Function to read the database
def read_database():
    if not os.path.exists(DATABASE_PATH):
        return []
    with open(DATABASE_PATH, 'r') as file:
        lines = file.readlines()
    data = [line.strip().split('|') for line in lines]
    return data

# Function to write to the database
def write_database(data):
    with open(DATABASE_PATH, 'w') as file:
        for record in data:
            file.write('|'.join(record) + '\n')

# Function to add a new entry
def add_entry(index, name, rank, position, contact):
    data = read_database()
    data.append([index, name, rank, position, contact])
    write_database(data)

# Function to edit an entry
def edit_entry(index, new_data):
    data = read_database()
    for record in data:
        if record[0] == index:
            record[1:] = new_data
            break
    write_database(data)

# Function to delete an entry
def delete_entry(index):
    data = read_database()
    data = [record for record in data if record[0] != index]
    write_database(data)

# Streamlit app layout
st.title('Signal Department Information Management')

# Search functionality
st.header('Search')
search_query = st.text_input('Enter search query')
if st.button('Search'):
    data = read_database()
    results = [record for record in data if search_query in record]
    st.write(results)

# Add entry functionality
st.header('Add New Entry')
index = st.text_input('Index')
name = st.text_input('Name')
rank = st.text_input('Rank')
position = st.text_input('Position')
contact = st.text_input('Contact')
if st.button('Add Entry'):
    add_entry(index, name, rank, position, contact)
    st.success('Entry added successfully')

# Edit entry functionality
st.header('Edit Entry')
edit_index = st.text_input('Index to Edit')
new_name = st.text_input('New Name')
new_rank = st.text_input('New Rank')
new_position = st.text_input('New Position')
new_contact = st.text_input('New Contact')
if st.button('Edit Entry'):
    edit_entry(edit_index, [new_name, new_rank, new_position, new_contact])
    st.success('Entry edited successfully')

# Delete entry functionality
st.header('Delete Entry')
delete_index = st.text_input('Index to Delete')
if st.button('Delete Entry'):
    delete_entry(delete_index)
    st.success('Entry deleted successfully')

# Display the current database
st.header('Current Database')
data = read_database()
st.write(data)
