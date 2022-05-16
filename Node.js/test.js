const moment = require("moment");
console.log("today", moment().format("YYYY-MM-DD"));
console.log("today+1", moment().add(1, "day").format("YYYY-MM-DD"));
console.log("today", moment().add(1, "week").format("YYYY-MM-DD"));
console.log("today", moment().add(1, "month").format("YYYY-MM-DD"));