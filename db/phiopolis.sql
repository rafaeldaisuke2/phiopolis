CREATE TABLE `usuario` (
 `id_usuario` VARCHAR(10) NOT NULL PRIMARY KEY,
 `nome` VARCHAR(50) NOT NULL,
 `cpf` CHAR(11) NOT NULL,
 `rg` VARCHAR(10) NOT NULL,
 `endereco` VARCHAR(100) NOT NULL,
 `email` VARCHAR(20) NOT NULL,
 `telefone` CHAR(11) NOT NULL,
 `senha` CHAR(64)
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
 `cota` INT NOT NULL,

 PRIMARY KEY (`conta`,`id_usuario`),

 FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
);


CREATE TABLE `consumo` (
 `id_consumo` INT NOT NULL,
 `conta` INT NOT NULL,
 `id_usuario` VARCHAR(10) NOT NULL,
 `mes` CHAR(3) NOT NULL,
 `ano` INT NOT NULL,
 `valor` FLOAT(10) NOT NULL,

 PRIMARY KEY (`id_consumo`,`conta`,`id_usuario`),

 FOREIGN KEY (`conta`,`id_usuario`) REFERENCES `cliente` (`conta`,`id_usuario`)
);


CREATE TABLE `contato` (
 `id_contato` INT NOT NULL,
 `conta` INT NOT NULL,
 `id_usuario` VARCHAR(10) NOT NULL,
 `data` DATE NOT NULL,

 PRIMARY KEY (`id_contato`,`conta`,`id_usuario`),

 FOREIGN KEY (`conta`,`id_usuario`) REFERENCES `cliente` (`conta`,`id_usuario`)
);

CREATE TABLE `fatura` (
 `id_fatura` INT NOT NULL PRIMARY KEY,
 `valor` FLOAT(10) NOT NULL,
 `vencimento` DATE NOT NULL
);


CREATE TABLE `pagamento` (
 `id_pagamento` INT NOT NULL,
 `conta` INT NOT NULL,
 `id_usuario` VARCHAR(10) NOT NULL,
 `id_fatura` INT NOT NULL,
 `data` DATE NOT NULL,

 PRIMARY KEY (`id_pagamento`,`conta`,`id_usuario`,`id_fatura`),

 FOREIGN KEY (`conta`,`id_usuario`) REFERENCES `cliente` (`conta`,`id_usuario`),
 FOREIGN KEY (`id_fatura`) REFERENCES `fatura` (`id_fatura`)
);


CREATE TABLE `recibo` (
 `id_recibo` INT NOT NULL,
 `conta` INT NOT NULL,
 `id_usuario` VARCHAR(10) NOT NULL,
 `id_pagamento` INT NOT NULL,
 `id_fatura` INT NOT NULL,
 `data_pagamento` DATE NOT NULL,
 `valor` FLOAT(10) NOT NULL,

 PRIMARY KEY (`id_recibo`,`conta`,`id_usuario`,`id_pagamento`,`id_fatura`),

 FOREIGN KEY (`conta`,`id_usuario`) REFERENCES `cliente` (`conta`,`id_usuario`),
 FOREIGN KEY (`id_pagamento`,`conta`,`id_usuario`,`id_fatura`) REFERENCES `pagamento` (`id_pagamento`,`conta`,`id_usuario`,`id_fatura`)
);


CREATE TABLE `resposta` (
 `id_resposta` INT NOT NULL,
 `id_admin` INT NOT NULL,
 `id_usuario` VARCHAR(10) NOT NULL,
 `data` DATE NOT NULL,

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
 `assunto` CHAR(20) NOT NULL,
 `conteudo` TEXT(1000) NOT NULL,
 `resposta` TEXT(1000) NOT NULL,
 `status` CHAR(20) NOT NULL,
 `data_criacao` DATE NOT NULL,

 PRIMARY KEY (`id_mensagem`,`id_contato`,`conta`,`id_usuario`,`id_resposta`,`id_admin`),

 FOREIGN KEY (`id_contato`,`conta`,`id_usuario`) REFERENCES `contato` (`id_contato`,`conta`,`id_usuario`),
 FOREIGN KEY (`id_resposta`,`id_admin`,`id_usuario`) REFERENCES `resposta` (`id_resposta`,`id_admin`,`id_usuario`)
);


