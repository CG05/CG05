/**
 * setCalendarYearMonth()함수를 이용하여 calendarYearMonth에
 * 연도와 월을 출력
 */
const dayArr = ["일", "월", "화", "수", "목", "금", "토"]
let curY = 0;
let curM = 0;

function setTimeView(date){
        let timeView = document.getElementById("timeView");
        let h = date.getHours();
        let m = date.getMinutes();
        let s = date.getSeconds();
        let str = "";
        str += convertHour(h);
        str += `:${twoWord(m)}:${twoWord(s)}`;
    
        timeView.innerText = str;

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

function setTimeDateView(date){
        let timeDateView = document.getElementById("timeDateView");
        let Y = date.getFullYear();
        let m = date.getMonth()+1;
        let d = date.getDate();
        let day = date.getDay();
        let str = `${Y}년 ${twoWord(m)}월 ${twoWord(d)}일 ${dayArr[day]}요일`;
    
        timeDateView.innerText = str;

}

function setCalendarYearMonth(){
        let date = new Date();
        curY = date.getFullYear();
        curM = date.getMonth()+1;
        alterCalendarYearMonth();

}

function alterCalendarYearMonth(){
    let calendarYearMonth = document.getElementById("calendarYearMonth");
    let str = `${curY}년 ${twoWord(curM)}월`;

    calendarYearMonth.innerText = str;

}

function twoWord(time){
    return String(time).padStart(2,"0");
}

function alterCalendarDate(opt){
    let calendarDate = document.getElementById("calendarDate");

    curM += opt;
    if (curM > 12){
        curY += 1;
        curM = 1;
    }else if(curM < 1){
        curY -= 1;
        curM = 12;
    }

    let firstDayLastDate = 
        getCurrentCalendar(curM,curM);

    calendarDate.innerHTML = '';
    calendarDate.appendChild(
        createTable(firstDayLastDate.firstDay-1, firstDayLastDate.lastDate)
    );
}

function createTable(firstDay, lastDate){
    let table = document.createElement("table");
    let maxI = (lastDate + firstDay)/7 + 1;
    let dateCnt = 1;

    for (var i=0;i<maxI;i++){
        let tr = document.createElement("tr");
        for(var j=0;j<7;j++){
            let td = document.createElement("td");
            if(i==0){
                td.innerHTML = dayArr[j];
            }else if (i==1 && j<firstDay){
                td.innerHTML = "";
            }else{
                td.innerHTML = dateCnt++;
            }
            tr.appendChild(td);
            if(lastDate < dateCnt){
                break;
            }
        }
        table.appendChild(tr);
    }
    return table;
}

function getCurrentCalendar(Y, M){
    return {
        firstDay : new Date(Y, M, 1).getDay(),
        lastDate : 32 - new Date(Y, M, 32).getDate()
    }
}

function setAlterButton(){
    let before = document.getElementById("calendarBeforeBtn");
    let after = document.getElementById("calendarAfterBtn");

    before.onclick = function (){
        alterCalendarDate(-1);
        alterCalendarYearMonth();
    }
    after.onclick = function (){
        alterCalendarDate(1);
        alterCalendarYearMonth();
    }
}

function setTimeWindowCtrlBtn(){
    let timeWindowCtrlBtn = document.getElementById("timeWindowCtrlBtn");
    timeWindowCtrlBtn.addEventListener('click',function(){
        let timeWindowCtrlBtn = document.getElementById("timeWindowCtrlBtn");
        let timeMain = document.getElementById("timeMain");
        let timeView = document.getElementById("timeView");
        let timeDateView = document.getElementById("timeDateView");

        if(timeWindowCtrlBtn.innerText == "-"){
            timeWindowCtrlBtn.innerText = "+";
            timeMain.setAttribute('class', 'minimumMain');
            timeView.setAttribute('class', 'minimum');
            timeDateView.setAttribute('class', 'minimum');
        }else{
            timeWindowCtrlBtn.innerText = "-";
            timeMain.removeAttribute('class');
            timeView.removeAttribute('class');
            timeDateView.removeAttribute('class');
        }
    });
}

function setCalendarWindowCtrlBtn(){
    let calendarWindowCtrlBtn = document.getElementById("calendarWindowCtrlBtn");
    calendarWindowCtrlBtn.addEventListener('click', function(){
        let calendarWindowCtrlBtn = document.getElementById("calendarWindowCtrlBtn");
        let calendarMain = document.getElementById("calendarMain");
        let calendarYearMonth = document.getElementById("calendarYearMonth");
        let calendarDate = document.getElementById("calendarDate");
        let calendarBeforeBtn = document.getElementById("calendarBeforeBtn");
        let calendarAfterBtn = document.getElementById("calendarAfterBtn");

        if(calendarWindowCtrlBtn.innerText == "-"){
            calendarWindowCtrlBtn.innerText = "+";
            calendarMain.setAttribute('class', "minimumMain");
            calendarYearMonth.setAttribute('class', "minimum");
            calendarDate.setAttribute('class', "minimum");
            calendarBeforeBtn.setAttribute('class', "minimum");
            calendarAfterBtn.setAttribute('class', "minimum");
        }else{
            calendarWindowCtrlBtn.innerText = "-";
            calendarMain.removeAttribute('class');
            calendarYearMonth.removeAttribute('class');
            calendarDate.removeAttribute('class');
            calendarBeforeBtn.removeAttribute('class');
            calendarAfterBtn.removeAttribute('class');
        }
    })
}


function main(){
    setInterval(function(){
        let date = new Date();
        setTimeView(date);
        setTimeDateView(date);
        
    })
    setCalendarYearMonth();
    alterCalendarDate(0);
    setAlterButton();
    setTimeWindowCtrlBtn();
    setCalendarWindowCtrlBtn();
}

let player = {name:"nicco", fat:true};
console.log(player);
player.fat = false;
console.log(player);