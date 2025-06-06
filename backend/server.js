// server.js
const express = require('express');
const db = require('./database');
const app = express();
const PORT = 3000;

app.use(express.json());

app.post('/login', (req, res) => {
    const { username, password } = req.body;

    const sql = `SELECT * FROM login WHERE username = ? AND password = ?`;
    db.get(sql, [username, password], (err, row) => {
        if (err) {
            res.status(500).json({ message: 'Internal error' });
        } else if (row) {
            res.json({ message: 'Login successful' });
        } else {
            res.status(401).json({ message: 'Invalid credentials' });
        }
    });
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
