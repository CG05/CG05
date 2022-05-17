const express = require('express');

const app = express();
// body-parser는 내장되어있음.  json 파싱하기 위해서 설정만 추가
app.use(express.json());
app.use(express.urlencoded({ extended: true }))

// response - json 데이터 보내기
app.post('/hello5', (req, res) => {
    const result = {
        code: 0,
        message: 'success'
    };
    res.send(result);
})

// request - json 데이터 받기
app.post('/hello6', (req, res) => {
    console.log(req.body);
    const result = req.body;
    res.send(result);
})

app.listen(8080, () => {
    console.log('server is listening 8080');
});