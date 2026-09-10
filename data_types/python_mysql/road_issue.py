import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'localhost',
    'database': 'road_issue',
    'user': 'root',
    'password':'Password@123'  
}

class RoadIssueDB:
    def __init__(self):
        self.connection = None
        self.connect()
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            print("✅ Connected to road_issue database")
        except Error as e:
            print(f"❌ Connection failed: {e}")
    
    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("🔌 Connection closed")
    
    # CREATE
    def create_issue(self, title, location, description=None, priority='medium', status='open'):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO issues (title, location, description, priority, status)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (title, location, description, priority, status)
            cursor.execute(query, values)
            self.connection.commit()
            print(f"✅ Issue created with ID: {cursor.lastrowid}")
            return cursor.lastrowid
        except Error as e:
            print(f"❌ Error creating issue: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
    
    # READ ALL
    def get_all_issues(self):
        cursor = None
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM issues ORDER BY created_at DESC")
            return cursor.fetchall()
        except Error as e:
            print(f"❌ Error: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
    
    # READ BY ID
    def get_issue_by_id(self, issue_id):
        cursor = None
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM issues WHERE id = %s"
            cursor.execute(query, (issue_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"❌ Error: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
    
    # UPDATE
    def update_issue(self, issue_id, **kwargs):
        cursor = None
        try:
            cursor = self.connection.cursor()
            allowed_fields = ['title', 'location', 'description', 'priority', 'status']
            updates = {k: v for k, v in kwargs.items() if k in allowed_fields}
            
            if not updates:
                print("⚠️ No valid fields to update")
                return False
            
            set_clause = ', '.join([f"{key} = %s" for key in updates.keys()])
            values = list(updates.values()) + [issue_id]
            
            query = f"UPDATE issues SET {set_clause} WHERE id = %s"
            cursor.execute(query, values)
            self.connection.commit()
            
            # updated_at will auto-update!
            if cursor.rowcount > 0:
                print(f"✅ Issue {issue_id} updated successfully")
                return True
            else:
                print(f"⚠️ Issue {issue_id} not found")
                return False
        except Error as e:
            print(f"❌ Error: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    # DELETE
    def delete_issue(self, issue_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM issues WHERE id = %s"
            cursor.execute(query, (issue_id,))
            self.connection.commit()
            
            if cursor.rowcount > 0:
                print(f"✅ Issue {issue_id} deleted")
                return True
            else:
                print(f"⚠️ Issue {issue_id} not found")
                return False
        except Error as e:
            print(f"❌ Error: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    # SEARCH
    def search_by_location(self, location):
        cursor = None
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM issues WHERE location LIKE %s"
            cursor.execute(query, (f'%{location}%',))
            return cursor.fetchall()
        except Error as e:
            print(f"❌ Error: {e}")
            return []
        finally:
            if cursor:
                cursor.close()


if __name__ == "__main__":
    db = RoadIssueDB()
    
    print("\n📋 ALL ISSUES:")
    for issue in db.get_all_issues():
        print(f"  #{issue['id']}: {issue['title']} | {issue['status']} | Created: {issue['created_at']}")
    
    print("\n📝 ADDING NEW ISSUE:")
    db.create_issue(
        title="New pothole detected",
        location="East Street",
        description="Large pothole near school",
        priority="high"
    )
    
    print("\n✏️ UPDATING ISSUE 1:")
    db.update_issue(1, status='resolved')
    
    db.close()