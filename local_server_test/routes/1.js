
var express = require('express');
var router = express.Router();

router.get('/', (req, res) => {
    console.log("First Page");
    return res.sendFile('C:\\Users\\wnsdu\\Desktop\\test\\public\\1.html');
});

module.exports = router;