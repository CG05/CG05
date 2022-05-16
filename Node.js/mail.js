// 1. JS 기초 문법
console.log("Hello World"); //console 사용법

let a = 5; //변수 초기화
let b = 3;
let c = a + b;
console.log('c = ', c); //결과 log 출력

//2.nodemailer 사용
const nodemailer = require('nodemailer'); //nodemailer 선언

//메일 서버 : mailtrap.io 활용
const email = {
    host: "smtp.mailtrap.io",
    port: 2525,
    auth: {
        user: "e92df2afbe4a37",
        pass: "a7d57eb84161f4"
    }
};

//메일 송신 함수 세팅
const send = async(Option) => {
    nodemailer.createTransport(email).sendMail(Option, (error, info) => {
        if (error) {
            console.log(error);
        } else {
            console.log(info);
            return info.response;
        }
    });
};

//보낼 이메일 세팅
let email_data = {
    from: 'sungcjfrb2@gmail.com',
    to: 'sungcjfrb2@gmail.com',
    subject: '테스트 메일입니다.',
    text: 'Node.js 한시간만에 끝내보자.'
};

send(email_data); //송신 명령