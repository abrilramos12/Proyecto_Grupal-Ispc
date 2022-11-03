-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Capacit
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Capacit
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Capacit` DEFAULT CHARACTER SET utf8 ;
USE `Capacit` ;

-- -----------------------------------------------------
-- Table `Capacit`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Capacit`.`User` (
  `id_user` VARCHAR(256) NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(32) NOT NULL,
  `active` TINYINT NOT NULL DEFAULT 1,
  `role` VARCHAR(45) NOT NULL,
  `create_time` DATETIME NULL,
  `user_git` VARCHAR(128) NULL,
  `user_linkedin` VARCHAR(128) NULL,
  PRIMARY KEY (`id_user`));


-- -----------------------------------------------------
-- Table `Capacit`.`Video`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Capacit`.`Video` (
  `id_video` INT NOT NULL,
  `description` VARCHAR(45) NULL,
  `blob` LONGBLOB NULL,
  PRIMARY KEY (`id_video`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Capacit`.`Course`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Capacit`.`Course` (
  `id_course` VARCHAR(256) NOT NULL,
  `name` VARCHAR(16) NOT NULL,
  `language` VARCHAR(45) NOT NULL,
  `tag_1` VARCHAR(45) NULL,
  `tag_2` VARCHAR(45) NULL,
  `link` VARCHAR(45) NULL,
  `Video_id_video` INT NOT NULL,
  PRIMARY KEY (`id_course`),
  INDEX `fk_course_Video_idx` (`Video_id_video` ASC) VISIBLE,
  CONSTRAINT `fk_course_Video`
    FOREIGN KEY (`Video_id_video`)
    REFERENCES `Capacit`.`Video` (`id_video`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `Capacit`.`Teacher`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Capacit`.`Teacher` (
  `user_id_user` VARCHAR(256) NOT NULL,
  `dni` VARCHAR(16) NULL,
  `Course_id_course` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`user_id_user`),
  INDEX `fk_teacher_user1_idx` (`user_id_user` ASC) VISIBLE,
  INDEX `fk_Teacher_Course1_idx` (`Course_id_course` ASC) VISIBLE,
  CONSTRAINT `fk_teacher_user1`
    FOREIGN KEY (`user_id_user`)
    REFERENCES `Capacit`.`User` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Teacher_Course1`
    FOREIGN KEY (`Course_id_course`)
    REFERENCES `Capacit`.`Course` (`id_course`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Capacit`.`Student`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Capacit`.`Student` (
  `user_id_user` VARCHAR(256) NOT NULL,
  `user_vip` TINYINT NOT NULL,
  PRIMARY KEY (`user_id_user`),
  INDEX `fk_alumne_user1_idx` (`user_id_user` ASC) VISIBLE,
  CONSTRAINT `fk_alumne_user1`
    FOREIGN KEY (`user_id_user`)
    REFERENCES `Capacit`.`User` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
