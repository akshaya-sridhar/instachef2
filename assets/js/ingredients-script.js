const ingredient_cards = document.querySelectorAll(".ingredients-cards .ingredient");

ingredient_cards.forEach(card => {
    if(!(card.innerHTML == "+90 More")) {
        card.addEventListener("click", event => {
            if(card.classList.contains("ingredient-selected")) {
                card.classList.remove("ingredient-selected");
            }
            else
                card.classList.add("ingredient-selected");
        })
    }
});


// For vegetables card
const vegetables_section = document.querySelector("#vegetables-section");
let vegetables = ["ginger root", "red onion", "celery","mushroom","jelepeno","scallion","potato","chili pepper","avocado","zucchini"];

vegetables_add = document.querySelector("#ingredients-vegetables");
vegetables_add.addEventListener("click", event => {
    vegetables_add.classList.add("hide-card");

    const items = vegetables.map(item => {
        let item_card = document.createElement("div");
        item_card.classList.add("ingredient");
        item_card.innerHTML = item;
        return item_card;
    });

    items.forEach(item => {
        vegetables_section.appendChild(item);
    });
});

// For fruits card
const fruits_section = document.querySelector("#fruits-section");
let fruits = ["watermelon","lemon", "lime", "apple","banana","rasin","mango","pear","grape","cherry"];

fruits_add = document.querySelector("#ingredients-fruits");
fruits_add.addEventListener("click", event => {
    fruits_add.classList.add("hide-card");

    const items = fruits.map(item => {
        let item_card = document.createElement("div");
        item_card.classList.add("ingredient");
        item_card.innerHTML = item;
        return item_card;
    });

    items.forEach(item => {
        fruits_section.appendChild(item);
    });
});

// For herbs card
const herbs_section = document.querySelector("#herbs-section");
let herbs = ["basil","nutmeg", "garlic powder", "clove","turmeric","rosemerry","onion powder","thyme","mint","cardamon"];

herbs_add = document.querySelector("#ingredients-herbs");
herbs_add.addEventListener("click", event => {
    herbs_add.classList.add("hide-card");

    const items = herbs.map(item => {
        let item_card = document.createElement("div");
        item_card.classList.add("ingredient");
        item_card.innerHTML = item;
        return item_card;
    });

    items.forEach(item => {
        herbs_section.appendChild(item);
    });
});

// For dairy card
const dairy_section = document.querySelector("#dairy-section");
let dairy = ["cheese","yogurt", "ice cream", "custard","ghee","goat milk","froasting","malai","whipped cream","milk powder"];

dairy_add = document.querySelector("#ingredients-dairy");
dairy_add.addEventListener("click", event => {
    dairy_add.classList.add("hide-card");

    const items = dairy.map(item => {
        let item_card = document.createElement("div");
        item_card.classList.add("ingredient");
        item_card.innerHTML = item;
        return item_card;
    });

    items.forEach(item => {
        dairy_section.appendChild(item);
    });
});

// For baking card
const baking_section = document.querySelector("#baking-section");
let baking = ["cake flour","corn flour", "coconut flour", "almond meal","baking mix","gelatin","chickpea flour","oat flour","expresso powder","brownie mix"];

baking_add = document.querySelector("#ingredients-baking");
baking_add.addEventListener("click", event => {
    baking_add.classList.add("hide-card");

    const items = baking.map(item => {
        let item_card = document.createElement("div");
        item_card.classList.add("ingredient");
        item_card.innerHTML = item;
        return item_card;
    });

    items.forEach(item => {
        baking_section.appendChild(item);
    });
});

// For meat card
const meat_section = document.querySelector("#meat-section");
let meat = ["sausage","ground ham", "hot dog", "pork fillet","fish","salami","mutton","smoked sausage"];

meat_add = document.querySelector("#ingredients-meat");
meat_add.addEventListener("click", event => {
    meat_add.classList.add("hide-card");

    const items = meat.map(item => {
        let item_card = document.createElement("div");
        item_card.classList.add("ingredient");
        item_card.innerHTML = item;
        return item_card;
    });

    items.forEach(item => {
        meat_section.appendChild(item);
    });
});

// For dessert card
const dessert_section = document.querySelector("#dessert-section");
let dessert = ["jam","candy", "doughnut", "cookies","honey","chocolate powder","wafer","maple sugar","corn syrup","chocochips"];

dessert_add = document.querySelector("#ingredients-dessert");
dessert_add.addEventListener("click", event => {
    dessert_add.classList.add("hide-card");

    const items = dessert.map(item => {
        let item_card = document.createElement("div");
        item_card.classList.add("ingredient");
        item_card.innerHTML = item;
        return item_card;
    });

    items.forEach(item => {
        dessert_section.appendChild(item);
    });
});