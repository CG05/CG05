/**
 * 문제1.
 * setTimeView() 함수를 만들고 그 안에 만드세요
 * new Date()를 이용해서 timeView에 시간 : 분 : 초 형태로 출력
 * - 오후 15:27:08
 * setInterval()을 이용해서 1초에 한번씩 새로고침
 */

function setTimeView(){
    setInterval(function(){
        let date = new Date();
        let timeView = document.getElementById("timeView");
        let h = date.getHours();
        let m = date.getMinutes();
        let s = date.getSeconds();
        let str = "";
        str += convertHour(h);
        str += `:${twoWord(m)}:${twoWord(s)}`;
    
        timeView.innerText = str;

    });
}

function convertHour(hour){
    let str = "";
    if (hour > 12){
        str = "오후 ";
        str += twoWord(hour-12);
    }else if(hour == 12){
        str = "오후 ";
        str += "12";
    }else if (hour == 0){
        str = "오전 ";
        str += "12";
    }else{
        str = "오전 ";
        str += twoWord(hour);
    }
    return str;
}

function setTimeDateView(){
    setInterval(function(){
        let date = new Date();
        let timeDateView = document.getElementById("timeDateView");
        let Y = date.getFullYear();
        let m = date.getMonth()+1;
        let d = date.getDate();
        let day = date.getDay();
        let str = `${Y}년 ${twoWord(m)}월 ${twoWord(d)}일 ${getDay(day)}`;
    
        timeDateView.innerText = str;

    });
}

function twoWord(time){
    return String(time).padStart(2,"0");
}

function getDay(day){
    let dayArr = ["일", "월", "화", "수", "목", "금", "토"];
    return dayArr[day] + "요일";
}

/**
 * 문제2.
 * main()함수를 만들고 setTimeView와 setTimeDateView함수를 실행시키세요
 * setTimeDateView함수를 생성하고 timeDateView에 오늘의 날짜를 출력해보세요.
 */



function main(){
    setTimeView();
    setTimeDateView();
}