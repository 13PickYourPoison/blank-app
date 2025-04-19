import sqlite3
import os
import pandas as pd
from datetime import datetime

# Create data directory
if not os.path.exists('data'):
    os.makedirs('data')

# Database connection function
def get_connection():
    return sqlite3.connect('data/greenforce.db')

# Initialize all tables
def init_db():
    conn = get_connection()
    
    # Create estimate summary table
    conn.execute('''
    CREATE TABLE IF NOT EXISTS estimate_summary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_number TEXT,
        program_code TEXT,
        total_price REAL,
        estimate_given_date TEXT,
        residential_or_commercial TEXT,
        sold_date TEXT,
        upload_date TEXT
    )
    ''')
    
    # Create production by tech table
    conn.execute('''
    CREATE TABLE IF NOT EXISTS production_by_tech (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tech_id TEXT,
        service_date TEXT,
        customer_number TEXT,
        service_type TEXT,
        revenue REAL,
        upload_date TEXT
    )
    ''')
    
    # Create sales report table
    conn.execute('''
    CREATE TABLE IF NOT EXISTS sales_report (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sale_date TEXT,
        salesperson TEXT,
        customer_number TEXT,
        program_type TEXT,
        sale_amount REAL,
        upload_date TEXT
    )
    ''')
    
    # Create cancel reports tables
    for year in [24, 25]:
        conn.execute(f'''
        CREATE TABLE IF NOT EXISTS cancel_report_{year} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_number TEXT,
            cancel_date TEXT,
            reason_code TEXT,
            program_type TEXT,
            annual_value REAL,
            upload_date TEXT
        )
        ''')
    
    conn.commit()
    conn.close()

# Save dataframe to a specific table
def save_to_table(df, table_name):
    # Add upload date
    df['upload_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Connect and save
    conn = get_connection()
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()
    
    return len(df)

# Load data from a table
def load_from_table(table_name, limit=1000):
    conn = get_connection()
    query = f"SELECT * FROM {table_name} ORDER BY upload_date DESC LIMIT {limit}"
    data = pd.read_sql(query, conn)
    conn.close()
    return data