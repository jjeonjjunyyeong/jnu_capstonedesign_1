const express = require('express');
const app = express();
const path = require('path');
const port = 8080;

var mainRouter = require('./routes/main.js');
var oneRouter = require('./routes/1.js');
var twoRouter = require('./routes/2.js');
var threeRouter = require('./routes/3.js');

app.use(express.static(path.join(__dirname, 'public')));

app.use('/', mainRouter);
app.use('/1', oneRouter);
app.use('/2', twoRouter);
app.use('/3', threeRouter);

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});