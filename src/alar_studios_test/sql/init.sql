CREATE TABLE users (
	id SERIAL NOT NULL,
	name VARCHAR(32),
	password_hash VARCHAR(102) NOT NULL,
	updated TIMESTAMP WITH TIME ZONE,
	auth_token VARCHAR(64),
	token_expire TIMESTAMP,
	PRIMARY KEY (id),
	UNIQUE (name)
);

CREATE TABLE permissions (
	user_id INTEGER NOT NULL,
	read BOOLEAN NOT NULL,
	"create" BOOLEAN NOT NULL,
	update BOOLEAN NOT NULL,
	delete BOOLEAN NOT NULL,
	PRIMARY KEY (user_id),
	FOREIGN KEY(user_id) REFERENCES users (id)
);

INSERT INTO users(name, password_hash) VALUES('root', 'pbkdf2:sha256:260000$OeeTl2O5J0Jj4jYy$2b1bb99d12c90c6ef7669f3c19dbd3634af3d823ea8e3bd9f65e0a4fb510e236');

INSERT INTO permissions(user_id, read, "create", update, delete) VALUES(1, true, true, true, true)
