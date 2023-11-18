var express = require('express');
var router = express.Router();

router.get('/', (req, res) => {
    console.log("main");
    return res.sendFile('C:\\Users\\wnsdu\\Desktop\\test\\public\\main.html');
});

module.exports = router;