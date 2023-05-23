CREATE TABLE diary (
    id INT AUTO_INCREMENT PRIMARY KEY,
    entry TEXT
);
INSERT INTO diary (entry) VALUES (%s);
SELECT * FROM diary;
