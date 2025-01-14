class Vendor:

    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []

    def add(self, new_item):
        """ Adds argument passed into new_item to Vendor's inventory list, and returns the new item. """
        self.inventory.append(new_item)
        return new_item

    def remove(self, item_to_remove):
        """ Removes argument passed into item_to_remove from Vendor's inventory list, and returns the removed item. """
        if item_to_remove not in self.inventory:
            return False
        self.inventory.remove(item_to_remove)
        removed_item = item_to_remove
        return removed_item

    def get_by_category(self, category):
        """ Returns a list of items that have the category attribute given argument for category """
        inventory_items_in_category = [
            item for item in self.inventory if item.category == category]
        return inventory_items_in_category

    def swap_items(self, trading_vendor, my_item, their_item):
        """
        Takes in 3 arguments: another vendor instance, an item in the calling vendor's inventory, and an item from the
        the other vendor's inventory.
        If the items are in their expected inventories, the two given items are traded, and we return True. 
        Else if either of the items aren't in their expected inventories, we return False.
        """
        if my_item not in self.inventory or their_item not in trading_vendor.inventory:
            return False

        self.remove(my_item)
        trading_vendor.add(my_item)
        self.add(their_item)
        trading_vendor.remove(their_item)
        return True

    def swap_first_item(self, trading_vendor):
        """ 
        Takes in 1 argument: another vendor instance. Trades the first item in the calling instance's inventory
        with the first item in the other vendor's first item. Returns True.
        """
        if not self.inventory or not trading_vendor.inventory:
            return False

        my_first = self.inventory[0]
        their_first = trading_vendor.inventory[0]
        self.swap_items(trading_vendor, my_first, their_first)
        return True

    def get_best_by_category(self, category):
        """ Returns the item of the best condition in a given category """
        items_in_category = self.get_by_category(category)
        if not items_in_category:
            return None

        best_item = items_in_category[0]
        for item in items_in_category:
            if item.condition > best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Takes in other vendor name, the category of item that is my priority,
        and the category of item that is their priority. 
        Looks for the item of best condition for each vendor's priority category, and
        swaps them. 
        """
        if not self.inventory or not other.inventory:
            return False

        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if their_best is None or my_best is None:
            return False

        self.swap_items(other, my_best, their_best)
        return True

    def get_newest(self):
        """gets newest item in inventory. If there is more than one newest, returns the item with the best condition"""
        if not self.inventory:
            return False
        
        item_ages = [item.age for item in self.inventory]
        newest = min(item_ages)

        newest_item = [item for item in self.inventory if item.age == newest]
        if len(newest_item) > 1:
            return max(newest_item, key=lambda item: item.condition)
        return newest_item[0]

    def swap_by_newest(self, other):
        """ Takes in two vendor instances. Swaps their newest items"""
        if not self.inventory or not other.inventory:
            return False

        my_newest = self.get_newest()
        their_newest = other.get_newest()
        self.swap_items(other, my_newest, their_newest)
        return True