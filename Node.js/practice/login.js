/* login.js */
require('dotenv').config();

const http = require('http');
const express = require('express');
const jwt = require('jsonwebtoken');
const bodyParser = require('body-parser');
const exp = require('constants');
const url = require('url');
const path = require("path");

const app = express();
const server = http.createServer(app);
const PORT = 8080;

const users = [
    { id: 'hello', pw: 'world' },
    { id: 'good', pw: 'bye' },
];

app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true })); // encode once : true
app.use(bodyParser.json());

// static 경로 추가
app.use(express.static(path.join(__dirname, "login-src/public")));

app.set('views', './login-src/views');
app.set('view engine', 'ejs'); //엔진 정의
app.engine('html', require('ejs').renderFile); //엔진 사용

//유저 확인 및 토큰 생성기
const login = (id, pw) => {
    let len = users.length;

    for (let i = 0; i < len; i++) {
        if (id === users[i].id && pw === users[i].pw) return id;
    }

    return '';
};

const generateAccessToken = (id) => {
    return jwt.sign({ id }, process.env.ACCESS_TOKEN_SECRET, {
        expiresIn: '15m',
    });
};

const generateRefreshToken = (id) => {
    return jwt.sign({ id }, process.env.REFRESH_TOKEN_SECRET, {
        expiresIn: '180days',
    });
};

//로그인 정보 입력창 접속

app.get('/auth', (req, res) => {
    res.render('auth.html');
});

//submit
app.post('/login', (req, res) => {
    var { id, pw } = req.body;

    let user = login(id, pw);

    if (user === "") {
        res.status(500).json({ result: "fail" });

        return;
    }

    let accessToken = generateAccessToken(user);
    let refreshToken = generateRefreshToken(user);

    // 성공했음
    res.json({ result: "success", accessToken, refreshToken });
});

const authenticateAccessToken = (req, res, next) => {
    let authHeader = req.headers['authorization'];
    let token = authHeader && authHeader.split(' ')[1];

    if (!token) {
        console.log('wrong token format or token is not sended');
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
};

app.post('/refresh', (req, res) => {
    req.header('refreshToken', refreshToken).send();
    let refreshToken = req.body.refreshToken;
    if (!refreshToken) return res.sendStatus(401);

    jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET, (error, user) => {
        if (error) return res.sendStatus(403);

        const accessToken = generateRefreshToken(user.id);

        res.json({ accessToken });
    });
});

app.get('/hello', authenticateAccessToken, (req, res) => {
    // req.header('accessToken', 'bearer ' + accessToken).send();
    console.log(req.user);
    res.render('hello.html');
});

//로그인 후 유저 활동 단계
app.get('/userInfo', authenticateAccessToken, (req, res) => {
    req.header('accessToken', 'bearer ' + accessToken).send();
    console.log(req.user);
    res.json(users.filter((user) => user.id === req.user.id));
});

server.listen(PORT, () => {
    console.log(`Server running on ${PORT}`);
});