var express = require('express');
var router = express.Router();

router.get('/', (req, res) => {
    console.log("Third Page");
    return res.sendFile('C:\\Users\\wnsdu\\Desktop\\test\\public\\3.html');
});

module.exports = router;