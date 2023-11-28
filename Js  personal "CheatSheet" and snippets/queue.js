class Queue {

    #elements = null;

    constructor() {
        this.#elements = [];
    }

    enqueue(element) {
        this.#elements.push(element);
    }

    dequeue() {
        if (this.isEmpty()) return -1;
        return this.#elements.shift();
    }

    exists(element) {
        return this.#elements.includes(element);
    }

    front() {
        if (this.isEmpty()) return -1;
        return this.#elements[0];
    }

    isEmpty() {
        return this.#elements.length === 0;
    }

    size() {
        return this.#elements.length;
    }

    print() {
        console.log(this.#elements);
    }
}
