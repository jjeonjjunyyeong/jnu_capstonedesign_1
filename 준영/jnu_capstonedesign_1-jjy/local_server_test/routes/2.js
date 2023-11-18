var express = require('express');
var router = express.Router();

router.get('/', (req, res) => {
    console.log("Second Page");
    return res.sendFile('C:\\Users\\wnsdu\\Desktop\\test\\public\\2.html');
});

module.exports = router;