// server.js
const express = require('express');
const db = require('./database');
const app = express();
const PORT = 3000;

app.use(express.json());

app.post('/login', (req, res) => {
    const { username, password } = req.body;

    console.log('Login Request:', username, password); // Debug

    const sql = `SELECT * FROM login WHERE username = ? AND password = ?`;
    db.get(sql, [username, password], (err, row) => {
        if (err) {
            console.error('Query Error:', err);
            res.status(500).json({ message: 'Internal error' });
        } else if (row) {
            console.log('User Found:', row); // Debug
            res.json({ message: 'Login successful' });
        } else {
            console.log('No match found'); // Debug
            res.status(401).json({ message: 'Invalid credentials' });
        }
    });
});


app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
