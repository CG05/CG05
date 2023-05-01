const express = require('express');
const http = require('http');
const path = require('path');
const { Server } = require('socket.io');
const mysql = require('mysql');

const app = express();
const PORT = 3000;
const server = http.createServer(app);
const io = new Server(server);
const userDb = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	password: 'Pomcom1123@',
	database: 'Users',
});
const AUTHDATA_TABLE = 'auth_data';
const LOGGEDUSERS_TABLE = 'logged_users';

app.set('views', '../../views'); //path 설정
app.set('view engine', 'ejs'); //엔진 정의
app.engine('html', require('ejs').renderFile); //엔진 사용

let usersAuthData = [];
let userId = 'unknown';

function getUserDb(table) {
	userDb.query(`SELECT * FROM ${table};`, function (error, auth_data) {
		if (error) {
			return console.log(error);
		}
		usersAuthData = auth_data;
	});
}
function signUp(id, pw) {
	userDb.query(
		`INSERT INTO ${AUTHDATA_TABLE} (id, pw, authority) VALUES ('${id}', '${pw}', 'user');`,
		function (error, auth_data) {
			if (error) {
				return console.log(error);
			}
		}
	);
	getUserDb(AUTHDATA_TABLE);
}
getUserDb(AUTHDATA_TABLE);

// 유저 정보를 찾는 함수
async function userName(socketId) {
	return new Promise((res,rej) => {
		userDb.query(`SELECT name FROM ${LOGGEDUSERS_TABLE} WHERE socket_id = '${socketId}';`, (error, results) => {
    if (error) {
      console.log(error);
			rej(undefined);
    } else {
			const name = results[0] && results[0].name;
      console.log(`${socketId}: ${name}`);
			res(name);
    }
	})
	
  });
}

// 유저 정보를 업데이트하는 함수
function updateUser(name, socketId) {
  const user = { name: name, socket_id: socketId };
  userDb.query(`INSERT INTO ${LOGGEDUSERS_TABLE} SET ? ON DUPLICATE KEY UPDATE socket_id='${socketId}';`, user, error => {
    if (error) {
      console.log(error);
    } else {
      console.log(`Updated socket ID for user ${name}: ${socketId}`);
    }
  });
}

async function deleteLoggedUser(socketId) {
	const name = await userName(socketId);
	userDb.query(`DELETE FROM ${LOGGEDUSERS_TABLE} WHERE socket_id = '${socketId}';`, (error, results) => {
   	if (error) {
    	  console.log(error);
   	} else {
      console.log(`${name}: ${socketId} has deleted.`);
    }
	});
}


app.use(express.static(path.join('../../public')));

app.get('/', (req, res) => {
	res.render('index.html');
});

server.listen(PORT, () => {
	console.log(`server is running on ${PORT}`);
});

io.emit('some event', {
	someProperty: 'some value',
	otherProperty: 'other value',
});

io.on('connection', (socket) => {
	socket.on('login', (user) => {
		let resId = '';
		let auth = false;
		let i = 0;
		while (i < usersAuthData.length) {
			if (user.id === usersAuthData[i].id && user.pw === usersAuthData[i].pw) {
				resId = user.id;
				console.log(socket.id);
				auth = true;
				break;
			}
			i = i + 1;
		}
		const res = { id: resId, auth: auth };
		io.emit('login', res);
	});

	socket.on('signUp', (req) => {
		console.log('signing up');
		var { id, pw } = req;
		let unsigned = true;
		let i = 0;
		while (i < usersAuthData.length) {
			if (id === usersAuthData[i].id) {
				unsigned = false;
				break;
			}
			i = i + 1;
		}
		if (unsigned) {
			signUp(id, pw);
		}
		io.emit('signUp', unsigned);
		console.log('emited');
	});

	socket.on('connecting', (name) => {
		const date = new Date();
		const hours = String(date.getHours()).padStart(2, '0');
		const minutes = String(date.getMinutes()).padStart(2, '0');
		io.emit('greeting',{name: name, greeting: `${name} logged in @[${hours}:${minutes}]`});
	});
	
	
	/**socket.on('nextRequest', (req) =>{
	//데이터베이스에서 현재 상태, 다음 선택지를 respond에 담기
		io.emit('nextRespond', respond);
	}*/
	
	/**socket.on('choice', (choice) =>{
	//데이터베이스에서 choice에 대한 결과를 result에 담기
		io.emit('result',result);
	}*/
	
	socket.on('chat message', async(res) => {
		console.log(res);
		const msg = res.msg;
		const socketId = socket.id;
		if(res.msg === 'memorizing user name...'){
			updateUser(res.name, socket.id);
		}else{
			const name = await userName(socketId);
			console.log(`${name}: ${socketId} chat message`);
			console.log('message: ' + msg);
			const date = new Date();
			const hours = String(date.getHours()).padStart(2, '0');
			const minutes = String(date.getMinutes()).padStart(2, '0');
			const _msg = `#${name}>> ${msg} @[${hours}:${minutes}]`;
			io.emit('chat message', _msg);
		}
	});

	socket.on('disconnect', async() => {
		const socketId = socket.id;
		const name = await userName(socketId);
		console.log(`${name} disconnected`);
		deleteLoggedUser(socketId);
	});
});
