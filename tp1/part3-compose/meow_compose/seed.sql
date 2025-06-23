CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    favorite_insult TEXT
);

INSERT INTO users (name, favorite_insult) VALUES
('Alice', 'You have something on your chin… no, the third one down.'),
('Bob', 'You bring everyone so much joy… when you leave the room.'),
('Charlie', 'You are as useless as the "ueue" in "queue".'),
('Diana', 'You have something on your face: stupidity.'),
('Eve', 'If I had a dollar for every smart thing you say, I would be broke.');