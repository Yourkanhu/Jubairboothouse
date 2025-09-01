import sqlite3

def check_database():
    try:
        conn = sqlite3.connect('jubair_boot_house.db')
        cursor = conn.cursor()
        
        # Check tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print("Tables in database:", [table[0] for table in tables])
        
        # Check each table for data
        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            print(f"Table '{table_name}': {count} rows")
            
            if count > 0:
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")
                rows = cursor.fetchall()
                print(f"Sample data from {table_name}:")
                for row in rows:
                    print(f"  {row}")
        
        # Specifically check products table
        print("\n--- Checking Products Table ---")
        try:
            cursor.execute("SELECT COUNT(*) FROM products")
            count = cursor.fetchone()[0]
            print(f"Products table has {count} rows")
            
            if count > 0:
                cursor.execute("SELECT * FROM products LIMIT 3")
                rows = cursor.fetchall()
                print("Sample products:")
                for row in rows:
                    print(f"  {row}")
            else:
                print("Products table is empty!")
                
        except Exception as e:
            print(f"Error checking products table: {e}")
        
        conn.close()
        
    except Exception as e:
        print(f"Error checking database: {e}")

if __name__ == "__main__":
    check_database()
