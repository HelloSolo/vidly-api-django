insert into vidly.movie_genre (name)
values ("Action"),("Thriller"),("Romance"), ("Comedy"), ("Sci-fi");

insert into vidly.movie_movie (title, imdbRating, genre_id, description, releaseDate, promoted)
values 	("Airplanes",3.0,1,"Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate distinctio consequatur saepe consectetur vero quidem asperiores quae unde neque in?",'2017-08-23',0),
		("Die Hard",7.0,1,"Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate distinctio consequatur saepe consectetur vero quidem asperiores quae unde neque in?",'2018-04-09',0),
        ("Gone Girl",4.0,2,"Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate distinctio consequatur saepe consectetur vero quidem asperiores quae unde neque in?",'2018-04-09',0),
        ("How To Train A Dragon",7.0,2,"Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate distinctio consequatur saepe consectetur vero quidem asperiores quae unde neque in?",'2018-04-09',0),
        ("Lover",8.0,3,"Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate distinctio consequatur saepe consectetur vero quidem asperiores quae unde neque in?",'2018-04-09',0),
        ("No Time To Die",8.9,2,"Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate distinctio consequatur saepe consectetur vero quidem asperiores quae unde neque in?",'2018-04-09',0),
        ("Run  Aways",5.6,2,"Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate distinctio consequatur saepe consectetur vero quidem asperiores quae unde neque in?",'2018-04-09',0),
        ("Terminator 3",9.0,1,"Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate distinctio consequatur saepe consectetur vero quidem asperiores quae unde neque in?",'2018-04-09',0),
        ("The Avengers",9.0,2,"Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate distinctio consequatur saepe consectetur vero quidem asperiores quae unde neque in?",'2018-04-09',0),
        ("The Big Bang Theory",8.9,4,"Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate distinctio consequatur saepe consectetur vero quidem asperiores quae unde neque in?",'2018-04-09',0),
        ("The Hangover",2.0,4,"Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate distinctio consequatur saepe consectetur vero quidem asperiores quae unde neque in?",'2018-04-09',0),
        ("Lord of The Rings",8.9,2,"Aragorn is revealed as the heir to the ancient kings as he, Gandalf and the other members of the broken fellowship struggle to save Gondor from Sauron's forces. Meanwhile, Frodo and Sam take the ring closer to the heart of Mordor, the dark lord's realm.",'2018-04-09',0),
("Star Trek(2016)",8.2,5,"The USS Enterprise crew explores the furthest reaches of uncharted space, where they encounter a mysterious new enemy who puts them and everything the Federation stands for to the test.",'2016-05-20',1);

insert into vidly.movie_subcriptiontype(plan, monthly_price, video_quality, resolution, devices)
values ("Free",0,"Fair","360p","Mobile"),
("Mobile",1000,"Good","480p","Mobile, Tablet"),
("Basic",1500,"Good","720p","Mobile, Tablet, Computer"),
("Standard",2000,"Better","1080p","Mobile, Tablet, Computer"),
("Premium",3000,"Best","4K+HDR","Mobile, Table, Computer, Smart TV");
       