const express = require('express');
const app = express();

app.use(express.static('public'));
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    if (!req.query.id) {
        req.query.id = Math.floor(Math.random() * 9) + 1;
    }

    res.render('index', req.query);
    }
);

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
