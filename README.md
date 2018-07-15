# Creating a server using flask, blueprint, swagger and mysql

check the requirment first and install it,

### Database setup in flask
```
    flask_app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    flask_app.config['MYSQL_DATABASE_USER'] = 'root'
    flask_app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
    flask_app.config['MYSQL_DATABASE_DB'] = 'mydatabase'
```
### Procedures:
to use the same Database that i used, the procedures that is in the database : 
```
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_firstname VARCHAR(100),
    IN p_lastname VARCHAR(100),
    IN p_username VARCHAR(100),
    IN p_email VARCHAR(100),
    IN p_password VARCHAR(100)
)
BEGIN
    if ( select exists (select 1 from user where username = p_username) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into user
        (
            firstname,
            lastname,
            username,
            email,
            password
            
        )
        values
        (
            p_firstname,
            p_lastname,
            p_username,
            p_email,
            p_password
        );
     
    END IF;
END
```
