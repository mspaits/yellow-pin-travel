fetch('/picsapi')
    .then(response => response.json())
    .then(data => {
        console.log(data);

        const randInt = Math.floor(Math.random() * data.length);
        let image = data[randInt];

        const picTag = document.getElementById('rotatingImage');
        console.log(picTag);
        picTag.src = image;
});
