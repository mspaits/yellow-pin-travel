const imageList = [
    "static/images/family_pics/6AFE3425-BD61-45C7-BB0B-0B7CA0DC6016.png",
    "static/images/family_pics/54A74EEE-695E-4707-8186-FDFF2F71F063.jpg",
    "static/images/family_pics/145604CD-C584-4EF3-9173-56B98A26CAE0.png",
    "static/images/family_pics/AA9373A2-CC76-45AD-8753-5553C6EEA915.jpg",
    "static/images/family_pics/D39BB460-4DBE-482F-9AFA-A1C5CC076BAB.jpg",
    "static/images/family_pics/IMG_0213.jpg",
    "static/images/family_pics/IMG_0934.jpg",
    "static/images/family_pics/IMG_2307.jpg",
];


const randInt = Math.floor(Math.random() * imageList.length);
console.log("Printing to console");
console.log(randInt);

let image = imageList[randInt];
console.log(image);

const picTag = document.getElementById('rotatingImage');
console.log(picTag);
picTag.src = image;