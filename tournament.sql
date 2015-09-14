-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Delete the database if it already exists
DROP DATABASE IF EXISTS tournament;

-- Create the database
CREATE DATABASE tournament;

-- Connect to the database
\c tournament;

-- Drop the tables if they already exist
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;

-- Create auto increment sequence
-- CREATE SEQUENCE ID_SEQUENCE INCREMENT 1 START 0;

-- Create the tables

-- Create Players Table
CREATE TABLE players (
	id serial primary key, --nextval(ID_SEQUENCE) - needed if using the ID_SEQUENCE sequence.
	name varchar(30),
	wins int	
);

-- Create Matches Table
CREATE TABLE matches (
	id serial primary key,
	winner int references players,
	loser int references players
);

-- 
CREATE VIEW winTotals as
	SELECT players.id, players.name, count(players.name) as wins, count(matches.winner) as matches 
	FROM players, matches 
	WHERE players.id = matches.winner 
	GROUP BY players.id
	ORDER BY wins desc; 
