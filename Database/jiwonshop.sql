CREATE TABLE role (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(32) NOT NULL
) ENGINE=INNODB;

CREATE TABLE user (
    id VARCHAR(32) PRIMARY KEY,
    password VARCHAR(32) NOT NULL,
    name VARCHAR(32) NOT NULL,
    phone VARCHAR(32) NOT NULL,
    email VARCHAR(32) default '',
    address varchar(64) default '',
    roleid INT NOT NULL,
    FOREIGN KEY (roleid) REFERENCES role(id)
) ENGINE=INNODB;

CREATE TABLE category(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(32) NOT NULL
) ENGINE=INNODB;

CREATE TABLE product (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    price INT NOT NULL,
    description VARCHAR(255) NOT NULL,
    categoryid INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (categoryid) REFERENCES category(id)
) ENGINE=INNODB;

CREATE TABLE order_history (
    id INT PRIMARY KEY AUTO_INCREMENT,
    userid VARCHAR(32) NOT NULL,
    productid INT NOT NULL,
    quantity INT NOT NULL,
    totalPrice INT NOT NULL,
    FOREIGN KEY (userid) REFERENCES user(id),
    FOREIGN KEY (productid) REFERENCES product(id)
) ENGINE=INNODB;

INSERT INTO category(name) values ('OUTER');
INSERT INTO category(name) values ('TOP');
INSERT INTO category(name) values ('BOTTOM');
INSERT INTO category(name) values ('ACC');

INSERT INTO role(name) values('ADMIN');
INSERT INTO role(name) values('MEMBER');

INSERT INTO user(id, password, name, phone, roleid) values('admin', 'admin', 'admin', '010-1234-5678', 1);
