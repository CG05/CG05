const fs = require("fs");
const path = require("path");

class Database {
  _data;
  constructor(data){
    this._data = data;
  }

  async create(key, value){
    try{
      if(this._data.has(key)){
        return false;
      }else{
        this._data.set(key, value);
        return true
      }
    }catch(error){
      return error;
    }
      
  }

  async read(key){
    try{
      if(key === undefined || key === null){
        return this._data;
        
      }else{
        return {value: this._data.get(key), hasKey: this._data.has(key)}
      }
    } catch(error){
      return error;
    }
  }

  async update(key, value){
    try {
      if(this._data.has(key)){
        this._data.set(key, value);
        return true;
      }else{
        return false;
      }
    } catch(error){
      return error;
    }
  }

  async delete(key){
    try {
      if(this._data.has(key)){
        this._data.delete(key);
        return true;
      }else{
        return false;
      }
    } catch(error){
      return error;
    }
  }
}

function loadAuth() {
  return new Promise((res, rej) => {
    const loaded = fs.readFileSync(path.join(__dirname, "../database/auth.json"));
    let parsed = "";
      parsed = JSON.parse(loaded);
    res(parsed);
  });
}

function loadUser() {
  return new Promise((res, rej) => {
    const loaded = fs.readFileSync(path.join(__dirname, "../database/user.json"));
    let parsed = "";
      parsed = JSON.parse(loaded);
    res(parsed);
  });
}

async function loadDB() {

    const authParsed = await loadAuth();
    const userParsed = await loadUser();
    return {authParsed:authParsed, userParsed: userParsed};
  
}

function saveAuth(map) {
  return new Promise((res, rej) => {
    const modified = [...map];
    const reducedData = modified.reduce((accum, current) => {
      return {
        ...accum,
        [current[0]]: current[1],
      };
    }, {});
    const jsonData = JSON.stringify(reducedData);

    fs.writeFileSync(path.join(__dirname, "../database/auth.json"), jsonData);
    res();
  });
  
}

function saveUser(map) {
  return new Promise((res, rej) => {
  const modified = [...map];
  const reducedData = modified.reduce((accum, current) => {
    return {
      ...accum,
      [current[0]]: current[1],
    };
  }, {});
  const jsonData = JSON.stringify(reducedData);

  fs.writeFileSync(path.join(__dirname, "../database/user.json"), jsonData);
  res();
});
  
}

async function saveDB(authMap, userMap) {
  await saveAuth(authMap);
  await saveUser(userMap);
}

module.exports = {
  Database,
  loadDB,
  saveDB,
  loadAuth,
  loadUser,
  saveAuth,
  saveUser
};