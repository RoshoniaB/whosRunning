-- settings.sql
CREATE DATABASE running;
CREATE USER runninguser WITH PASSWORD 'running';
GRANT ALL PRIVILEGES ON DATABASE running TO runninguser;