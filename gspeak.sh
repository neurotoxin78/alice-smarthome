#!/bin/bash
echo "Начинается запись..."
arecord -d 3 -q -f cd -r 16000 speech.wav # Записываем звуковой файл speech.wav длиной в 3 секунды с рейтом 16 мГц
echo "Запись закончена"
sox speech.wav speech.flac gain -n -5 silence 1 5 2% # Конвертируем speech.wav в speech.flac
#rm speech.wav # Удаляем speech.wav, т.к. он нам уже не требуется
#echo "Анализ голоса..."
#wget -v -U "Mozilla/5.0" --post-file speech.flac --header="Content-Type: audio/x-flac; rate=16000" -O - "http://www.google.com/speech-api/v1/recognize?lang=ru-RU&client=chromium" > all.ret # Отправляем Google speech.flac и полученный ответ сохраняем в файл all.ret
#rm speech.flac # Удаляем speech.flac, т.к. он нам уже не требуется
#cat all.ret | sed 's/.*utterance":"//' | sed 's/","confidence.*//' > text.txt # Вычленяем значение utterance в файл text.txt
#cat all.ret | sed 's/.*confidence"://' | sed 's/}]}.*//' > confidence.txt # Вычленяем значение confidence в файл confidence.txt
#rm all.ret # Удаляем all.ret, т.к. он нам уже не требуется
#TEXT="$(cat text.txt)" # Переменной TEXT присваиваем содержимое файла text.txt 
#CONFIDENCE="$(cat confidence.txt)" # Переменной CONFIDENCE присваиваем содержимое файла confidence.txt
#rm text.txt # Удаляем text.txt, т.к. он нам уже не требуется
#rm confidence.txt # Удаляем confidence.txt, т.к. он нам уже не требуется
#echo $TEXT # Выводим значение переменной TEXT
#echo $CONFIDENCE # Выводим значение переменной CONFIDENCE
