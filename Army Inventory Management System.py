

import time

def main():
    # Initial data
    army_data = {
        "Camp Alpha": {
            "Rifles": {"qty": 50, "price": 20000},
            "Rations": {"qty": 1000, "price": 50}
        },
        "Camp Bravo": {
            "Rifles": {"qty": 10, "price": 20000},
            "Medkits": {"qty": 20, "price": 500}
        }
    }

    while True:
        print("\n=== 🇮🇳 COMMAND HQ DASHBOARD ===")
        print("1. View All Camps & Assets")
        print("2. Add New Camp / Update Stock")
        print("3. SEARCH Item (Global Intel)")
        print("4. TRANSFER Supplies (Logistics)")
        print("5. Exit")
        
        choice = input("Enter Command: ")

        # VIEW REPORT 
        if choice == '1':
            print("\n--- SITUATION REPORT ---")
            grand_total = 0
            for camp, items in army_data.items():
                print(f" {camp}")
                for item, details in items.items():
                    val = details['qty'] * details['price']
                    print(f"   - {item}: {details['qty']} units | Val: ₹{val}")
                    grand_total += val
            print(f"\n TOTAL MILITARY BUDGET DEPLOYED: ₹{grand_total}")

        # 2. ADD DATA
        elif choice == '2':
            camp = input("Enter Camp Name: ").strip()
            if camp not in army_data:
                print(f"Creating new base: {camp}...")
                army_data[camp] = {}
            
            item = input("Enter Item Name: ").title()
            try:
                qty = int(input("Enter Quantity: "))
                price = int(input("Enter Price (₹): "))
                army_data[camp][item] = {"qty": qty, "price": price}
                print(" Inventory Updated.")
            except ValueError:
                print(" Error: Use numbers for quantity/price.")

        
        elif choice == '3':
            target = input("Enter Item to find (e.g. Rifles): ").title()
            print(f"\n SEARCHING FOR: {target}...")
            found = False
            total_count = 0
            
            for camp, items in army_data.items():
                if target in items:
                    count = items[target]['qty']
                    print(f"   -> Found at {camp}: {count} units")
                    total_count += count
                    found = True
            
            if found:
                print(f" Total {target} across all camps: {total_count}")
            else:
                print(" Item not found in any camp.")

        
        elif choice == '4':
            print("\n--- LOGISTICS TRANSFER ---")
            source = input("From Camp: ").strip()
            dest = input("To Camp: ").strip()
            item = input("Item to move: ").title()
            
            
            if source in army_data and dest in army_data:
                
                if item in army_data[source]:
                    current_qty = army_data[source][item]['qty']
                    print(f"Available at {source}: {current_qty}")
                    
                    try:
                        move_qty = int(input("Quantity to move: "))
                        
                        
                        if move_qty <= current_qty:
                            
                            army_data[source][item]['qty'] -= move_qty
                            
                     
                            if item not in army_data[dest]:
                                
                                price = army_data[source][item]['price']
                                army_data[dest][item] = {"qty": 0, "price": price}
                            
                            army_data[dest][item]['qty'] += move_qty
                            
                            print(f" TRANSFER COMPLETE: Moved {move_qty} {item} from {source} to {dest}.")
                        else:
                            print(" Insufficient stock!")
                    except ValueError:
                        print(" Invalid number.")
                else:
                    print(f" {source} does not have {item}.")
            else:
                print("One or both camps do not exist.")

        elif choice == '5':
            print("Jai Hind. Over And Out!")
            break
        else:
            print("Invalid Command.")

if __name__ == "__main__":
    main()
