int ledPin = 12;                
int inputPin = 14;             
int pirState = LOW;            
int val = 0;  
int buzzerPin = 13;                 

void setup() {
  pinMode(ledPin, OUTPUT);    
  pinMode(inputPin, INPUT);   
  pinMode(buzzerPin , OUTPUT);
  Serial.begin(9600);
}

void loop() {
  val = digitalRead(inputPin);  
  if (val == HIGH) {            
    digitalWrite(ledPin, HIGH);
    tone(buzzerPin, 100);
    delay(1000);  
    noTone(buzzerPin);
    delay(1000);
    tone(buzzerPin, 100, 1000);
    delay(2000);
    if (pirState == LOW) {
      Serial.println("Motion is detected animal intrusion");
      pirState = HIGH;
    }
  } else {
    digitalWrite(ledPin, LOW); 
    if (pirState == HIGH) {
      
      Serial.println("Motion ended");
    
      pirState = LOW;
    }
  }
}
