//3.웹서버 만들기 with express
const express = require('express');

const app = express();

const server = app.listen(3000, () => {
    console.log('Start Server : localhost : 3000');
});
//서버에서 request된 반응을 어떤 기능으로 mapping 하는 것을 'routing'이라고 한다.
//html페이지를 render하기 위한 사전작업
app.set('views', __dirname + '/Node.js/views'); //path 설정
app.set('view engine', 'ejs'); //엔진 정의
app.engine('html', require('ejs').renderFile); //엔진 사용

app.get('/', function(req, res) { // /~로 router 지정
    res.render('index.html') //router에 따른 기능 mapping
});
app.get('/about', function(req, res) { //router: /about일 때
    res.render('about.html')
});

//DB연결
// var mysql = require('mysql');
// var pool = mysql.createPool({
//     connectionLimit: 10,
//     host: '127.0.0.1',
//     user: 'root',
//     password: '',
//     database: 'customers'
// });

// app.get('/db', function(req, res) { //router: /about일 때
//     pool.getConnection(function(err, connection) {
//         if (err) throw err; // not connected!

//         // Use the connection
//         connection.query('select * from Test', function(error, results, fields) {
//             res.send(JSON.stringify(results));
//             console.log('results', results);
//             // When done with the connection, release it.
//             connection.release();

//             // Handle error after the release.
//             if (error) throw error;

//             // Don't use the connection here, it has been returned to the pool.
//         });
//     });
// });