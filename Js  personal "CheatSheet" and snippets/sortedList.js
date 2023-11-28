class SortedList {

    #elements = null;

    constructor() {
        this.#elements = [];
    }

    insert(element) {
        if (this.isEmpty()) {
            this.#elements.push(element);
        } else {
            let inserted = false;

            for (let i = 0; i < this.#elements.length; i++) {
                if (element < this.#elements[i]) {
                    this.#elements.splice(i, 0, element);
                    inserted = true;
                    break;
                }
            }

            if (!inserted) {
                this.#elements.push(element); // Aggiunge alla fine se è l'elemento più grande
            }
        }
    }

    exists(element) {
        return this.#elements.includes(element);
    }

    remove(element) {
        const index = this.#elements.indexOf(element);
        if (index !== -1) {
            this.#elements.splice(index, 1);
        }
    }

    isEmpty() {
        return this.#elements.length === 0;
    }

    size() {
        return this.#elements.length;
    }

    print() {
        return this.#elements;
    }
}
