class MenuItem:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class CartItem:
    def __init__(self, item_name):
        self.item_name = item_name
        self.next = None

class CityMap:
    def __init__(self):
        self.adj_list = {}

    def add_route(self, from_location, to_location, distance):
        if from_location not in self.adj_list:
            self.adj_list[from_location] = []
        self.adj_list[from_location].append((to_location, distance))

    def show_routes(self, from_location):
        if from_location in self.adj_list:
            print(f"Routes from {from_location}:")
            for route in self.adj_list[from_location]:
                print(f"To {route[0]} Distance: {route[1]} km")
        else:
            print(f"No routes found from {from_location}.")

    def dijkstra(self, start, end):
        pq = [(0, start)]
        distances = {start: 0}
        previous_nodes = {start: None}

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_node == end:
                path = []
                while previous_nodes[current_node] is not None:
                    path.append(current_node)
                    current_node = previous_nodes[current_node]
                path.append(start)
                return path[::-1], distances[end]

            for neighbor, weight in self.adj_list.get(current_node, []):
                distance = current_distance + weight
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        return None, float("inf")

menu_root = MenuItem("Menu")
cart_head = None
order_stack = []
delivery_queue = []
city_map = CityMap()

def add_menu_item(parent, child_name):
    child = MenuItem(child_name)
    parent.add_child(child)

def remove_menu_item(parent, child_name):
    parent.children = [child for child in parent.children if child.name != child_name]

def display_menu(root, indent=""):
    if root is None:
        return
    print(indent + f"- {root.name}")
    for child in root.children:
        display_menu(child, indent + "  ")

def add_to_cart(item_name):
    global cart_head
    new_item = CartItem(item_name)
    new_item.next = cart_head
    cart_head = new_item
    print(f"{item_name} added to cart.")

def place_order(order_id):
    order_stack.append(order_id)
    delivery_queue.append(order_id)
    print(f"Order {order_id} placed successfully.")

def undo_last_order():
    if order_stack:
        print(f"Undoing order: {order_stack.pop()}")
    else:
        print("No orders to undo.")

def process_delivery():
    if delivery_queue:
        print(f"Delivering Order: {delivery_queue.pop(0)}")
    else:
        print("No deliveries pending.")

def show_cart():
    global cart_head
    temp = cart_head
    print("Cart Items:")
    while temp is not None:
        print(f"- {temp.item_name}")
        temp = temp.next

def search_menu(root, item_name):
    if root is None:
        return None
    if root.name == item_name:
        return root
    for child in root.children:
        result = search_menu(child, item_name)
        if result:
            return result
    return None

def user_menu():
    while True:
        print("\nUser Menu:")
        print("1. Display Menu")
        print("2. Add Item to Cart")
        print("3. Show Cart")
        print("4. Place Order")
        print("5. Undo Last Order")
        print("6. Process Delivery")
        print("7. Show Routes")
        print("8. Find Shortest Path")
        print("9. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_menu(menu_root)
        elif choice == 2:
            item_name = input("Enter item name to add to cart: ")
            add_to_cart(item_name)
        elif choice == 3:
            show_cart()
        elif choice == 4:
            order_id = input("Enter order ID: ")
            place_order(order_id)
        elif choice == 5:
            undo_last_order()
        elif choice == 6:
            process_delivery()
        elif choice == 7:
            from_location = input("Enter starting location: ")
            city_map.show_routes(from_location)
        elif choice == 8:
            start = input("Enter starting location: ")
            end = input("Enter destination: ")
            path, distance = city_map.dijkstra(start, end)
            if path:
                print(f"Shortest Path: {path} with distance {distance} km")
            else:
                print("No path found.")
        elif choice == 9:
            print("Exiting User Menu.")
            break
        else:
            print("Invalid choice, please try again.")

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Item to Menu")
        print("2. Remove Item from Menu")
        print("3. Display Menu")
        print("4. Exit Admin Menu")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            parent_name = input("Enter parent category: ")
            item_name = input("Enter item name to add: ")
            parent = search_menu(menu_root, parent_name)
            if parent:
                add_menu_item(parent, item_name)
                print(f"{item_name} added to {parent_name}.")
            else:
                print(f"Parent category {parent_name} not found.")
        elif choice == 2:
            parent_name = input("Enter parent category: ")
            item_name = input("Enter item name to remove: ")
            parent = search_menu(menu_root, parent_name)
            if parent:
                remove_menu_item(parent, item_name)
                print(f"{item_name} removed from {parent_name}.")
            else:
                print(f"Parent category {parent_name} not found.")
        elif choice == 3:
            display_menu(menu_root)
        elif choice == 4:
            print("Exiting Admin Menu.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    add_menu_item(menu_root, "Main Course")
    add_menu_item(menu_root, "Desserts")
    add_menu_item(menu_root.children[0], "Pizza")
    add_menu_item(menu_root.children[0], "Burger")

    city_map.add_route("RestaurantA", "CustomerB", 5)
    city_map.add_route("RestaurantA", "CustomerC", 8)

    while True:
        print("\nMain Menu:")
        print("1. User Menu")
        print("2. Admin Menu")
        print("3. Exit")
        main_choice = int(input("Enter your choice: "))

        if main_choice == 1:
            user_menu()
        elif main_choice == 2:
            admin_menu()
        elif main_choice == 3:
            print("Exiting Program.")
            break
        else:
            print("Invalid choice, please try again.")
