-- -----------------------------------------------------
-- Schema cinema
-- -----------------------------------------------------
CREATE SCHEMA cinema;
USE cinema ;

-- -----------------------------------------------------
-- Table tipofilme
-- -----------------------------------------------------
CREATE TABLE tipofilme (
  i_idCategoria_TipoFilme INT NOT NULL,
  s_genero_TipoFilme VARCHAR(5) NOT NULL,
  PRIMARY KEY (i_idCategoria_TipoFilme));
-- -----------------------------------------------------
-- Table filme
-- -----------------------------------------------------
CREATE TABLE filme (
  i_id_filme INT NOT NULL,
  s_titulo_filme VARCHAR(30) NOT NULL,
  s_nacionalidade_filme VARCHAR(10) NOT NULL,
  s_estudio_filme VARCHAR(10) NOT NULL,
  i_tipoFilme_filme INT NOT NULL,
  s_atores_filme VARCHAR(45) NOT NULL,
  PRIMARY KEY (i_id_filme, s_atores_filme),
  INDEX fk_tipoFilme (i_tipoFilme_filme ASC) VISIBLE,
  CONSTRAINT fk_tipoFilme
    FOREIGN KEY (i_tipoFilme_filme)
    REFERENCES tipofilme (i_idCategoria_TipoFilme));
