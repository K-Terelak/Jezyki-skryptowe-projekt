#!/bin/bash

RED='\033[0;31m';
PURPLE='\033[0;35m';
ORANGE='\033[0;33m';
GREEN='\033[032m';
NC='\033[0m';

pause() {
printf "${GREEN}";
read -p "Nacisnij enter zeby kontynuowac.";
printf "${NC}";
}

menu() {
clear
printf "${ORANGE}"
echo "|^^^^  MENU  ^^^^|"
echo "|________________|"
echo "| 1 - Start      |"
echo "| 2 - Informacje |"
echo "| 3 - Backup     |"
echo "| 4 - Zakoncz    |"
echo "|________________|"
printf "${NC}";
read -n 1 -s wybor;
case $wybor in
"1")
     dir="output"
      if [ -d $dir ]
        then
            rm -r $dir
        fi
        mkdir $dir

        echo
    for file in "input"/*
    do
      file="${file:6}"
      python3 main.py "$file"
    done
    if [ -d $dir ]
    then
        if [ "$(ls -A $dir)" ]; then
        python3 raport.py
        echo
            echo "Program uruchomiony pomyslnie, otwieram wygenerowany raport"
            xdg-open Raport.html </dev/null >/dev/null 2>&1 & disown
        else
          echo "Brak wynikow dzialania programu"
        fi
    fi

    pause;
    menu
    ;;
"2")
    printf "${PURPLE}";
        echo "Olimpiada informatyczna IV";
    echo "Organizujac splywy, wypozyczamy na kajaki. Wszystkie kajaki sa jednakowe. W jednym kajaku moga poplynac co najwyzej dwie osoby, a suma ich wag nie moze przekroczyc ustalonego maksymalnego obciazenia. Aby zaplacic jak najmniej, szukamy sposobu rozmieszczenia wszystkich uczestnikow splywu w minimalnej liczbie kajakow.";
    printf "${RED}";
    echo "Autor: Krzysztof Terelak.";
    printf "${NC}";
    pause;
    menu;
        ;;
"3")
        if [ ! -f "Raport.html" ]; then
          echo "Nie udalo sie stworzyc kopi zapasowej raportu, bo go nie ma ;("
        else
          if [ ! -d "backups" ];
          then
              mkdir backups
          fi

          printf -v date '%(%d-%m-%Y-%H:%M:%S)T\n' -1
          mkdir backups/$date

          cp -R input backups/$date
          cp -R output backups/$date
          cp Raport.html backups/$date
          cp style.css backups/$date

          echo "Backup został utworzony pomyslnie";

        fi
        pause;
        menu;
        ;;
"4")
    clear;
        exit;
        ;;
*)
    echo "Nie znam polecenia";
    pause;
    menu;
esac;
};


menu