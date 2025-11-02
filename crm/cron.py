import datetime
import requests
import random # Added for a simulated result

# --- Existing Function (CRM Heartbeat) ---

def log_crm_heartbeat():
    """Logs the health status of the CRM GraphQL endpoint."""
    now = datetime.datetime.now().strftime('%d/%m/%Y-%H:%M:%S')
    try:
        # Assuming this is your Django/Graphene GraphQL endpoint
        response = requests.post('http://localhost:8000/graphql', json={"query": "{ hello }"})
        health = response.json().get("data", {}).get("hello", "No response")
    except Exception as e:
        health = f"Error: {e}"

    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"{now} CRM is alive - GraphQL: {health}\n")

# --- New Function (Low Stock Update) ---

def update_low_stock_products():
    """
    Simulates the process of updating low stock products.
    Logs the result to a dedicated file.
    """
    now = datetime.datetime.now().strftime('%d/%m/%Y-%H:%M:%S')
    LOG_FILE = "/tmp/low_stock_updates_log.txt"

    try:
        # ** Replace this with your actual logic **
        # Example: Query the database, check stock levels, send notifications, etc.
        # For demonstration, we'll simulate a successful update count
        updated_count = random.randint(1, 5)
        
        # Simulated logic for updating products
        log_message = f"SUCCESS: Checked inventory. Updated **{updated_count}** products flagged as low stock."
        
    except Exception as e:
        # Handle exceptions during the update process (e.g., database connection error)
        log_message = f"ERROR: Failed to update low stock products. Details: {e}"

    # Log the timestamp and the outcome to the specified file
    with open(LOG_FILE, "a") as f:
        f.write(f"{now} Low Stock Update: {log_message}\n")

# --- Execution ---

if __name__ == "__main__":
    print("--- Running CRM Heartbeat Check ---")
    log_crm_heartbeat()
    
    print("--- Running Low Stock Update Process ---")
    update_low_stock_products()
    
    print(f"Check logs in /tmp/crm_heartbeat_log.txt and /tmp/low_stock_updates_log.txt")
