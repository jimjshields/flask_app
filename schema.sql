drop table if exists imdb_top_250;
create table imdb_top_250 (
	id integer primary key autoincrement,
	rank integer not null,
	imdb_rating numeric not null,
	took_url text not null,
	title text not null,
	num_votes integer not null,
	took_date_url text not null,
	date date not null,
	imdb_id text not null,
	title_key text not null,
	standard_title text not null
	);