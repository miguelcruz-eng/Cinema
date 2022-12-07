CREATE database cinema;
USE cinema ;

-- Tabela: atores
CREATE TABLE atores (
  i_id_atoresFilme INT NOT NULL,
  s_nome_ator VARCHAR(20) NOT NULL,
  PRIMARY KEY (i_id_atoresFilme));

-- Tabela: tipocliente
CREATE TABLE tipocliente (
  i_id_TCliente INT NOT NULL,
  s_desc_TCliente VARCHAR(15) NULL DEFAULT NULL,
  PRIMARY KEY (i_id_TCliente));

-- Tabela: cliente
CREATE TABLE cliente (
  i_id_cliente INT NOT NULL,
  s_nome_cliente VARCHAR(15) NOT NULL,
  d_dataNas_cliente DATE NOT NULL,
  i_tipo_cliente INT NOT NULL,
  PRIMARY KEY (i_id_cliente),
  INDEX fk_cliente (i_tipo_cliente ASC) VISIBLE,
  CONSTRAINT fk_cliente
    FOREIGN KEY (i_tipo_cliente)
    REFERENCES tipocliente (i_id_TCliente));

-- Tabela: estreias
CREATE TABLE estreias (
  i_idEstreia_est INT NOT NULL,
  d_dataEstreia_est DATE NOT NULL,
  ingressos_i_cod_ingresso INT NOT NULL,
  PRIMARY KEY (i_idEstreia_est, ingressos_i_cod_ingresso));

-- Tabela: tipofilme;
CREATE TABLE tipofilme (
  i_idCategoria_TipoFilme INT NOT NULL,
  s_genero_TipoFilme VARCHAR(5) NOT NULL,
  PRIMARY KEY (i_idCategoria_TipoFilme));

-- Tabela: filme
CREATE TABLE filme (
  i_id_filme INT NOT NULL,
  s_titulo_filme VARCHAR(30) NOT NULL,
  s_nacionalidade_filme VARCHAR(10) NOT NULL,
  s_estudio_filme VARCHAR(10) NOT NULL,
  i_tipoFilme_filme INT NOT NULL,
  i_id_atores INT NOT NULL,
  PRIMARY KEY (i_id_filme, i_id_atores),
  INDEX fk_tipoFilme (i_tipoFilme_filme ASC) VISIBLE,
  INDEX fk_atores_filme (i_id_atores ASC) VISIBLE,
  CONSTRAINT fk_atores_filme
    FOREIGN KEY (i_id_atores)
    REFERENCES atores (i_id_atoresFilme),
  CONSTRAINT fk_tipoFilme
    FOREIGN KEY (i_tipoFilme_filme)
    REFERENCES tipofilme (i_idCategoria_TipoFilme));

-- Tabela: sala
CREATE TABLE sala (
  i_cod_sala INT NOT NULL,
  i_capa_sala INT NOT NULL,
  i_poltrona_sala INT NOT NULL,
  i_numero_sala INT NOT NULL,
  PRIMARY KEY (i_cod_sala));

-- Tabela: secoes
CREATE TABLE secoes (
  i_cod_secoes INT NOT NULL,
  d_data_secoes DATE NOT NULL,
  h_hora_secoes DATETIME NOT NULL,
  i_TipoSala_secoes INT NOT NULL,
  filme_i_id_filme INT NOT NULL,
  PRIMARY KEY (i_cod_secoes, filme_i_id_filme),
  INDEX i_TipoSala_secoes (i_TipoSala_secoes ASC) VISIBLE,
  INDEX fk_secoes_filme1_idx (filme_i_id_filme ASC) VISIBLE,
  CONSTRAINT fk_secoes_filme1
    FOREIGN KEY (filme_i_id_filme)
    REFERENCES filme (i_id_filme),
  CONSTRAINT secoes_ibfk_1
    FOREIGN KEY (i_TipoSala_secoes)
    REFERENCES sala (i_cod_sala));

-- Tabela: ingressos
CREATE TABLE ingressos (
  i_cod_ingresso INT NOT NULL,
  f_preco_ingresso INT NOT NULL,
  secoes_i_cod_secoes INT NOT NULL,
  i_id_estreia INT NOT NULL,
  PRIMARY KEY (i_cod_ingresso),
  INDEX fk_ingressos_secoes1_idx (secoes_i_cod_secoes ASC) VISIBLE,
  CONSTRAINT fk_ingressos_secoes1
    FOREIGN KEY (secoes_i_cod_secoes)
    REFERENCES secoes (i_cod_secoes));

-- Tabela: lanches
CREATE TABLE lanches (
  i_cod_lanche INT NOT NULL,
  f_preco_lanche FLOAT NOT NULL,
  i_quantidade_lanche INT NOT NULL,
  i_tipo_lanche INT NOT NULL,
  PRIMARY KEY (i_cod_lanche));

-- Tabela: comprar
CREATE TABLE comprar (
  i_ingresso_comprar INT NOT NULL,
  i_lanches_comprar INT NOT NULL,
  i_estreia_comprar INT NOT NULL,
  i_bilhe_ INT NOT NULL,
  PRIMARY KEY (i_ingresso_comprar, i_lanches_comprar, i_estreia_comprar, i_bilhe_),
  INDEX fk_comprar_estreias1_idx (i_estreia_comprar ASC) VISIBLE,
  INDEX fk_comprar_lanches1_idx (i_lanches_comprar ASC) VISIBLE,
  CONSTRAINT fk_comprar_estreias1
    FOREIGN KEY (i_estreia_comprar)
    REFERENCES estreias (i_idEstreia_est),
  CONSTRAINT fk_comprar_ingressos1
    FOREIGN KEY (i_ingresso_comprar)
    REFERENCES ingressos (i_cod_ingresso),
  CONSTRAINT fk_comprar_lanches1
    FOREIGN KEY (i_lanches_comprar)
    REFERENCES lanches (i_cod_lanche));

-- Tabela: bilheteria
CREATE TABLE bilheteria (
  FormaPagamento INT NOT NULL,
  cliente_id_bilhe INT NOT NULL,
  mostra_ofertas INT NOT NULL,
  comprar_i_ingresso_comprar INT NOT NULL,
  comprar_i_lanches_comprar INT NOT NULL,
  comprar_i_estreia_comprar INT NOT NULL,
  comprar_i_bilhe_ INT NOT NULL,
  PRIMARY KEY (cliente_id_bilhe, mostra_ofertas),
  INDEX fk_bilheteria_cliente1_idx (cliente_id_bilhe ASC) VISIBLE,
  INDEX fk_bilheteria_comprar1_idx (comprar_i_ingresso_comprar ASC, comprar_i_lanches_comprar ASC, comprar_i_estreia_comprar ASC, comprar_i_bilhe_ ASC) VISIBLE,
  CONSTRAINT fk_bilheteria_cliente1
    FOREIGN KEY (cliente_id_bilhe)
    REFERENCES cliente (i_id_cliente)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_bilheteria_comprar1
    FOREIGN KEY (comprar_i_ingresso_comprar , comprar_i_lanches_comprar , comprar_i_estreia_comprar , comprar_i_bilhe_)
    REFERENCES comprar (i_ingresso_comprar , i_lanches_comprar , i_estreia_comprar , i_bilhe_)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

-- Tabela: ofertas
CREATE TABLE ofertas (
  i_id_ofertas INT NOT NULL,
  ofertas VARCHAR(45) NOT NULL
  );
