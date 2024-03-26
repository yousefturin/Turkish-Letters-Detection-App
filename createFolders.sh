#!/bin/bash

# Define the Turkish alphabet
turkish_alphabet="A B C Ç D E F G Ğ H I İ J K L M N O Ö P R S Ş T U Ü V Y Z"

# Create folders for each letter in the Turkish alphabet
for letter in $turkish_alphabet; do
    mkdir "$letter"
done