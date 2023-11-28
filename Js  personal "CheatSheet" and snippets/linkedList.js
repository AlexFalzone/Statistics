class ListNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedList {
    #head = null;
    #size = 0;

    constructor() {
        this.#head = null;
        this.#size = 0;
    }

    add(value) {
        const newNode = new ListNode(value);
        if (!this.#head) {
            this.#head = newNode;
        } else {
            let current = this.#head;
            while (current.next) {
                current = current.next;
            }
            current.next = newNode;
        }
        this.#size++;
    }

    remove(value) {
        if (!this.#head) return;

        if (this.#head.value === value) {
            this.#head = this.#head.next;
            this.#size--;
            return;
        }

        let current = this.#head;
        while (current.next) {
            if (current.next.value === value) {
                current.next = current.next.next;
                this.#size--;
                return;
            }
            current = current.next;
        }
    }

    retrieve(index) {
        let current = this.#head;
        for (let i = 0; i < index; i++) {
            if (!current) return null;
            current = current.next;
        }
        return current ? current.value : null;
    }

    exists(value) {
        let current = this.#head;

        while (current) {
            if (current.value === value) {
                return true;
            }
            current = current.next;
        }
        return false;
    }

    removeElement(value) {
        let current = this.#head;
        let prev = null;

        while (current) {
            if (current.value === value) {
                if (prev === null) {
                    this.#head = current.next;
                } else {
                    prev.next = current.next;
                }
                this.#size--;
                return current.value;
            }
            prev = current;
            current = current.next;
        }
        return -1;
    }

    isEmpty() {
        return this.#size === 0;
    }

    size() {
        return this.#size;
    }

    print() {
        let current = this.#head;
        let output = "";
        while (current) {
            output += current.value + " ";
            current = current.next;
        }
        console.log(output);
    }
}
