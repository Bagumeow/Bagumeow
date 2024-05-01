var app = document.getElementById('app');
var loading = document.getElementById('loading');

var typewriter = new Typewriter(app, {
    loop: true,
    delay: 150
});

typewriter.typeString('My name is <strong>Bagumeow</strong>')
    .pauseFor(1)
    .pauseFor(100)
    .deleteAll()
    .typeString('<strong>Welcome to my github profile</strong>')
    .pauseFor(100)
    .start();

var typewriter = new Typewriter(loading, {
    loop: false,
    cursor: '.',
    delay: 500
});

typewriter.typeString('...')
    .pauseFor(100)
    .start();