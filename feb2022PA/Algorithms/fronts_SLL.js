// Add Front
// Write a method that accepts a value and create a new node, 
// assign it to the list head, and return a pointer to the new head node.

class SLL {
    addFront(value) {
        let new_node = new Node(value);
        if(!this.head) {
            this.head = new_node;
            return this;
        }
        new_node.next = this.head;
        this.head = new_node;
        return this;
    }
}


// Remove Front
// Write a method to remove the head node and return the new 
// list head node. If the list is empty, return null.

class SLL {
    removeFront() {
        if (this.head == null){
            return null;
        } else {
            let temp = this.head;
            this.head = this.next;
            delete temp;
            return this.head;
        }
    }
}

// Front
// Write a method to return the value (not the node) at the head
// of the list. If the list is empty, return null.

class SLL {
    front() {
        if (this.head == null){
            return null;
        } else if (this.next == null){
            return this.head;
        }
    }
}