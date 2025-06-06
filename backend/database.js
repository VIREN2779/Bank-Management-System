// database.js
const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');

const DB_PATH = './db/dbschema.sql';

const db = new sqlite3.Database(DB_PATH, (err) => {
    if (err) {
        console.error('Database connection error:', err);
    } else {
        console.log('Connected to SQLite database.');
        const sql = fs.readFileSync('./db/database.sql', 'utf8');
        db.exec(sql, (err) => {
            if (err) {
                console.error('Failed to create tables:', err);
            } else {
                console.log('Tables ensured.');
            }
        });
    }
});

module.exports = db;
