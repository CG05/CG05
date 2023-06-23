const express = require("express");
const app = express();
const port = 3000;

app.set('views', '/workspace/CG05/Node.js/socketChat/views1'); 
app.set("view engine", 'ejs');
app.engine("html", require("ejs").renderFile);

app.get("/", function(req, res){
	res.render("index1.html");
});

app.listen(port, ()=>{
	console.log("서버가 실행됩니다.");
});