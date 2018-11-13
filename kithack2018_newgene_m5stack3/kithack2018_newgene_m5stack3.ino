#include <M5Stack.h>

// the setup routine runs once when M5Stack starts up
void setup() {
  
  // initialize the M5Stack object
  M5.begin();

  // Lcd display
  M5.Lcd.fillScreen(WHITE);
  M5.Lcd.fillCircle(80, 100, 30, BLACK);
  M5.Lcd.fillCircle(240, 100, 30, BLACK);
  M5.Lcd.fillTriangle(120, 180, 200, 180, 160, 230, BLACK);

}

// the loop routine runs over and over again forever
void loop(){
  
  M5.update();
}
