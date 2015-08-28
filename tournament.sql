-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create the database
CREATE DATABASE tournament;

-- Connect to the database
\c tournament;

-- Create auto increment sequence
CREATE SEQUENCE ID_SEQUENCE INCREMENT 1 START 0;

-- Create the tables
-- Create Players Table
CREATE TABLE players (
	id serial primary key not null nextval(ID_SEQUENCE),
	name varchar(30)	
);
-- Create Matches Table
CREATE TABLE matches (
	p1 varchar(30) references players.name,
	p2 varchar(30) references players.name,
	winner int references players.id
);

CREATE VIEW winTotals as
	SELECT players.id, players.name, count(players.name) as wins, count(matches.winner) as matches 
	FROM players, matches 
	WHERE players.id = matches.winner 
	GROUP BY players.id
	ORDER BY wins desc; 
