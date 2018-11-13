#include "misaki_utf16_print.h"
#include <M5Stack.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <TinyGPS++.h>

//環境によって変える
#include "private.h" // <--WifiのSSIDとパスワードはこの中に隔離しました
const String Address = "10.0.1.33:8000";

//機体ごとに変える
const int key = 1;

//基本的に変えない
const String message_source_url = "http://" + Address + "/polls/m5stack/";
const String data_destination_url = "http://" + Address + "/polls/" + key + "/";

HardwareSerial GPS_s(2);
TinyGPSPlus gps;

void setup()
{
  M5.begin();
  GPS_s.begin(9600);
  WiFi.begin(SSID, PASSWORD);
  int x = 0;
  int y = misakiPrint(0, 0, "WiFi にせつぞく中");

  while (WiFi.status() != WL_CONNECTED)
  {
    misakiPrint(x, y, ".");
    x += 8;
    delay(100);
  }
  M5.Lcd.fillScreen(BLACK);
  misakiPrint(0, 0, "せつぞく完りょう");
  send();
}

void send()
{
  int ans_int = 0;
  HTTPClient http;
  http.begin(message_source_url);
  int httpCode = http.GET();

  if (httpCode == HTTP_CODE_OK)
  {
    String body = http.getString();
    //misakiPrint(0, 0, "Response Body");
    M5.Lcd.fillScreen(BLACK);
    Answer ans = display_message(body);
    M5.Lcd.fillScreen(BLACK);
    if (ans == Answer::Yes)
    {
      ans_int = 1;
    }
    else
    {
      ans_int = 2;
    }
  }
  else
  {
    M5.Lcd.fillScreen(BLACK);
    misakiPrint(0, 0, "メッセージのしゅとくにしっぱいしました");
  }
  // GPSの値取得を待つ
  
  //while (!gps.location.isUpdated())
  //{
    while (GPS_s.available() > 0)
    {
      if (gps.encode(GPS_s.read()))
      {
        break;
      }
    }
  //}
  //  http://{address}/polls/1/{message 1 or 2}/緯度/経度/m5stack_send
  String answer_str = String(ans_int);
  String ido = String(gps.location.lat(), 6);
  String kedo = String(gps.location.lng(), 6);
  String res_url = String(data_destination_url + answer_str + "/" + ido + "/" + kedo + "/m5stack_send");
  M5.Lcd.fillScreen(BLACK);
  misakiPrint(0, 0, res_url);
  http.begin(res_url);
  int httpCode2 = http.GET();
  if (httpCode2 == HTTP_CODE_OK)
  {
    misakiPrint(0, 24 * 6, "send");
  }
  else
  {
    misakiPrint(0, 24 * 6, "faild");
  }

  delay(10000);
}

void loop() {}
