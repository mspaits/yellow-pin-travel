const imageList = [
    "static/images/rand_stock/object 3 pin.png",
    "static/images/rand_stock/object 4 pin.png",
    "static/images/rand_stock/object 5 pin.png",
];


const randInt = Math.floor(Math.random() * imageList.length);
console.log("Printing to console");
console.log(randInt);

let image = imageList[randInt];
console.log(image);

const picTag = document.getElementById('rotatingImage');
console.log(picTag);
picTag.src = image;