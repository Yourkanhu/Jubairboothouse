import sqlite3
from datetime import datetime

def check_favourites():
    try:
        conn = sqlite3.connect('jubair_boot_house.db')
        cursor = conn.cursor()
        
        print("=== CHECKING FAVOURITES DATABASE ===")
        
        # Check if user_favourites table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user_favourites'")
        if not cursor.fetchone():
            print("❌ user_favourites table does not exist!")
            return
        
        # Check user_favourites table
        print("\n--- User Favourites Table ---")
        cursor.execute("SELECT COUNT(*) FROM user_favourites")
        count = cursor.fetchone()[0]
        print(f"Total favourites: {count}")
        
        if count > 0:
            cursor.execute("SELECT * FROM user_favourites")
            rows = cursor.fetchall()
            print("All favourites:")
            for row in rows:
                print(f"  ID: {row[0]}, User ID: {row[1]}, Product ID: {row[2]}, User Email: {row[3]}, Created: {row[4]}")
        else:
            print("No favourites found in database")
        
        # Check users table
        print("\n--- Users Table ---")
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        print(f"Total users: {user_count}")
        
        if user_count > 0:
            cursor.execute("SELECT id, name, email FROM users")
            users = cursor.fetchall()
            print("Users:")
            for user in users:
                print(f"  ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
        
        # Check products table
        print("\n--- Products Table ---")
        cursor.execute("SELECT COUNT(*) FROM products")
        product_count = cursor.fetchone()[0]
        print(f"Total products: {product_count}")
        
        if product_count > 0:
            cursor.execute("SELECT id, name, category FROM products LIMIT 5")
            products = cursor.fetchall()
            print("Sample products:")
            for product in products:
                print(f"  ID: {product[0]}, Name: {product[1]}, Category: {product[2]}")
        
        # Check sessions table
        print("\n--- Sessions Table ---")
        cursor.execute("SELECT COUNT(*) FROM sessions")
        session_count = cursor.fetchone()[0]
        print(f"Total sessions: {session_count}")
        
        if session_count > 0:
            cursor.execute("SELECT id, session_id, username, user_type, user_id, is_active FROM sessions ORDER BY created_at DESC LIMIT 5")
            sessions = cursor.fetchall()
            print("Recent sessions:")
            for session in sessions:
                print(f"  ID: {session[0]}, Session ID: {session[1][:20]}..., Username: {session[2]}, Type: {session[3]}, User ID: {session[4]}, Active: {session[5]}")
        
        # Check for orphaned favourites (favourites without valid users or products)
        print("\n--- Checking for Orphaned Favourites ---")
        cursor.execute("""
            SELECT uf.id, uf.user_id, uf.product_id, u.name as user_name, p.name as product_name
            FROM user_favourites uf
            LEFT JOIN users u ON uf.user_id = u.id
            LEFT JOIN products p ON uf.product_id = p.id
            WHERE u.id IS NULL OR p.id IS NULL
        """)
        orphaned = cursor.fetchall()
        if orphaned:
            print("❌ Found orphaned favourites:")
            for orphan in orphaned:
                print(f"  Favourite ID: {orphan[0]}, User ID: {orphan[1]}, Product ID: {orphan[2]}, User Name: {orphan[3]}, Product Name: {orphan[4]}")
        else:
            print("✅ No orphaned favourites found")
        
        conn.close()
        
    except Exception as e:
        print(f"Error checking favourites: {e}")

def add_test_favourite():
    """Add a test favourite to the database"""
    try:
        conn = sqlite3.connect('jubair_boot_house.db')
        cursor = conn.cursor()
        
        # Check if we have users and products
        cursor.execute("SELECT id FROM users LIMIT 1")
        user = cursor.fetchone()
        if not user:
            print("❌ No users found in database")
            return
        
        cursor.execute("SELECT id FROM products LIMIT 1")
        product = cursor.fetchone()
        if not product:
            print("❌ No products found in database")
            return
        
        user_id = user[0]
        product_id = product[0]
        
        # Add test favourite
        cursor.execute("""
            INSERT INTO user_favourites (user_id, product_id, user_email, created_at)
            VALUES (?, ?, ?, ?)
        """, (user_id, product_id, "test@example.com", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        
        conn.commit()
        print(f"✅ Added test favourite: User ID {user_id}, Product ID {product_id}")
        
        conn.close()
        
    except Exception as e:
        print(f"Error adding test favourite: {e}")

if __name__ == "__main__":
    check_favourites()
    print("\n" + "="*50)
    print("Would you like to add a test favourite? (y/n): ", end="")
    response = input().lower()
    if response == 'y':
        add_test_favourite()
        print("\n" + "="*50)
        check_favourites()
