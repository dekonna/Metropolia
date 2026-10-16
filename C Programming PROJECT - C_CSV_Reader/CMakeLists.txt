cmake_minimum_required(VERSION 4.3)
project(C_CSV_Reader C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(C_CSV_Reader
        file_handler.c
        file_handler.h
        main.c
        temperature_logic.c
        temperature_logic.h)
