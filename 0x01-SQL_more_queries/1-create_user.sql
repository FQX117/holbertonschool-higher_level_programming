--a script that creates the MySQL server user
CREATE user
    IF NOT EXISTS user_0d_1 @ localhost
    IDENTIFIED BY user_0d_1_pwd;
GRANT ALL privileges
    ON *.*
    TO user_0d_1 @ localhost
    IDENTIFIED BY user_0d_1_pwd;
FLUSH PRVILEGES;
