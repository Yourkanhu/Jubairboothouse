#!/usr/bin/env python3
"""
Migration script to add images column to products table
"""

import sqlite3
import os

def migrate_database():
    """Add images column to products table"""
    db_path = "jubair_boot_house.db"
    
    if not os.path.exists(db_path):
        print(f"Database file {db_path} not found!")
        return
    
    try:
        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if images column already exists
        cursor.execute("PRAGMA table_info(products)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'images' not in columns:
            # Add images column
            cursor.execute("ALTER TABLE products ADD COLUMN images TEXT")
            print("✅ Successfully added 'images' column to products table")
        else:
            print("ℹ️  'images' column already exists in products table")
        
        # Commit changes
        conn.commit()
        print("✅ Migration completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during migration: {str(e)}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    print("🔄 Starting database migration...")
    migrate_database()
    print("🏁 Migration process finished!")
