const express = require('express');
const http = require('http');
const path = require('path');
const app = express();
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);
const PORT = 8080;

io.emit('some event', { someProperty: 'some value', otherProperty: 'other value' }); // This will emit the event to all connected sockets

io.on("connection", (socket) => {
  console.log("a user connected");
  socket.broadcast.emit('hi');
  socket.on('chat message', (msg) => {
    console.log('message: ' + msg);
    io.emit('chat message', msg);
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