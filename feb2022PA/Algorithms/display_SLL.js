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

    addFront(value){
        let new_node = new Node(value);
        if (this.head == null){
            this.head = new_node;
            return this;
        }
        new_node.next = this.head;
        this.head = new_node;
        return this;
    }

// Display
// Create display() that returns a string containing all list values. 

    display() {
        let runner = this.head;
        let values = "";
        while(runner!==null){
            values = values + " " + runner.val;
            runner = runner.next;
        }
        return values;
    }
}

console.log("--Add new nodes to front for example--")
let sll1 = new SLL();
sll1.addFront(4).addFront(8).addFront(5).addFront(9).addFront(6)
console.log(sll1)
console.log("--Display all node values in list--")
console.log(sll1.display())