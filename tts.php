#!/usr/bin/php

<?
  $text = $argv[1];
  $uagent = "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2";
  $text = urlencode(iconv("UTF-8", "UTF-8", $text));
  $url= "http://translate.google.com/translate_tts?tl=ru&q=$text";
  $ch = curl_init( $url );
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($ch, CURLOPT_HEADER, 0);
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
  curl_setopt($ch, CURLOPT_ENCODING, "");
  curl_setopt($ch, CURLOPT_USERAGENT, $uagent);
  curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 120);
  curl_setopt($ch, CURLOPT_TIMEOUT, 120);
  curl_setopt($ch, CURLOPT_MAXREDIRS, 10);

  $content = curl_exec( $ch );
  curl_close( $ch );

  $file = fopen("current.mp3","wt") or die("err");
  fputs($file,$content);
  fclose($file);

?>
