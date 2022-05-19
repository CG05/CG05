const express = require('express');

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }))

app.get('/api/hello', (req, res) => {
        res.send('hello world');
    })
    // 모든 http method 허용, 스트링 리턴
app.use('/hello', (req, res) => {
    res.send('Hello test');
})

//GET만 허용
app.get('/hello2', (req, res) => {
    res.send('Hello test');
})

// GET + query parameter로 데이터 전송
app.get('/hello3', (req, res) => {
        const { name } = req.query;
        res.send(`Hello ${name}`);
    })
    //http://localhost:8080/hello3?name=chulkyu 에서 ?name= 으로 name이라는 query parameter를 받는다.

// GET + uri parameter로 데이터 전송
app.get('/hello32/:name', (req, res) => {
        const { name } = req.params;
        res.send(`Hello ${name}`);
    })
    //http://localhost:8080/hello32/chulkyu 에서 /:name에 의해 /다음에 오는 요소를 uri parameter로 받는다.

// post 전송, x-www-form-urlencoded 방식
app.post('/hello4', (req, res) => {
    const { name } = req.body;
    res.send(`Hello ${name}`);
})

app.listen(8080, () => {
    console.log('server is listening 8080');
});