-- Creates the database hbtn_ d_2 and the user user_0d_2
-- The user_0d_2 has SELECT privilege on hbtn_0d_2 with password user_0d_2_pwd
-- Creates the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create the user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- grants SELECT privileges to a user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
