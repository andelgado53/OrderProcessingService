from app.src.shelf.Shelf import Shelf

class ShelvesManager:
    
    def store_order(self, internal_order, shelves):
        """Recieves an order and the shelves and puts the order in the appropiate shelf"""
        shelve = shelves[internal_order.get_temp()]
        overflow_shelve = shelves["overflow"]
        if shelve.has_room():
            shelve.store_order(internal_order)
            print("[+] Order id {order_id} has been shelved in {shelve_name} shelf.".format(shelve_name=shelve.get_shelf_temperature(), order_id=internal_order.get_order_id()))
            return [internal_order.get_order_id(), shelve.get_shelf_temperature()]
        elif overflow_shelve.has_room():
            overflow_shelve.store_order(internal_order)
            print("[+] Order id {order_id} has been shelved in {shelve_name} shelf.".format(shelve_name="overflow", order_id=internal_order.get_order_id()))
            return [internal_order.get_order_id(), 'overflow']
        else:
            return self._move_from_overflow_to_any(internal_order, shelves)
    
    def _move_from_overflow_to_any(self, internal_order, shelves):
        """This method handles the use case where the overflow shelfe is full and the proper temperature shelf is full as well.
            The logic followed is that we try to moveany item from the overflow to its appropiate shelf. If it is not possible
            to make this move, we discard the item in the overflow shelf that is closest to expiration and put the new order in 
            its place
        """
        # TODO: Too much going on here. Refactor this method to simplify it. 
        overflow_shelve = shelves["overflow"]
        for order in overflow_shelve.orders:
            order_to_move = overflow_shelve.peak_order_from_shelf(order)
            order_temp = order_to_move.get_temp()
            # Find first order in the overflow shelf that can be moved to a shelf with the correct temp
            # and put the new order in the overflow shelf
            if shelves[order_temp].has_room():
                print("[+] Order id {order_id} has been moved from overflow shelf to {new_shelf}".format(order_id=order_to_move.get_order_id(), new_shelf=order_to_move.get_temp()))
                shelves[order_temp].store_order(overflow_shelve.remove_order_from_shelf(order_to_move.get_order_id()))
                overflow_shelve.store_order(internal_order)
                print("[+] Order id {order_id} has been stored in overflow shelf".format(order_id=internal_order.get_order_id()))
                return [internal_order.get_order_id(), 'overflow']

        # If all shelves are full, then find order in the overflow shelf that is closest to expiration and dispose it,
        # put the new order in the overflow shelf
        oldeste_order_in_overflow = overflow_shelve.get_item_closer_to_expiration(internal_order.get_order_cooked_time())
        print("[+] There is no room in any shelf. Discarding order {order}".format(order=oldeste_order_in_overflow.print()))
        print("[+] Order age {age}".format(age=oldeste_order_in_overflow.get_order_age_in_secs(internal_order.get_order_cooked_time())))
        print("[+] Order time left before it expires {time_to_live}".format(time_to_live=oldeste_order_in_overflow.get_time_before_expiration(internal_order.get_order_cooked_time())))
        overflow_shelve.remove_order_from_shelf(oldeste_order_in_overflow)
        overflow_shelve.store_order(internal_order)
        print("[+] Order {order} has been stored in the overflow shelf".format(order=internal_order.print()))
        return [internal_order.get_order_id(), 'overflow']