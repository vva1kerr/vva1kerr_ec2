import sqlite3
import hashlib
from typing import Optional, Tuple

def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_user(username: str, password: str, database: str) -> Tuple[bool, Optional[str]]:
    """
    Verify user credentials against the database.
    Returns (success, error_message)
    """
    try:
        con = sqlite3.connect(f"database/{database}.db")
        cur = con.cursor()
        
        # Get user from database
        cur.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cur.fetchone()
        
        if not result:
            return False, "User not found"
            
        stored_password = result[0]
        hashed_password = hash_password(password)
        
        if stored_password != hashed_password:
            return False, "Invalid password"
            
        return True, None
        
    except sqlite3.Error as e:
        return False, f"Database error: {str(e)}"
    finally:
        if 'con' in locals():
            con.close() 