const express = require('express');
const http = require('http');
const path = require('path');
const app = express();
const server = http.createServer(app);
const { Server } = require('socket.io');
const io = new Server(server);
const PORT = 8080;
const date = new Date();


io.emit('some event', { someProperty: 'some value', otherProperty: 'other value' });


io.on("connection", (socket) => {
  console.log("a user connected");
  socket.broadcast.emit('hi');
  socket.on('chat message', (msg) => {
    console.log('message: ' + msg);
    const hours = String(date.getHours()).padStart(2, "0");
    const minutes = String(date.getMinutes()).padStart(2, "0");
    _msg = `${msg} @[${hours}:${minutes}]`
    io.emit('chat message', _msg);
  });
  socket.on('disconnect', () => {
    console.log("user disconnected");
  });
});

app.use(express.static(path.join(__dirname, "../../public")));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, "../../views/index.html"));
});

server.listen(PORT, () => {
  console.log(`server is running on ${PORT}`);
});