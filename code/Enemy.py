#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))


class Enemy3(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.vertical_speed = ENTITY_SPEED['Enemy3']  # Velocidade de movimento vertical
        self.direction = 1  # 1 para descer, -1 para subir
        self.vertical_moving = True  # Flag para indicar que o movimento vertical está ativo
        self.time_since_last_shot = 0

    def move(self):
        # Movimenta no eixo horizontal (da direita para a esquerda)
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Verifica a movimentação vertical
        if self.vertical_moving:
            # Movimenta no eixo vertical (subindo ou descendo)
            if self.rect.top <= 0:  # Bateu na borda superior
                self.direction = 1  # Começa a descer
                self.vertical_speed = ENTITY_SPEED['Enemy3'] * 2  # Dobro da velocidade
            elif self.rect.bottom >= WIN_HEIGHT:  # Bateu na borda inferior
                self.direction = -1  # Começa a subir
                self.vertical_speed = ENTITY_SPEED['Enemy3']  # Velocidade normal

            # Aplica o movimento vertical com a direção e velocidade definida
            self.rect.centery += self.vertical_speed * self.direction

    def shoot(self):
        # Aqui, vamos ajustar para garantir que o disparo ocorra
        self.time_since_last_shot += 1  # Aumenta o contador de tempo

        # Se o tempo de disparo for atingido, dispara
        if self.time_since_last_shot >= ENTITY_SHOT_DELAY[self.name]:
            self.time_since_last_shot = 0  # Reseta o contador
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

        # Caso não esteja na hora de disparar, retorna None
        return None