-- -----------------------------------------------------
-- Table atores
-- -----------------------------------------------------
CREATE TABLE atores (
  i_id_ator INT NOT NULL,
  s_nome_ator VARCHAR(20) NOT NULL,
  atorescol VARCHAR(45) NULL,
  PRIMARY KEY (i_id_ator, s_nome_ator),
  INDEX fk_atores_filme1_idx (s_nome_ator ASC) VISIBLE,
  CONSTRAINT fk_atores_filme1
    FOREIGN KEY (s_nome_ator)
    REFERENCES filme (s_atores_filme)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
-- -----------------------------------------------------
-- Table tipocliente
-- -----------------------------------------------------
CREATE TABLE tipocliente (
  i_id_TCliente INT NOT NULL,
  s_desc_TCliente VARCHAR(15) NULL DEFAULT NULL,
  PRIMARY KEY (i_id_TCliente));
-- -----------------------------------------------------
-- Table sala
-- -----------------------------------------------------
CREATE TABLE sala (
  i_cod_sala INT NOT NULL,
  i_capa_sala INT NOT NULL,
  i_poltrona_sala INT NOT NULL,
  i_numero_sala INT NOT NULL,
  PRIMARY KEY (i_cod_sala));
-- -----------------------------------------------------
-- Table secoes
-- -----------------------------------------------------
CREATE TABLE secoes (
  i_cod_secoes INT NOT NULL,
  d_data_secoes DATE NOT NULL,
  h_hora_secoes DATETIME NOT NULL,
  i_TipoSala_secoes INT NOT NULL,
  filme_i_id_filme INT NOT NULL,
  PRIMARY KEY (i_cod_secoes, filme_i_id_filme),
  INDEX i_TipoSala_secoes (i_TipoSala_secoes ASC) VISIBLE,
  INDEX fk_secoes_filme1_idx (filme_i_id_filme ASC) VISIBLE,
  CONSTRAINT secoes_ibfk_1
    FOREIGN KEY (i_TipoSala_secoes)
    REFERENCES sala (i_cod_sala),
  CONSTRAINT fk_secoes_filme1
    FOREIGN KEY (filme_i_id_filme)
    REFERENCES filme (i_id_filme)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
-- -----------------------------------------------------
-- Table ingressos
-- -----------------------------------------------------
CREATE TABLE ingressos (
  i_cod_ingresso INT NOT NULL,
  f_preco_ingresso INT NOT NULL,
  secoes_i_cod_secoes INT NOT NULL,
  INDEX fk_ingressos_secoes1_idx (secoes_i_cod_secoes ASC) VISIBLE,
  CONSTRAINT fk_ingressos_secoes1
    FOREIGN KEY (secoes_i_cod_secoes)
    REFERENCES secoes (i_cod_secoes)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
-- -----------------------------------------------------
-- Table estreias
-- -----------------------------------------------------
CREATE TABLE estreias (
  i_idEstreia_est INT NOT NULL,
  d_dataEstreia_est DATE NOT NULL,
  ingressos_i_cod_ingresso INT NOT NULL,
  PRIMARY KEY (i_idEstreia_est, ingressos_i_cod_ingresso),
  INDEX fk_estreias_ingressos1_idx (ingressos_i_cod_ingresso ASC) VISIBLE,
  CONSTRAINT fk_estreias_ingressos1
    FOREIGN KEY (ingressos_i_cod_ingresso)
    REFERENCES ingressos (i_cod_ingresso)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
-- -----------------------------------------------------
-- Table lanches
-- -----------------------------------------------------
CREATE TABLE lanches (
  i_cod_lanche INT NOT NULL,
  f_preco_lanche FLOAT NOT NULL,
  i_quantidade_lanche INT NOT NULL,
  i_tipo_lanche INT NOT NULL,
  PRIMARY KEY (i_cod_lanche));
-- -----------------------------------------------------
-- Table comprar
-- -----------------------------------------------------
CREATE TABLE comprar (
  i_ingresso_comprar INT NOT NULL,
  i_lanches_comprar INT NOT NULL,
  i_estreia_comprar INT NOT NULL,
  checaBilhe_comprar INT NOT NULL,
  PRIMARY KEY (i_ingresso_comprar, i_lanches_comprar, i_estreia_comprar, checaBilhe_comprar),
  INDEX fk_comprar_estreias1_idx (i_estreia_comprar ASC) VISIBLE,
  INDEX fk_comprar_lanches1_idx (i_lanches_comprar ASC) VISIBLE,
  CONSTRAINT fk_comprar_estreias1
    FOREIGN KEY (i_estreia_comprar)
    REFERENCES estreias (i_idEstreia_est)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_comprar_lanches1
    FOREIGN KEY (i_lanches_comprar)
    REFERENCES lanches (i_cod_lanche)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_comprar_ingressos1
    FOREIGN KEY (i_ingresso_comprar)
    REFERENCES ingressos (i_cod_ingresso)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
-- -----------------------------------------------------
-- Table ofertas
-- -----------------------------------------------------
CREATE TABLE ofertas (
  i_id_ofertas INT NOT NULL,
  PRIMARY KEY (i_id_ofertas));

-- -----------------------------------------------------
-- Table Bilheteria
-- -----------------------------------------------------
CREATE TABLE Bilheteria (
  FormaPagamento INT NOT NULL,
  compra_id_bilhe INT NOT NULL,
  cliente_id_bilhe INT NOT NULL,
  mostra_ofertas INT NULL,
  PRIMARY KEY (compra_id_bilhe, cliente_id_bilhe, mostra_ofertas),
  INDEX fk_Bilheteria_ofertas1_idx (mostra_ofertas ASC) VISIBLE,
  CONSTRAINT fk_Bilheteria_comprar1
    FOREIGN KEY (compra_id_bilhe)
    REFERENCES comprar (checaBilhe_comprar)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Bilheteria_ofertas1
    FOREIGN KEY (mostra_ofertas)
    REFERENCES ofertas (i_id_ofertas)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

-- -----------------------------------------------------
-- Table cliente
-- -----------------------------------------------------
CREATE TABLE cliente (
  i_id_cliente INT NOT NULL,
  s_nome_cliente VARCHAR(15) NOT NULL,
  d_dataNas_cliente DATE NOT NULL,
  i_tipo_cliente INT NOT NULL,
  PRIMARY KEY (i_id_cliente),
  INDEX fk_cliente (i_tipo_cliente ASC) VISIBLE,
  CONSTRAINT fk_cliente
    FOREIGN KEY (i_tipo_cliente)
    REFERENCES tipocliente (i_id_TCliente),
  CONSTRAINT fk_cliente_Bilheteria1
    FOREIGN KEY (i_id_cliente)
    REFERENCES Bilheteria (cliente_id_bilhe)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
