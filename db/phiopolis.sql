CREATE TABLE `usuario` (
 `id_usuario` VARCHAR(10) NOT NULL PRIMARY KEY,
 `nome` VARCHAR(50),
 `cpf` CHAR(11),
 `rg` VARCHAR(10),
 `endereco` VARCHAR(100),
 `email` VARCHAR(20),
 `telefone` CHAR(11)
);


CREATE TABLE `administrador` (
 `id_admin` INT NOT NULL,
 `id_usuario` VARCHAR(10) NOT NULL,

 PRIMARY KEY (`id_admin`,`id_usuario`),

 FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
);


CREATE TABLE `cliente` (
 `conta` INT NOT NULL,
 `id_usuario` VARCHAR(10) NOT NULL,
 `status` BOOLEAN NOT NULL,
 `sensor` INT NOT NULL,
 `cota` INT,

 PRIMARY KEY (`conta`,`id_usuario`),

 FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
);


CREATE TABLE `consumo` (
 `id_consumo` INT NOT NULL,
 `conta` INT NOT NULL,
 `id_usuario` VARCHAR(10) NOT NULL,
 `mes` CHAR(3),
 `ano` INT,
 `valor` FLOAT(10),

 PRIMARY KEY (`id_consumo`,`conta`,`id_usuario`),

 FOREIGN KEY (`conta`,`id_usuario`) REFERENCES `cliente` (`conta`,`id_usuario`)
);


CREATE TABLE `contato` (
 `id_contato` INT NOT NULL,
 `conta` INT NOT NULL,
 `id_usuario` VARCHAR(10) NOT NULL,
 `data` DATE,

 PRIMARY KEY (`id_contato`,`conta`,`id_usuario`),

 FOREIGN KEY (`conta`,`id_usuario`) REFERENCES `cliente` (`conta`,`id_usuario`)
);


CREATE TABLE `fatura` (
 `conta` INT NOT NULL,
 `id_fatura` VARCHAR(10) NOT NULL,
 `valor` FLOAT(10),
 `vencimento` DATE,

 PRIMARY KEY (`conta`,`id_fatura`),

 FOREIGN KEY (`conta`,`id_fatura`) REFERENCES `cliente` (`conta`,`id_usuario`)
);


CREATE TABLE `pagamento` (
 `id_pagamento` INT NOT NULL,
 `conta` INT NOT NULL,
 `id_usuario` VARCHAR(10) NOT NULL,
 `data` DATE,

 PRIMARY KEY (`id_pagamento`,`conta`,`id_usuario`),

 FOREIGN KEY (`conta`,`id_usuario`) REFERENCES `cliente` (`conta`,`id_usuario`),
 FOREIGN KEY (`conta`,`id_usuario`) REFERENCES `fatura` (`conta`,`id_fatura`)
);


CREATE TABLE `recibo` (
 `id_recibo` INT NOT NULL,
 `conta` INT NOT NULL,
 `id_usuario` VARCHAR(10) NOT NULL,
 `id_pagamento` INT NOT NULL,
 `data_pagamento` DATE,
 `valor` FLOAT(10),

 PRIMARY KEY (`id_recibo`,`conta`,`id_usuario`,`id_pagamento`),

 FOREIGN KEY (`conta`,`id_usuario`) REFERENCES `cliente` (`conta`,`id_usuario`),
 FOREIGN KEY (`id_pagamento`,`conta`,`id_usuario`,`conta`,`id_usuario`) REFERENCES `pagamento` (`id_pagamento`,`conta`,`id_usuario`,`conta_0`,`id_0_0`)
);


CREATE TABLE `resposta` (
 `id_resposta` INT NOT NULL,
 `id_admin` INT NOT NULL,
 `id_usuario` VARCHAR(10) NOT NULL,
 `data` DATE,

 PRIMARY KEY (`id_resposta`,`id_admin`,`id_usuario`),

 FOREIGN KEY (`id_admin`,`id_usuario`) REFERENCES `administrador` (`id_admin`,`id_usuario`)
);


CREATE TABLE `mensagem` (
 `id_mensagem` INT NOT NULL,
 `id_contato` INT NOT NULL,
 `conta` INT NOT NULL,
 `id_usuario` VARCHAR(10) NOT NULL,
 `id_resposta` INT NOT NULL,
 `id_admin` INT NOT NULL,
 `assunto` CHAR(20),
 `conteudo` CHAR(1000),
 `resposta` CHAR(1000),
 `status` CHAR(20),
 `data_criacao` DATE,

 PRIMARY KEY (`id_mensagem`,`id_contato`,`conta`,`id_usuario`,`id_resposta`,`id_admin`),

 FOREIGN KEY (`id_contato`,`conta`,`id_usuario`) REFERENCES `contato` (`id_contato`,`conta`,`id_usuario`),
 FOREIGN KEY (`id_resposta`,`id_admin`,`id_usuario`) REFERENCES `resposta` (`id_resposta`,`id_admin`,`id_usuario`)
);


