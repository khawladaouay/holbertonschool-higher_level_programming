-- lists all the cities of california that can be found in the database hbtn_0d_usa
SELECT id, name
	from cities
	where state_id IN
		(SELECT id
		from states
  		where name = "California")
	ORDER BY id;