const int ledPin = 13;
String command;
void setup(){
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  if (Serial.available()) {
    command = Serial.readString();
  }
  Serial.println(command);
  
  if(command == "two"){
    light(2, command);
    command = "";
  }

  delay(500);
}

void light(int n, String command){
  while(1){
    Serial.println(command);
    if(Serial.readString()){
      break;
    }
  }
}
