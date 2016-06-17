/* Copyright (C) 2016 Embecosm Limited and University of Bristol

   Contributor Graham Markall <graham.markall@embecosm.com>

   This file is part of the Bristol/Embecosm Embedded Benchmark Suite.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program. If not, see <http://www.gnu.org/licenses/>. */

#include <stdio.h>
#include <support.h>

void initialise_board()
{
    printf("initialise_board()\n");
}

void start_trigger()
{
    printf("start_trigger()\n");
    // 0x45 = 'E', 0x4D = 'M', 0x42 = 'B', 0x45 = 'E'
    asm volatile ("addi a0, a0, 0x45\n addi a0, a0, 0x4D\n addi a0, a0, 0x42\n addi a0, a0, 0x45" : : : "a0");
}

void stop_trigger()
{
    // 0x43 = 'C', 0x4F = 'O', 0x53 = 'S', 0x4D = 'M'
    asm volatile ("addi a0, a0, 0x43\n addi a0, a0, 0x4F\n addi a0, a0, 0x53\n addi a0, a0, 0x4D" : : : "a0");
    printf("stop_trigger()\n");
}


