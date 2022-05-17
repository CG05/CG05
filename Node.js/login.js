/* login.js */
require("dotenv").config();

const http = require("http");
const express = require("express");
const jwt = require("jsonwebtoken");
const bodyParser = require("body-parser");
const exp = require("constants");
const url = require("url");

const app = express();
const server = http.createServer(app);
const PORT = 8080;

const users = [
    { id: "hello", pw: "world" },
    { id: "good", pw: "bye" },
];

app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true })); // encode once : true
app.use(bodyParser.json());

app.set('views', './views');
app.set('view engine', 'ejs');

//유저 확인 및 토큰 생성기
const login = (id, pw) => {
    let len = users.length;

    for (let i = 0; i < len; i++) {
        if (id === users[i].id && pw === users[i].pw)
            return id;

    }
    return "";
};

const generateAccessToken = (id) => {
    return jwt.sign({ id }, process.env.ACCESS_TOKEN_SECRET, {
        expiresIn: "15m",
    });
};

const generateRefreshToken = (id) => {
    return jwt.sign({ id }, process.env.REFRESH_TOKEN_SECRET, {
        expiresIn: "180days",
    });
};

//로그인 정보 입력창 접속
app.get('/auth', (req, res) => {
    res.render('auth');
});

//submit
app.post("/login", (req, res) => {
    let id = req.body.id;
    let pw = req.body.pw;
    var _url = req.url;

    let user = login(id, pw);
    if (user === "") return res.sendStatus(500);

    let accessToken = generateAccessToken(user);
    let refreshToken = generateRefreshToken(user);

    res.json({ accessToken, refreshToken });
    _url = 'hello';

});

const authenticateAccessToken = (req, res, next) => {
    let authHeader = req.headers["authorization"];
    let token = authHeader && authHeader.split(" ")[1];

    if (!token) {
        console.log("wrong token format or token is not sended");
        return res.sendStatus(400);
    }

    jwt.verify(token, process.env.ACCESS_TOKEN_SECRET, (error, user) => {
        if (error) {
            console.log(error);
            return res.sendStatus(403);
        }

        req.user = user;
        next();
    });
}

app.post("/refresh", (req, res) => {
    res.header('refreshToken', process.env.REFRESH_TOKEN_SECRET).send();
    let refreshToken = req.body.refreshToken;
    if (!refreshToken) return res.sendStatus(401);

    jwt.verify(
        refreshToken,
        process.env.REFRESH_TOKEN_SECRET,
        (error, user) => {
            if (error) return res.sendStatus(403);

            const accessToken = generateRefreshToken(user.id);

            res.json({ accessToken });
        }
    );
});
app.get("/hello", authenticateAccessToken, (req, res) => {
    res.header('accessToken', 'bearer ' + process.env.ACCESS_TOKEN_SECRET).send();
    console.log(req.user);
    res.render('hello');
});


//로그인 후 유저 활동 단계
app.get("/userInfo", authenticateAccessToken, (req, res) => {
    res.header('accessToken', 'bearer ' + process.env.ACCESS_TOKEN_SECRET).send();
    console.log(req.user);
    res.json(users.filter((user) => user.id === req.user.id));
});

server.listen(PORT, () => {
    console.log(`Server running on ${PORT}`);
});