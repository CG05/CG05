const http = require("http");
const express = require("express");
const app = express();
const bodyParser = require("body-parser");

const server = http.createServer(app);
const PORT = 3000;

app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true })); // encode once : true
app.use(bodyParser.json());

fetch('/', {
        method: "POST",
        body: {
            accessToken: 1234,
            refreshToken: 1234
        }
    })
    .then((response) => {
        console.log(response.json())
    });


server.listen(PORT, () => {
    console.log(`Server running on ${PORT}`);
});