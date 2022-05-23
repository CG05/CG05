const toDoForm = document.getElementById("todo-form");
const toDoInput = toDoForm.querySelector("input");
const toDoList = document.getElementById("todo-list");
//how can we store toDoList items? -> use 'localStorage' as string.
let toDos = [];
const TODOS_KEY = "todos"

function saveToDos() {
    //how cab we store array as string in the localStorage?
    //we can make anything to string by 'JSON.stringify()'
    localStorage.setItem(TODOS_KEY, JSON.stringify(toDos));
    //we can turn back these strings to array by 'JSON.parse()'
}

function deleteToDo(event) {
    //we can get an info from the argument 'event'
    console.log(event.target.parentElement);
    const li = event.target.parentElement;
    li.remove(); //and remove it simply
}

function paintToDo(newToDo) {
    const li = document.createElement("li");
    const span = document.createElement("span");
    const button = document.createElement("button");
    button.innerText = "❌";
    button.addEventListener("click", deleteToDo);
    //how can we know which button get clicked? ->'event'argument
    li.appendChild(span);
    li.appendChild(button);
    span.innerText = newToDo;
    toDoList.appendChild(li);
}

function handleToDoSubmit(event) {
    event.preventDefault();
    console.log(toDoInput.value);
    const newToDo = toDoInput.value;
    toDos.push(newToDo);
    console.log(toDos);
    paintToDo(newToDo);
    saveToDos();

    toDoInput.value = "";
}

toDoForm.addEventListener("submit", handleToDoSubmit);

const savedToDos = localStorage.getItem(TODOS_KEY);

if (savedToDos !== null) {
    const parsedToDos = JSON.parse(savedToDos);
    //turn back to array -> we can use it as array!
    toDos = parsedToDos; //we should update 'toDos' to make it remember what we saved
    parsedToDos.forEach(paintToDo);
    //'forEach' gives another item 0 to the end each time it calls 'paintToDo'
}