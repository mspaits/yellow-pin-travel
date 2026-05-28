fetch('/picsapi')
    .then(response => response.json())
    .then(data => {

        const randInt = Math.floor(Math.random() * data.length);
        let image = data[randInt];

        const picTag = document.getElementById('rotatingImage');
        picTag.src = image;
});
