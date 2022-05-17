/* getpost.js */
const express = require('express');
const app = express();
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true })); // encode once : true

app.set('views', './views');
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    res.render('getpost_index');
});
app.get('/get', (req, res) => {
    res.send("GET");
});
app.post('/post', (req, res) => {
    res.send("POST");
});
app.listen(3000, () => {
    console.log('Connected at 3000');
});