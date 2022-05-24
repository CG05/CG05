'use strict';

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
  //you can use filter to erase something from array
  //you should make to return false from function in the filter
  //function sexyFilter(item){return item !== 3;} 
  //[1,2,3,4,5].filter(sexyFilter)=> [1,2,4,5] : you can erase 3.
  toDos = toDos.filter((toDo) => toDo.id !== parseInt(li.id));
  saveToDos();

}

function paintToDo(newToDoObj) {
  const li = document.createElement("li");
  li.id = newToDoObj.id;
  const span = document.createElement("span");
  const button = document.createElement("button");
  button.innerText = "❌";
  button.addEventListener("click", deleteToDo);
  //how can we know which button get clicked? ->'event'argument
  li.appendChild(span);
  li.appendChild(button);
  span.innerText = newToDoObj.text;
  toDoList.appendChild(li);
}

function handleToDoSubmit(event) {
  event.preventDefault();
  console.log(toDoInput.value);
  const newToDo = toDoInput.value;
  const newToDoObj = {
    text: newToDo,
    id: Date.now(),
  }
  toDos.push(newToDoObj);
  console.log(toDos);
  paintToDo(newToDoObj);
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