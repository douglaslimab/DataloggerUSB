#include <LiquidCrystal.h>

//  LCD object
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);
//  Menu / Keys Variables
int key, item;
bool menu;
//  Temperature Sensor Constants
const int B = 4275;
const int R0 = 100000;
//  Time Control
unsigned long currentMillis;
long previousMillis1 = 0;
long previousMillis2 = 0;
long previousMillis3 = 0;
long previousMillis4 = 0;

int loopTime1 = 1000;
int loopTime2 = 300;
int loopTime3 = 300;
int loopTime4 = 100;

bool serialConnection = false;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);

  lcd.clear();
  lcd.begin(16, 2);
  lcd.setCursor(1, 0);
  homeScreen();

  pinMode(A0, INPUT);
  pinMode(A4, INPUT);
}

void loop() {
  currentMillis = millis();

  //  Send Data ------------------------------------------------------------------------  
  if (currentMillis - previousMillis1 >= loopTime1) {
    previousMillis1 = currentMillis;

    Serial.println(getTemperature());
  }

  //  Read Keys ---------------------------------------------------------------------------
  if (currentMillis - previousMillis2 >= loopTime2){
    previousMillis2 = currentMillis;
    key = getKey();

    if(key == 1){
      menu = true;
      item--;
    }
    if(key == 2){
      menu = true;
      item++;
    }
    if(key == 0){
      menu = false;
      temperatureScreen();
    }
  }
  
  //  Load Screen -------------------------------------------------------------------------------------
  if (currentMillis - previousMillis3 >= loopTime3){
    previousMillis3 = currentMillis;
    if(menu)
    updateMenu();
  }  

  // Confirm connection -------------------------------------------------------------------------------
  if (currentMillis - previousMillis4 >= loopTime4){
    previousMillis4 = currentMillis;
    char serial_pack[4];

    if (Serial.available()){
      for (int i = 0; i < 4; i++){
        serial_pack[i] = Serial.read();
        delay(5);
      }
    
      lcd.setCursor(15, 0);
      lcd.print(serial_pack[0]);
    } else {
      lcd.setCursor(15, 0);
      lcd.print("-");
    }
  }
//  delay(200);
}

//  read keys
//  get variables
//  set menu
//  load screen

int getKey(){
  int pressed, lastKey, currentKey;

  lastKey = 5;
  if(analogRead(A0) < 50){  //  Right
    pressed = 0;
  } else if(analogRead(A0) < 300){  //  Up
    pressed = 1;
  } else if(analogRead(A0) < 500){  //  Down
    pressed = 2;
  } else if(analogRead(A0) < 750){  //  Left
    pressed = 3;
  } else if(analogRead(A0) < 850){  //  Right
    pressed = 4;
  } else {    //  None
    pressed = 5;
  }

  if(currentKey != lastKey){
    return pressed;
    lastKey = currentKey;
  }
    
}
void updateMenu(){
  switch (item){
    case 0:
      item = 1;
      break;
    case 1:
      lcd.clear();
      lcd.print(">MenuItem1");
      lcd.setCursor(0, 1);
      lcd.print(" MenuItem2");
      break;
    case 2:
      lcd.clear();
      lcd.print(" MenuItem1");
      lcd.setCursor(0, 1);
      lcd.print(">MenuItem2");
      break;
    case 3:
      lcd.clear();
      lcd.print(">MenuItem3");
      lcd.setCursor(0, 1);
      lcd.print(" MenuItem4");
      break;
    case 4:
      lcd.clear();
      lcd.print(" MenuItem3");
      lcd.setCursor(0, 1);
      lcd.print(">MenuItem4");
      break;
    case 5:
      item = 4;
      break;
  }
}
void homeScreen(){
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(">USB Datalogger");
  lcd.setCursor(0, 1);
  lcd.print(" Douglas Lima ");
}
void temperatureScreen(){
  float temperature;

  temperature = getTemperature();

  lcd.clear();
  lcd.print("<Temperature: ");
  lcd.setCursor(1, 1);
  lcd.print(temperature);
  lcd.setCursor(6, 1);
  lcd.print((char)223); 
  lcd.print("C");
}
float getTemperature(){  
  int temp = analogRead(A4);
  float R = 1023.0/temp-1.0;
  R = R0*R; 
  float temperature = 1.0/(log(R/R0)/B+1/298.15)-273.15; // converttion based on the datasheet
 
  return temperature;
}