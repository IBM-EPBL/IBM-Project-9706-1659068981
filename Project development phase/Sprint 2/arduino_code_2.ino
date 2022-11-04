#include "SPI.h"
#include "Adafruit_GFX.h"
#include "Adafruit_ILI9341.h"

#define TFT_DC 2
#define TFT_CS 15
Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC);

int inputPin2 = 12;                
int inputPin = 14;             
int pirState = LOW;            
int val = 0;  
int val2=0;
int buzzerPin = 13; 
              

void setup() {
  pinMode(inputPin2, INPUT);    
  pinMode(inputPin, INPUT);   
  pinMode(buzzerPin , OUTPUT);
  Serial.begin(9600);
  tft.begin();

  
}

void loop() {
  val = digitalRead(inputPin);  
  val2= digitalRead(inputPin2);
  if (val == HIGH) {
    tone(buzzerPin, 100);
    delay(1000);  
    noTone(buzzerPin);
    delay(1000);
    tone(buzzerPin, 100, 1000);
    delay(2000);
    if (pirState == LOW) {
      Serial.println("Motion is detected animal intrusion at location 1");
      pirState = HIGH;
      tft.setCursor(20, 120);
      tft.setTextColor(ILI9341_RED);
      tft.setTextSize(3);
      tft.println("Motion is detected animal intrusion at location 1");
    }
  } 
  else if (val2 == HIGH) {            
    tone(buzzerPin, 100);
    delay(1000);  
    noTone(buzzerPin);
    delay(1000);
    tone(buzzerPin, 100, 1000);
    delay(2000);
    if (pirState == LOW) {
      Serial.println("Motion is detected animal intrusion at location 2");
      pirState = HIGH;
      tft.setCursor(20, 120);
      tft.setTextColor(ILI9341_RED);
      tft.setTextSize(3);
      tft.println("Motion is detected animal intrusion a location 2");
    }
  } else {
    if (pirState == HIGH) {
      
      Serial.println("Motion ended");
    
      pirState = LOW;
    }
  }
}


