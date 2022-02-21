class Node {
    constructor(value){
        this.val = value;
        this.next = null;
    }
}

class SLL {
    constructor(){
        this.head = null;
    }

// Add Front
// Write a method that accepts a value and create a new node, 
// assign it to the list head, and return a pointer to the new head node.

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

// Remove Front
// Write a method to remove the head node and return the new 
// list head node. If the list is empty, return null.

    removeFront() {
        if (this.head == null){
            return null;
        }
        let temp = this.head
        this.head = temp.next;
        let new_head = this.head
        return new_head;
    }

// Front
// Write a method to return the value (not the node) at the head
// of the list. If the list is empty, return null.

    front() {
        if (this.head == null){
            return null;
        } else if (this.next == null){
            let front = this.head
            return front.val;
        }
    }
}

console.log("--Add new nodes to front--")
let sll1 = new SLL();
sll1.addFront(4).addFront(8).addFront(5).addFront(9).addFront(6)
console.log(sll1)
console.log("--Remove front node and return new head node--")
sll1.removeFront()
console.log(sll1)
console.log("--Return VALUE of the head of the list--")
console.log("Head value is: " + sll1.front())